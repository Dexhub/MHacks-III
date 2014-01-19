from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=30)
    birthday = models.DateField()

	def __unicode__(self,obj):
		for userdict in obj:
			name=userdict['name']
			birthday=userdict['birthday']
			print (name)
			print(birthday)
		
			


