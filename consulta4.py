from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from generar_tablas import Reaccion

# Conexión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Agrupar por tipo_emocion y contar
reporte = session.query(Reaccion.tipo_emocion, func.count().label("cantidad")) \
                 .group_by(Reaccion.tipo_emocion).all()

print("Reporte de emociones usadas:")
for emocion, cantidad in reporte:
    print(f"\t- {emocion}: {cantidad} veces")
