# Coloca el código de tu juego en este archivo.

# Declara los personajes/variables usados en el juego:

define capi = Character("Prof. Capi", color = "#855f39")
define materias = ["Ahorros", "Dinero", "Gestión", "Inflación", "Resumen"]
define lentes = 25000
define sombrero = 50000
define albirroja = 75000
define color = 100000

default ahorro = 0
default meta = 0
default energia = 8
default dias_lentes = 0
default nro_dias_de_semana = 1
default dia_semana = "Lunes"

#IMG PERSONAJES
image profe_capi = "capybara.png"
image capi_ok = "capybara ok.png"
image capi_enojado = "capybara enojado.png"
image capi_sad = "capybara sad.png"
image capi_sentado = "capybara sentado.png"
image capi_boca_abierta = "capybara boca abierta.png"
image capi_boca_cerrada = "capybara boca cerrada.png"
image capi_cantinero = "capybara_cantinero.png"
image capi_chau = "capybara_diciendo_adios.png"
image capi_zzz = "capybara_durmiendo_sn.png"
image capi_empanada = "capybara_comiendo_empanada.png"


#IMG FONDOS 
image escuela = "bg_frente1.jpeg"
image aula = "bg_aula.jpeg"
image escuela_recreo = "bg_frente.jpeg"
image escuela_tarde = "bg_frente1_tarde.jpeg"
image habitacion = "bg_noche.jpg"


# El juego comienza aquí.
label start:
    scene escuela
    show capi_sentado at left
    play sound "audio/timbre_escuela.mp3"
    capi 'Buenos Dias'
    play music "audio/relax_lofi.mp3"
    $ name = renpy.input ("Cual es tu nombre?")
    $ name = name.strip()
    hide capi_sentado
    show capi_boca_abierta at left
    capi "Hola [name]!!"
    capi "Soy el [capi], especialista en finanzas. Estoy para ayudarte a tener más ideas de como usar mejor tu dinero de manera divertida."
    capi "Para empezar el juego solo tienes que elegir la meta a alcanzar."
    capi "Anotar la cantidad de dinero que utilizas durante el día."
    # capi "Responder preguntas sobre el uso correcto del dinero con el [capi]."
    capi "Al final de cada clase te haré unas pequeñas preguntas. Puedes estar tranquilo, con tus capacidades sé que lo lograrás"
    capi"¡Juntos llegaremos más rápido a la meta que quieras alcanzar!"
    "Para ir avanzando en la história debes de presionar el boton de enter o la barra espaciadora"
    hide capi_boca_abierta
    
###########################################################################################################################
#LLAMAMOS AL CÓDIGO DE ARA!
    call screen boton

###########################################################################################################################

label objetivos:

    # menu:
    #     "Sombrero Piri precio 50000 en 10 días":
    #         jump sombrero
    #     "Lentes precio 25000 en 5 días":
    #         jump lentes
    #     "La Albirroja precio 75000 en 15 días":
    #         jump albirroja
    #     "Bandera del Paraguay 100000 en 20 días":
    #         jump bandera

    "Acompaña diariamente al [capi] a conocer sobre gestión financiera mediante nuevas palabras y creando tu propio plan."
    show capi_boca_abierta at truecenter with fade
    
# while True:
#BLOQUE DE CÓDIGO QUE QUEREMOS CORRER
    # if horas_del_dia == 8: #AQUÍ INICIAMOS EL DÍA
    capi "Por favor [name], elije un objetivo."
    hide capi_boca_abierta
   
    call screen selector #LLAMAMOS AL MENÚ DE OBJETIVOS
   
label sombrero:
    jump objetivos
label albirroja:
    jump objetivos
label color:
    jump objetivos


