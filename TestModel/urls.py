from django.urls import path
from . import views
app_name = 'TestModelAppName'
urlpatterns = [
    # ex: /TestModel/
    path('', views.index, name='index'),
    # ex: /TestModel/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /TestModel/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /TestModel/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
