from django.contrib import admin
from django.contrib.auth import views as auth_view
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users import views as users_view

urlpatterns = [
    path("", include("todo.urls")),
    path("admin/", admin.site.urls),
    path("register/", users_view.register, name="register"),
    path("profile/", users_view.profile, name="profile"),
    path(
        "login/",
        auth_view.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_view.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
