from django.db import models

class Interested_subject(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
        

class City(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class student(models.Model):
    name = models.CharField(max_length=200)
    interests = models.ManyToManyField(Interested_subject)

    def __str__(self):
        return self.name

class studentAddress(models.Model):
    student = models.OneToOneField(student , on_delete=models.CASCADE)
    city = models.ForeignKey(City , on_delete= models.CASCADE)
    street_address = models.CharField(max_length=100)


    def __str__(self):
        return self.student.name +'(' + self.street_address  + ')'
