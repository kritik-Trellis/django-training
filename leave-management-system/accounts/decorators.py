from django.http import HttpResponse
from django.shortcuts import redirect


# def unauthenticated_user(view_func):
#     def wrapper_func(request,*args,**kwargs):
#         if not request.user.is_authenticated:
#             return view_func(request,*args,**kwargs)
#     return wrapper_func


def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args,**kwargs):
            group=None
            if(request.user.groups.exists()):
                group=request.user.groups.all()[0].name
            if group==allowed_roles[0]:
                return redirect('admin')
            if group==allowed_roles[1]:
                return redirect('employee')
            if group==allowed_roles[2]:
                return redirect('manager')
            


            print("Working",allowed_roles)
            return view_func(request,*args,**kwargs)
        return wrapper_func
    return decorator
