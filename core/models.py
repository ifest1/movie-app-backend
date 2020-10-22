from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from .managers import AccountManager

class Movie(models.Model):
    imdb_title_id = models.CharField(primary_key=True, max_length=45)
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    date_published = models.CharField(max_length=20)
    genre = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)
    country = models.CharField(max_length=45)
    language = models.CharField(max_length=45)
    director = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    production_company = models.CharField(max_length=100)
    actors = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    avg_vote = models.CharField(max_length=20)
    votes = models.CharField(max_length=20)
    budget = models.CharField(max_length=30)
    usa_gross_income = models.CharField(max_length=45)
    worldwide_gross_income = models.CharField(max_length=45)
    metascore = models.CharField(max_length=45)
    reviews_from_users = models.CharField(max_length=45)
    reviews_from_critics =models.CharField(max_length=45)
    

class Account(AbstractUser):
    username = None

    email = models.EmailField(verbose_name="email", max_length=65, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    def __str__(self):
        return self.email


class UserFavoriteMovies(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    imdb_title = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("user", "imdb_title"))

class UserSuggestions(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    imdb_title = models.ForeignKey(Movie, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("user", "imdb_title"))

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)