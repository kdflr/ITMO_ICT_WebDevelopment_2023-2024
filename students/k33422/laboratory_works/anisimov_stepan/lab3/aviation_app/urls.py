from django.urls import path
from rest_framework import routers
from djoser.views import TokenCreateView, TokenDestroyView
from .views import (
    AirplaneDetailView, FlightDetailView,
    CrewMemberDetailView, TransitStopDetailView,
    EmployeeDetailView, UserCreateView, AirplaneViewSet, FlightViewSet, CrewMemberViewSet, TransitStopViewSet,
    EmployeeViewSet
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v2',
      description="Description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="hardbeat34@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny,],
)

router = routers.DefaultRouter()


router.register(r'airplanes', AirplaneViewSet, basename='airplane')
router.register(r'flights', FlightViewSet, basename='flight')
router.register(r'crewmembers', CrewMemberViewSet, basename='crewmember')
router.register(r'transitstops', TransitStopViewSet, basename='transitstop')
router.register(r'employees', EmployeeViewSet, basename='employee')


urlpatterns = [
    path('airplanes/<int:pk>/', AirplaneDetailView.as_view(), name='airplane-detail'),
    path('flights/<int:pk>/', FlightDetailView.as_view(), name='flight-detail'),
    path('crewmembers/<int:pk>/', CrewMemberDetailView.as_view(), name='crewmember-detail'),
    path('transitstops/<int:pk>/', TransitStopDetailView.as_view(), name='transitstop-detail'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('token/create/', TokenCreateView.as_view(), name='token-create'),
    path('token/destroy/', TokenDestroyView.as_view(), name='token-destroy'),
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

urlpatterns += router.urls

