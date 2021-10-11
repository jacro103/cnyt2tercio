import libreria as lc
import matriz as lc
def amplitude_ket(n1, n2, k1, k2):
    k3 = k2
    r1 = lc.producto_Interno(n1, k1)
    r2 = lc.producto_Interno(n2, k2)
    return lc.producto_Interno(r1, r2)


def proba(h, ket):
    r = lc.norma(ket)
    x = ket[h]
    y = x
    sum_1 = lc.cplxmult(x, y)
    sum_2 = abs(sum_1[0] + sum_1[1])
    pro = sum_2/(r ** 2)
    return pro



def varianza(M, v):
    if len(M) == len(v[0]):
        H = lc.multmat(M, lc.trama(v))
        w = [[]]
        for j in H:
            w[0].append(j[0])
        x = lc.multmat(lc.trama(w), v)
        E = x[0][0][0] + x[1][0][1]
        m1 = lc.ident(E, M)
        N = lc.cplxrest(M, m1)
        Delta = lc.multmat(N, N)
        r = v
        for i in range(len(v)):
            for j in range(len(v[0])):
                x = v[i][j]
                c = x[0] ** 2
                t = x[1] ** 2
                r[i][j] = (c, t)
        Rf = lc.multmat(r, Delta)
        x = lc.prm(Rf[0][0])
        return round(x[0], 1)


def estadospropios(ob, v):
    ob1 = []
    for i in range(len(ob)):
        ob1.append([])
        for j in range(len(ob[0])):
            ob1[i].append(ob[i][j])
    for i in range(len(ob1)):
        for j in range(len(ob1[0])):
            ob1[i][j] = lc.complejo(ob1[i][j])
    N = list(ob1[0])
    y = varianza(ob, v)
    return N, y