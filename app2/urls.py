from django.urls import path
from app2 import views
app_name="app2"
urlpatterns = [
    path('',views.index,name="index"),
    path('page2/',views.page2,name="page2"),
]
