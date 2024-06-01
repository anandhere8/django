from django.urls import path
from . import views

app_name="food"
urlpatterns = [
    path('',view=views.index,name='index'), 
    path('<int:item_id>', view=views.detail, name='detail')
]
