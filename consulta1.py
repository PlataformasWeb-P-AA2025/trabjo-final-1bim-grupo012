from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from generar_tablas import Usuario, Publicacion

# Se conecta a la base de datos usando la cadena definida en configuracion.py
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

nombre_usuario = "Nicole"  # Nombre del usuario del que se quieren listar publicaciones

# Se busca el usuario exacto en la base de datos
usuario = session.query(Usuario).filter_by(nombre=nombre_usuario).first()

# Si se encuentra el usuario, se listan sus publicaciones
if usuario:
    print(f"Publicaciones de {usuario.nombre}:")
    for pub in usuario.publicaciones:
        print(f"\t- {pub.publicacion}")
else:
    print("Usuario no encontrado.")
