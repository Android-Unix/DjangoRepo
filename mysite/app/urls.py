from django.urls import path
from . import views

urlpatterns = [
    path('' , views.printMessage , name = 'app') ,
    path('<int:question_id>/' , views.get_votes , name = 'votes' ) ,
]
