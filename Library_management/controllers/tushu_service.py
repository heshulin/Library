from Library_management.models import User,Book
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import response

def tushu():
    b = Book.objects.all()
    return b