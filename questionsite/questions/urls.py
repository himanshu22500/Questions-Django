from django.urls import path

from . import views 

urlpatterns = [
    path('', views.get_list_of_questions, name='index'),
    path('create/', views.create_question, name='index'),
    path('<int:question_id>/get/', views.get_question, name='get_list_of_questions'),
    path('<int:question_id>/update/', views.update_question, name='get_list_of_questions'),
    path('<int:question_id>/delete/', views.delete_question, name='get_list_of_questions'),
]