from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('council', 'Local Council'),
        ('company', 'Management Company'),
        ('contractor', 'Contractor'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='council')

    def is_council(self):
        return self.role == 'council'
    
    def is_company(self):
        return self.role == 'company'

    def is_contractor(self):
        return self.role == 'contractor'

class Project(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_projects')
    assigned_company = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_projects', limit_choices_to={'role': 'company'})
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ProjectRequirement(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='requirements')
    name = models.CharField(max_length=100) # e.g. Excavation, Traffic Management
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.project.title}"

class Bid(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )

    contractor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids', limit_choices_to={'role': 'contractor'})
    requirement = models.ForeignKey(ProjectRequirement, on_delete=models.CASCADE, related_name='bids')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bid by {self.contractor.username} on {self.requirement.name}"
