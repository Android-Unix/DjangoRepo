from django.urls import path
from . import views

urlpatterns = [
    path('' , views.render_home_page) ,
    path('index/', views.index, name='index'),
    path('index/<int:question_id>/', views.detail, name='detail'),
    path('index/<int:question_id>/results/', views.results, name='results'),
    path('index/<int:question_id>/vote/', views.vote, name='vote'),
]