label lentes:
    hide capi_boca_abierta
    show capi_ok at left with fade
    capi "[name] elegiste los lentes."
    capi "Te cuento el objetivo de los lentes:"
    capi "Tienes 5 días para ahorrar la cantidad de [lentes] Gs."
    capi "[name] el recreo díario de 5000 Gs. te ayudará a lograr tus metas."
    capi "Cuando llegues a [lentes] Gs. podrás jugar nuevamente y elegir nuevos objetivos y de paso aprenderemos muchísimo."
    capi "No te preocupes [name], YO!, el [capi] te guiaré hasta llegar a tu meta lo más rápido posible."
    hide capi_ok
    
    while dias_lentes <= 5:
        play sound "audio/timbre_escuela.mp3"
        menu:
            "Pasar a la clase del día":
                jump clases



##################################################################################
#PÁGINA DE DAVID

    label clases:
        $energia -= 2
        $dias_lentes += 1
        show screen progreso #LLAMAMOS A LA PANTALLITA
        $ahorro += 5000
        scene aula

        show profe_capi at right
        capi "¡Muy buenos días estudiantes!"

        if dias_lentes == 1:
            capi "La lección del día será sobre [materias[0]]."
            hide profe_capi

            show capi_ok at left
            capi "El ahorro es la parte del dinero guardada para poder gastarla más adelante. Ahorrar es muy importante. No debes gastar todo tu dinero porque seguro que lo necesitarás mañana: un regalo, la bici que tanto te gusta, tu revista favorita"
            capi "Cuando tienes dinero, no hace falta gastarlo enseguida. Puedes guardarlo para algo imnportante en el futuro. Esto se llama ahorrar"
            capi "El agua cuesta dinero. Malgastarla es un gasto innecesario. Es muy importante no dejar los grifos abiertos."
            capi "Puedes gastar para tí, y también para los demás."
            hide capi_ok

            menu quiz: #PANTALLA DE PREGUNTAS
                "Te invito a demostrar tus conocimientos.":
                    jump preguntas

        label preguntas:
            $energia -= 1
            hide capi_sad
            show capi_sentado at left 
            menu caramelos:
                "Si no tienes mucho dinero para comprar tu juguete preferido, ¿qué harías?"
                "Dejo de ahorrar unos días para comprarlo":
                    jump excelente
                "Me gasto mis ahorros":
                    jump error
                "Prefiero guardar mi dinero y seguir ahorrando":
                    jump error

        label excelente:
            hide capi_sentado
            scene bg_aula
            show capi_ok at left
            capi "Genial, has respondido correctamente."
            play sound "audio/timbre_escuela.mp3"
            hide capi_ok
            show capi_boca_abierta at right with fade
            capi "WOW, ¡miren la hora! Es tiempo del recreo."
            capi "¡A DIVERTIRSE!"
            jump recreo

        label error:
            hide capi_sentado
            show capi_sad at left
            capi "Ohh, la respuesta no es correcta."
            capi "Pero animos para la proxima!"
            jump preguntas    
        
        # elif dias_lentes == 2:
        #     capi "Continuemos con el objetivo lentes."
        #     capi "La lección del día será sobre [materias[1]]."
        #     hide profe_capi

        #     show capi_ok at left
        #     capi "El dinero se gana con trabajo y con esfuerzo. Las personas reciben dinero a cambio de vender productos o realizar servicios. Muchos niños y también jovenes se esfuerzan haciendo pequeños recados y ayudando en las tareas del hogar"
        #     capi "Las personas reciben dinero cuando trabajan vendiendo productos. Cuando compramos algo, tenemos que pagar por ello"
        #     capi "Muchas veces los abuelos, cuando ven la libreta del grado, les regalan alguna que otra monedas o hasta un billete. Y ustedes piensan muy bien en qué las gastarán, para ello es muy importante comentarlo con sus padres."
        #     hide capi_ok

        #     menu quiz #: #PANTALLA DE PREGUNTAS
        #         "Te invito a demostrar tus conocimientos.":
        #             jump preguntas

        # label preguntas:
        #     $energia -= 1
        #     hide capi_sad
        #     show capi_sentado at left 
        #     menu caramelos:
        #         "¿Con qué se consiguen caramelos, jueguetes, ropa, etc.?"
        #         "Con papel de colores":
        #             jump error
        #         "Con dinero":
        #             jump excelente
        #         "Me lo dan mis padres":
        #             jump error

        # label excelente:
        #     hide capi_sentado
        #     scene bg_aula
        #     show capi_ok at left
        #     capi "Genial, has respondido correctamente."
        #     play sound "audio/timbre_escuela.mp3"
        #     hide capi_ok
        #     show capi_boca_abierta at right with fade
        #     capi "WOW, ¡miren la hora! Es tiempo del recreo."
        #     capi "¡A DIVERTIRSE!"
        #     jump recreo

        # label error:
        #     hide capi_sentado
        #     show capi_sad at left
        #     capi "Ohh, la respuesta no es correcta."
        #     capi "Pero animos para la proxima!"
        #     capi "¡Recuerda! Es el dinero lo que usamos para comprar lo que necesitemos y hasta a veces lo que queremos."
        #     jump preguntas

        # elif dias_lentes == 3:
        #     capi "Continuemos con el objetivo lentes."
        #     capi "La lección del día será sobre [materias[2]]."
        #     hide profe_capi

        #     show capi_ok at left
        #     capi "La educación financiera es muy importante algunos de los beneficios son:"
        #     capi "Empezamos a ser más responsables con el dinero, paso fundamental para poder apreciar lo que se tiene "
        #     capi "Comprenden el valor de las cosas, porque cuando planifican y ahorran comprenden su valor e incluso los conceptos matemáticos básicos"
        #     capi "Idean formas de generar ingresos y por último son más organizados."
        #     hide capi_ok

        #     menu quiz # #PANTALLA DE PREGUNTAS
        #         "Te invito a demostrar tus conocimientos.":
        #             jump preguntas

        # label preguntas:
        #     $energia -= 1
        #     hide capi_sad
        #     show capi_sentado at left 
        #     menu caramelos:
        #         "Si por tu cumpleaños recibes de regalo 100.000 guaranies ¿Qué harías? "
        #         "Comprar mi juguete preferido":
        #             jump error
        #         "Comprar mi juguete preferido y ahorrar una parte":
        #             jump excelente
        #         "Ahorrar":
        #             jump error

        # label excelente:
        #     hide capi_sentado
        #     scene bg_aula
        #     show capi_ok at left
        #     capi "Genial, has respondido correctamente."
        #     play sound "audio/timbre_escuela.mp3"
        #     hide capi_ok
        #     show capi_boca_abierta at right with fade
        #     capi "WOW, ¡miren la hora! Es tiempo del recreo."
        #     capi "¡A DIVERTIRSE!"
        #     jump recreo

        # label error:
        #     hide capi_sentado
        #     show capi_sad at left
        #     capi "Ohh, la respuesta no es correcta."
        #     capi "Pero animos para la proxima!"
        #     capi "¡Recuerda! Un Plan de gastos es la idea que tienes de como gastaras el dinero que recibes, elegir cuanto ahorrar y gastar en el tiempo."
        #     jump preguntas
        
        # elif dias_lentes == 4:
        #     capi "Continuemos con el objetivo lentes."
        #     capi "La lección del día será sobre [materias[0]]."
        #     hide profe_capi

        #     show capi_ok at left
        #     capi "La educación financiera es muy importante algunos de los beneficios son:"
        #     capi "Empezamos a ser más responsables con el dinero, paso fundamental para poder apreciar lo que se tiene "
        #     capi "Comprenden el valor de las cosas, porque cuando planifican y ahorran comprenden su valor e incluso los conceptos matemáticos básicos"
        #     capi "Idean formas de generar ingresos y por último son más organizados."
        #     hide capi_ok

        #     menu quiz # #PANTALLA DE PREGUNTAS
        #         "Te invito a demostrar tus conocimientos.":
        #             jump preguntas

        # label preguntas:
        #     $energia -= 1
        #     hide capi_sad
        #     show capi_sentado at left 
        #     menu caramelos:
        #         "Si por tu cumpleaños recibes de regalo 100.000 guaranies ¿Qué harías? "
        #         "Comprar mi juguete preferido":
        #             jump error
        #         "Comprar mi juguete preferido y ahorrar una parte":
        #             jump excelente
        #         "Ahorrar":
        #             jump error

        # label excelente:
        #     hide capi_sentado
        #     scene bg_aula
        #     show capi_ok at left
        #     capi "Genial, has respondido correctamente."
        #     play sound "audio/timbre_escuela.mp3"
        #     hide capi_ok
        #     show capi_boca_abierta at right with fade
        #     capi "WOW, ¡miren la hora! Es tiempo del recreo."
        #     capi "¡A DIVERTIRSE!"
        #     jump recreo

        # label error:
        #     hide capi_sentado
        #     show capi_sad at left
        #     capi "Ohh, la respuesta no es correcta."
        #     capi "Pero animos para la proxima!"
        #     capi "¡Recuerda! Un Plan de gastos es la idea que tienes de como gastaras el dinero que recibes, elegir cuanto ahorrar y gastar en el tiempo."
        #     jump preguntas

        # elif dias_lentes == 5:
        #     capi "Continuemos con el objetivo lentes."
        #     capi "La última lección de la semana será sobre [materias[4]]."
        #     hide profe_capi

        #     show capi_ok at left
        #     capi "Repaso sobre la inflación."
        #     capi "Existe inflación cuando se produce un incremento general de los precios al comparar dos periodos de tiempo." 
        #     capi "Repaso sobre el ahorro."
        #     capi "Cuando tienes dinero, no hace falta gastarlo enseguida. Puedes guardarlo para algo imnportante en el futuro. Esto se llama ahorrar"
        #     hide capi_ok
        #     show capi_ok at right
        #     capi "Repaso sobre la gestión financiera."
        #     capi "Empezamos a ser más responsables con el dinero, paso fundamental para poder apreciar lo que se tiene" 
        #     capi "Repaso sobre el dinero." 
        #     capi "El dinero se gana con trabajo y con esfuerzo. Las personas reciben dinero a cambio de vender productos o realizar servicios. Muchos niños y también jovenes se esfuerzan haciendo pequeños recados y ayudando en las tareas del hogar"
        #     hide capi_ok

        #     menu quiz #PANTALLA DE PREGUNTAS
        #         "Te invito a demostrar tus conocimientos.":
        #             jump preguntas

        # label preguntas:
        #     $energia -= 1
        #     hide capi_sad
        #     show capi_sentado at left 
        #     menu caramelos:
        #         "Si el valor de la moneda disminuye ¿Puedo comprar siempre la misma cantidad cosas?"
        #         "Motomami":
        #             jump error
        #         "N, de ni se te ocurra ni pensarlo":
        #             jump excelente
        #         "La respuesta está en tu corazón, perrito feliz":
        #             jump error

        # label excelente:
        #     hide capi_sentado
        #     scene bg_aula
        #     show capi_ok at left
        #     capi "Genial, has respondido correctamente."
        #     play sound "audio/timbre_escuela.mp3"
        #     hide capi_ok
        #     show capi_boca_abierta at right with fade
        #     capi "WOW, ¡miren la hora! Es tiempo del recreo."
        #     capi "¡A DIVERTIRSE!"
        #     jump recreo


        # label error:
        #     hide capi_sentado
        #     show capi_sad at left
        #     capi "Ohh, la respuesta no es correcta."
        #     capi "Pero animos para la proxima!"
        #     capi "¡Recuerda! que con una misma cantidad de dinero se pueden pagar menos cosas."
        #     jump preguntas

