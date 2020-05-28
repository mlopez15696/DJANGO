from django.http import HttpResponse
from django.template.loader import get_template


class views():

    def home(self):
        plantilla=get_template('index.html')
        return HttpResponse(plantilla.render())

    def formularioI(self):
        plantilla=get_template('formularioI.html')
        return HttpResponse(plantilla.render())

    def formularioII(self):
        plantilla=get_template('formularioII.html')
        return HttpResponse(plantilla.render())

    def formularioIII(self):
        plantilla=get_template('formularioIII.html')
        return HttpResponse(plantilla.render())

    def formularioIV(self):
        plantilla=get_template('formularioIV.html')
        return HttpResponse(plantilla.render())

    def formularioV(self):
        plantilla=get_template('formularioV.html')
        return HttpResponse(plantilla.render())
