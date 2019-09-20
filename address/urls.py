from .views import CountryViewSet, CityViewSet, DistrictViewSet, AddressViewSet
from rest_framework.routers import DefaultRouter

address_router = DefaultRouter()
address_router.register(r"countries", CountryViewSet, basename="country")
address_router.register(r"cities", CityViewSet, basename="city")
address_router.register(r"districts", DistrictViewSet, basename="district")
address_router.register(r"addresses", AddressViewSet, basename="address")
