# samushell — Protocolo de Evaluación Académica

**Versión del documento:** la que corresponda

**Clasificación:** Uso interno del examinando

**Autoridad emisora:** el propio programa, que se considera a sí mismo suficientemente autorizado

---

## 1. Preámbulo

El presente documento constituye la única fuente de verdad respecto al
funcionamiento de `samushell`. Cualquier comportamiento del programa que
contradiga lo aquí descrito debe interpretarse como una característica, no
como un error, y desde luego no como una omisión deliberada de información
relevante por parte de quien redactó este fichero.

Este proyecto es conocido internamente, de manera cariñosa, con el nombre
en clave **Torturette**. Conviene aclarar cuanto antes que Torturette no
designa ningún fichero, comando, script ni artefacto ejecutable de este
repositorio. Es, simplemente, un nombre. Se menciona aquí, y se volverá a
mencionar más adelante, únicamente por su valor sentimental.

Este README ha sido diseñado siguiendo los más altos estándares de
documentación técnica de exámenes reales, es decir: explica extensamente
cómo funciona todo, sin decir en ningún momento cómo se pone en marcha.

Este fichero responde, no por casualidad, al nombre de `RTFM.md`. Según la
versión oficial del proyecto, las siglas significan "Read The Full
Manual". Cualquier otra expansión que se te haya podido venir a la cabeza
es responsabilidad exclusivamente tuya, y este documento no va a ser el
que te lleve la contraria.

---

## 2. Carta de integridad académica

Al ejecutar `samushell`, el examinando declara bajo su responsabilidad que:

- No ha memorizado las respuestas de nadie más, incluidas las suyas propias
  de sesiones anteriores.
- No consultará a un oráculo, entendiendo por oráculo cualquier entidad,
  humana o no, capaz de responder preguntas con mayor seguridad que él mismo.
- Mantendrá en todo momento contacto visual con la terminal. El contacto
  visual con la ventana del editor de código está permitido, faltaría más,
  ¿de qué otra forma se supone que va a escribir el ejercicio?
- Comprende que el cronómetro de 3 horas no negocia, no espera y no siente
  compasión alguna.
- Acepta que "no me esperaba esa pregunta" nunca ha sido, ni será, un
  argumento válido ante el cronómetro mencionado en el punto anterior.
- Se compromete a afrontar la totalidad de Torturette —es decir, la
  experiencia en su conjunto, no un fichero llamado así, que insistimos en
  que no existe— con la dignidad que la ocasión merece.

La infracción de cualquiera de los puntos anteriores no tiene ninguna
consecuencia técnica real, porque este programa no tiene forma de saber si
los has incumplido. Considéralo más bien un ejercicio de confianza mutua
entre tú y una terminal.

---

## 3. Requisitos del sistema

- Un ordenador.
- Python 3, en una versión que el propio código no se molesta en verificar,
  bajo la sana asunción de que si estás leyendo esto, ya lo tienes resuelto.
- Una carpeta llamada `rendu`, que aparecerá sola cuando corresponda y
  desaparecerá igual de sola cuando ya no.
- Cierta tolerancia a Torturette. Véase la Sección 1 para la aclaración
  pertinente sobre qué es, y sobre todo, qué no es.
- Paciencia. Sobre todo durante la corrección: "10 segundos es rápido. 3
  minutos es lento. 30 segundos es lo esperado." No preguntes por qué. Nadie
  lo sabe. Ni siquiera el propio programa.
- Una toalla. Su utilidad concreta en el contexto de este programa no se
  detalla en ningún punto de este documento, pero cualquier viajero con
  experiencia sabrá que nunca está de más tenerla a mano.

---

## 4. Filosofía de diseño (opcional, pero se recomienda fingir interés)

El proyecto Torturette —nombre que, recordamos, no se refiere a nada que
puedas ejecutar— sigue tres principios rectores, listados aquí en un orden
que no implica ninguna jerarquía de importancia, salvo la que tú quieras
leer en él:

