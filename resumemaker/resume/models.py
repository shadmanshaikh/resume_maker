from django.db import models


class Tool(models.Model):
    name = models.CharField(max_length=100)
    flag = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class CodingSkill(models.Model):
    name = models.CharField(max_length=255)
    flag = models.IntegerField(default=1)

    def __str__(self):
        return self.name

################################################################################

class Projects(models.Model):
    project_name = models.CharField(max_length=255)
    technology_used = models.CharField(max_length=255)
    description = models.TextField()
    role_responsibilities = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    flag = models.BooleanField(default=1)

    def __str__(self):
        return self.project_name

    

        
################################################################################
class Designation(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=20)
    linkedin = models.URLField(max_length=200)
    professional_summary = models.TextField()
    tools = models.ManyToManyField(Tool)
    coding_skills = models.ManyToManyField(CodingSkill)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    is_current_employee = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    mapped_project = models.ManyToManyField(Projects)
    
    def __str__(self):
        return self.name


#################################################################################


