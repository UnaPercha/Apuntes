from django.http import HttpResponse

def saludo(request): #para crear una vista debemos pasarle la variable 'request' de la librería HttpResponse a una función como primer parámetro. Esto enviará una request al servidor
    return HttpResponse("Hola mamaguebo") #para mostrar lo que queremos en pantalla debemos usar el objeto HttpResponse el cual responderá a la request del servidor con un "Hola mamaguebo"
#una vez hecha la vista ir al archivo urls.py para indicarle a python donde lo queremos mostrar

def byebye(request):
    return HttpResponse("Bye bye carechimbas")