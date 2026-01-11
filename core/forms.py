from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from .models import User, Project, ProjectRequirement, Bid

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('role', 'email', 'first_name', 'last_name')
        widgets = {
            'role': forms.Select(attrs={'class': 'select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'input'
        self.fields['role'].widget.attrs['class'] = 'select'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'location', 'assigned_company']
        labels = {
            'assigned_company': 'Assign Management Company (Optional)',
        }
        widgets = {
            'description': forms.Textarea(attrs={'class': 'textarea', 'rows': 4}),
            'assigned_company': forms.Select(attrs={'class': 'select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
             if not isinstance(field.widget, (forms.Textarea, forms.Select)):
                field.widget.attrs['class'] = 'input'

ProjectRequirementFormSet = inlineformset_factory(
    Project, ProjectRequirement, fields=('name', 'description'),
    extra=1, can_delete=True,
    widgets={
        'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Requirement Name'}),
        'description': forms.Textarea(attrs={'class': 'textarea', 'rows': 2, 'placeholder': 'Description'}),
    }
)

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'textarea', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
             if not isinstance(field.widget, forms.Textarea):
                field.widget.attrs['class'] = 'input'
