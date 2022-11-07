import imp
from nturl2path import url2pathname
from django.urls import path
from core.views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
]
