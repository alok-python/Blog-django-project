from django.urls import path
from .views import blog, index,about,contact,post,undr

urlpatterns = [
 
    path('', index,name="home"),
    path('about/',about,name="home"),
    path('contact/', contact,name="home"),
    path('blog/', blog,name="blog"),
    path('<slug:slug>/',post,name="post"),
    path('under-construction',undr,name="under")

   
]