from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_guest, name="register"),
    path("", views.HotelListView.as_view()),
    path("booking/", views.BookingListView.as_view()),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("<str:hotel_city>/rooms/<str:room_type>/review", views.leave_review),
    path("<str:hotel_city>/rooms/<str:room_type>/", views.booking_view, name="book"),
    path("<str:hotel_city>/rooms/", views.RoomListView.as_view()),
]