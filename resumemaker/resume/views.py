from io import BytesIO
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User



def userlogin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
            
    return render (request,'login.html')

@login_required(login_url='/')
def home(request):
    tool_count = Tool.objects.count()
    coding_skill_count = CodingSkill.objects.count()
    project_count = Projects.objects.count()
    employee_count = Employee.objects.count()

    context = {
        'tool_count': tool_count,
        'coding_skill_count': coding_skill_count,
        'project_count': project_count,
        'employee_count': employee_count,
    }
    return render(request, 'dashboard.html', context)
def userlogout(request):
    logout(request)
    return redirect('/')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Tool
from .forms import ToolForm


def tools_list(request):
    tools = Tool.objects.filter(flag=True)
    return render(request, 'tools_list.html', {'tools': tools})

def create_tool(request):
    if request.method == 'POST':
        form = ToolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tools_list')
    else:
        form = ToolForm()
    return render(request, 'tool_form.html', {'form': form})

def edit_tool(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    if request.method == 'POST':
        form = ToolForm(request.POST, instance=tool)
        if form.is_valid():
            form.save()
            return redirect('tools_list')
    else:
        form = ToolForm(instance=tool)
    return render(request, 'tool_form.html', {'form': form})

def delete_tool(request, pk):
    tool = get_object_or_404(Tool, pk=pk)
    tool.flag = False
    tool.save()
    return redirect('tools_list')
from .forms import CodingSkillForm
from .models import CodingSkill

def coding_list(request):
    coding_skills = CodingSkill.objects.filter(flag=1)
    return render(request, 'coding_list.html', {'coding_skills': coding_skills})

def create_coding_skill(request):
    if request.method == 'POST':
        form = CodingSkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coding_list')
    else:
        form = CodingSkillForm()
    return render(request, 'create_coding_skill.html', {'form': form})

def edit_coding_skill(request, coding_skill_id):
    coding_skill = get_object_or_404(CodingSkill, id=coding_skill_id)
    if request.method == 'POST':
        form = CodingSkillForm(request.POST, instance=coding_skill)
        if form.is_valid():
            form.save()
            return redirect('coding_list')
    else:
        form = CodingSkillForm(instance=coding_skill)
    return render(request, 'edit_coding_skill.html', {'form': form, 'coding_skill': coding_skill})

def delete_coding_skill(request, coding_skill_id):
    coding_skill = get_object_or_404(CodingSkill, id=coding_skill_id)
    coding_skill.flag = 0
    coding_skill.save()
    return redirect('coding_list')





################################################################################
from django.shortcuts import render
from .models import Employee
from django.shortcuts import render, redirect
from .forms import EmployeeForm
from django.shortcuts import render, get_object_or_404, redirect
from .forms import EmployeeForm
from .models import Employee
from django.shortcuts import get_object_or_404, redirect
from .models import Employee


def employee_list(request):
    employees = Employee.objects.filter(is_deleted=False)
    return render(request, 'employee_list.html', {'employees': employees})


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})


def employee_edit(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})



def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.is_deleted = True
    employee.save()
    return redirect('list')


##########################################################################################
#pdf and word filegeneration
import ast

def view_resume(request,id):
    employee = get_object_or_404(Employee, id=id)
    ename = employee.name
    edesignation=employee.designation
    eeamil = employee.email
    ephone = employee.phone
    elinkedin = employee.linkedin
    epsummery = employee.professional_summary.split('#')
    etools=employee.tools.all()
    eskill=employee.coding_skills.all()
    eid=id
    eproject=employee.mapped_project.all()

    for project in eproject:
        project.role_responsibilities = project.role_responsibilities.split('#')
        project.technology_used = ast.literal_eval(project.technology_used)
       

    context = {
        'ename': ename,
        'edesignation': edesignation,
        'eemail' : eeamil,
        'ephone' : ephone,
        'elinkedin' : elinkedin,
        'epsummery': epsummery,
        'etools': etools,
        'eskill': eskill,
        'eid': eid,
        'eproject': eproject,

        }
    
    return render(request, 'resume.html', context)




################################################################################################


from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Employee, Projects
from .forms import MapProjectForm

def map_project(request,id):
    employee = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = MapProjectForm(request.POST)
        if form.is_valid():
            projects = form.cleaned_data['projects']
            employee.mapped_project.set(projects)
            return redirect('list')
    else:
        form = MapProjectForm()
        form.fields['projects'].queryset = Projects.objects.filter(flag=True)
    return render(request, 'map_project.html', {'form': form})

#########################################################################################


# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Projects,Technology
# from .forms import ProjectForm, ProjectUpdateForm

# def project_list(request):
#     projects = Projects.objects.filter(flag=1)
#     context = {'projects': projects}
#     return render(request, 'project_list.html', context)

# def project_create(request):
#     form = ProjectForm(request.POST or None)
#     tech = Technology.objects.all()
#     if form.is_valid():
#         form.save()
#         return redirect('project_list')
#     context = {'form': form , 'tech':tech}
#     return render(request, 'create_project.html', context)

# def project_update(request, pk):
#     project = get_object_or_404(Projects, pk=pk)
#     tech = Technology.objects.all()
#     form = ProjectUpdateForm(request.POST or None, instance=project)
#     if form.is_valid():
#         form.save()
#         return redirect('project_list')
#     context = {'form': form, 'project': project,'tech':tech}
#     return render(request, 'edit_project.html', context)

# def project_delete(request, pk):
#     project = get_object_or_404(Projects, pk=pk)
#     if request.method == 'POST':
#         project.flag = 0
#         project.save()
#         return redirect('project_list')
#     context = {'project': project}
#     return render(request, 'project_delete.html', context)

from django.shortcuts import render
from .models import Projects

def project_list(request):
    projects = Projects.objects.filter(flag=1)
    context = {'projects': projects}
    return render(request, 'project_list.html', context)
from django.shortcuts import render, redirect
from .forms import ProjectForm

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    context = {'form': form}
    return render(request, 'project_create.html', context)

    
from django.shortcuts import render, get_object_or_404, redirect
from .models import Projects
from .forms import ProjectForm

def project_edit(request, pk):
    project = get_object_or_404(Projects, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    context = {'form': form}
    return render(request, 'edit_project.html', context)

from django.shortcuts import get_object_or_404, redirect, render
from .models import Projects
from .forms import ProjectForm

def project_delete(request, pk):
    project = get_object_or_404(Projects, pk=pk)
    if request.method == 'POST':
        project.flag = 0  # Soft delete the project by setting flag to 0
        project.save()
        return redirect('project_list')
    context = {'project': project}
    return render(request, 'delete_project.html', context)