from django.db import models

# Create your models here.

class kotakSurat(models.Model):
	nama = models.CharField(max_length=50,blank=True,default='anonym')
	saran = models.CharField(max_length=255)
	keluhan = models.CharField(max_length=255)

	def __str__(self):
		return "{}".format(self.id,self.nama)