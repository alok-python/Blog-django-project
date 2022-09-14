from django.db import models


# Create your models here.




class Categories(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200,blank=False)
    discription=models.CharField(max_length=250)
    date=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return "Catogry     :-" +self.title


class Post(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200,blank=False)
    categories=models.ForeignKey(Categories,on_delete=models.CASCADE)
    slug=models.SlugField(max_length=130)
    date=models.DateTimeField(auto_now_add=True, null=True)
    content=models.TextField()


    def __str__(self):
        return "Post     :-" +self.title





class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=200,blank=False)
    lname=models.CharField(max_length=200,blank=False)
    email=models.CharField(max_length=200,blank=False)
    message=models.CharField(max_length=200,blank=False)
    time=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return "Message from     :-" +self.fname