#######################################################################################################
#PÁGINA DE GABRIEL

    label recreo:
            $energia -= 3
            stop music
            play music "audio/niños.mp3" 
            scene escuela_recreo
            "¡Hey!, ya llegó la hora del recreo, ¡te mereces un descanso!"
            jump bocadillo

    label bocadillo:
        show capi_cantinero at left with fade
        capi "¿Quieres comprar un bocadillo?"
        menu:
            "No gracias, no quiero gastar mi dinero":
                hide capi_cantinero
                capi "Genial, ¡Has elegido ahorrar!"
                play sound "audio/timbre_escuela.mp3"
                "El tiempo pasa rápido cuando nos divertimos."
                show capi_boca_abierta at truecenter with fade
                capi "Volvamos a la clase."
                hide capi_cantinero
                jump repaso
            "¡Si! tengo ganas de comer. Te costará 2500 Gs.":
                hide capi_cantinero
                show capi_empanada at right with fade
                "ñam, ñam, ñam... delicioso."
                $ ahorro -= 2500 
                hide capi_empanada
                play sound "audio/timbre_escuela.mp3"
                "El tiempo pasa rápido cuando nos divertimos."
                hide capi_cantinero
                show capi_boca_abierta at truecenter with fade
                capi "Volvamos a la clase."
                jump repaso

    label repaso:
        play music "audio/relax_lofi.mp3"
        scene aula

        show capi_boca_abierta at truecenter
        capi "¿Te parece bien dar un repaso a la lección de hoy?"
        hide capi_boca_abierta
        menu:
            "Si, por favor.":
                show capi_boca_abierta at truecenter
                capi "¡Genial!"  #opción “a” te lleva de nuevo a la definición de dinero
                jump pagina4b
            "No gracias, lo entendí bien.":
                jump salida #la opción “b” va directo a la siguiente pag

    ################################
    #CLASE DE REPASO

    label pagina4b:
        scene aula
        show profe_capi at right
        capi "La primera lección del día fue sobre el dinero."
        hide profe_capi
        show capi_ok at left
        capi "Como comentamos antes, el dinero da valor a las cosas, tiene forma de moneda, billete o tarjeta y sirve para comprar todo aquello que queremos o necesitamos."
        hide capi_ok
        show capi_boca_abierta at truecenter
        capi "Quieres responder de nuevo el cuestionario."
        hide capi_boca_abierta
        menu quiz_ejercitario:
            "Si, quiero volver a practicar.":
                jump repaso_preguntas
            "No, esta vez me quedó más claro.":
                jump salida

    label repaso_preguntas:
        hide capi_sad
        hide capi_boca_abierta
        show capi_sentado at left with fade
        menu preguntas2:
            "¿Con qué se consiguen los caramelos, juguetes, ropa, etc?"
            "Con dinero.":
                jump correcta
            "Con papel u hoja de plantas.":
                jump incorrecta
            "Me lo dan mis padres.":
                jump incorrecta

    # En ambos labels tiene como parte final el jump que se puede usar para retornar a otra pagina 
    # para poder usarse en otras pantallas
    label correcta:
        scene bg_aula
        show capi_ok at left
        capi 'Genial, has respondido correctamente.'
        play sound "audio/timbre_escuela.mp3"
        hide capi_ok
        show capi_boca_abierta at truecenter with fade
        capi "¡Ha llegado el final del día!"
        capi "Nos vemos mañana."
        jump salida

    label incorrecta:
        hide capi_sentado
        show capi_sad at left
        capi 'Ohh, la respuesta no es correcta.'
        capi '¡Pero animos para la proxima!'
        jump repaso_preguntas

    label salida:
        scene escuela_tarde
        "Hoy fue un día divertidísimo."
        "Mañana será otro día lleno de información y diversión."
        menu:
            "Ir a casa":
                jump casa

    label casa:
        hide screen progreso
        scene habitacion
        "Llegas a casa y te preparas para dormir."
        show capi_zzz at left with fade
        capi "Veamos tus avances"
        hide capi_zzz
        menu:
            "Ver mi progreso":
                jump final

    label final:
        show screen ahorros
        "Estos son tus ahorros"
        $ meta = lentes - ahorro 
        "Te faltan [meta] Gs. para llegar a la meta" 
    
    # return
