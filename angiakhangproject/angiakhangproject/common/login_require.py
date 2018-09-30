from django.http import HttpResponseRedirect


def user_login_required(f):
    def wrap(request, *args, **kwargs):
        if 'user_login' not in request.session.keys():
            return HttpResponseRedirect("/user/login")
        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap