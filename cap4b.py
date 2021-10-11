import libreriados as lc

def ParticulaPosicion(ket,X):

    return lc.detectarParticula(ket,X)
def transitarVectorVector(ket,ket2):

    return lc.transitarVector(ket,ket2)
def valorEsperado(obs,ket):
    obsSobreket = lc.accion(obs, ket)
    bra = lc.matrizConjugada(obsSobreket)
    ket1 = lc.transpuesta([ket])
    bra1 = lc.transpuesta(bra)
    car = lc.multiplicacionMatrizMatriz(bra1, ket1)[0][0]
    return car

def varianzaObservable(obs,ket):
    nve = lc.multiplicacion(valorEsperado(obs, ket), (-1, 0))
    mve = lc.multiplicacionEscalarMatriz(lc.matrizIdentidad(len(obs)), nve)
    delta = lc.sumaMatrices(obs, mve)
    deltaCuadrado = lc.multiplicacionMatrizMatriz(delta, delta)
    var = valorEsperado(deltaCuadrado, ket)
    return var
def propiosObservable(obs):
    for i in range(len(obs)):
        for j in range(len(obs[0])):
            obs[i][j]=complex(obs[i][j][0],obs[i][j][1])
    return obs

def probabilidadObservable(obs,ket):

    valP,vectP = propiosObservable(obs)
    probs=[]
    for v in vectP:
        p=lc.transitarVector(v,ket)
        probs.append(p)
    return probs
def dinamica(un,init,steps):
    up=[un]
    ur=un
    for p in range(steps):
        ur=lc.multiplicacionMatrizMatriz(ur,ur)
        up.append(ur)
    un1=[]
    for k in range(len(up)):
        un1=lc.multiplicacionMatrizMatriz(up[k],up[k-1])
    temp=lc.accion(un1,init)
    return temp