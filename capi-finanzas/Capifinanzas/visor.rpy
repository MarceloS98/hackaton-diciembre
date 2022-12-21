screen boton():
    vbox:
        xalign 0.5
        yalign 0.5
        textbutton _("Educación Financiera") action Jump("objetivos")
    
    vbox:
        xalign 0.5
        yalign 0.7
        frame:
            margin (10, 10, 10, 10)
            padding (30, 20, 30, 20)
            text "La educación financiera te enseña sobre el uso del dinero, el ahorro y como organizarnos correctamente para lograr el bienestar económico"


screen progreso(): #CREA UNA VENTANITA
    
    frame: #CREA UN MARCO PARA EL CUADRO
        xalign 0.0 #ALINEA A LA IZQUIERDA
        yalign 0.0
        margin (10, 10, 10, 10)
        padding (30, 20, 30, 20)
        
        has hbox
        spacing 10 #ESPACIO DE LA VENTANA PRINCIPAL
        
        vbox: #CREA UNA CAJA/COLUMNA
            spacing 5 #ESPACIO ENTRE CAJAS
            text "Ahorros: "
            text "Meta: "

        vbox: #CREA OTRA CAJA/COLUMNA
            spacing 5 #ESPACIO ENTRE CAJAS
            xsize 70 #ESPACIO FIJO DE LOS NÚMEROS DE LA CAJA
            text "[ahorro]" xalign 1.0
            text "[lentes]" xalign 1.0


#CAMBIAR BOTONES A IMAGENES

screen selector():
    vbox:
        xalign 0.5
        yalign 0.1
        frame:
            margin (10, 10, 10, 10)
            padding (30, 20, 30, 20)
            text "Elije tu Objetivo"
    hbox:
        #AL LLAMAR LA FUNCIÓN SCREEN DEJAMOS DE USAR MENÚ Y COMENZAMOS A USAR textbutton y action, TAMBIÉN LA FUNCIÓN DE jump SE ESCRIBE DIFERENTE Jump (CON J MAYÚSCULA)
        #SI QUEREMOS QUE LOS BOTONES SEAN IMAGENES LA SINTAXIS SERIA LA SIGUIENTE: imagebutton idle "nombre_imagen.png/jpg/webp"
        spacing 240
        xpos 180
        ypos 370
        imagebutton idle "OBJETIVOS/sombrero_idle.png" hover "OBJETIVOS/sombrero_hover.png ":
            action Jump("sombrero")
            #TOOLTIP DA UNA PEQUEÑA DESCRIPCIÓN DE LA IMG
            #_() ES UNA FUNCIÓN DE TRADUCCIÓN POR SI ALGUNA VEZ SE QUIERA TRADUCIR
            # tooltip _("precio 50000 en 10 días")
        imagebutton idle "OBJETIVOS/lentes_idle.png" hover "OBJETIVOS/lentes_hover.png":
            action Jump("lentes")
            # tooltip _("precio 25000 en 5 días")
        imagebutton idle "OBJETIVOS/albirroja_idle.png" hover "OBJETIVOS/albirroja_hover.png":
            action Jump("albirroja")
            # tooltip _("precio 75000 en 15 días")
        imagebutton idle "OBJETIVOS/color_idle.png" hover "OBJETIVOS/color_hover.png":
            action Jump("color")
            # tooltip _("precio 100000 en 20 días")

screen ahorros(): #CREA UNA VENTANITA
    
    frame: #CREA UN MARCO PARA EL CUADRO
        xalign 0.5 #ALINEA A LA IZQUIERDA
        yalign 0.5
        margin (30, 30, 30, 30)
        padding (60, 40, 60, 40)
        has hbox
        spacing 10 #ESPACIO DE LA VENTANA PRINCIPAL
        
        vbox: #CREA UNA CAJA/COLUMNA
            spacing 5 #ESPACIO ENTRE CAJAS
            text "Ahorros: [ahorro]"
        
        # ANTERIORMENTE DEFINIMOS LA TOOLTIP PERO NO SE MUESTRA EN PANTALLA PARA ELLO TENEMOS QUE USAR LO SIGUIENTE:
        #     1- DEFINIR UNA VARIABLE
        #     2- QUE SEA IGUAL A GetTooltip() así si existe una se va a mostrar en la pantalla
        #     3- NO SIEMPRE VA A EXISTIR UN TOOLTIP POR LO QUE TENEMOS QUE DEFINIR UNA CONDICIÓN
        #         if pista:
        #             text "[pista!t]"
        
        # $ pista = GetTooltip()
        
        # if pista:
        #     frame:
        #         text "[pista!t]" # SOLO SI HAY UN TOOLTIP VA A MOSTRAR EL TEXTO
        #         xalign 0.0
        #         yalign 0.0
        #         margin (10, 10, 10, 10)
        #         padding (30, 20, 30, 20)