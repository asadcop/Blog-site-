from django.contrib import admin
from django.urls import path
from myblog import views
from django.conf.urls.static import static
from django.conf import settings
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
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)