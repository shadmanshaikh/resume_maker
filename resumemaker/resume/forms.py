from django import forms
from .models import Tool,CodingSkill,Employee,Designation

class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ('name',)


class CodingSkillForm(forms.ModelForm):
    class Meta:
        model = CodingSkill
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
#####################################################################################

class EmployeeForm(forms.ModelForm):
    tools = forms.ModelMultipleChoiceField(queryset=Tool.objects.all())
    coding_skills = forms.ModelMultipleChoiceField(queryset=CodingSkill.objects.all())
    designation = forms.ModelChoiceField(queryset=Designation.objects.all())

    class Meta:
        model = Employee
        fields = ['name', 'email', 'phone', 'linkedin' ,'professional_summary', 'tools', 'coding_skills', 'designation', 'is_current_employee']

############################################################################################

from django import forms
from .models import Projects

class MapProjectForm(forms.Form):
    projects = forms.ModelMultipleChoiceField(queryset=Projects.objects.none(), widget=forms.SelectMultiple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['projects'].queryset = Projects.objects.filter(flag=True)
################################################################################################################


# from django import forms
# from .models import Projects, Technology
# from django.db.models import Q


# class ProjectForm(forms.ModelForm):
#     technology_used = forms.ModelMultipleChoiceField(queryset=Technology.objects.all(), widget=forms.CheckboxSelectMultiple)
#     role_responsibilities = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))

#     class Meta:
#         model = Projects
#         fields = ['project_name', 'technology_used', 'description', 'role_responsibilities', 'start_date', 'end_date', 'is_active']

# class ProjectUpdateForm(forms.ModelForm):
#     technology_used = forms.ModelMultipleChoiceField(queryset=Technology.objects.all(), widget=forms.CheckboxSelectMultiple)
#     role_responsibilities = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))

#     class Meta:
#         model = Projects
#         fields = ['project_name', 'technology_used', 'description', 'role_responsibilities', 'start_date', 'end_date', 'is_active']


# from django import forms
# from .models import Projects

# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Projects
#         fields = ['project_name', 'technology_used', 'description', 'role_responsibilities', 'start_date', 'end_date', 'is_active']

from itertools import chain
from .models import Tool, CodingSkill
from django.forms.widgets import CheckboxSelectMultiple



class ProjectForm(forms.ModelForm):
    technology_used = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Projects
        fields = ['project_name', 'technology_used', 'description', 'role_responsibilities', 'start_date', 'end_date', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Update the choices attribute of the MultipleChoiceField
        tools = Tool.objects.filter(flag=True)
        coding_skills = CodingSkill.objects.filter(flag=1)
        choices = list(chain(tools, coding_skills))
        self.fields['technology_used'].choices = [(choice.name, choice.name) for choice in choices]
        self.fields['technology_used'].widget.attrs.update({'class': 'flex-row'})

    
