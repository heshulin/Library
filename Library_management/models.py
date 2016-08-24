from django.db import models

# Create your models here.
class User(models.Model):
    UserNumber = models.CharField(max_length=255)
    PassWord = models.CharField(max_length=255)
    TrueName = models.CharField(max_length=255)
    IsManager = models.IntegerField(max_length=11)
    Professional = models.CharField(max_length=255)
    Grade = models.IntegerField(max_length=11)
    MaxNum = models.IntegerField(max_length=11)
    UserCategory = models.CharField(max_length=255)

class Subscribe(models.Model):
    SubscribeId = models.IntegerField(primary_key=True,)
    UserId = models.IntegerField()
    BookId = models.IntegerField()
    StartTime = models.DateTimeField()
    EndTime = models.DateTimeField()
    State = models.IntegerField()


class BookCategory(models.Model):
    Tag = models.CharField(max_length=255)
    Category = models.CharField(max_length=255)



class Book(models.Model):
    BookCategorytag = models.CharField(max_length=255)
    BookName = models.CharField(max_length=255)
    Author = models.CharField(max_length=255)
    Press = models.CharField(max_length=255)
    publicationdate = models.DateTimeField()
    ISBN = models.CharField(max_length=255)
    Edition = models.CharField(max_length=255)
    Price = models.FloatField(max_length=11)
    BookNum = models.IntegerField(max_length=11)

    def __str__(self):
        return 'BookName=' + self.BookName


class Record(models.Model):
    UserId = models.IntegerField(max_length=11)
    BookId = models.IntegerField(max_length=11)
    ReturnTime = models.DateTimeField()
    State = models.IntegerField(max_length=11)




class BlackList(models.Model):
    UserId = models.IntegerField(max_length=11)
    BlackNum = models.IntegerField(max_length=11)

    def __str__(self):
        return 'UserId=' + self.UserId + 'BlackNum=' + self.BlackNum







