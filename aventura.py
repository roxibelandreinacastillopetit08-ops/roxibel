start = print(" te despiertas en una cueva junto con una nota y una antorcha, que haces??")

opcion_inicio = input("que haces??: NOTA o ANTORCHA ").lower() #PRIMER NIVEL DE PREGUNTAS



if opcion_inicio == "nota":  
    print("lees la nota,tiene unas indicaciones que decides seguir")
    print("no ves mucho pero alcanzas a oir algo,se oye peligroso")
    opcion_trampa = input("que haces??: AGACHARTE o CORRER ").lower() #SEGUNDO NIVEL DE PREGUNTAS
    if opcion_trampa == "agacharte": 
        print("te agrachas y evitas unas flechas que convenientemente")
        print("pasan por encima de ti y ves como se acerca una luz pequeña")
        opcion_duda = input(" ACERCARSE o HACERSE MUERTO ").lower() # TERCER NIVEL DE PRECUNTAS
        if opcion_duda == "hacerse muerto":
            print("te tiras al piso y sientes como se acerca alguien que te")
            print("sube asu hombro y despues de una rato te tira en lo que")
            print("abres los ojos y ves que te llevo a un tipo de aldea en el bosque")
            opcion_aldea = input("cual es tu siguiente movimiento: EXPLORAR o ESPERAR ").lower() #CUARTO NIVEL DE PREGUNTAS
            if opcion_aldea == "explorar":
                print("sales a explorar ye encuentras unas armas")
                print("tienes la oportunidad de atacar ")
                opcion_armas = input("que haces: ATACAR,DEJAR o SUICIDARTE").lower() # QUINTO NIVEL Y SEXTO DE PREGUNTAS
                if opcion_armas == "atacar":
                    print("tomas una espada de tu preferencia y te dispones a atacar a los canibales por la espalda")
                    print("matas a la mayoria hasta que solo quedan los canibales indefensos")
                    print("uno de ellos te pides que pares, que no te joden mas")
                    opcion_moral = input(" lo... MATAR o IRTE").lower() #sexto de verdad eeeeeeeeeqws

                    if opcion_moral == "matar":
                        print("tanto matar canibales te volves un loco psicopata, sobrevives")
                        print("pero ahora te as vuelto un monstruo que mata gente por gusto")
                        print("FIN (final: psicopata. ocupese usted de bucar referencias)")

                    elif opcion_moral == "irte":
                        print("te vas, y los canibales restantes dicen que te dejaran en paz")
                        print("mientras no vuelvas a ese lugar")
                        print("FIN (final feliz. para ti pero no para los canibales)")

                    else :
                        print("pon algo valido")

                elif opcion_armas == "dejar":
                    print("no agarras nada y tratas de escapar pero")
                    print("cuando estas apunto de irte te encuentran")
                    print("FIN (final:desarmado) con el poder pero sin la volutantad de tomarlo")

                elif opcion_armas == "suicidarse":
                    print("coges el arma de tu preferencia y te la clavas en el estomago")
                    print("con tal de no sufrir mas cierras los ojos y mueres")
                    print("FIN (final cobarde)")

                else :
                    ("pon algo valido")
                       



            elif opcion_aldea == "esperar":
                print("te quedas donde estas sin hacer nada esperando un milagro")
                print("despues de una rato los canibales ven que no te mataron y te rodean")
                opcion_peligro = input("que haces??: DIALOGAR,DEFENDERTE o CORRER").lower()

                if opcion_peligro == "dialogar":
                    print("tratas de hablar con la horda enfurecida de los canibales")
                    print("pero apenas dices algo se te tiran todos encima")
                    print("FIN (Final:redada. como en resident evil 4 pero no eres tan guapo como leon jeje)")

                elif opcion_peligro == "defenderte":
                    print("tratas de defenderte pero no puedes hacer nada contra tantos enemigos")
                    print("se te tiran encima y te comen vivo para variar")
                    print("FIN (es final porque te comen vivo en los otros nomas te matan,claro)")

                elif opcion_peligro == "correr":
                    print("apuntas a espaldas de los canibales gritando (comidaaaaaaa)") 
                    print("y como tienen el coeficiente intelectual tan bajo  voltean")
                    print("aprovechas y te vas corriendo sin que se den cuenta")
                    print("FIN (final: ojala te hubieran matado)")

            else :
                print("decidete")

             

        elif opcion_duda == "acercarse":
            print("te acercas despacio y tratas de hablar pero no alcanzas")
            print("a decir algo porque te llega un disparo de flecha al pecho")
            print("FIN (Final:descuidado . nada que decir)")

        else :
            print("pon algo valido")
        
        
    elif opcion_trampa == "correr":
        print("logras esquivar esquivar las flechas corriendo")
        print("pero noesquivas a los canibales que te querian matar")
        print("FIN (final:suerte a medias. NYE JEJE)")
    else:
        print("pon algo valido")

elif opcion_inicio == "antorcha":
    print("enciendes la antorcha y ves 3 caminos")
    print("el primero con agua,el segundo con algo al fondo")
    print("y el tercero sin nada a la vista")
    opcion_caminos = input("cual vas: PRIMERO,SEGUNDO o TERCERO").lower() #SEGUNDO NIVEL DE PEGUNTAS DE ESTE LADO

    if opcion_caminos == "primero":
        print(" te acercas al agua y de ella salen serpiertes venenosas que te matan")
        print("FIN (final: serpientes. si hay serpientes de agua )")
    
    elif opcion_caminos == "segundo":
        print("anvanzas y ves que ese algo eran trampas que haces")
        opcion_trampas2 = input(" ESQUIVAS o DESACTIVAR").lower() # TERCER NIVEL DE PREGUNTAS DE ESTE LADO

        if opcion_trampas2 == "esquivas":
            print("empiezas a esquivar las trampas y logras ver la salida y salir con exito.")
            print("FIN (final:agil. pudo ser mas interesante per no queria escribir)")

        elif opcion_trampas2 == "desactivar":
            print("tratas de desactivar las trampas pero te caen flechaz venenosas no te matan al instante")
            print("pero te dejan sufriendo por horas sin poder salir,comer,beber agua,respirar bien")
            print("y sin poder ver a tu mama enferma que estaba recibiendo quimioterapia")
            print("FIN (final:sufrimiento. te lo mereces?)")

        else :
            print("pon algo valido")


    elif opcion_caminos == "tercero":
        print(" vas con la ilusion de irte para tu casa perooo")
        print("justo en la salida encuentras unos canibales y ps")
        print("FIN (final:iluso. a la otra te fijas)")

    else :
        print("pon algo bueeno")
        


else:
    print("pon algo valido")