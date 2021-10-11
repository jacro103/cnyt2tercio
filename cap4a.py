import libreriados as lc
def detectarParticula(ket,X):
    normaKet=lc.normaMatriz([ket])
    normaComplejo=lc.normaMatriz([[ket[X]]])
    return (normaComplejo**2)/(normaKet**2)
def transitarVector(ket,ket2):
    ket1=lc.transpuesta([ket])
    bra=lc.matrizConjugada([ket2])
    car=lc.multiplicacionMatrizMatriz(bra,ket1)[0][0]
    normaBra=lc.normaMatriz(bra)
    normaket=lc.normaMatriz(ket1)
    car2=(normaBra*normaket,0)
    return lc.division(car,car2)

def interfaz():
    ket=[tuple(map(float, x.split(","))) for x in (input("ket ").split(" "))]
    opt = int(input("Opcion"))
    while opt!=0:
        if (opt==1):
            print("Ingrese posicion")
            X= int(input("X: "))
            print(detectarParticula(ket,X))
        elif (opt==2):
            print("Ingrese vector ket")
            ket2=[tuple(map(float, x.split(","))) for x in (input("ket ").split(" "))]
            print(transitarVector(ket,ket2))
        else:
            print("Opcion Invalida")
        opt = int(input("Opcion "))