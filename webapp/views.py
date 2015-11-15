from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from settings import *

from healthvaultlib.helpers.connection import Connection
from healthvaultlib.methods.getthings import GetThings

def index(request):
  loginurl = HV_SHELL_URL+"/redirect.aspx?target=AUTH&targetqs=?appid="+HV_APPID+"%26redirect="+APP_ACTION_URL
  template_values = {'loginurl':loginurl,
      'HV_APPID':HV_APPID,
    'APP_ACTION_URL':APP_ACTION_URL,
    'HV_SHELL_URL':HV_SHELL_URL,
    'HV_SERVICE_SERVER': HV_SERVICE_SERVER,
    'APP_PUBLIC_KEY': APP_PUBLIC_KEY[:20]+"...",
    'APP_PRIVATE_KEY':APP_PRIVATE_KEY[:20]+"...",
    'APP_THUMBPRINT':APP_THUMBPRINT[:20]+"...",
      }
  return render_to_response('index.html', template_values)

def mvaultaction(request):
     target = ''
     if request.GET.has_key('target'):
         target  = request.GET['target']
     else:
        return HttpResponse('')
     target = target.lower()
     if target == "home":
        return HttpResponseRedirect('/')
     if target == "appauthsuccess":
        set_authenticated_connection(request, request.GET['wctoken'])
        return HttpResponseRedirect('/mvaultentry?target=appauthsuccess')
     if target == "serviceagreement":
        return HttpResponseRedirect('/YouAPPTermsOfService.html')
     if target == "help":
        return HttpResponseRedirect('/YourAppHelp.html')
     if target == "privacy":
        return HttpResponseRedirect('/YourAppPrivacy.html')
     if target == "appAuthreject":
        return HttpResponseRedirect('/')
     if target == "selectedrecordchanged":
        return HttpResponseRedirect('/')
     if target == "sharerecordsuccess":
        return HttpResponseRedirect('/')
     if target == "sharerecordfailed":
        return HttpResponseRedirect('/')
     if target == "signout":
        del request.session['connection']
        return HttpResponseRedirect('/')
     return HttpResponse('')

def mvaultentry(request):
    method = GetThings()
    method.execute(request.session['connection'])
    return render_to_response('hvdata.html', {})

def set_authenticated_connection(request, wctoken):
    if 'connection' not in request.session:
        conn = Connection(HV_APPID, HV_SERVICE_SERVER)
        conn.thumbprint = APP_THUMBPRINT
        conn.user_auth_token = wctoken
        conn.connect()
        conn.set_person_and_record_from_personinfo()
        request.session['connection'] = conn
