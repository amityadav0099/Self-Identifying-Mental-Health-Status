
from django.urls import path
from . import views

app_name = 'assessment'  # 👈 Add this line

urlpatterns = [
    path('quiz/', views.start_assessment, name='quiz'),
    path('result/', views.result, name='result'),
    
]
