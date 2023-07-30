from django.urls import path
from . import views


urlpatterns = [
    path('contents/', views.ContentListAPIView.as_view()),
    path('contents/<int:pk>/', views.ContentDetailAPIView.as_view()),

    path('contents/by_need_count/', views.ContentStatisticAPIView.as_view())
]
