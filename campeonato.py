
FinCampeonato="NO"
empatados=0
ganados=0
TOTAL=0
perdidos=0
totperd=0
totgan=0
totemp=0

while FinCampeonato=="NO":
    perdidos = int(input("Ingresa CANTIDAD de partidos perdidos esta semana: "))
    totperd=totperd+perdidos
    empatados = int(input("Ingresa CANTIDAD de partidos empatados esta semana: "))
    totemp=totemp+empatados

    
    ganados = int(input("Ingresa CANTIDAD de partidos ganados esta semana: "))
    totgan=totgan+ganados
    
    FinCampeonato=input("Es el fin del campeonato? (SI/NO): ")

TOTAL= totemp+totgan*3
print("Puntaje total del campeonato: ", TOTAL )