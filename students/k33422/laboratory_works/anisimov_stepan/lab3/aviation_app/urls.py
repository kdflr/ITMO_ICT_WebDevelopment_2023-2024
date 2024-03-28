from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import AircraftList, AircraftDetail, FlightList, FlightDetail, CrewMemberList, CrewMemberDetail, \
    EmployeeList, EmployeeDetail, CustomUserViewSet
from djoser.views import TokenCreateView, TokenDestroyView, UserViewSet

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

urlpatterns = [
    path('api/aircrafts/', AircraftList.as_view(), name='aircraft-list'),
    path('api/aircrafts/<int:pk>/', AircraftDetail.as_view(), name='aircraft-detail'),

    path('api/flights/', FlightList.as_view(), name='flight-list'),
    path('api/flights/<int:pk>/', FlightDetail.as_view(), name='flight-detail'),

    path('api/crew-members/', CrewMemberList.as_view(), name='crew-member-list'),
    path('api/crew-members/<int:pk>/', CrewMemberDetail.as_view(), name='crew-member-detail'),

    path('api/employees/', EmployeeList.as_view(), name='employee-list'),
    path('api/employees/<int:pk>/', EmployeeDetail.as_view(), name='employee-detail'),

    path('auth/register/', UserViewSet.as_view({'post': 'create'}), name='user-create'),
    path('auth/login/', TokenCreateView.as_view(), name='token-create'),
    path('auth/logout/', TokenDestroyView.as_view(), name='token-destroy'),

    path('auth/profile/', CustomUserViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='user-profile'),
    path('auth/profile/<int:user_id>/', CustomUserViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='user-profile'),

    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')

]