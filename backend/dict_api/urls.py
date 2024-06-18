from . import views
from django.urls import path


urlpatterns = [
    path('search/', views.search_view.as_view()),
]
