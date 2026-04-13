"""Models for firewall policies."""
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Zone(models.Model):
    """Represents a security zone in the firewall."""
    
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Address(models.Model):
    """Represents an IP address or address group."""
    
    ADDRESS_TYPES = [
        ('ipv4', 'IPv4 Address'),
        ('ipv4_range', 'IPv4 Range'),
        ('ipv6', 'IPv6 Address'),
        ('ipv6_range', 'IPv6 Range'),
        ('hostname', 'Hostname'),
        ('group', 'Address Group'),
    ]
    
    name = models.CharField(max_length=100, unique=True)
    address_type = models.CharField(max_length=20, choices=ADDRESS_TYPES)
    value = models.CharField(max_length=255, help_text="IP address, range, hostname, or group name")
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Addresses"
    
    def __str__(self):
        return f"{self.name} ({self.value})"


class Service(models.Model):
    """Represents a service (port/protocol)."""
    
    PROTOCOLS = [
        ('tcp', 'TCP'),
        ('udp', 'UDP'),
        ('icmp', 'ICMP'),
        ('both', 'TCP and UDP'),
    ]
    
    name = models.CharField(max_length=100, unique=True)
    protocol = models.CharField(max_length=10, choices=PROTOCOLS)
    port = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(65535)],
        help_text="Port number (1-65535)"
    )
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
        unique_together = ['protocol', 'port']
    
    def __str__(self):
        return f"{self.name} ({self.protocol}/{self.port})"


class Policy(models.Model):
    """Represents a firewall policy."""
    
    ACTIONS = [
        ('allow', 'Allow'),
        ('deny', 'Deny'),
        ('reject', 'Reject'),
    ]
    
    name = models.CharField(max_length=100, unique=True)
    priority = models.IntegerField(
        validators=[MinValueValidator(1)],
        help_text="Lower number = higher priority"
    )
    
    # Policy scope
    source_zone = models.ForeignKey(
        Zone,
        on_delete=models.PROTECT,
        related_name='policies_as_source'
    )
    destination_zone = models.ForeignKey(
        Zone,
        on_delete=models.PROTECT,
        related_name='policies_as_destination'
    )
    
    # Traffic definition
    source_addresses = models.ManyToManyField(
        Address,
        related_name='policies_as_source',
        help_text="Source IP addresses"
    )
    destination_addresses = models.ManyToManyField(
        Address,
        related_name='policies_as_destination',
        help_text="Destination IP addresses"
    )
    services = models.ManyToManyField(
        Service,
        help_text="Services allowed by this policy"
    )
    
    # Action and logging
    action = models.CharField(max_length=10, choices=ACTIONS, default='deny')
    logging_enabled = models.BooleanField(default=True)
    
    # Metadata
    description = models.TextField(blank=True)
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['priority', 'name']
        verbose_name_plural = "Policies"
    
    def __str__(self):
        return f"{self.priority}: {self.name} ({self.action.upper()})"


class PolicyLog(models.Model):
    """Audit log for policy changes."""
    
    ACTIONS = [
        ('created', 'Created'),
        ('updated', 'Updated'),
        ('deleted', 'Deleted'),
        ('enabled', 'Enabled'),
        ('disabled', 'Disabled'),
    ]
    
    policy = models.ForeignKey(
        Policy,
        on_delete=models.CASCADE,
        related_name='logs'
    )
    action = models.CharField(max_length=20, choices=ACTIONS)
    user = models.CharField(max_length=100, help_text="Username who made the change")
    changes = models.JSONField(default=dict, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.policy.name} - {self.action} by {self.user}"