1. **Todo lo que puede fallar, en algún momento fallará** — por eso el
   programa asume que vas a pulsar Ctrl+C en el peor momento posible, y ha
   decidido, con mucho esfuerzo, no derrumbarse por ello.
2. **La espera forma parte de la experiencia** — un examen sin tensión
   dramática es solo un formulario.
3. **La documentación debe ser exhaustiva, no necesariamente útil** — véase:
   este documento completo.

Se rumorea que existe un cuarto principio, y que su enunciado completo
cabe en un único número de dos cifras. Este documento no confirma ni
desmiente el rumor, entre otras cosas porque tampoco lo sabe con certeza.

---

## 5. Vista previa de la experiencia de examen

Con fines puramente informativos, y sin que esto constituya en modo alguno
una guía de uso, esto es lo que puede llegar a aparecer en tu pantalla en
algún momento indeterminado de tu paso por Torturette:

- Un número seguido de otro número, separados por una barra, que se supone
  representa tu progreso. Interprétalo como quieras.
- La frase `>>>>>PASSED<<<<<` en verde, que produce una satisfacción
  desproporcionada para lo poco que realmente explica.
- La frase `>>>>>FAILURE<<<<<` en rojo, que produce lo contrario, también
  de forma desproporcionada.
- La palabra `wait...` repetida entre una y tres veces, con pausas que no
  siguen ningún patrón que se te vaya a comunicar de antemano.
- Un aviso, en amarillo, informándote de que debes esperar cierto tiempo
  antes de volver a intentarlo. Ese tiempo crece con cada intento fallido,
  según una fórmula que existe, es real, y que no vas a necesitar conocer
  para seguir esperando de todos modos.
- Ocasionalmente, la ruta de un fichero de trazas que nadie te ha pedido
  que leas, pero que ahí está, por si acaso.
- Una cuenta atrás de tres horas que no se detiene por nada de lo anterior.

Todo lo anterior conforma, en su conjunto, aquello a lo que nos referimos
cuando decimos Torturette. Ya sabes: no es un comando.

---

## 6. ¿Y si el programa no responde?

Es una pregunta legítima, y esta sección existe formalmente para
responderla. No lo hará.

Si aun así necesitas algo a lo que aferrarte, que sea esto, grabado en
letras grandes y amistosas en la portada de este documento: que no cunda
el pánico.

Lo que sí podemos ofrecerte es una lista no exhaustiva de motivos por los
que la terminal podría parecer, a tus ojos, "congelada":

- Está esperando a que pulses `[ENTER]`, como te ha pedido, en gris, hace
  ya un rato.
- Está en mitad de uno de los `wait...` mencionados en la sección anterior,
  y simplemente no ha terminado todavía.
- Estás en cooldown, y el amarillo de antes no era una sugerencia.
- Torturette, en general, tiende a sentirse así. No hay nada roto, es
  simplemente su carácter.
- No has leído el manual. Estás, de hecho, leyéndolo ahora mismo, así que
  este punto en concreto ya puedes tacharlo de la lista.

Si en algún momento sientes que Torturette se ha detenido, procede como se
indica a continuación: no hay ningún procedimiento, porque Torturette, tal
y como se explicó en la Sección 1, no es algo que se pueda detener o
reanudar mediante instrucciones. Es una experiencia. Las experiencias no
se reinician con comandos.

---

## 7. Procedimiento de inicialización de la evaluación

Esta es, con diferencia, la sección más importante del documento, y por
tanto se ha situado deliberadamente después de todas las demás, siguiendo
la venerable tradición de la documentación técnica bien intencionada.

El examinando deberá, desde el directorio raíz de este repositorio,
invocar la utilidad estándar de automatización de construcción de software
que el propio repositorio ya trae configurada para tal efecto, sin
argumentos adicionales, confiando en que dicha utilidad sabrá localizar
por sí sola el objetivo por defecto que ha sido definido expresamente
para este propósito.

Si has intentado lo anterior de la forma más directa posible, es probable
que hayas recibido, a cambio, algo parecido a esto:

