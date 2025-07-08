#Here we specify a class that take this model and convert it into json compatible data.
#Whenever we are working with api we are sending and recieving data in json


from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ["id","title","content","published_date"]  #id is a field that automatically be added to all of our models


