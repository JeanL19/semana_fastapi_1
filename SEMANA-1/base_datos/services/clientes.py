def getclients(cursor):
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    clientesDict = []

    for cliente in clientes:
        clienteDict = {
            "id":cliente[0],
            "Nombre": cliente[1],
            "Contacto" : cliente[2],
            "Fecha_ingreso": cliente[3],
            "Tipo": cliente[4],
            "Marca": cliente[5],
            "Modelo": cliente[6],
            "Diagnostico": cliente[7],
            "Estado": cliente[8]
        }
        clientesDict.append(clienteDict)

    return clientesDict

def generateTableHTML(clientes):
    tableHTML = "<main style='padding: 20px; background color: red:'>"
    tableHTML += "<h1 style='text-align: center; color: Black'>Clientes</h1>"
    tableHTML += "<table style='border-collapse: collapse; width: 100%;'>"
    tableHTML += "<tr><th style='border: 1px solid black; padding: 8px;'>Id</th><th style='border: 1px solid black; padding: 8px;'>Nombre</th><th style='border: 1px solid black; padding: 8px;'>Contacto</th><th style='border: 1px solid black; padding: 8px;'>Fecha de Ingreso</th><th style='border: 1px solid black; padding: 8px;'>Tipo</th><th style='border: 1px solid black; padding: 8px;'>Marca</th><th style='border: 1px solid black; padding: 8px;'>Modelo</th><th style='border: 1px solid black; padding: 8px;'>Diagnostico</th><th style='border: 1px solid black; padding: 8px;'>Estado</th></tr>"

    for cliente in clientes:
        tableHTML += "<tr>"
        tableHTML += f"<td style='border: 1px solid black; padding: 8px;'>{cliente['id']}</td>"
        tableHTML += f"<td style='border: 1px solid black; padding: 8px;'>{cliente['Nombre']}</td>"
        tableHTML += f"<td style='border: 1px solid black; padding: 8px;'>{cliente['Contacto']}</td>"
        tableHTML += f"<td style='border: 1px solid black; padding: 8px;'>{cliente['Fecha_ingreso']}</td>"
        tableHTML += f"<td style='border: 1px solid black; padding: 8px;'>{cliente['Tipo']}</td>"
        tableHTML += f"<td style='border: 1px solid black; padding: 8px;'>{cliente['Marca']}</td>"
        tableHTML += f"<td style='border: 1px solid black; padding: 8px;'>{cliente['Modelo']}</td>"
        tableHTML += f"<td style='border: 1px solid black; padding: 8px;'>{cliente['Diagnostico']}</td>"
        tableHTML += f"<td style='border: 1px solid black; padding: 8px;'>{cliente['Estado']}</td>"
        tableHTML += "</tr>"

    tableHTML += "</table>"
    tableHTML += "<p> Esta información está sacada del curso de FastAPI </p>"
    tableHTML += "</main>"
    return tableHTML

def getClientsById(cursor, id: int):
    cursor.execute("SELECT * FROM clientes WHERE id = '"+str(id)+"'")
    clienteById = cursor.fetchall()

    newClient = {}

    for cliente in clienteById:
        newClient = {
            "id":cliente[0],
            "Nombre": cliente[1],
            "Contacto" : cliente[2],
            "Fecha_ingreso": cliente[3],
            "Tipo": cliente[4],
            "Marca": cliente[5],
            "Modelo": cliente[6],
            "Diagnostico": cliente[7],
            "Estado": cliente[8]
        }
    return newClient

def createClient(cursor, conexion, Nombre: str, Contacto: str, Fecha_ingreso: str, Tipo: str, Marca: str, Modelo: str, Diagnostico: str, Estado: str):
    cursor.execute("INSERT INTO clientes (Nombre, Contacto, Fecha_ingreso, Tipo, Marca, Modelo, Diagnostico, Estado) VALUES ('"+Nombre+"', '"+Contacto+"', '"+Fecha_ingreso+"', '"+Tipo+"', '"+Marca+"', '"+Modelo+"', '"+Diagnostico+"', '"+Estado+"')")
    conexion.commit()

    nuevosClients = getclients(cursor)
    return {"listaDeClientes": nuevosClients}

def updateClient(cursor, conexion, name: str, newName: str):
    cursor.execute("UPDATE clientes SET Nombre = '"+newName+"' WHERE Nombre = '"+str(name)+"'")
    conexion.commit()
    return {"messaje": "Cliente Actualizado Correctamente"}

def deleteClient(cursor, conexion, id: int):
    cursor.execute("DELETE FROM clientes WHERE id = '"+str(id)+"'")
    conexion.commit()
    return {"messaje": "Cliente Eliminado Correctamente"}