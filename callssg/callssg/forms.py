from django import forms
from .models import Cliente, Notas

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('cedula', 'genero', 'zurdo', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido', 'estado_civil', 'fecha_nacimiento', 'mascota', 'ocupacion', 'telefono1', 'telefono2', 'telefono3', 'telefono4', 'email', 'direccion', 'calle1', 'calle2', 'departamento','barrio')
        labels = {
            'cedula': 'Cedula del Cliente: ',
            'genero': 'Genero',
            'zurdo': 'Zurdo',
            'primer_nombre': 'Primer Nombre: ',
            'segundo_nombre': 'Segundo Nombre: ',
            'primer_apellido': 'Primer Apellido: ',
            'segundo_apellido': 'Segundo Apellido: ',
            'estado_civil': 'Estado Civil: ',
            'fecha_nacimiento': 'Fecha de Nacimiento: ',
            'mascota': 'Mascota: ',
            'ocupacion': 'Ocupacion: ',
            'telefono1': 'Telefono1: ',
            'telefono2': 'Telefono2: ',
            'telefono3': 'Telefono3: ',
            'telefono4': 'Telefono4: ',
            'email': 'Email: ',
            'direccion': 'Direccion: ',
            'calle1': 'Calle1: ',
            'calle2': 'Calle2: ',
            'departamento': 'Departamento: ',
            'barrio': 'barrio: '
        }

class NotasForm(forms.ModelForm):
    class Meta:
        model = Notas
        fields = ['notas']