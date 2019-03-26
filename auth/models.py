from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    email = models.EmailField(max_length=50)
    password_hash = models.CharField(max_length=100)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.username + '--' + self.type


class Student(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    education = models.CharField(max_length=50)
    institute = models.CharField(max_length=100)
    address = models.TextField(max_length=1000)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)

    def __str__(self):
        return self.username + '--' + self.first_name + ' ' + self.last_name





