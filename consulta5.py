from sqlalchemy import create_engine, not_, or_
from sqlalchemy.orm import sessionmaker
from configuracion import cadena_base_datos
from generar_tablas import Reaccion, Usuario

# Conexión
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# Emociones que se van a filtrar
emociones = ["alegre", "enojado", "pensativo"]

# Condición para excluir nombres que empiezan con vocal
vocales = ('A', 'E', 'I', 'O', 'U')
condicion_no_vocal = ~or_(
    Usuario.nombre.ilike("A%"),
    Usuario.nombre.ilike("E%"),
    Usuario.nombre.ilike("I%"),
    Usuario.nombre.ilike("O%"),
    Usuario.nombre.ilike("U%")
)

# Consulta
reacciones = session.query(Reaccion).join(Usuario).filter(
    Reaccion.tipo_emocion.in_(emociones),
    condicion_no_vocal
).all()

# Mostrar resultados
print("Reacciones filtradas:")
for reaccion in reacciones:
    print(f"\t- {reaccion.usuario.nombre} reaccionó '{reaccion.tipo_emocion}': \"{reaccion.publicacion.publicacion}\"")
