nombre=input('Ingresa tu nombre: ')
fecha_nacimiento=input('Ingresa tu fecha de nacimiento: DD/MM/AA: ')
dia_evaluar=fecha_nacimiento[:2]
mes_evaluar=fecha_nacimiento[3:5]


if int(mes_evaluar)>12:
    print('Has ingresado un mes incorrecto')
elif mes_evaluar=="01":
    if int(dia_evaluar)>31:
        print('Fecha inválida, verifícala!')
    elif int(dia_evaluar)<=20:
        print(f"{nombre}, tu signo zodiacal es: Capricornio")
    else:
        print(f"{nombre}, tu signo zodiacal es: Aquario")
elif mes_evaluar=="02":
    if int(dia_evaluar)>28:
        print("Fecha inválida, verifícala")
    elif int(dia_evaluar)<=18:
        print(f"{nombre}, tu signo zodiacal es: Aquario")
    else:
        print(f"{nombre}, tu signo zodiacal es: Piscis")
elif mes_evaluar=="03":
    if int(dia_evaluar)>31:
        print("Fecha inválida, verifícala")
    elif int(dia_evaluar)<=20:
        print(f"{nombre}, tu signo zodiacal es: Piscis")
    else:
        print(f"{nombre}, tu signo zodiacal es: Aries")
elif mes_evaluar=="04":
    if int(dia_evaluar)>30:
        print("Fecha inválida, verifícala")
    elif int(dia_evaluar)<=20:
        print(f"{nombre}, tu signo zodiacal es: Aries")
    else:
        print(f"{nombre}, tu signo zodiacal es: Tauro")
elif mes_evaluar=="05":
    if int(dia_evaluar)>31:
        print("Fecha inválida, verifícala")
    elif int(dia_evaluar)<=20:
        print(f"{nombre}, tu signo zodiacal es: Tauro")
    else:
        print(f"{nombre}, tu signo zodiacal es: Geminis")
elif mes_evaluar=="06":
    if int(dia_evaluar)>30:
        print("Fecha inválida, verifícala")
    elif int(dia_evaluar)<=21:
        print(f"{nombre}, tu signo zodiacal es: Geminis")
    else:
        print(f"{nombre}, tu signo zodiacal es: Cancer")
elif mes_evaluar=="07":
    if int(dia_evaluar)>31:
        print("Fecha inválida, verifícala")
    elif int(dia_evaluar)<=22:
        print(f"{nombre}, tu signo zodiacal es: Cancer")
    else:
        print(f"{nombre}, tu signo zodiacal es: Leo")
elif mes_evaluar=="08":
    if int(dia_evaluar)>31:
        print("Fecha inválida, verifícala")
    elif int(dia_evaluar)<=23:
        print(f"{nombre}, tu signo zodiacal es: Leo")
    else:
        print(f"{nombre}, tu signo zodiacal es: Virgo")
elif mes_evaluar=="09":
    if int(dia_evaluar)>30:
        print("Fecha inválida, verifícala")
    elif int(dia_evaluar)<=23:
        print(f"{nombre}, tu signo zodiacal es: Virgo")
    else:
        print(f"{nombre}, tu signo zodiacal es: Libra")
elif mes_evaluar=="10":
    if int(dia_evaluar)>31:
        print("Fecha inválida, verifícala")
    elif int(dia_evaluar)<=23:
        print(f"{nombre}, tu signo zodiacal es: Libra")
    else:
        print(f"{nombre}, tu signo zodiacal es: Scorpion")
elif mes_evaluar=="11":
    if int(dia_evaluar)>30:
        print("Fecha inválida, verifícala")
    elif int(dia_evaluar)<=23:
        print(f"{nombre}, tu signo zodiacal es: Scoprion")
    else:
        print(f"{nombre}, tu signo zodiacal es: Sagitario")
elif mes_evaluar=="12":
    if int(dia_evaluar)>31:
        print("Fecha inválida, verifícala")
    elif int(dia_evaluar)<=21:
        print(f"{nombre}, tu signo zodiacal es: Sagitario")
    else:
        print(f"{nombre}, tu signo zodiacal es: Capricornio")
else:
    print("Los días y los meses los debes de colocar así 02/04 por ejemplo")
