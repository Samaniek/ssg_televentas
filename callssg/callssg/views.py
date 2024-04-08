from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Cliente, Notas
from .forms import NotasForm

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

    # Renderizar la plantilla con los datos paginados
    context = {'page_obj': page_obj}
    return render(request, 'cliente.html', context)


def agregar_notas(request):
    if request.method == 'POST':
        form = NotasForm(request.POST)
        if form.is_valid():
            form.save()
            notas = form.cleaned_data['notas']
            print("Notas guardadas:", notas)  # Agregar este print para verificar el guardado de las notas

            # Recuperar las notas guardadas en la base de datos
            notas_guardadas = Notas.objects.all()  # Asegúrate de importar el modelo Notas
            print("Notas recuperadas de la base de datos:", notas_guardadas)  # Agregar este print para verificar las notas recuperadas

            return redirect('cliente')  # Redirigir a la página de clientes si el formulario es válido
    else:
        form = NotasForm()

    # Recuperar las notas guardadas en la base de datos
    notas_guardadas = Notas.objects.all()
    return render(request, 'agregar_notas.html', {'form': form, 'notas_guardadas': notas_guardadas})

















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