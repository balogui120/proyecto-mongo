from conector import ConectorMongoDB

conector = ConectorMongoDB()
cliente = conector.conectarse()
librosColeccion = conector.coleccion()

for libros in librosColeccion.find().limit(2):
    print(libros)

