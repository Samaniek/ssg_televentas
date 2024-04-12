from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Cliente, Notas
from .forms import NotasForm
from django.shortcuts import get_object_or_404
#from .forms import ClienteForm

def clientes_view(request):
    # Obtener todos los clientes de la base de datos
    clientes = Cliente.objects.all().order_by('cedula')
    
    # Paginar los clientes (por ejemplo, x clientes por página)
    paginator = Paginator(clientes, 1)
    
    # Obtener el número de página de la URL (si no se especifica, será la primera página)
    page_number = request.GET.get('page')
    
    # Obtener la página actual
    page_obj = paginator.get_page(page_number)
    
    # Obtener la cédula del cliente actual, si no se proporciona, tomar el primer cliente de la base de datos
    cliente_id = request.POST.get('cliente')
    if not cliente_id:
        primer_cliente = clientes.first()
        if not primer_cliente:
            return HttpResponse("No hay clientes en la base de datos")  # O maneja de alguna otra manera si no hay clientes
        cliente_id = primer_cliente.cedula

    # Obtener el cliente actual
    cliente = get_object_or_404(Cliente, cedula=cliente_id)

    # Obtener la última nota del cliente
    ultima_nota = cliente.notas_set.last()

    if request.method == 'POST':
        form = NotasForm(request.POST)
        if form.is_valid():
            nota_texto = form.cleaned_data['texto']
            if ultima_nota:
                # Si ya hay una nota para este cliente, actualízala
                ultima_nota.texto = nota_texto
                ultima_nota.save()
            else:
                # Si no hay una nota para este cliente, crea una nueva
                nueva_nota = Notas(cliente=cliente, texto=nota_texto)
                nueva_nota.save()
            return redirect('clientes_view')  # Redirige a la vista para evitar resubmitir el formulario
    else:
        form = NotasForm(initial={'cliente': cliente_id})  # Inicializa el formulario con el ID del cliente
    
    # Renderizar la plantilla con los datos paginados y el formulario de notas
    context = {'page_obj': page_obj, 'form': form, 'ultima_nota': ultima_nota}
    return render(request, 'cliente.html', context)

"""
def agregar_notas(request):
    if request.method == 'POST':
        form = NotasForm(request.POST)
        if form.is_valid():
            form.save()
            notas = form.cleaned_data['notas']
            print("Notas guardadas:", notas)  # Agregar este print para verificar el guardado de las notas

             # Recuperar las notas guardadas en la base de datos
            notas_guardadas = Notas.objects.all()  # Asegúrate de importar el modelo Notas
            return render(request, 'agregar_notas.html', {'form': form, 'notas_guardadas': notas_guardadas})

            # Guardar las notas en la base de datos
        return redirect('cliente')  # Cambia 'clientes' por la ruta correcta a tu vista de clientes
    else:
        form = NotasForm()
    return render(request, 'agregar_notas.html', {'form': form})
"""

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