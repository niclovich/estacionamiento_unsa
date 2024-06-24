from django.db import models

# Create your models here.
class Dependencia(models.Model):
    id_depe = models.AutoField(primary_key=True)
    nomb_depe = models.CharField(max_length=255)

    def __str__(self):
        return self.nomb_depe
    
#Docente , NO Docente , ETC    
class Escalafon(models.Model):
    id_escala = models.AutoField(primary_key=True)
    nomb_escala = models.CharField(max_length=255)

    def __str__(self):
        return self.nomb_escala


class Categoria(models.Model):
    id_cate = models.AutoField(primary_key=True)
    nomb_cate = models.CharField(max_length=255)

    def __str__(self):
        return self.nomb_cate
    
class Usuario(models.Model):
    nomb_usuario = models.CharField(max_length=255)
    apel_usuario = models.CharField(max_length=255)
    dni_usuario = models.CharField(max_length=20, unique=True)
    correo_usuario = models.EmailField(unique=True)
    password_usuario = models.CharField(max_length=255)
    fechanac_usuario = models.DateField()
    id_cate = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    id_escala = models.ForeignKey(Escalafon, on_delete=models.CASCADE)
    id_depe = models.ForeignKey(Dependencia, on_delete=models.CASCADE)
    legajo_usuario = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nomb_usuario} {self.apel_usuario}"