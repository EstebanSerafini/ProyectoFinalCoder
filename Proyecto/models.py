from django.db import models

class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - E-Mail: {self.email}"

class Plan(models.Model):
    numero = models.IntegerField()
    sucursal = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=20)
    clinica = models.CharField(max_length=20)
    sanatorio = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Numero: {self.numero} - Sucursal: {self.sucursal} - Especialidad: {self.especialidad} - Clinica: {self.clinica} - Sanatorio: {self.sanatorio}"