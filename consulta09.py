from sqlalchemy import create_engine, func, desc
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from generar_tablas import Reaccion

# Consulta 9: Mostrar la emoción más popular (la más veces usada)

# Se conecta a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Se cuenta cuantas veces aparece cada emoción y se ordena de mayor a menor
resultado = session.query(Reaccion.tipo_emocion, func.count(Reaccion.tipo_emocion))\
    .group_by(Reaccion.tipo_emocion).order_by(desc(func.count(Reaccion.tipo_emocion))).first()

# Se muestra el resultado accediendo por el indice
if resultado:
    emocion, cantidad = resultado
    print(f"La emoción más popular es '{emocion}' con {cantidad} usos.")
else:
    print("No hay reacciones registradas.")
