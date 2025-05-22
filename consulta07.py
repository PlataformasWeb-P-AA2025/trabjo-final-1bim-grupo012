from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from generar_tablas import Usuario, Publicacion

# Consulta 7: Mostrar usuarios que han publicado más de 4 veces

# Se conecta a la base de datos
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

limite_publicaciones = 4  # valor a cambiar del condicional >

# Se consulta a los usuarios que tengan más de X publicaciones
# Se une con publicaciones y se agrupa por usuario ademas de contar cuántas tiene cada uno
usuarios = (session.query(Usuario).join(Publicacion).group_by(Usuario.id)
            .having(func.count(Publicacion.id) > limite_publicaciones).all())

# Se muestra el resultado con un mensaje formateado
print(f"Usuarios que han publicado más de {limite_publicaciones} veces:")

for usuario in usuarios:
    print(f"\t- {usuario.nombre}")
