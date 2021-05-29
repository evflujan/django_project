# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
import datetime

name = 'httprequest'

def data(request):

    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    cookies = request.COOKIES

    msg = f'''
<html>
Path: {path}<br>
Scheme: {scheme}<br>
Method: {method}<br>
Address: {address}<br>
User agent: {user_agent}<br>
Cookies: {cookies}<br>
Cookie_value: {value}

</html>
'''
    response = HttpResponse(msg, content_type='text/html', charset='utf-8')

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

    if count > 3:
        value = 'e001afac'
    else:
        value = 'e001afac' + ' - ' + 'view count=' + str(count)

    cookie_name = 'dj4e_cookie'

    response.set_cookie(cookie_name, value, max_age = None, expires = None)


    return response



def now(request):
    now = datetime.datetime.now()
    msg = f'Today is {now}'
    return HttpResponse(msg, content_type='text/html', charset='utf-8')


def SetSession(request):
    request.session['author'] = 'Sir Arthur Conan Doyle'
    return HttpResponse('The Session has been successfully set')


def GetSession(request):
    author = request.session['author']
    return HttpResponse(f'The author is: {author}')
