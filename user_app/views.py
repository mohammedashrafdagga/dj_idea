from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def main(request):

    return HttpResponse(str(f'Hello User  {request.user.first_name} {request.user.last_name} in app.'))
