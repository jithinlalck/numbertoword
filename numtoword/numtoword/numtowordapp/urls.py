from . import views
from django.urls import path
app_name='numtowordapp'

urlpatterns = [
    path('', views.fn_index, name='fn_index'),
    path('convert/',views.fn_convert,name='fn_convert'),
    path('play/',views.fn_play,name='fn_play')
]