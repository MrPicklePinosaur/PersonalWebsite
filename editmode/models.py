from django.db import models

# Create your models here.
class Project(models.Model):
	name = models.CharField(max_length=64)
	slug = models.SlugField()
	summary = models.CharField(max_length=255) #brief description that is shown on preview card
	description = models.TextField()
	images = models.ImageField(blank=True)
	files = models.FileField(blank=True)

	def __str__(self):
		return self.name