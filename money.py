#esercitazione money laboratorio

print("Money")
print("Determina il numero minimo di banconote")

print("")

importo = input("Inserisci un importo: ")

importo=int(importo)
n_venti=0
n_dieci=0
n_cinque=0
n_uno=0

if(importo<=0):
    print("Errore!!!")

else:
    n_venti = importo//20
    importo = importo - 20 * n_venti

    n_dieci = importo // 10
    importo = importo - 10 * n_dieci
    
    n_cinque = importo // 5
    importo = importo - 5 * n_cinque

    n_uno = importo  

    print("Banconote da $20: ", n_venti)
    print("Banconote da $10: ", n_dieci)
    print("Banconote da $5: ", n_cinque)
    print("Banconote da $1: ", n_uno)
