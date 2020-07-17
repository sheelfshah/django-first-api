from django.urls import path
from api_app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('users/', views.UserList.as_view(), name="user_list"),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="user_detail"),
    path('models/', views.TrialModelList.as_view(), name="model_list"),
    path('models/<int:pk>/', views.TrialModelDetail.as_view(), name="model_detail"),
    path('', views.api_root),
]
urlpatterns = format_suffix_patterns(urlpatterns)
