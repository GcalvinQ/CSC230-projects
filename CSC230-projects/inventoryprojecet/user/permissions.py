from django.contrib.auth.models import Permission

class UserPermsissions(Permission):
    # Add any additional fields or methods as needed
    description = 'Permissions'