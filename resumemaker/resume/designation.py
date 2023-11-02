from .models import Designation



# create a list of Designation instances
designations = [
    {'name': 'Software Engineer'},
    {'name': 'Senior Software Engineer'},
    {'name': 'Technical Lead'},
    {'name': 'Project Manager'},
    {'name': 'Product Manager'},
    {'name': 'Business Analyst'},
    {'name': 'Quality Assurance Engineer'},
    {'name': 'UI/UX Designer'},
    {'name': 'Data Scientist'},
    {'name': 'DevOps Engineer'}
]

# insert the records into the database
Designation.objects.bulk_create([Designation(**d) for d in designations])


# python manage.py shell

# >>> from app_name.models import Designation
# >>> designations = [
# ...     {'name': 'Software Engineer'},
# ...     {'name': 'Senior Software Engineer'},
# ...     {'name': 'Technical Lead'},
# ...     {'name': 'Project Manager'},
# ...     {'name': 'Product Manager'},
# ...     {'name': 'Business Analyst'},
# ...     {'name': 'Quality Assurance Engineer'},
# ...     {'name': 'UI/UX Designer'},
# ...     {'name': 'Data Scientist'},
# ...     {'name': 'DevOps Engineer'}
# ... ]
# >>> for d in designations:
# ...     new_designation = Designation(**d)
# ...     new_designation.save()

# >>> exit()
