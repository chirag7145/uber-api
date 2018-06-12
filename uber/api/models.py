from django.db import models
import math
# Create your models here.
class Price(models.Model):
    start_lattitude = models.DecimalField(default = 0.0,max_digits=5,decimal_places=2)
    start_longitude = models.DecimalField(default = 0.0,max_digits=5,decimal_places=2)
    end_lattitude = models.DecimalField(default = 0.0,max_digits=5,decimal_places=2)
    end_longitude = models.DecimalField(default = 0.0,max_digits=5,decimal_places=2)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20,blank=False,help_text="Name")
    username = models.CharField(foreign_key=True,max_length=20,blank=False,help_text="UserName")
    phone_no = models.IntegerField(blank=False,help_text="Mobile No.")

    class Meta:
        ordering = ('created',)

    def get_absolute_url(self):
        return reverse('User Details',args=[str(self.id)])

    def _str_(self):
        return self.username
        # return 10*(abs(end_latitude-start_latitude) + abs(end_longitude-start_longitude))
    # def price(self,start_lattitude,start_longitude,end_lattitude,end_longitude):
    #     return return 10*(abs(end_latitude-start_latitude) + abs(end_longitude-start_longitude))
    #     pass
    # def price(self):
    def display_price(self):
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
        display_price.short_description = 'Genre'


class Driver(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20,blank=False,help_text="Name")
    username = models.CharField(primary_key=True,max_length=20,blank=False,help_text="UserName")
    phone_no = models.IntegerField(blank=False,help_text="Mobile No.")
    aadhar_no = models.IntegerField(blank=False,help_text="Aadhar Card No.")
    licence_no = models.CharField(max_length=15,blank=False,help_text="Licence No.")
    car_no = models.CharField(default='',max_length=15,blank=False,help_text="Car No.")
    class Meta:
        ordering = ('created',)

    def get_absolute_url(self):
        return reverse('Driver Details',args=[str(self.id)])

    def _str_(self):
        return f'{self.username} ({self.aadhar_no})'




from django.db import models

# Create your models here.

from django.urls import reverse #Used to generate urls by reversing the URL patterns


class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Language(models.Model):
    """
    Model representing a Language (e.g. English, French, Japanese, etc.)
    """
    name = models.CharField(max_length=200, help_text="Enter a the book's natural language (e.g. English, French, Japanese etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
      # Foreign Key used because book can only have one author, but authors can have multiple books
      # Author as a string rather than object because it hasn't been declared yet in file.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
      # ManyToManyField used because a genre can contain many books and a Book can cover many genres.
      # Genre class has already been defined so we can specify the object above.
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
        display_genre.short_description = 'Genre'


    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


import uuid # Required for unique book instances
from datetime import date

from django.contrib.auth.models import User #Required to assign User as a borrower

class RideInstance(models.Model):

    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    car = models.ForeignKey('Car', on_delete=models.SET_NULL, null=True)
    # imprint = models.CharField(max_length=200)
    ride_status = models.DateField(null=True, blank=True)
    # borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    start_lattitude = models.DecimalField(default = 0.0,max_digits=5,decimal_places=2)
    start_longitude = models.DecimalField(default = 0.0,max_digits=5,decimal_places=2)
    end_lattitude = models.DecimalField(default = 0.0,max_digits=5,decimal_places=2)
    end_longitude = models.DecimalField(default = 0.0,max_digits=5,decimal_places=2)
    @property
    def status(self):
        if self. and date.today() > self.due_back:
            return True
        return False


    # LOAN_STATUS = (
    #     ('d', 'Maintenance'),
    #     ('o', 'On loan'),
    #     ('a', 'Available'),
    #     ('r', 'Reserved'),
    # )
    CAR_STATUS = (
        ('o', 'On the way'),
        ('a', 'Arriving'),
        ('t', 'On trip'),
        ('r', 'Reached'),
    )


    status= models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', help_text='Book availability')

    class Meta:
        ordering = [""]
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        """
        String for representing the Model object.
        """
        #return '%s (%s)' % (self.id,self.book.title)
        return '{0} ({1})'.format(self.id,self.book.title)
