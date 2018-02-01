from django.urls import path

from . import views

urlpatterns = [
    path('questions/', views.ListQuestion.as_view()),
    path('answers/', views.ListAnswer.as_view()),
    path('questions/<int:pk>/', views.DetailQuestion.as_view()),
    path('answers/<int:pk>/', views.DetailAnswer.as_view()),
    path('questions/<int:pk>/answers/', views.ListQuestionAnswers.as_view())
]
