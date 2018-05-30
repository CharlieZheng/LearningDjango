"""fuction docstring"""
from django.urls import path
from . import views

app_name = 'TestModelAppName'

urlpatterns = [
    # ex: /TestModel/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /TestModel/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /TestModel/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /TestModel/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
