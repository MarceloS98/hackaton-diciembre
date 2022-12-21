# Creacion del personaje
define capy = Character('capy', color="#E74C3C", image='capy')


# Utilizacion de las imagenes 
# Para las imagenes se puso el nombre del archivo y variable con el mismo nombre salvo la palabra
# Side para las imagene asi lograr la carga de la imagen
image define capy hablando  = 'side capy hablando.png'
image capy_hablando = 'side capy callado.png'

image define capy Sad = 'side capy Sad.png'
image capyLloron = 'side capy Sad.png'

image define capy ok = 'side capy ok.png'
image capyOk = 'side capy ok.png'


# Inicio de la app que seria el label de inicio 
# Que al momento de sumarse con el siguiente codigo cambiaria el nombre
label start:
     $ name = renpy.input('Cual es tu nombre?')
     $ name = name.strip()
     scene bg_frente
     # la variable dentro del label no reconocia espacios en el nombre de la variable de ahi que se
     # declaro dos variables para su uso 
     show capy_hablando at right
     capy 'Hola [name], buenos dias'
     capy 'La primera leccion del dia sera sobre el dinero'

# Siguiente 'pantalla'
label aviso:
     scene bg_frente
     show capyOk at left
     capy 'Sabias que? El dinero da valor a las cosas, tiene forma de moneda, billete
     o tarjeta y sirve para comprar todo aquello  que queremos o nesesitamos'

# pantalla de las peguntas 
label preguntas:
     menu caramelos:
          "Te invito a demostrar tus conocimientos"
          "Como se consiguen los caramelos?"
          "a- Con dinero":
               jump ConDinero
          "b- Con papel u hoja de plantas":
               jump Perdedor
          "c- Me lo dan mis padres":
               jump Perdedor

# En ambos labels tiene como parte final el jump que se puede usar para retornar a otra pagina 
# para poder usarse en otras pantallas
label ConDinero:
     scene bg_frente
     show capyOk at left
     capy 'Genial, has ganado'
     jump aviso

label Perdedor:
     scene bg_frente
     show capyLloron at left
     capy 'Ohh, la respuesta no es correcta'
     capy 'pero animos para la proxima!'
     jump aviso