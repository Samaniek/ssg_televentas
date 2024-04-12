from django.db import models

class Cliente(models.Model):
    
    cedula = models.CharField(primary_key=True, max_length=20)
    genero = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    zurdo = models.BooleanField(default=False)
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100, blank=True, null=True)
    primer_apellido = models.CharField(max_length=100)
    segundo_apellido = models.CharField(max_length=100, blank=True, null=True)
    estado_civil = models.IntegerField()
    fecha_nacimiento = models.DateField()
    mascota = models.BooleanField(default=False)
    ocupacion = models.IntegerField()
    telefono1 = models.CharField(max_length=100)
    telefono2 = models.CharField(max_length=100, blank=True, null=True)
    telefono3 = models.CharField(max_length=100, blank=True, null=True)
    telefono4 = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=255)
    calle1 = models.CharField(max_length=255, blank=True, null=True)
    calle2 = models.CharField(max_length=255, blank=True, null=True)
    departamento = models.IntegerField()
    barrio = models.IntegerField()
    

class Meta:
    verbose_name='cliente'
    verbose_name_plural='clientes'


class Notas(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto


#class Operador(models.Model):
    # Si necesitas guardar información específica del operador, agrégala aquí
    #pass
