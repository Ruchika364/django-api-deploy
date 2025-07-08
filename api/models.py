from django.db import models

# Create your models here.
# Django uses ORM. It maps a python object to a database instance
#It allows to use multiple type of databases

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add =  True)

    def __str__(self):
        return self.title
    


    
