from conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()

baseDatos = cliente["mi_primera_base_datos"]

coleccion = baseDatos["mi_primera_coleccion"]

documento = { "nombre": "Brenda", "apellido": "Alonso" }

insercion = coleccion.insert_one(documento)