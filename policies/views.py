"""Views for firewall policies."""
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Policy, Zone, Address, Service
from .forms import PolicyForm


class PolicyListView(LoginRequiredMixin, ListView):
    """List all firewall policies."""
    model = Policy
    template_name = 'policies/policy_list.html'
    context_object_name = 'policies'
    paginate_by = 20
    
    def get_queryset(self):
        queryset = Policy.objects.all().prefetch_related(
            'source_zone', 'destination_zone', 
            'source_addresses', 'destination_addresses', 'services'
        )
        
        # Search filter
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | 
                Q(description__icontains=search)
            )
        
        # Status filter
        status = self.request.GET.get('status')
        if status == 'enabled':
            queryset = queryset.filter(enabled=True)
        elif status == 'disabled':
            queryset = queryset.filter(enabled=False)
        
        return queryset


class PolicyDetailView(LoginRequiredMixin, DetailView):
    """Display policy details."""
    model = Policy
    template_name = 'policies/policy_detail.html'
    context_object_name = 'policy'


class PolicyCreateView(LoginRequiredMixin, CreateView):
    """Create a new policy."""
    model = Policy
    form_class = PolicyForm
    template_name = 'policies/policy_form.html'
    success_url = reverse_lazy('policy-list')


class PolicyUpdateView(LoginRequiredMixin, UpdateView):
    """Update an existing policy."""
    model = Policy
    form_class = PolicyForm
    template_name = 'policies/policy_form.html'
    success_url = reverse_lazy('policy-list')


class PolicyDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a policy."""
    model = Policy
    template_name = 'policies/policy_confirm_delete.html'
    success_url = reverse_lazy('policy-list')


class ZoneListView(LoginRequiredMixin, ListView):
    """List all zones."""
    model = Zone
    template_name = 'policies/zone_list.html'
    context_object_name = 'zones'


class APIZoneList(LoginRequiredMixin, ListView):
    """API endpoint to list zones (JSON)."""
    model = Zone
    
    def get(self, request, *args, **kwargs):
        zones = Zone.objects.all().values('id', 'name')
        return JsonResponse(list(zones), safe=False)


class APIAddressList(LoginRequiredMixin, ListView):
    """API endpoint to list addresses (JSON)."""
    model = Address
    
    def get(self, request, *args, **kwargs):
        addresses = Address.objects.all().values('id', 'name', 'address_type', 'value')
        return JsonResponse(list(addresses), safe=False)


class APIServiceList(LoginRequiredMixin, ListView):
    """API endpoint to list services (JSON)."""
    model = Service
    
    def get(self, request, *args, **kwargs):
        services = Service.objects.all().values('id', 'name', 'protocol', 'port')
        return JsonResponse(list(services), safe=False)
