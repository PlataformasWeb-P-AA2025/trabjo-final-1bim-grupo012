## Prompt utilizado

La mayoría de las consultas las desarrollamos nosotros mismos usando lo que ya conocíamos: `filter_by`, `join`, `.all()`, `.first()`, etc. Solo en una parte pedimos ayuda específica, que fue para hacer la consulta que muestra **cuál es la emoción más popular** entre todas las reacciones.

Teníamos la idea mas o menos pero no sabíamos cómo combinar bien el conteo con el orden, y luego sacar solo el resultado más alto. En lugar de pedir que nos den la consulta lista, lo que hicimos fue pedir una orientación. Prompt:

> “Queremos hacer una consulta que nos diga cuál es la emoción que más se ha repetido en todas las reacciones. Ya sabemos usar `filter_by`, `join`, `.all()` y `.first()`, pero no estamos seguros de cómo agrupar las emociones, contarlas y luego sacar solo la que tenga más. ¿Nos puedes enseñar cómo armar esa consulta paso a paso con lo que ya manejamos?”

Gracias a eso pudimos entender cómo usar `group_by` junto con `count()` y `order_by(desc(...))` para lograr el resultado, y después lo adaptamos para que quede en nuestro estilo. El resto de consultas lo trabajamos por nuestra cuenta.
