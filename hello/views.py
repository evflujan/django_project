from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

name = 'hello'

def myview(request):

    cookie_name = 'dj4e_cookie'
    if cookie_name in request.COOKIES:
        value = request.COOKIES[cookie_name]
    else:
        value = 'e001afac'

    session_name = 'view_count'
    if session_name not in request.session:
        count = 1
    else:
        count = request.session[session_name] + 1

    if count > 3:
        count = 1

    request.session[session_name] = count

    msg = 'view count=' + str(count)

    response = HttpResponse(msg, content_type='text/html', charset='utf-8')

    response.set_cookie(cookie_name, value, max_age = None, expires = None)

    return response
