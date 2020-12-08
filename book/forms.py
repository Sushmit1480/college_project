from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import fine,Book,Student
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class FineForm(ModelForm):
    class Meta():
        model = fine
        fields = '__all__'
#class BookCreate(forms.ModelForm):
#	class Meta:
#		model = Book
#		fields = '__all__'
        
#class StudentCreate(forms.ModelForm):
#	class Meta:
#		model = Student
#		fields = '__all__'