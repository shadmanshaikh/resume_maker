from . import views
from django.conf import settings
from django.conf.urls.static import static


from .views import project_list, project_create, project_edit, project_delete



from django.urls import path,include

urlpatterns = [
    path('', views.userlogin,name='login'),
    path('dashboard',views.home,name='dashboard'),
   
    path('logout',views.userlogout,name='logout'),

     path('tools-list', views.tools_list, name='tools_list'),
    path('create_tool/', views.create_tool, name='create_tool'),
    path('edittools/<int:pk>/', views.edit_tool, name='edit_tool'),
    path('deletetools/<int:pk>/', views.delete_tool, name='delete_tool'),

    path('coding-list', views.coding_list, name='coding_list'),
    path('createcodingskill/', views.create_coding_skill, name='create_coding_skill'),
    path('<int:coding_skill_id>/editcodingskill/', views.edit_coding_skill, name='edit_coding_skill'),
    path('<int:coding_skill_id>/deletecodingskill/', views.delete_coding_skill, name='delete_coding_skill'),

    #path('projects-list', views.projects_list, name='projects_list'),
    #path('create_project/', views.create_project, name='create_project'),
    # path('editprojects/<int:pk>/', views.edit_project, name='edit_project'),
    # path('deleteprojects/<int:pk>/', views.delete_project, name='delete_project'),

    # path('Project_list', views.project_list, name='project_list'),
    # path('create-project/', views.project_create, name='create_project'),
    # path('edit-project/<int:pk>/', views.project_update, name='edit_project'),
    # path('delete-project/<int:pk>/', views.project_delete, name='delete_project'),
 
    path('project_list', project_list, name='project_list'),
    path('create-project/', project_create, name='project_create'),
    path('<int:pk>/editproject/', project_edit, name='project_edit'),
    path('<int:pk>/deleteproject/', project_delete, name='project_delete'),
 
##########################################################################################
    path('employee-list', views.employee_list, name='list'),
    path('create-employee/', views.employee_create, name='create'),
    path('<int:id>/edit-employee/', views.employee_edit, name='edit'),
    path('<int:id>/delete-employee/', views.employee_delete, name='delete'),
##########################################################################################
   
    path('view_resume/<int:id>', views.view_resume, name="view_resume"),

##########################################################################################

    path('projectmap/<int:id>', views.map_project,name="map_project"),
 



]






