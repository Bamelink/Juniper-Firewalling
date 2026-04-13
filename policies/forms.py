"""Forms for firewall policies."""
from django import forms
from .models import Policy, Zone, Address, Service


class PolicyForm(forms.ModelForm):
    """Form for creating/editing policies."""
    
    class Meta:
        model = Policy
        fields = [
            'name', 'priority', 'source_zone', 'destination_zone',
            'source_addresses', 'destination_addresses', 'services',
            'action', 'logging_enabled', 'enabled', 'description'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Policy name'
            }),
            'priority': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1'
            }),
            'source_zone': forms.Select(attrs={'class': 'form-control'}),
            'destination_zone': forms.Select(attrs={'class': 'form-control'}),
            'source_addresses': forms.SelectMultiple(attrs={'class': 'form-control', 'size': '5'}),
            'destination_addresses': forms.SelectMultiple(attrs={'class': 'form-control', 'size': '5'}),
            'services': forms.SelectMultiple(attrs={'class': 'form-control', 'size': '5'}),
            'action': forms.Select(attrs={'class': 'form-control'}),
            'logging_enabled': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'enabled': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '4'
            }),
        }
