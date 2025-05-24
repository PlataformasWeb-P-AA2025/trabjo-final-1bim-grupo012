from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from generar_tablas import Usuario, Reaccion

# Conexión a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

nombre_usuario = "Shelley"  # Cambiar por el nombre deseado

# Buscar el usuario
usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()

# Listar las publicaciones donde reaccionó
if usuario:
    print(f"Publicaciones en las que reaccionó {usuario.nombre}:")
    for reaccion in usuario.reacciones:
        print(f"\t- \"{reaccion.publicacion.publicacion}\" con emoción: {reaccion.tipo_emocion}")
else:
    print("Usuario no encontrado.")
