from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from generar_tablas import Usuario, Publicacion

# Consulta 6: Contar cuántas publicaciones ha hecho cada usuario

# Se conecta a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Se arma la consulta para contar publicaciones por cada usuario
# Se usa join para unir usuario con publicación
# func.count cuenta cuántas publicaciones tiene cada uno
usuarios = session.query(Usuario.nombre, func.count(Publicacion.id)).join(Publicacion).group_by(Usuario.id).all()

# Se muestra el resultado con el nombre del usuario y la cantidad
for nombre, cantidad in usuarios:
    print(f"{nombre} ha publicado {cantidad} vez/veces.")
