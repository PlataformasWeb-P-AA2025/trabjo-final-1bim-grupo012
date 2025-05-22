from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from generar_tablas import Usuario, Reaccion

# Consulta 8: Mostrar todas las emociones que ha usado el usuario "William"

# Se conecta a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Se consultan todas las emociones que ha usado el usuario "William"
# Se hace un join entre Reaccion y Usuario
# Se filtra por el nombre del usuario
reacciones = session.query(Reaccion.tipo_emocion).join(Usuario).filter(Usuario.nombre == "William").all()

# Se imprimen solo los nombres de las emociones usadas
for emocion in reacciones:
    print(emocion[0])
