from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('',views.home),
    path('',views.index),
    path('add',views.add,name='add'),
]
