from django.db import models
from django.shortcuts import render,reverse
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Employee(models.Model):
	company = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)
	post = models.CharField(max_length=50)
	address = models.CharField(max_length=30)
	birthdate = models.DateTimeField()
	mobile_no = models.IntegerField(blank=True,null=True)
	image  = models.FileField(blank=True,null=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("employee:detail", kwargs={"pk": self.id})
        # return "/products/{slug}/".format(slug=self.slug)
        
  

    