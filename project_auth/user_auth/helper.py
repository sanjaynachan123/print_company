import os
from .models import CustomUser


    
def check_super_admin(request):
    user = request.user
    user_roles = get_all_user_roles(user)
    if user_roles:
        return 'SUPER_ADMIN' in user_roles
    else:
        return False

def check_end_user(request):
    user = request.user
    user_roles = get_all_user_roles(user)
    if user_roles:
        return 'END_USER' in user_roles
    else:
        return False    

def get_all_user_roles(user):
    if isinstance(user,CustomUser):
        user_roles = user.userrole_set.all()
        return [str(user_role.role) for user_role in user_roles]
    else:
        return []     

def check_end_user_objects(request,obj):
    user = request.user
    if isinstance(obj,CustomUser):
        return user.id == obj.id     

def update_path(path):
    return os.path.normpath(path).replace('\\', '/')
