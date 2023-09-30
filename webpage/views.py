from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import  Hplaptop
from .models import  Dell_laptop
from .models import  Toshiba_laptop
from .models import Techno_phone
from .models import  Redmi_phone
from .models import Infinix_phone

def main(request):
   template = loader.get_template("main.html")
   return HttpResponse(template.render())

def products(request):
   template = loader.get_template("products.html")
   return HttpResponse(template.render())

def Laptop_to_choose(request):
   template = loader.get_template("Laptop_to_choose.html")
   return HttpResponse(template.render())

def Phone_to_choose(request):
   template = loader.get_template("Phone_to_choose.html")
   return HttpResponse(template.render())

def Hplaptops(request):
   hp = Hplaptop.objects.all().values()
   template = loader.get_template("Hplaptops.html")
   context = {
      "hp" : hp,
   }
   return HttpResponse(template.render(context, request))

def Hpdetails(request, id):
   hp = Hplaptop.objects.get(id=id)
   template = loader.get_template("Hpdetails.html")
   context = {
      "hp" : hp,
   }
   return HttpResponse(template.render(context, request))

def Dell_laptops(request):
   dell = Dell_laptop.objects.all().values()
   template = loader.get_template("Dell_laptops.html")
   context = {
      "dell" : dell,
   }
   return HttpResponse(template.render(context, request))

def Dell_details(request, id):
   dell = Dell_laptop.objects.get(id=id)
   template = loader.get_template("Dell_details.html")
   context = {
      "dell" : dell,
   }
   return HttpResponse(template.render(context, request))


def Toshiba_laptops(request):
   toshiba = Toshiba_laptop.objects.all().values()
   template = loader.get_template("Toshiba_laptops.html")
   context = {
      "toshiba" : toshiba
   }
   return HttpResponse(template.render(context, request))

def Toshiba_details(request, id):
   toshiba = Toshiba_laptop.objects.get(id=id)
   template = loader.get_template("Toshiba_details.html")
   context = {
      "toshiba" : toshiba,
   }
   return HttpResponse(template.render(context, request))

def Techno_phones(request):
   techno = Techno_phone.objects.all().values()
   template = loader.get_template("Techno_phones.html")
   context = {
      "techno" : techno,
   }
   return HttpResponse(template.render(context, request))

def Techno_details(request, id):
   techno = Techno_phone.objects.get(id=id)
   template = loader.get_template("Techno_details.html")
   context = {
      "techno" : techno,
   }
   return HttpResponse(template.render(context, request))

def Redmi_phones(request):
   redmi = Redmi_phone.objects.all().values()
   template = loader.get_template("Redmi_phones.html")
   context = {
      "redmi" : redmi,
   }
   return HttpResponse(template.render(context, request))

def Redmi_details(request, id):
   redmi = Redmi_phone.objects.get(id=id)
   template = loader.get_template("Redmi_details.html")
   context = {
      "redmi" : redmi
   }
   return HttpResponse(template.render(context, request))

def Infinix_phones(request):
   infinix = Infinix_phone.objects.all().values()
   template = loader.get_template("Infinix_phones.html")
   context = {
      "infinix" : infinix,
   }
   return HttpResponse(template.render(context, request))

def Infinix_details(request, id):
   infinix = Infinix_phone.objects.get(id=id)
   template = loader.get_template("Infinix_details.html")
   context = {
      "infinix" : infinix,
   }
   return HttpResponse(template.render(context, request))






# Create your views here.

