from django.db import models
from django.utils import timezone

class Area(models.Model):
	descricao = models.CharField(max_length=200)
	cor = models.CharField(max_length=200)
	#status = models.BooleanField(default=False)
	status = models.DateTimeField(blank=True, null=True)

	'''def ati_des(self):
		if self.status == True:
			self.data_at = timezone.now():
			self.save()
			
		elif self.status == False:
			self.save()'''

	def __str__(self):
		return self.descricao

class Noticia(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	area = models.ForeignKey(Area, on_delete=models.SET_NULL, blank=True, null=True, related_name='area')
	title = models.CharField(max_length=200)
	text = models.TextField()
	published_date = models.DateTimeField(blank=True, null=True)
	photo = models.ImageField(upload_to='imagens/', null=True, blank=True)

	
	def __str__(self):
		return self.title