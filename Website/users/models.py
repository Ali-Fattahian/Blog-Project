from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    slug = models.SlugField(default='user-slug-field', editable=False)
    profile_picture = models.ImageField(upload_to = 'users_profile_picture', default = 'users_profile_picture/default_user_image.png')
    email = models.EmailField(null = True, blank = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    social_twitter = models.URLField(null = True, blank = True)
    social_facebook = models.URLField(null = True, blank = True)
    social_linkedin = models.URLField(null = True, blank = True)
    social_github = models.URLField(null = True, blank = True)
    social_instagram = models.URLField(null = True, blank = True)
    website = models.URLField(null = True, blank = True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)