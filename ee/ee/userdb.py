from django.http import HttpResponse
from app.models import user

def userdb(request):
    user_int = user(username='xiao',regtime='121212',money='222')
    back = user_int.save()
    return HttpResponse(back)
