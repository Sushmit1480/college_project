from rest_framework import serializers
from book.models import Book,Student

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ('id','name', 'author', 'isbn', 'discription', 'copies', 'available', 'language', 'image')

class StudentSerializer(serializers.ModelSerializer):
		class Meta:
			model = Student
			fields = ('id','student_name','book_assign','reg_no','branch','assign_date','due_date','due_fine')