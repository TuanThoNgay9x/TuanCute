from django.urls import path
from . import views


app_name = "Login"
urlpatterns = [
    path('', views.Indexclass.as_view(), name='Indexclass'),
    path('login', views.loginclass.as_view(), name='login'),
    path('userview', views.Viewuser.as_view(), name='viewuser'),
    path('product', views.viewproduct),
    path('addpost', views.AddPost.as_view(), name='addpost'),
]