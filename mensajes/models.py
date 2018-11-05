from django.db import models

# Create your models here.
class sugerencias(models.Model):
    nombre = models.CharField(max_length = 250, default = ' ')

    correo = models.CharField(max_length = 250, default = ' ')

    sugerencia = models.CharField(max_length = 2000, default = '')

    '''
    esto es para que en la terminal de PS
    se ensenien los datos de la base y no solo tonteras
    al escribir sugerencias.objects.all()
    '''
    def __str__(self):  
        return ("nombre: {}, correo: {}, sugerencia: {}".format(self.nombre, self.correo, self.sugerencia)) 