"""Posts models."""

# Django
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save

from .utils import unique_slug_generator

class Post(models.Model):
	"""Post model."""

	user = models.ForeignKey(User, on_delete=models.CASCADE)
	profile = models.ForeignKey('users.Profile', on_delete=models.PROTECT)

	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True, blank=True)
	photo = models.ImageField(upload_to='posts/photos')

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		"""Return title and username."""

		return '{} by @{}'.format(self.title, self.user.username)
