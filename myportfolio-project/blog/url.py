from django.urls import path
from . import views


urlpatterns = [
    path('',views.allblog,name='allblog'),
    path('<int:id_>/',views.detail,name='detail'),
]
