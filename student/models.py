from django.db import models

# Create your models here.

class Studentdetails(models.Model):
    Student_ID = models.IntegerField(primary_key=True)
    First_Name = models.CharField(max_length=500)
    Last_Name = models.CharField(max_length=500)
    Major = models.CharField(max_length=500)
    Year = models.CharField(max_length=500)
    GPA = models.DecimalField(max_digits=20, decimal_places=2)

class Bookdetails(models.Model):
    Book_Id = models.IntegerField(primary_key=True)
    Book_Title = models.CharField(max_length=500)
    Author_Name = models.CharField(max_length=500)
    Reserved = models.IntegerField()


class CommentData(models.Model):
    useremail = models.CharField(max_length=1000)
    usercomment = models.TextField()

class Reservationdata(models.Model):
    StudentID = models.IntegerField()
    BookTitle = models.CharField(max_length=500)