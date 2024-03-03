from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name="index"),
    path('u_hobby', views.u_hobby, name="u_hobby"),
]

urlpatterns += staticfiles_urlpatterns()