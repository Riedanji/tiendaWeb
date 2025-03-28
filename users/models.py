from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    correo_electronico = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre

    USERNAME_FIELD = 'correo_electronico'
    REQUIRED_FIELDS = ['nombre']
    
    
    #user = Users(nombre = 'Richard', correo_electronico = 'Richard@gmail.com',co
#ntrasena = '123456')
