from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.get_owner),
    path('owner/list/', views.get_owners_list),
    path('car/list/', views.CarListView.as_view()),
    path('car/<int:pk>/', views.CarRetrieveView.as_view()),
    path('car/<int:pk>/update/', views.CarUpdateView.as_view()),
    path('car/create/', views.CarCreate.as_view()),
    path('car/<int:pk>/delete/', views.CarDeleteView.as_view()),
    path('owner/create', views.create_owner_view),
]