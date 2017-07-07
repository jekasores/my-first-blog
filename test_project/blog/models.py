from django.db import models #adiciona pedaco de outros arquivos
from django.utils import timezone #adiciona pedaco de outros arquivos

class Post(models.Model): #cria classe para definir objeto. Post eh o nome do modelo - reconhecido pelo django salvo no db
	author= models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField();
	created_date = models.DateTimeField(blank=True, null=True)
	published_date = models.DateTimeField(blank=True, null=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()
	def __str__(self):
		return self.title