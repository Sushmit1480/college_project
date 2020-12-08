from django.urls import path
from .views import BookAPIView,StudentAPIView


urlpatterns = [
	path('book/', BookAPIView.as_view()),
	path('student/', StudentAPIView.as_view()),
]