
import os
from contextlib import contextmanager
from subprocess import check_call, Popen, PIPE

from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import now

DATETIME_FORMAT = '%Y%m%d_%H%M%S'


class Command(BaseCommand):
    help = 'Build/bundle the application for deployment to production.'

    def add_arguments(self, parser):
        parser.add_argument(
            '-o', '--output', default=None, dest='output',
            help='Specifies file to which the output is written.'
        )
        parser.add_argument(
            '-r', '--git-reference', default='master', dest='ref',
            help='Git reference to bundle, e.g. a branch or commit hash.',
        )

    @contextmanager
    def step(self, msg='', success='done', failure='fail'):
        self.stdout.write('  - %s ' % msg, ending='')
        try:
            yield
        except Exception:
            self.stdout.write(self.style.ERROR(failure))
            raise

        self.stdout.write(self.style.SUCCESS(success))

    def handle(self, *args, **options):
        ref = options['ref']
        ts = now().strftime(DATETIME_FORMAT)
        path = 'bundles/build-%(ref)s-%(ts)s' % locals()
        out = options['output'] or (path + '.zip')

        msg = 'Creating application bundle for: %s' % ref
        self.stdout.write(self.style.MIGRATE_HEADING(msg))

        # copy the project to archive directory
        with self.step('Creating build directory at...'):
            archive = Popen(['git',  'archive', ref], stdout=PIPE)
            check_call(['mkdir', '-p', path])
            check_call(['tar', '-x', '-C', path], stdin=archive.stdout)
            archive.stdout.close()
            archive.wait()
            if archive.returncode > 0:
                raise CommandError("'%s' is an invalid git reference" % ref)

        # javascript build
        if os.path.exists(os.path.join(path, 'package.json')):
            with self.step('Found \'package.json\'. Building javascript...'):
                check_call(['npm', 'install', '--only=production'], cwd=path, stdout=PIPE)
                check_call(['npm', 'run', 'build'], cwd=path, stdout=PIPE)
        else:
            self.stdout.write('  - No \'package.json\' found. Skipping javascript build.')

        # Create zip archive
        with self.step('Writing bundle...'):
            check_call(['zip', '-r', os.path.abspath(out), '.'], cwd=path, stdout=PIPE)
        self.stdout.write('')

        # write paths to stdout
        if not out.startswith(path):
            self.stdout.write('Build directory:')
            self.stdout.write(self.style.NOTICE('  %s' % path))
        self.stdout.write('Bundle path:')
        self.stdout.write(self.style.NOTICE('  %s' % out))
