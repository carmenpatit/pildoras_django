from django.shortcuts import render
from TiendaApp.models import  Producto, Categoria

# Create your views here.
def tienda(request):

   
    productos_list = Producto.objects.all()

    return render ( request , 'tienda/tienda.html', {'productos_list':productos_list } )
