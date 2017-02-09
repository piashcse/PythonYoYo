from django.db import models

# Create your models here.
#MVC MODEL VIEW CONTROLER
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length = 120) # max_length = 120
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("detail", kwargs={"id":self.id})
        #return "/detail/%s/"%(self.id)
