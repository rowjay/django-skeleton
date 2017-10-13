
from django.contrib.auth import views as auth_views


class LoginView(auth_views.LoginView):
    template_name = 'registration/auth/login.html'
    redirect_authenticated_user = True


class LogoutView(auth_views.LogoutView):
    next_page = '/'


class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'registration/auth/password_change_form.html'


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'registration/auth/password_change_done.html'


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'registration/auth/password_reset_form.html'


class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'registration/auth/password_reset_done.html'


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'registration/auth/password_reset_confirm.html'


class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'registration/auth/password_reset_complete.html'
