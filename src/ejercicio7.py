################
# Lola Agustina Fioramanti - @lolafioramanti
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir un programa que permita transformar un número solicitado expresado en grados, minutos y segundos a segundos a segundos. Y otra que haga el cambio en el sentido contrario, devolviendo una tuple.

Recuerden que un grado son 60 minutos y un minuto son 60 segundos.
PRECONDICIONES: Los valores ingresados deben ser enteros positivos pertenecientes a cierto intervalo.
POSTCONDICIONES: Los valores de salida deben ser enteros positivos.
"""
def sexadecimal_a_decimal(horas, minutos, segundos):
    ''' Esta función convierte horas, minutos y segundos a segundos.'''
    horas *= 3600
    minutos *= 60
    a_segundos = horas + minutos + segundos
    return a_segundos
def decimal_a_sexadecimal(numero):
    '''Esta función convierte segundos a horas, minutos y segundos.'''
    segundo = numero % 60
    minuto = (numero // 60) % 60
    hora = (numero // 60) // 60
    return hora, minuto, segundo

def principal():
    '''Esta función interactúa con el usuario. En ella se solicitan los valores a convertir, y se muestran los resultados. Para lograrlo se encarga de utilizar la entrada, funciones y salida del algoritmo.'''
    horas = int(input("Ingrese las horas: "))
    if horas >= 0:
        minutos = int(input("Ingrese los minutos: "))
        if minutos >= 0 and minutos < 60:
            segundos = int(input("Ingrese los segundos: "))
            if segundos >= 0 and segundos < 60:
                conversion1 = sexadecimal_a_decimal(horas, minutos, segundos)
                print(f"{horas}:{minutos}:{segundos} equivale a {conversion1} segundos") 
                print()
                numero = int(input("Ingrese los segundos a convertir en hs, min y s: "))
                if numero >= 0:
                    hora, minuto, segundo = decimal_a_sexadecimal(numero)
                    print(f"{numero} equivale a {hora}hs {minuto}min {segundo}s")
                else:
                    print("Error, los segundos no pueden ser números negativos.")
            else:
                print("Error, los segundos deben ser como mínimo 0 y como máximo 59.")
        else:
            print("Error, los minutos deben ser como mínimo 0 y como máximo 59.")
    else:
        print("Error, las horas no pueden expresarse con números negativos.")



if __name__ == "__main__":
    principal()