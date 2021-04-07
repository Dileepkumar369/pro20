from django.urls import path
from app3 import views
app_name="app3"
urlpatterns = [
    path('',views.index,name="index"),
    path('page3/',views.page3,name="page3"),
    path('<data>/',views.through_data,name="through_data"),
]
