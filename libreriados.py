import math
# operaciones complejos
def suma(a, b):
    real = a[0] + b[0]
    imag = a[1] + b[1]
    return ( real, imag )
    return (a1 + a2, b1 + b2)

def resta(c, d):
    real = c[0] - d[0]
    imag = c[1] - d[1]
    return (real, imag)

def multiplicacion(a, b):
    real = (a[0] * b[0])-(a[1] * b[1])
    imag = (a[0] * b[1])+(a[1] * b[0])
    return (real, imag)
def division(a, b):
    real = ((a[0] * b[0]) + (a[1] * b[1])) / ((b[0] * b[0]) + (b[1] * b[1]))
    imag = ((b[0] * a[1]) - (a[0] * b[1])) / ((b[0] * b[0]) + (b[1] * b[1]))
    return (real, imag)

def modulo(c):
    a1, b1 = c[0], c[1]
    return (a1 ** 2 + b1 ** 2) ** (1 / 2)
def conjugado(a):
    real = a[0]
    imag = -a[1]
    return (real, imag)
def sumaVectores(v, w):
    n = len(v)
    r = [(0,0)] *n
    for k in range(n):
        r[k]=suma(v[k],w[k])
    return r
def inversa(a):
    n = len(a)
    print(n)
    r = [(0,0)] * n
    for k in range(n):
        r[k] = multiplicacion((-1,0),a[k])
    return r
def multiplicacionEscalarVector(v1, c):
    for j in range(len(v1)):
        v1[j] = multiplicacion(v1[j], c)
    return v1
def sumaMatrices(m1, m2):
    for j in range(len(m1)):
        m1[j] = sumaVectores(m1[j], m2[j])
    return m1
def inversaMatriz(m1):
    for j in range(len(m1)):
        m1[j] = inversa(m1[j])
    return m1
def multiplicacionEscalarMatriz(m1, c):
    for j in range(len(m1)):
        m1[j] = multiplicacionEscalarVector(m1[j], c)
    return m1
def transpuesta(m1):
    m2 = [[(0, 0) for x in m1] for x in m1[0]]
    for j in range(len(m1[0])):
        for k in range(len(m1)):
            m2[j][k] = m1[k][j]
    return m2
def matrizConjugada(m1):
    for j in range(len(m1)):
        for k in range(len(m1[0])):
            m1[j][k] = conjugado(m1[j][k])
    return m1

def matrizAdjunta(m1):
    return matrizConjugada(transpuesta(m1))

def multiplicacionMatrizMatriz(m1, m2):
    m3 = [[(0, 0) for x in m2[0]] for x in m1]
    for j in range(len(m1)):
        for k in range(len(m2[0])):
            resultado = (0, 0)
            for h in range(len(m2)):
                resultado = suma(multiplicacion(m1[j][h], m2[h][k]), resultado)
                m3[j][k] = resultado
        return m3
def accion(m1, v1):
    return multiplicacionMatrizMatriz(m1, transpuesta([v1]))
def sumaDiagonal(m1):
    sumaD = (0, 0)
    for j in range(len(m1)):
        sumaD = suma(m1[j][j], sumaD)
    return sumaD
def productoInternoMatriz(m1, m2):
    return sumaDiagonal(multiplicacionMatrizMatriz(matrizAdjunta(m1), m2))

def normaMatriz( m1):
    return math.sqrt(productoInternoMatriz(m1, m1)[0])

def distanciaMatrizMatriz(m1, m2):
    return normaMatriz(sumaMatrices(m1, inversaMatriz(m2)))

def matrizIdentidad(n):
    ident = [[(0, 0) for x in range(n)] for x in range(n)]
    for j in range(n):
        ident[j][j] = (1, 0)
    return ident

def matrizUnitaria(m1):
    ident = matrizIdentidad(len(m1))
    m1 = multiplicacionMatrizMatriz(matrizAdjunta(m1), m1)
    esUnitaria = True
    for j in range(len(m1)):
        for k in range(len(m1)):
            if (m1[j][k] != ident[j][k]):
                esUnitaria = False
                break
    return esUnitaria

def matrizHermitian(m1):
    esHermitian = True
    m2 = matrizAdjunta(m1)
    for j in range(len(m1)):
        for k in range(len(m1)):
            if (resta(m1[j][k], m2[j][k]) != (0, 0)):
                esHermitian = False
                break
    return esHermitian

def productoTensor(m1, m2):
    m = len(m1)
    n = len(m2)
    m3 = [[(0, 0) for x in range(len(m1[0]) * len(m2[0]))] for x in range(m * n)]
    for j in range(len(m3)):
        for k in range(len(m3[0])):
            m3[j][k] = multiplicacion(m1[j // n][k // m], m2[j % n][k % m])
    return m3

def detectarParticula(ket,X):
    normaKet=normaMatriz([ket])
    normaComplejo=normaMatriz([[ket[X]]])
    return (normaComplejo**2)/(normaKet**2)
def transitarVector(ket,ket2):
    ket1=transpuesta([ket])
    bra=matrizConjugada([ket2])
    car=multiplicacionMatrizMatriz(bra,ket1)[0][0]
    normaBra=normaMatriz(bra)
    normaket=normaMatriz(ket1)
    car2=(normaBra*normaket,0)
    return division(car,car2)