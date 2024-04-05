from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Cliente
#from .forms import ClienteForm

def clientes_view(request):
    # Obtener todos los clientes de la base de datos
    clientes = Cliente.objects.all()

    # Paginar los clientes (por ejemplo, 10 clientes por página)
    paginator = Paginator(clientes, 1)

    # Obtener el número de página de la URL (si no se especifica, será la primera página)
    page_number = request.GET.get('page')
    
    # Obtener la página actual
    page_obj = paginator.get_page(page_number)

    # Renderizar la plantilla con los datos paginados
    return render(request, 'cliente.html', {'page_obj': page_obj})

"""
def vista_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente.html')  # Redirige a una página de confirmación o donde necesites
    else:
        form = ClienteForm()
    return render(request, 'vista_cliente.html', {'form': form})
"""