from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import BookSerializer
from .models import Book


# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *argss):
        cover = request.data['cover']
        print("request")
        print('/media/', cover)
        Book.objects.create(cover=cover)
        return HttpResponse({'message': 'Book created'}, status=200)