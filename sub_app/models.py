from django.db import models
from django.db import models


#django model.
class SkinModel(models.Model):
	pic=models.ImageField(upload_to='images',blank=True)
	url=models.CharField(max_length=100,blank=True)

