from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('name/' , views.get_name , name = 'name'),
    path('<int:question_id>/', views.detail_id, name='detail_id'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]