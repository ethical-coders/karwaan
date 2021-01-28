from django.urls import path

from . import views
#from .views import IndexView

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    #path('',IndexView.as_view(),name='index')
    path('blog-single',views.blog1,name='blog-single')
    #path('iot',views.blog2,name='iot')
   
]
