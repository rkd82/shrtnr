from django.db import models

# Create your models here.
class item(models.Model):
	def __str__(self):
		return self.linkid
	linkid = models.CharField(max_length=5)
	link = models.URLField(max_length=5000)
	created = models.DateTimeField('Created Date')

