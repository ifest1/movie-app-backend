from django.contrib import admin
from django.urls import path, include
from core import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('favorites/', views.FavoriteMovies.as_view()),
    path('register/', views.Registration.as_view()),
    path('login/', obtain_auth_token)
]
