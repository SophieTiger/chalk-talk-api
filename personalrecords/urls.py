from django.urls import path
from personalrecords import views

urlpatterns = [
    path('personalrecords/', views.PersonalRecordList.as_view()),
    path('personalrecords/<int:pk>/', views.PersonalRecordDetail.as_view()),
]