from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

name = 'hello'

def myview(request):

    if 'dj4e_cookie' in request.COOKIES:
        value = request.COOKIES['dj4e_cookie']
    else:
        value = ''

    if value:
        count = int(value[-1])
        count += 1
    else:
        count  = 1

    if count > 9:
        count  = 1

    value = 'e001afac' + ' - ' + 'view count=' + str(count)

    cookie_name = 'dj4e_cookie'

    msg = value
    response = HttpResponse(msg, content_type='text/html', charset='utf-8')

    response.set_cookie(cookie_name, value, max_age = None, expires = None)

    return response
