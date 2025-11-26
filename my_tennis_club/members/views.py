from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from .models import Member
from django.db.models import Q

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def details(request, id):
  try:
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
      'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))
  except Member.DoesNotExist:
    template = loader.get_template('404.html')
    return HttpResponse(template.render({}, request), status=404)

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render({}, request))

def myfirst(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render({}, request))

def custom_404(request, exception=None):
  template = loader.get_template('404.html')
  return HttpResponse(template.render({}, request), status=404)


def testing(request):
  template = loader.get_template('template.html')
  miembros = Member.objects.all().values()
  column_firstnames = Member.objects.values_list('firstname')
  records_firtname = Member.objects.filter(firstname = 'Andres').values()
  records_OR_andres = Member.objects.filter(Q(firstname='Andres') | Q(firstname='andres')).values()
  startwith_a = Member.objects.filter(firstname__startswith='a').values()
  iendswith_s = Member.objects.filter(lastname__iendswith='s').values() 
  contains_e = Member.objects.filter(email__contains='e').values()
  range_id = Member.objects.filter(id__range=(2,4)).values()
  range_letras= Member.objects.filter(firstname__range=('a','m')).values()
  filter_id_gt = Member.objects.filter(id__gt=3).values()
  orderby_firstname = Member.objects.all().order_by('firstname').values()
  orderby_lastname_desc = Member.objects.all().order_by('-lastname').values()
  
  context = {
  'fruits': ['Apple', 'Banana', 'Cherry'], 
  'miembros': miembros,
  'column_firstnames': column_firstnames,
  'records_firtname': records_firtname,
  'records_OR_andres': records_OR_andres,
  'startwith_a': startwith_a,
  'iendswith_s': iendswith_s, 
  'contains_e': contains_e,
  'range_id': range_id,
  'range_letras': range_letras,
  'filter_id_gt': filter_id_gt,
  'orderby_firstname': orderby_firstname,
  'orderby_lastname_desc': orderby_lastname_desc,
  }
  return HttpResponse(template.render(context, request))