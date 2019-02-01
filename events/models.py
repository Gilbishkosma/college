from django.db import models
from users.models import CustomUser

class Events(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	price = models.IntegerField(default=0)
	pdflink = models.URLField(max_length=200)
	imglink = models.ImageField(upload_to = 'img/',null=True,blank=True)
	active  = models.BooleanField(default=True)
	private = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class Participant(models.Model):
	user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
	event = models.ForeignKey(Events,on_delete=models.CASCADE,related_name="participate_event")
	payment = models.BooleanField(default=False)

	def __str__(self):
		return "{}:{}".format(self.user,self.event)

class Coordinator(models.Model):
	user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
	event = models.ForeignKey(Events,on_delete=models.CASCADE,related_name="coordinate_event")

	def __str__(self):
		return "{}:{}".format(self.user,self.event)