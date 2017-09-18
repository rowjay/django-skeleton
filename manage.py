#!/usr/bin/env python
import os.path
import sys

import environ

if __name__ == "__main__":
    envfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    if os.path.exists(envfile):
        environ.Env.read_env(envfile)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
