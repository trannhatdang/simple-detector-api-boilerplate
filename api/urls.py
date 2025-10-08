from django.urls import path

#Stores urls. Ishmael feet.
from . import views

urlpatterns = [
    path('analyze', views.ListAnalyzeTextView.as_view()),
    path('analyze/<int:pk>', views.UpdateBasicTextView.as_view()),
]
