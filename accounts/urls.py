from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = 'accounts'

urlpatterns = [
    path("signup",views.signup, name='signup'),
    path('logout',views.user_logout,name = 'logout' ),
    path('login',views.user_login,name = 'login' ),
    path('password_change',auth_views.PasswordChangeView.as_view(
        # template_name="change_password.html",
        success_url = reverse_lazy('accounts:change_password_done')
        ),
        name = 'change_password' ),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name="change_password_done.html"
        ),
          name='change_password_done'),

    path('edit_account/',views.EditAccount.as_view(),name='edit_account')

    
]

