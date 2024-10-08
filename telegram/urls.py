from django.urls import path
from . import views


urlpatterns = [
	path('process_update/', views.process_update),
]
