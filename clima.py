from tkinter import *
import requests

ventana = Tk()
ventana.geometry("360x550")
ventana.resizable(1,1)
ventana.config(bg="light blue")
#Buscar ciudad
ciudadNombre=Entry(ventana, font = ('Comic Sans MS', 14), justify="center", bg="#BAF8F7")
ciudadNombre.grid(row=0, column=0, padx=50, pady=5)
#Boton buscar
buscar=Button(ventana, text="Buscar", font = ('Comic Sans MS', 10), width=10, height=2, command= lambda: busqueda(ciudadNombre.get()), bg="#BAF8F7")
buscar.grid(row=1, column=0, padx=50, pady=5)
#Mostrar Clima
ciudad=Label(font= ("Comic Sans MS", 20), bg="light blue")
ciudad.grid(row=2, column=0, padx=50, pady=5)

temperatura=Label(font= ("Comic Sans MS", 40), bg="light blue")
temperatura.grid(row=3, column=0, padx=10, pady=10)

descripcion=Label(font= ("Comic Sans MS", 20), bg="light blue")
descripcion.grid(row=4, column=0, padx=10, pady=10)

minimo=Label(font= ("Comic Sans MS", 15), bg="light blue")
minimo.grid(row=5, column=0, padx=10, pady=10)

maximo=Label(font= ("Comic Sans MS", 15), bg="light blue")
maximo.grid(row=6, column=0, padx=10, pady=10)

humedad=Label(font= ("Comic Sans MS", 10), bg="light blue")
humedad.grid(row=7, column=0, padx=10, pady=10)
#c5f363fcf0724e3f3504167ec4083a5e api key
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

#Llamar API (weather map)
def busqueda(ciudad):
    API_key = "c5f363fcf0724e3f3504167ec4083a5e"
    URL = "https://api.openweathermap.org/data/2.5/weather"
    parametros = {"APPID" : API_key, "q" : ciudad, "units" : "metrics"}
    response = requests.get(URL, params = parametros)
    clima=response.json()
    print(response.json())

    show(clima)

    print(clima["name"])
    print(clima["main"]["temp"])
    print(clima["main"]["temp_min"])
    print(clima["main"]["temp_max"])
    print(clima["main"]["humidity"])
    print(clima["weather"][0]["description"])

def show(clima):
    c = clima["name"]
    t = clima["main"]["temp"] - 273.15
    d = clima["weather"][0]["description"]
    mini = clima["main"]["temp_min"] - 273.15
    maxi = clima["main"]["temp_max"] - 273.15
    h = clima["main"]["humidity"]

    ciudad["text"] = c
    temperatura["text"] = str(t) + "°C"
    descripcion["text"] = d
    minimo["text"] = "Temperatura mínima: " + str(mini) + "°C"
    maximo["text"] = "Temperatura máxima: " + str(maxi) + "°C"
    humedad["text"] = "Humedad: " + str(h) + "%"

ventana.mainloop()