from django.urls import path
from .views import StudentALLview

urlpatterns = [
path('get_all/',StudentALLview.as_view())

]