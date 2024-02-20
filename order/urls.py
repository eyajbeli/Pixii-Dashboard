from django.urls import include, path
from rest_framework import routers
from .views import OrderView,OrderUpdateStatusView


router = routers.DefaultRouter()
router.register(r'orders', OrderView, basename="order")

urlpatterns = [
    path('', include(router.urls)),
    path('status/<int:order_id>/',OrderUpdateStatusView.as_view,name='update_status')
]