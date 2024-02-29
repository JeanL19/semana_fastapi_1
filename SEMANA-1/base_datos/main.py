from services.clientes import getclients, generateTableHTML, getClientsById, createClient, updateClient, deleteClient
from config.db import cursor, conexion
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/clientes", response_class=HTMLResponse)
async def obtener_clientes():
    clients = getclients(cursor)
    return generateTableHTML(clients)

@app.get("/clientes/{id}")
async def obtener_clientes(id:int):
    resultadoCliente = getClientsById(cursor, id)
    return resultadoCliente

@app.post("/crear-cliente")
async def   crear_cliente(Nombre: str, Contacto: str, Fecha_ingreso: str, Tipo: str, Marca: str, Modelo: str, Diagnostico: str, Estado: str):
    return createClient(cursor, conexion, Nombre, Contacto, Fecha_ingreso, Tipo, Marca, Modelo, Diagnostico, Estado)

@app.put("/actualizar-cliente/{name}")
async def actualizar_cliente(name:str, newName: str):
    return updateClient(cursor, conexion, name, newName)

@app.delete("/Eliminar-cliente/{id}")
async def eliminar_Clente(id: int):
    return deleteClient(cursor, conexion, id) 