# -*- coding: utf-8 -*-
from datetime import date,datetime,timedelta
from datetime import *

week = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
time = ["Tarde", "Noite", "Madrugada", "Manhã"]
days_of_Month = [31,28,31,30,31,30,31,31,30,31,30,31]
folga = {}

hj = date.today().toordinal() # data de hoje transformada para fazer soma de dias 
days = int(date.today().strftime("%d")) # variável para iniciar dias (no futuro vai receber o date.today())
dayFirst = 0
month = int(date.today().strftime("%m"))
monthrange = days_of_Month[month-1]
folga 
dia_da_semana = date.weekday(date.today())
day_off = 0 
while dayFirst < monthrange:
    dayFirst +=1
    day_off +=1
    #folga simulada da madrugada
    if day_off == 6:
        if dayFirst < 10:
            folga = date.today().strftime("0"+str(dayFirst)+"/%m/%Y")
            print("Madrugada : {}".format(folga))
            #print(week[dayFirst])
        else:
            folga = date.today().strftime(str(dayFirst)+"/%m/%Y")
            print("Madrugada : {}".format(folga))
            #print(week[dayFirst])# IndexError: list index out of range
     #folga simulada da manhã
    if day_off == 7:
        if dayFirst < 10:
            folga = date.today().strftime("0"+str(dayFirst)+"/%m/%Y")
            print("Manhã : {}".format(folga))
            #print(week[dayFirst])
        else:
            folga = date.today().strftime(str(dayFirst)+"/%m/%Y")
            print("Manhã : {}".format(folga))
            #print(week[dayFirst])# IndexError: list index out of range
     #folga simulada da tarde
    if day_off == 8:
        if dayFirst < 10:
            folga = date.today().strftime("0"+str(dayFirst)+"/%m/%Y")
            print("Tarde : {}".format(folga))
            #print(week[dayFirst])
        else:
            folga = date.today().strftime(str(dayFirst)+"/%m/%Y")
            print("Tarde : {}".format(folga))
            #print(week[dayFirst])# IndexError: list index out of range
     #folga simulada da Noite
    if day_off == 9:
        if dayFirst < 10:
            folga = date.today().strftime("0"+str(dayFirst)+"/%m/%Y")
            print("Noite : {}".format(folga))
            #print(week[dayFirst])
        else:
            folga = date.today().strftime(str(dayFirst)+"/%m/%Y")
            print("Noite : {}".format(folga))
            #print(week[dayFirst])# IndexError: list index out of range
        day_off = 3
    
        