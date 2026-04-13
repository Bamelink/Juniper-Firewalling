"""URL configuration for policies app."""
from django.urls import path
from . import views

app_name = 'policies'

urlpatterns = [
    # Policy views
    path('', views.PolicyListView.as_view(), name='policy-list'),
    path('<int:pk>/', views.PolicyDetailView.as_view(), name='policy-detail'),
    path('create/', views.PolicyCreateView.as_view(), name='policy-create'),
    path('<int:pk>/update/', views.PolicyUpdateView.as_view(), name='policy-update'),
    path('<int:pk>/delete/', views.PolicyDeleteView.as_view(), name='policy-delete'),
    
    # Zone views
    path('zones/', views.ZoneListView.as_view(), name='zone-list'),
    
    # API endpoints
    path('api/zones/', views.APIZoneList.as_view(), name='api-zones'),
    path('api/addresses/', views.APIAddressList.as_view(), name='api-addresses'),
    path('api/services/', views.APIServiceList.as_view(), name='api-services'),
]
