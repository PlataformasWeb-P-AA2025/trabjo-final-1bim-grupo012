from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from generar_tablas import Publicacion, Reaccion, Usuario

# Conexión a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Texto exacto de la publicación
contenido_publicacion = "Bruno Fernandes del Liverpool fue expulsado por doble amarilla en el debut de la temporada."

# Se busca la publicación exacta
publicacion = session.query(Publicacion).filter_by(publicacion=contenido_publicacion).first()

# Si se encuentra, se listan las reacciones asociadas
if publicacion:
    print(f"Reacciones a la publicación:\n\t\"{publicacion.publicacion}\"")
    for reaccion in publicacion.reacciones:
        print(f"\t- {reaccion.usuario.nombre}: {reaccion.tipo_emocion}")
else:
    print("Publicación no encontrada.")
