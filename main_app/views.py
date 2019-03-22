from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Wishitem

# Create your views here.
def wishitems_index(request):
  wishitems = Wishitem.objects.all()

  template = 'index.html'

  context = {
    'wishitems': wishitems
  }

  return render(request, template, context)

class WishitemAdd(CreateView):
  model = Wishitem
  fields = '__all__'
  success_url = '/'

def wishitem_delete(request, wishitem_id):
  wishitem = Wishitem.objects.filter(id=wishitem_id)
  wishitem.delete()

  template = '/'

  return redirect(template)