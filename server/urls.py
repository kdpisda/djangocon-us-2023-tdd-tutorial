"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView  # noqa
from drf_spectacular.views import SpectacularRedocView  # noqa
from drf_spectacular.views import SpectacularSwaggerView  # noqa
from rest_framework_simplejwt.views import TokenObtainSlidingView  # noqa
from rest_framework_simplejwt.views import TokenRefreshSlidingView  # noqa

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/token/", TokenObtainSlidingView.as_view(), name="token_obtain"),
    path(
        "auth/token/refresh/",
        TokenRefreshSlidingView.as_view(),
        name="token_refresh",
    ),
    path("todo/", include("todo.urls")),
    path(
        "docs/schema/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),
    path(
        "docs/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path(
        "docs/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
]
