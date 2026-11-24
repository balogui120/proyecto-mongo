from conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()
librosColeccion = conector.coleccion()

librosColeccion.drop() # Elimina la colección libros