from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from .models import Book,Student
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect,get_object_or_404
from .forms import SignUpForm,FineForm
from django.urls import reverse

class about(TemplateView):
        template_name = 'book/about.html'
        
class Book_list(ListView):
    model = Book
    
class Student_list(ListView):
    model = Student
    
class Book_create(LoginRequiredMixin, CreateView):
    fields = ('name','author','isbn','discription','copies','available','language','image')
    model = Book
    success_url = reverse_lazy('book_list')
    
class Student_create(LoginRequiredMixin, CreateView):
    fields = ('student_name','book_assign','reg_no','branch','assign_date','due_date','due_fine')
    model = Student
    success_url = reverse_lazy('student_list')
    
class Book_update(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'book/book_list.html'
    fields = ('name','author','isbn','discription','copies','available','language','image')
    model = Book
    success_url = reverse_lazy('book_list')
    
class Student_update(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'book/student_list.html'
    fields = ('student_name','book_assign','reg_no','branch','assign_date','due_date','due_fine')
    model = Student
    success_url = reverse_lazy('student_list')
    
class Book_delete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')
    
class Student_delete(LoginRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')
    
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('book_list')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
    
def Fine_confirmation(request,pk):
    form = FineForm()
    if request.method == 'POST':
        form = FineForm(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['student_name']
            reg_no = form.cleaned_data['reg_no']
            branch = form.cleaned_data['branch']
            
            student = get_object_or_404(Student, pk=pk)
            student.reg_no = reg_no
            student.branch = branch
            student.save()
            
            return redirect('return_fine', pk = student.id)
            
    return render(request, 'book/fine_confirmation.html', {'form' : form})
    
    
def return_fine(request, pk):
    if request.user.is_authenticated:
        fine = get_object_or_404(Student, pk = pk)
        
    return render(request,'book/fine_payment.html', {'fine':fine})
    
def logoutuser(request):
    logout(request)
    return redirect('login')

def show_book(request, pk):
        if request.user.is_authenticated:
            info = get_object_or_404(Book, pk = pk)

        return render(request,'book/show_book.html', {'info':info})
