from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from settings import *

from healthvaultlib.helpers.connection import Connection
from healthvaultlib.methods.getthings import GetThings
from healthvaultlib.objects.thinggroup import ThingGroup
from healthvaultlib.objects.thingfilter import ThingFilter
from healthvaultlib.objects.thingformat import ThingFormat

from lxml import etree

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
        wctoken = ''
        if request.method == 'GET':
            wctoken = request.GET['wctoken']
        else:
            wctoken = request.POST['wctoken']
        set_authenticated_connection(request, wctoken)
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
    height_filter = ThingFilter()
    height_format = ThingFormat()
    height_format.sections.append('core')
    height_format.sections.append('xml')
    height_filter.typeids.append('40750a6a-89b2-455c-bd8d-b420a4cb500b')
    height_group = ThingGroup()
    height_group.filters = [height_filter]
    height_group.format = height_format
    height_group.max = 10

    basic_filter = ThingFilter()
    basic_format = ThingFormat()
    basic_format.sections.append('core')
    basic_filter.typeids.append('3b3e6b16-eb69-483c-8d7e-dfe116ae6092')
    basic_group = ThingGroup()
    basic_group.filters = [basic_filter]
    basic_group.format = basic_format


    method = GetThings([height_group, basic_group])
    method.execute(request.session['connection'])
    args = {}
    keys = []
    args['demographic'] = method.response.groups[1].healthrecorditems[0]
    args['heights'] = method.response.groups[0].healthrecorditems
    return render_to_response('hvdata.html', args)

def set_authenticated_connection(request, wctoken):
    if 'connection' in request.session:
        del request.session['connection']
    conn = Connection(HV_APPID, HV_SERVICE_SERVER)
    conn.thumbprint = APP_THUMBPRINT
    conn.publickey = APP_PUBLIC_KEY
    conn.privatekey = APP_PRIVATE_KEY
    conn.user_auth_token = wctoken
    conn.connect()
    conn.set_person_and_record_from_personinfo()
    request.session['connection'] = conn
