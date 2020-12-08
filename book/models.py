from django.db import models
from django.urls import reverse

Branch=[
    ('IT','IT'),
    ('CSE','CSE'),
    ('MECH','MECH'),
    ('PROD','PROD'),
    ('CHEM','CHEM'),
    ('CIVIL','CIVIL'),
    ('TEXT','TEXT'),
    ('EXTC','EXTC'),
    ('ELECT','ELECT'),
    ('INSTRU','INSTRU')
]

Language=[
    ('English','English'),
    ('Marathi','Marathi'),
    ('Hindi','Hindi')
]

Available=[
    ('Yes','Yes'),
    ('No','No')
]

class Book(models.Model):
    name = models.CharField(max_length = 60)
    author = models.CharField(max_length = 40, default = 'Random')
    isbn = models.CharField(max_length = 12)
    discription = models.TextField()
    copies = models.IntegerField(default = 50)
    available = models.CharField(max_length = 3, choices = Available, default = 'Yes')
    language = models.CharField(max_length = 7, choices = Language, default = 'English')
    image = models.ImageField()
    
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return  reverse(book_list)
    
class Student(models.Model):
    student_name = models.CharField(max_length = 30)
    book_assign = models.ForeignKey(Book, on_delete = models.CASCADE,blank=True, null=True)
    reg_no = models.CharField(max_length = 15, default = '***')
    branch = models.CharField(max_length = 6, choices = Branch, default = 'IT')
    assign_date = models.DateField('book assign date')
    due_date = models.DateField('Due on')
    due_fine = models.DecimalField(max_digits = 5, decimal_places = 2)
    
    def __str__(self):
        return self.student_name
        
    def total_fine(self):
        return self.due_fine
        
        
class fine(models.Model):
    student_name = models.CharField(max_length = 40, default = 'Robot')
    reg_no = models.CharField(max_length = 15)
    branch = models.CharField(max_length = 6, choices = Branch, default = 'IT')