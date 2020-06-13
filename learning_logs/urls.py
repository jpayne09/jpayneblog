"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    #Show all topics.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #New topic
    path('new_topic/', views.new_topic, name='new_topic'),
    #New Entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #Edit entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
app_name = "learning_logs"