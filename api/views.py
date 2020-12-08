from rest_framework import generics
from book.models import Book,Student
from .serializers import BookSerializer,StudentSerializer

class BookAPIView(generics.ListAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class StudentAPIView(generics.ListAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer