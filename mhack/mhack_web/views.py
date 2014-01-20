from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from mhack_web import models as m
from django import template
from django.template.defaultfilters import stringfilter
from django.template import RequestContext,loader

register = template.Library()
# Create your views here.
name=""
friends_info = [{'birthday': '04/06', 'id': '517614939', 'name': 'Shannon Hunter'}, {'birthday': '07/14/1994', 'id': '1306797872', 'name': 'Kaylee Marie Allen'}, {'birthday': '09/15', 'id': '100000073500871', 'name': 'Jada Leigh'}, {'birthday': '09/07/1994', 'id': '100000351939887', 'name': 'April Roulette'}, {'birthday': '12/22', 'id': '100001348159093', 'name': 'Heidi Butler'}, {'birthday': '09/06/1995', 'id': '100001361974023', 'name': 'Xena Roulette'}, {'birthday': '12/22', 'id': '100001402788224', 'name': 'Sammy Leckie'}, {'birthday': '07/03', 'id': '100002690531733', 'name': 'Mercedes Heaven Beaar'}, {'birthday': '07/15/1994', 'id': '100002957226119', 'name': 'Savanah Littlejohn'}]

u=m.temp(friends_info)
info=m.UserList



def postcard(request):
	#t=request.GET.get('postcard','')
	return render_to_response('postcard.html',{'name':name})

def mug(request):
	#t=request.GET.get('postcard','')
	return render_to_response('mug.html',{'name':name})

def login3(request):
	t=request.GET.get('m','')
	global name
	name=t
	return render_to_response('login3.html',{'name':t})

def order(request):
	t=request.GET.get('m','')
	return render_to_response('order.html',{'name':t})

def poster(request):
	t=request.GET.get('m','')
	return  render_to_response('poster.html',{'name':t})

def login2(request):
	t=get_template('login2.html')
	c=Context({"info":info})
	return HttpResponse(t.render(c))
	#c=RequestContext(request,{'1':2,
	#'2':3,
	#'4':5})
	#return render_to_response('login2.html',{"info":info})
	return render_to_response('login2.html',c)

def login(request):
	t=get_template('login.html')
	c=Context()
	return HttpResponse(t.render(c))

"""@register.filter
def lookup(d,key):
	return d[key]"""

def friends(request):
	t=get_template('friends.html')
	c=Context()
	return HttpResponse(t.render(c))