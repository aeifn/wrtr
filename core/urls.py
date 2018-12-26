from django.urls import path
from core import views

urlpatterns = [
        path('',views.add,name='add'),
        path('<int:id>/',views.article,name='article'),
        ]