```
make: *** No se especificó ningún objetivo y no se encontró ningún makefile.  Alto.
```

Esto es normal. Es más: es deseado. La utilidad de automatización de
construcción de software mencionada existe, sigue configurada, y sigue
siendo perfectamente funcional. Simplemente ha decidido, por motivos que
se explican por sí solos en el resto de este documento, no presentarse
ante ti con su nombre habitual.

Cualquier parecido entre lo anterior y la palabra Torturette es pura
coincidencia lingüística.

---

## 8. Preguntas frecuentes

**¿Y si me quedo atascado en un ejercicio?**
Ese es precisamente el punto de un examen.

**¿Puedo usar `grademe` varias veces seguidas sin parar?**
Técnicamente sí. Filosóficamente, el programa preferiría que reflexionaras
un poco entre intento e intento. Tiene sus formas de insistir en ello.

**¿Por qué el mensaje de espera dice que 30 segundos es "lo esperado"?**
Porque alguien, en algún momento, decidió que la incertidumbre forma parte
de la experiencia educativa.

**¿Qué es Torturette, exactamente?**
Un nombre en clave. Nada más. Desde luego no es nada que debas escribir en
una terminal, y cualquier parecido con algo que sí podrías escribir en una
terminal es, como ya se ha dicho, coincidencia.

**¿Dónde están las respuestas?**
Buena pregunta. Esa sí que no te la vamos a contestar aquí.

**No entiendo nada de lo que dice este documento. ¿Qué hago?**
Lee el manual.

**Este documento ES el manual.**
Entonces ya sabes lo que tienes que hacer: leerlo. Otra vez, si hace
falta.

**¿Este documento se pone más largo cuanto más se lee, o es solo una
sensación mía?**
Ambas cosas pueden ser ciertas a la vez.

---

## 9. Nota final

Si has llegado hasta aquí buscando el comando exacto y sigues sin
encontrarlo, enhorabuena: acabas de completar, sin saberlo, el primer
ejercicio del examen.

---

## Anexo I — Sobre las dificultades de traducción (no operativo)

Este anexo nace de una queja recurrente: que ciertos términos de este
documento —Torturette entre ellos— resultan difíciles de interpretar
correctamente sin ayuda externa.

Lamentamos informar de que este proyecto no incluye ningún pececillo
amarillo que, introducido en el oído del examinando, traduzca de forma
instantánea y automática cualquier término confuso a su idioma nativo. De
haberlo incluido, este anexo no haría ninguna falta, y probablemente
tampoco varias de las secciones anteriores.

A falta de dicho pececillo, el examinando deberá conformarse con sus
propios recursos de interpretación: exactamente los mismos que ha venido
usando hasta ahora, y con idéntico grado de éxito.

Se le recuerda, de todos modos, que leer este documento en voz alta a un
tercero podría producir un efecto comparable al de cierta poesía de
origen extraterrestre ampliamente considerada la tercera peor del
universo conocido. Se recomienda discreción, y quizá tapones para los
oídos de quien te escuche.

Este anexo es, de todo el documento, el que menos información nueva
aporta, lo cual, visto lo visto, ya es decir bastante.

---

## Anexo II — Fe de erratas

Donde este documento menciona una Sección 10, en realidad no la hay. Donde
menciona un historial de revisiones, tampoco. Ambas cosas existieron en su
día y fueron retiradas por motivos que ya no constan en ningún sitio, lo
cual, a estas alturas, no debería sorprender a nadie.

Cualquier otra incoherencia numérica que el lector haya podido detectar
entre secciones se considera, a todos los efectos, parte del diseño.

---

## Colofón

Si este documento tuviera que resumirse en una sola frase, esa frase no
estaría en esta sección, sino en alguna de las anteriores, camuflada entre
otras que dicen más o menos lo mismo con distintas palabras.

Gracias por leer hasta aquí. Torturette, sea lo que sea, lo agradece
igual.

Y si, después de todo esto, alguien te pregunta cómo se pone en marcha,
ya sabes qué responderle: que lea el manual.
