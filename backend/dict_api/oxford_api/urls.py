from django.urls import path
from . import views

urlpatterns = [
    path("synonyms/", views.SynonymsView.as_view()),
]

