from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Project, Bid, ProjectRequirement
from .forms import CustomUserCreationForm, ProjectForm, ProjectRequirementFormSet, BidForm

def is_council(user):
    return user.is_authenticated and user.role == 'council'

from django.core.paginator import Paginator

def project_list(request):
    project_list = Project.objects.filter(status='open').order_by('-created_at')
    paginator = Paginator(project_list, 6) # Show 6 projects per page
    page_number = request.GET.get('page')
    projects = paginator.get_page(page_number)
    return render(request, 'project_list.html', {'projects': projects})

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def dashboard(request):
    user = request.user
    context = {}
    
    if user.is_council():
        context['projects'] = user.created_projects.all()
    elif user.is_contractor():
        context['bids'] = user.bids.all()
        # Simple recommendation: all open projects
        context['recommended_projects'] = Project.objects.filter(status='open').exclude(id__in=user.bids.values_list('requirement__project_id', flat=True))
    elif user.is_company():
        context['projects'] = user.assigned_projects.all()
        
    return render(request, 'dashboard.html', context)

@user_passes_test(is_council)
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        formset = ProjectRequirementFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            formset.instance = project
            formset.save()
            return redirect('dashboard')
    else:
        form = ProjectForm()
        formset = ProjectRequirementFormSet()
    
    return render(request, 'create_project.html', {'form': form, 'formset': formset})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'project_detail.html', {'project': project})

@login_required
def place_bid(request, requirement_id):
    requirement = ProjectRequirement.objects.get(id=requirement_id)
    if not request.user.is_contractor():
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.contractor = request.user
            bid.requirement = requirement
            bid.save()
            return redirect('dashboard')
    else:
        form = BidForm()
    
    return render(request, 'place_bid.html', {'form': form, 'requirement': requirement})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def manage_bid(request, bid_id, action):
    bid = get_object_or_404(Bid, id=bid_id)
    project = bid.requirement.project
    
    # Check permission: Must be Council (creator) or Assigned Management Company
    is_authorized = (request.user == project.created_by) or (project.assigned_company and request.user == project.assigned_company)
    
    if not is_authorized:
        return redirect('dashboard')
        
    if action == 'accept':
        bid.status = 'accepted'
        # Optional: Reject other bids for this requirement automatically?
        # For now, just accept this one.
    elif action == 'reject':
        bid.status = 'rejected'
        
    bid.save()
    return redirect('project_detail', pk=project.id)
