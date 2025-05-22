from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from generar_tablas import Publicacion, Reaccion

# Consulta 10: Mostrar publicaciones que no han recibido ninguna reacción

# Se conecta a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# se trae todas las publicaciones existentes
publicaciones = session.query(Publicacion).all()

# revisamos una por una si tiene al menos una reacción
print("Publicaciones sin ninguna reacción:\n")
encontradas = False

for pub in publicaciones:
    # Se consulta si existe alguna reacción con el mismo publicacion_id
    reaccion = session.query(Reaccion).filter_by(publicacion_id=pub.id).first()

    if not reaccion:
        print(f"- {pub.publicacion}")  # Se imprime solo si no tiene reacciones
        encontradas = True

# mensaje cadena final por si no se hallo ninguna sin reacciones
if not encontradas:
    print("Todas las publicaciones tienen al menos una reacción.")
