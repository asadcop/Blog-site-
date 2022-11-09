from django.contrib import admin
from django.urls import path
from myblog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('signup/', views.signup),
    path('login/', views.loggin),
    path('logout/', views.loggout),
    path('mypost/', views.mypost),
    path('newpost/', views.newpost),
    path('update/<idup>', views.update, name="up"),
    path('delete/<idde>', views.delete, name="del"),
    
]
