# **Métodos Numéricos** - 1er Cuatrimestre 2024 [^1][^2] <!-- omit in toc -->

# Apuntes de Juan Cruz Barcos <!-- omit in toc -->

[Tabla de contenidos](#métodos-numéricos---1er-cuatrimestre-2024-1)- [Apuntes de clases](#apuntes-de-clases)

- [Clases teóricas](#clases-teóricas)
  - [Clase 1: 18 de marzo](#clase-1-18-de-marzo)
    - [1. Vectores](#1-vectores)
      - [**Definición**](#definición)
      - [**Suma**](#suma)
      - [**Multiplicación por escalar**](#multiplicación-por-escalar)
      - [**Producto interno**](#producto-interno)
      - [**Combinación lineal**](#combinación-lineal)
      - [**Vectores linealmente independientes**](#vectores-linealmente-independientes)
      - [**Vectores linealmente dependientes**](#vectores-linealmente-dependientes)
      - [**Subespacio generado**](#subespacio-generado)
      - [**Dimensión de S**](#dimensión-de-s)
      - [**Base de S**](#base-de-s)
    - [2. Matrices](#2-matrices)
      - [**Definición**](#definición-1)
      - [**Suma**](#suma-1)
      - [**Producto por escalar**](#producto-por-escalar)
      - [**Multiplicación**](#multiplicación)
      - [**Matriz identidad**](#matriz-identidad)
      - [**Matriz diagonal**](#matriz-diagonal)
      - [**Matriz triangular superior**](#matriz-triangular-superior)
      - [**Matriz triangular inferior**](#matriz-triangular-inferior)
      - [**Rango de una matriz**](#rango-de-una-matriz)
      - [**Matriz inversa**](#matriz-inversa)
      - [**Matriz estrictamente diagonal dominante**](#matriz-estrictamente-diagonal-dominante)
      - [**Matriz transpuesta**](#matriz-transpuesta)
      - [**Matriz de permutación**](#matriz-de-permutación)
      - [**Multiplicar por matrices de permutación**](#multiplicar-por-matrices-de-permutación)
      - [**Matriz elemental (tipo 1)**](#matriz-elemental-tipo-1)
      - [**Multiplicar por matriz elemental (tipo 1)**](#multiplicar-por-matriz-elemental-tipo-1)
      - [**Matriz elemental (tipo 2)**](#matriz-elemental-tipo-2)
      - [**Multiplicar por matriz elemental (tipo 2)**](#multiplicar-por-matriz-elemental-tipo-2)
      - [**Transformación linal**](#transformación-linal)
      - [**Espacio imagen**](#espacio-imagen)
      - [**Espacio nulo**](#espacio-nulo)
    - [3. Sistemas de ecuaciones lineales](#3-sistemas-de-ecuaciones-lineales)
      - [**Definición**](#definición-2)
    - [Tarea](#tarea)
      - [**Ejercicio 1**](#ejercicio-1)
      - [**Ejercicio 2**](#ejercicio-2)
    - [Tarea resuelta](#tarea-resuelta)
      - [**Ejercicio 1**](#ejercicio-1-1)
      - [**Ejercicio 2**](#ejercicio-2-1)
  - [Clase 2: 25 de marzo](#clase-2-25-de-marzo)
    - [Sistemas de ecuaciones lineales](#sistemas-de-ecuaciones-lineales)
      - [**Equivalencia de sistemas de ecuaciones**](#equivalencia-de-sistemas-de-ecuaciones)
    - [Sistemas de ecuaciones lineales fáciles](#sistemas-de-ecuaciones-lineales-fáciles)
      - [**Matriz diagonal**](#matriz-diagonal-1)
      - [**Matriz triangular superior**](#matriz-triangular-superior-1)
    - [Método de Eliminación Gaussiana](#método-de-eliminación-gaussiana)
      - [**Algoritmo**](#algoritmo)
      - [**Esquema básico**](#esquema-básico)
    - [Estrategias de pivoteo](#estrategias-de-pivoteo)
      - [**Pivoteo parcial**](#pivoteo-parcial)
      - [**Pivoteo completo**](#pivoteo-completo)
    - [Factorización LU](#factorización-lu)
      - [**Beneficio algorítmico**](#beneficio-algorítmico)
      - [**Procedimiento**](#procedimiento)
      - [**Propiedades**](#propiedades)
- [Clases prácticas](#clases-prácticas)
  - [Clase 1: 20 de marzo](#clase-1-20-de-marzo)
    - [Vectores canónicos](#vectores-canónicos)
    - [Multiplicación de matrices por vectores canónicos](#multiplicación-de-matrices-por-vectores-canónicos)
    - [Combinaciones lineales](#combinaciones-lineales)
    - [Independencia lineal](#independencia-lineal)
    - [Base](#base)
      - [**Propiedad**](#propiedad)
    - [Transformación lineal](#transformación-lineal)
    - [Relación entre transformaciones lineales y matrices](#relación-entre-transformaciones-lineales-y-matrices)
      - [**Proposición**](#proposición)
    - [Traza de una matriz](#traza-de-una-matriz)
    - [Núcleo](#núcleo)
      - [**Hallar el núcleo de una transformación lineal**](#hallar-el-núcleo-de-una-transformación-lineal)
    - [Imagen](#imagen)
      - [**Hallar la imagen de una transformación lineal**](#hallar-la-imagen-de-una-transformación-lineal)
    - [Teorema de la dimensión](#teorema-de-la-dimensión)
- [Guías prácticas](#guías-prácticas)
  - [Guía práctica 1](#guía-práctica-1)
    - [Guía práctica 1 - Ejercicio 1](#guía-práctica-1---ejercicio-1)
      - [**1) a.**](#1-a)
      - [**1) b.**](#1-b)
      - [**1) c.**](#1-c)
      - [**1) d.**](#1-d)
    - [Guía práctica 1 - Ejercicio 2](#guía-práctica-1---ejercicio-2)
      - [**2) a.**](#2-a)
      - [**2) b.**](#2-b)
      - [**2) c.**](#2-c)
      - [3) ¿Qué otras particiones son posibles?](#3-qué-otras-particiones-son-posibles)
    - [Guía práctica 1 - Ejercicio 3](#guía-práctica-1---ejercicio-3)
      - [**3) a.**](#3-a)
      - [**3) b.**](#3-b)
    - [Guía práctica 1 - Ejercicio 4](#guía-práctica-1---ejercicio-4)
      - [**4) a.**](#4-a)
      - [**4) b.**](#4-b)
    - [Guía práctica 1 - Ejercicio 5](#guía-práctica-1---ejercicio-5)
    - [Práctica 1 - Ejercicio 20](#práctica-1---ejercicio-20)
      - [**20) a.**](#20-a)
      - [**20) b.**](#20-b)
      - [**20) c.**](#20-c)

# Clases teóricas

## Clase 1: 18 de marzo

### 1. Vectores

#### **Definición**

$v \in \mathbb{R}^n$ n-upla de coeficientes reales
$v = (v_{1},v_{2},...,v_{n})$

#### **Suma**

Intuición: suma lugar a lugar.  
$w = v + u$ con $w_i = v_i + u_i$ para $i = 1,...,n$ (conmutativa, asociativa).

#### **Multiplicación por escalar**

Intuición: Multiplica todos los números del vector por el escalar.  
Sea $a \in \mathbb{R}$, $w = \alpha v$ con $w_{i} = \alpha v_{i}$ para $i = 1,...,n$

#### **Producto interno**

Intuición: Multiplicación lugar a lugar y suma de los resultados.

$$
< u, v > = \sum_{i = 1}^{n} u_i v_i
$$

#### **Combinación lineal**

$$
w = \sum_{k=1}^{K} a_k v^k
$$

#### **Vectores linealmente independientes**

$$
\sum_{k=1}^{K} a_k v^k = 0 \to a_k = 0 \forall k = 1,...,K
$$

#### **Vectores linealmente dependientes**

Existen $a_k$ con $k = 1,...,K$ no todos nulos tal que

$$
\sum_{k=1}^{K} a_k v^k = 0
$$

#### **Subespacio generado**

$$
S = \{x \in \mathbb{R}^n \text{ tal que } x = \sum_{k=1}^{K} \alpha_k v^k\}
$$

#### **Dimensión de S**

Cantidad máxima de vectores linealmente independientes en S.

#### **Base de S**

Conjunto de vectores linealmente independientes que generan a S.

### 2. Matrices

#### **Definición**

$A \in \mathbb{R}^{mxn}$

$$
A =
\begin{bmatrix}
a_{11} & a_{12} & ... & a_{1n} \\
a_{21} & a_{22} & ... & a_{2n} \\
... & ... & ... & ... \\
a_{i1} & a_{i2} & ... & a_{in} \\
... & ... & ... & ... \\
a_{m1} & a_{m2} & ... & a_{mn}
\end{bmatrix}
$$

#### **Suma**

Intruición: suma lugar a lugar.  
Definida si $m = p, n = q$  
$C = A + B$ con $c_{ij} = a_{ij} + b_{ij}$ para $i = 1,...,m$, $j = 1,...,n.$  
$C \in \mathbb{R}^{mxn}$ (conmutativa, asociativa)

#### **Producto por escalar**

Intuición: multiplica cada elemento de la matriz por el escalar.  
$C = \alpha A$ con $c_{ij} = \alpha a_{ij}$ para $i = 1,...,m$, $j = 1,...,n$, $C \in \mathbb{R}^{mxn}$

#### **Multiplicación**

Definida si $n = p$. $C = AB$ tal que
$A \in \mathbb{R}^{mxn}$, $B \in \mathbb{R}^{pxq}$

$$
c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}, \text{ para } i = 1,...,m, j = 1,...,q, C \in \mathbb{R}^{mxq}
$$

NO es conmutativa.

#### **Matriz identidad**

Intuición: Diagonal de unos y el resto ceros.  
$I \in \mathbb{R}^{nxn}$ si
$I_{ii} = 1$, $I_{ij} = 0$ si $i \neq j$

#### **Matriz diagonal**

Intuición: Diagonal de números y el resto cero.  
$D \in \mathbb{R}^{nxn}$ si
$D_{ii} = k_i, D_{ij} = 0$ si $i \neq j$

#### **Matriz triangular superior**

Intuición: De la diagonal para abajo es todo ceros.  
$U \in \mathbb{R}^{nxn}$ con $u_{ij} = 0$ si $i > j$  
Producto de triangulares superiores es triangular superior.
El determinante de una matriz triangular es el producto de los elementos de su diagonal.

#### **Matriz triangular inferior**

Intuición: De la diagonal para arriba es todo ceros.  
$L \in \mathbb{R}^{nxn}$ con $l_{ij} = 0$ si $i < j$  
Producto de triangulares inferiores es triangular inferior.
El determinante de una matriz triangular es el producto de los elementos de su diagonal.

#### **Rango de una matriz**

Cantidad máxima de columnas o filas linealmente independiente.

#### **Matriz inversa**

Definida si $m = n$. $A^{-1} \in \mathbb{R}^{nxn}$.
$AA^{-1} = A^{-1}A = I$  
$A$ inversible $\iff rang(A) = n \iff det(A) \neq 0 \text{ (matriz no singular)}$  
La inversa (si existe) de una matriz diagonal es matriz diagonal.  
La inversa (si existe) de una matriz triangular inferior es matriz triangular inferior.  
La inversa (si existe) de una matriz triangular superior es matriz triangular superior.

#### **Matriz estrictamente diagonal dominante**

Intuición: Cada elemento de la diagonal es mayor a la suma del resto de los elementos de su fila (todo en valor absoluto).  
$A \in \mathbb{R}^{nxn}$

$$
|a_{ii}| > \sum_{j\neq i} |a_{ij}| ~ \forall 1,...,n
$$

#### **Matriz transpuesta**

Intuición: Las filas ahora son las columnas y las columnas las filas.  
$A^t \in \mathbb{R}^{nxm}$  
$a^t_{ij} = a_{ji}$ para todo $i = 1,...,m$, $j = 1,...,n$  
$(A^t)^t = A$  
$(A + B)^t = A^t + B^t$  
$(AB)^t = B^t A^t$  
$(A^t)^{-1} = (A^{-1})^t$

#### **Matriz de permutación**

$P \in \mathbb{R}^{nxn}$. Son una permutación de las filas (o columnas) de la matriz identidad.

#### **Multiplicar por matrices de permutación**

Intuición: Si multiplico con la matriz de permutación a izquierda, permuta las filas.  
Si multiplico con la matriz de permutación a derecha, permuta las columnas.

#### **Matriz elemental (tipo 1)**

$E \in \mathbb{R}^{nxn}$. Matriz identidad con una fila multiplicada por un escalar no nulo.

#### **Multiplicar por matriz elemental (tipo 1)**

Intuición: Si multiplico con la matriz elemental a izquierda, multiplica la fila por el escalar.  
Si multiplico con la matriz elemental a derecha, multiplica la columna por el escalar.

#### **Matriz elemental (tipo 2)**

$E \in \mathbb{R}^{nxn}$. Matriz identidad con un elemento no nulo fuera de la diagonal.

#### **Multiplicar por matriz elemental (tipo 2)**

Intuición: Si multiplico con la matriz elemental a izquierda con un escalar en $I_{ij}$, a la fila i le suma la fila j multiplicada por el escalar.  
Si multiplico con la matriz elemental a derecha con un escalar en $I_{ij}$, a la columna j le suma la columna i multiplicada por el escalar.

#### **Transformación linal**

Multiplicar una matriz $A \in \mathbb{R}^{mxn}$ por un vector $x \in \mathbb{R}^{nx1}$ y obtener $y \in \mathbb{R}^{mx1}$

#### **Espacio imagen**

$Im(A) = {y \in \mathbb{R}^m \text{ tal que existe } x \in \mathbb{R}^n \text{ con } Ax = y}$

#### **Espacio nulo**

$N(A) = {x \in \mathbb{R}^n \text{ tal que } Ax = 0}$  
$N(A) \neq {0} \iff \text{ las columnas de A son linealmente dependientes.}$

### 3. Sistemas de ecuaciones lineales

#### **Definición**

$a_{11} x_1 + a_{12} x_2 + ... + a_{1n} x_n = b_1$  
$a_{21} x_1 + a_{22} x_2 + ... + a_{2n} x_n = b_2$  
...  
$a_{n1} x_1 + a_{n2} x_2 + ... + a_{nn} x_n = b_n$

$A \in \mathbb{R}^{mxn}$

$$
A =
\begin{bmatrix}
a_{11} & a_{12} & ... & a_{1n} \\
a_{21} & a_{22} & ... & a_{2n} \\
... & ... & ... & ... \\
a_{i1} & a_{i2} & ... & a_{in} \\
... & ... & ... & ... \\
a_{m1} & a_{m2} & ... & a_{mn}
\end{bmatrix}
$$

$$
x =
\begin{bmatrix}
x_{11} & x_{12} & ... & x_{1n}
\end{bmatrix}
$$

$$
b =
\begin{bmatrix}
b_{11} & b_{12} & ... & b_{1n}
\end{bmatrix}
$$

$$Ax = b$$

### Tarea

#### **Ejercicio 1**

Demostrar que el producto de dos matrices diagonales inferiores es una matriz diagonal inferior (ídem superior).

#### **Ejercicio 2**

Demostrar que la inversa (si existe) de una matriz triangular inferior es matriz triangular inferior. (ídem superior).

### Tarea resuelta

#### **Ejercicio 1**

Tomando dos matrices diagonales superiores genéricas $A$ y $B \in \mathbb{R}^{nxn}$, veamos el resultado de $C = AB$.

$$
c_{ij} = \sum_{k=1}^{n} a_{ik}*b_{kj}
$$

Recordemos que, como ambas son matrices diagonales superiores, debajo de la diagonal, sus valores son 0. Por lo tanto, en $c_{ij}$, donde $i > j$, en la fila $i$ de $A$, tendremos exactamente $i - 1$ posiciones con valor 0, pues son aquellas posiciones donde $i > j$ y que, por definición, son 0. Además, en la columna $j$ de $B$, tendremos exactamente $n - j$ posiciones con valor 0, pues son las posiciones donde $i > j$ y, por definición, distintas de 0.  
Luego, para

$$
\sum_{k=1}^{i-1} a_{ik} b_{kj}
$$

$a_{ik}$ siempre será 0, por lo que la sumatoria será 0.  
Para

$$
\sum_{k=i}^{n} a_{ik} b_{kj}
$$

$b_{kj}$ siempre será 0, pues $k > j$, por comenzar siendo $i$, que es mayor a $j$, por lo que la sumatoria será 0.  
Por lo tanto, para todas las posiciones debajo de la diagonal, el valor resultante será 0.  
Luego, $C$ es diagonal superior. Ídem para diagonal inferior, invirtiendo el sentido.

#### **Ejercicio 2**

Sea $A \in \mathbb{R}^{nxn}$ tiangular superior y $BA = I_n$.  
Teniendo en cuenta que $A$ es triangular superior, $b_{11} a_{11} = 1$ y $b_{j1} a_{11} = 0$. Por lo tanto, la primera columna de B es

$$
\begin{bmatrix}
a_{11}^{-1} \\
0 \\
: \\
0
\end{bmatrix}
$$

Suponiendo $j > 1$ e inductivamente que las $j-1$ primeras columnas de B son

$$
\begin{bmatrix}
b_{11} = a_{11}^{-1} & ... & b_{1j-2} & b_{1j-1} \\
: & : & : & : \\
0 & ... & 0 & b_{j-1j-1} = a_{j-1j-1}^{-1} \\
: & : & : & : \\
0 & ... & 0 & 0
\end{bmatrix}
$$

Vamos a probar que $b_{jj} = a_{jj}^{-1}$ y $b_{kj} = 0, k=j+1,...,n$.

$b_{jj} = a_{jj}^{-1}$:  
$BA_{jj}$ debe ser 1, luego,  
$b_{j1} a_{1j} + ... + b_{jj} a_{jj} + ... + b_{jn} a_{nj} = 1$

Por inducción,  
$b_{j1} = ... = b_{jj-1} = 0$

Y por tiangularidad de $A$  
$a_{j+1j} = ... = a_{nj} = 0, k > j$

Se tiene  
$b_{jj}a_{jj} = 1$ y $b_{jj}=a_{jj}^{-1}$

$b_{kj}=0, k=j+1,...,n$:  
$BA_{kj}$ $= 0$, luego  
$b_{k1} a_{1j} + ... + {b_kj} a_{jj} + ... + n_{jn} a_{nj} = 1$

Por inducción,  
$b_{k1} = ... = b_{kj-1} = 0$

Y por triangularidad de A  
$a_{j+1j} = ... = a_{nj} = 0, k > j$

Luego, $b_{kj}a_{jj} = 0$, puesto que $a_{jj}$ es no nulo, $b_{kj}$ debe serlo.

## Clase 2: 25 de marzo

### Sistemas de ecuaciones lineales
$A \in \mathbb{R}^{nxn}, b \in \mathbb{R}^n$. Se busca $x \in \mathbb{R}^n$ tal que $Ax = b$.  
Si $b \notin Im(A)$, el sistema no tiene solución.  
Si $b \in Im(A)$, puede existir una única solución o infinitas.

#### **Equivalencia de sistemas de ecuaciones**
Los sistemas $Ax = b$ y $Bx = d$ son equivalentes si tienen el mismo conjunto de soluciones.  
Dada una matriz $A$, sumar, restar, permutar o multiplicar filas (o columnas) por coeficientes no nulos, la matriz resultante es equivalente.  
En el caso de la permutación de columnas, la solución también queda permutada en relación a las permutaciones realizadas.

### Sistemas de ecuaciones lineales fáciles

#### **Matriz diagonal**
Sea $D \in \mathbb{R}^{nxn}$ matriz diagonal, $b \in \mathbb{R}^n$  
Si $d_{ii} \neq 0$ para todo $i = 1,...,n$, existe solución y es única.  
$$
x_i = b_1 / d_{ii} \text{ para todo } i = 1,...,n
$$  
$O(n)$ operaciones elementales.  
Si existe algún $d_{ii} = 0$, el sistema puede no tener solución o tener infinitas soluciones.  
Depende de si $b_i$ es igual o distinto de $0$.

#### **Matriz triangular superior**
Sea $U \in \mathbb{R}^{nxn}$ matriz diagonal superior, $b \in \mathbb{R}^n$  
Si $u_{ii} \neq 0$ para todo $i = 1,...,n$, existe solución y es única.
$$
x_n = b_n / u_{nn}
$$
$$
x_{n-1} = (b_{n-1} - u_{n-1n} x_n) / u_{n-1 n-1}
$$
$$
...
$$
$$
x_i = (b_i - \sum_{j = i+1}^{n} u_{ij} x_j ) / u_{ii}
$$
$$
...
$$
$$
x_1 = (b_1 - \sum_{j = 2}^{n} u_{1j} x_j) / u_{11}
$$

Backward sustitution, $O(n^2)$ operaciones elementales.

$U \in \mathbb{R}^{nxn}$ matriz triangular superior, $b \in \mathbb{R}^n$  
Si existe algún $d_{ii} = 0$, el sistema puede no tener solución o tener infinitas soluciones.  
Para matrices triangulares inferiores valen las mismas propiedades

### Método de Eliminación Gaussiana
El objetivo es construir un sistema equivalente cuya matriz asociada sea fácil.  
Para hacer esto, se suman, restan, permutan o multiplican por coeficientes no nulos sus filas (o columnas).

#### **Algoritmo**
$$
\begin{bmatrix}
a_{11}^0 & a_{12}^0 & ... & a_{1n}^0 & | & b_1^0 \\\
: & : & : & : & | & : \\\
a_{i1}^0 & a_{i2}^0 & ... & a_{in}^0 & | & b_i^0 \\\
: & : & : & : & | & : \\\
a_{n1}^0 & a_{n2}^0 & ... & a_{nn}^0 & | & b_n^0
\end{bmatrix}
$$
$$
\to 
F_2 - (a_{21}^0 / a_{11}^0) F_1 \\
... \\
F_i - (a_{i1}^0 / a_{11}^0) F_1 \\
... \\
F_n - (a_{n1}^0 / a_{11}^0) F_1 \\
$$
$$
\begin{bmatrix}
a_{11}^1 & a_{12}^1 & ... & a_{1n}^1 & | & b_1^1 \\\
: & : & : & : & | & : \\\
0 & a_{i2}^1 & ... & a_{in}^1 & | & b_i^1 \\\
: & : & : & : & | & : \\\
0 & a_{n2}^1 & ... & a_{nn}^1 & | & b_n^1
\end{bmatrix}
$$

Se ejecuta de manera similar para todas las filas, hasta tener 
$$
\begin{bmatrix}
a_{11}^n & a_{12}^n & ... & a_{1 n-1}^n & a_{1n}^n & | & b_1^n \\\
: & : & : & : & : & | & : \\\
0 & 0 & ... & a_{i n-1}^n & a_{in}^n & | & b_i^n \\\
: & : & : & : & : & | & : \\\
0 & 0 & ... & 0 & a_{nn}^n & | & b_n^n
\end{bmatrix}
$$

#### **Esquema básico**
```
for (i = 1) to (n - 1):
  for (j = i + 1) to (n):
    M[j][i] = A^{i-1}[j][i] / A^{i-1}[i][i]
    for (k = i) to (n + 1):
      A^{i}[j][k] = A^{i-1}[j][k] - M[j][i] * A^{i-1}[i][k]
```
Condición necesaria: $a_{ii}^{i-1} \neq 0$ para todo $i = 1,...,n-1$  
El coste algorítmico es $O(n^3)$.

### Estrategias de pivoteo

#### **Pivoteo parcial**
Entre las filas $i$ a $n$, utilizar como fila pivote aquella con mayor $|a_{ji}^{i - 1}|$. Realizar la permutación necesaria entre las filas para ubicar en el lugar $ii$ dicho coeficiente.

#### **Pivoteo completo**
Entre las filas $i$ a $n$ y las columnas $i$ a $n$, calcular el mayor $|a_{kl}^{i - 1}|$. Realizar la permutación necesaria entre las filas y las columnas para ubicar en el lugar $ii$ dicho coeficiente.

### Factorización LU
El objetivo es factorizar una matriz como el producto de una matriz diagonal inferior y otra diagonal superior.  
$Ax = b = LUx$  

#### **Beneficio algorítmico**
Una vez teniendo la factorización LU, para cualquier sistema de ecuaciones donde se use $A$, podemos hacer  
$Ly = b, Ux = y$  
Esta resolución tiene complejidad $O(n^2)$.

#### **Procedimiento**
Sea $A \in \mathbb{R}^{nxn}$. Supongamos que aplicamos eliminación Gaussiana y se verifica que $a_{ii}^{i-1} \neq 0$ para todo $i = 1,...,n-1$. Esta matriz triangular superior, será $U$.  
Si expresamos matricialmente el proceso de eliminación Gaussiana realizado para obtener $U$, con  
$$
M^i = 
\begin{bmatrix}
1 & ... & 0 & 0 & ... & 0 \\\
: & : & : & : & : & : \\\
0 & ... & 1 & 0 & ... & 0 \\\
0 & ... & -m_{i+1 i} & 1 & ... & 0 \\\
: & : & : & : & : & : \\\
0 & ... & -m_{ni} & 0 & ... & 1
\end{bmatrix}
$$
Todas las $M_i$ son triangular inferior. El producto de triangulares inferiores es triangular inferior e inversa de triangular inferior es triangular inferior.  
Por lo tanto, $L$ será la inversa del producto de todas las matrices $M$.  
$$
M^1 M^2 ... M^{n-1} A = U
$$
Llamo $T$ a $M^1 M^2 ... M^{n-1}$
$$
\Rightarrow T A = U
$$
$$
\Rightarrow T^{-1} T A = T^{-1} U
$$
$$
\Rightarrow I A = T^{-1} U
$$
$$
\Rightarrow A = T^{-1} U
$$
Luego, $T^{-1}$ es $L$.  
Sabemos que $T$ es inversible ya que $det(T) = 1$ (producto de la diagonal).  
Más aún, $L = I + m_{1}^{t} e_1 + ... + m_{n-1}^{t} e_{n-1}$. Esto debido a que 
$$
(M^1 M^2 ... M^{n-1})^{-1} = (M^1)^{-1} (M^2)^{-1} ... (M^{n-1})^{-1}
$$

Y sabemos que $M^i = I - m_i^t e_i$  
Luego, $(M^i)^{-1} = I + m_i^t e_i$, por lo que tenemos (haciendo distributiva de las multiplicaciones)
$$
I + m_{1}^{t} e_1 + ... + m_{n-1}^{t} e_{n-1}
$$

#### **Propiedades**
- No toda matriz inversible tiene factorización LU. Por ejemplo, $\begin{bmatrix} 0 & 1 \\\ 1 & 0 \end{bmatrix}$
- Si $A \in \mathbb{R}^{nxn}$ es no singular y existe factorización LU, entonces es única.
- Si $A \in \mathbb{R}^{nxn}$ tiene todas sus submatrices principales no singulares, entonces tiene factorización LU.
- Si $A \in \mathbb{R}^{nxn}$ es estrictamente diagonal dominante, entonces tiene factorización LU.



# Clases prácticas

## Clase 1: 20 de marzo

### Vectores canónicos

El vector canónico $e_i \in \mathbb{R}^{nx1}$, es aquel que posee el valor 0 en todas sus posiciones, excepto por la posición $i$, donde vale 1.

### Multiplicación de matrices por vectores canónicos

$Ae_i$ es igual a la columna $i$ de $A$.  
$e_i^tA$ es igual a la fila $i$ de $A$.

### Combinaciones lineales

Si $C = \{v_1,...,v_k\}$ es un conjunto de vectores en $\mathbb{R}^n$  
Se dice que $x \in \mathbb{R}^n$ es combinación lineal de $C$ si:

$$
\exists {\alpha}_1,...,{\alpha}_k \in \mathbb{R} / x = {\alpha}_1v_1 + ... + {\alpha}_kv_k
$$

### Independencia lineal

$S = < v_1,...,v_k >$ es el conjunto de todas las combinaciones lineales de $v_1,...,v_k$. Le llamamos subespacio generado por $v_1,...,v_k$. A $v_1,...,v_k$ le llamamos generadores de $S$.

### Base

$B \subseteq \mathbb{V}$ es una base del espacio vectorial $\mathbb{V}$ si es un sistema de generadores linealmente independiente.

- $< B > = \mathbb{V}$
- $B$ es linealmente independiente

#### **Propiedad**

Todas las bases de un espacio vectorial tienen el mismo cardinal. Ese cardinal se va a llamar dimensión del espacio vectorial.

### Transformación lineal

$f: \mathbb{V} \to \mathbb{W}$ es una transformación lineal $\iff$

- $f(v) + f(w) = f(v + w) ~~ \forall v,w \in \mathbb{V}$
- $f(\lambda v) = \lambda f(v) ~~ \forall \lambda \in \mathbb{R}, \forall v \in \mathbb{V}$

### Relación entre transformaciones lineales y matrices

$A \in \mathbb{R}^{nxm}, x \in \mathbb{R}^m$  
$f(x) = Ax, f: \mathbb{R}^m \to \mathbb{R}^n$  
$f$ resulta una transformación lineal.

#### **Proposición**

Para cada $f$, podemos encontrar la única $A$ tal que $f(x) = Ax$, donde definimos $A = M(f)$.

### Traza de una matriz

La traza de una matriz es la suma de los elementos de la diagonal.

$$
tr(A) = \sum_{i=1}^n a_{ii}, A \in \mathbb{R}^{nxm}
$$

### Núcleo

$f(x) = Ax, f: \mathbb{R}^n \to \mathbb{R}^m$  
$Nu(f) = Nu(A) = \{x \in \mathbb{R}^n / f(x) = 0\}$

#### **Hallar el núcleo de una transformación lineal**

Para hallar el núcleo de una transformación lineal, se puede armar el sistema de ecuaciones de $A = M(f)$ tal que el resultado es 0.  
$Ax = 0$  
Por ejemplo:

$$
\begin{bmatrix}
  1 & 2 & 0 \\\
  0 & 1 & 0
\end{bmatrix}
\begin{bmatrix}
  x_1 \\\ x_2 \\\ x_3
\end{bmatrix} =
\begin{bmatrix}
  0 \\\ 0
\end{bmatrix}
$$

Luego, el núcleo será $x$ tal que:

$$
\begin{cases}
1x_1 + 2x_2 + 0x_3 = 0 \\\
0x_1 + 1x_2 + 0x_3 = 0
\end{cases}
$$

### Imagen

$f: \mathbb{R}^n \to \mathbb{R}^m, A = M(f)$  
$Im(f) = \{ Ax / x \in \mathbb{R}^n\}$

#### **Hallar la imagen de una transformación lineal**

La imagen de una transformación lineal es equivalente al subespacio generado por las columnas de la matriz $A$ tal que $A = M(f)$.

### Teorema de la dimensión

Sea $f: \mathbb{V} \to \mathbb{W}$,  
$dim(Nu(f)) + dim(Im(f)) = dim(\mathbb{V})$

# Guías prácticas

## Guía práctica 1

### Guía práctica 1 - Ejercicio 1

#### **1) a.**

Falso. $A \in \mathbb{R}^{nxm}$ y $z \in \mathbb{R}^{nx1}$, por lo que no se pueden multiplicar.

#### **1) b.**

Falso. El resultado de multiplicar $x \in \mathbb{R}^{nx1}$ y $z^t \in \mathbb{R}^{1xn}$ debe pertenecer a $\mathbb{R}^{nxn}$, no a $\mathbb{R}^{1x1}$.

#### **1) c.**

Verdadero.

#### **1) d.**

Verdadero.

### Guía práctica 1 - Ejercicio 2

#### **2) a.**

$C_{11} = A_{11}B_{11} + A_{12}B_{21} = 1 + 9 = 10$ y $C_{11} \in \mathbb{R}^{1x1}$

$C_{12} = A_{11}B_{12} + A_{12}B_{22} = [1, 1] + [0, 3] = [1,4]$ y $C_{12} \in \mathbb{R}^{1x2}$

$C_{21} = A_{21}B_{11} + A_{22}B_{21} = [0,1]^t + [7,2]^t = [7,3]^t$ y $C_{21} \in \mathbb{R}^{1x2}$

$$
C_{22} = A_{21} B_{12} + A_{22} B_{22} = \begin{bmatrix} 0 & 0 \\\ 1 & 1 \end{bmatrix} + \begin{bmatrix} 0 & 5 \\\ 0 & 2 \end{bmatrix} = \begin{bmatrix} 0 & 5 \\\ 1 & 2 \end{bmatrix}
$$

$$
C_{22} \in \mathbb{\mathbb{R}}^{2x2}
$$

#### **2) b.**

$C_{11} = A_{11}B_{11} + A_{12}B_{21}$ donde $A_{11} \in \mathbb{R}^{1x2}$ y $B_{11} \in \mathbb{R}^{1x1}$. Por lo tanto, no es posible.

#### **2) c.**

$C_{11} = A_{11}B_{11} + A_{12}B_{21}$ donde $A_{12} \in \mathbb{R}^{2x2}$ y $B_{21} \in \mathbb{R}^{1x2}$. Por lo tanto, no es posible.

#### 3) ¿Qué otras particiones son posibles?

Son posibles todas aquellas particiones donde en la diagonal queden particiones cuadradas y de los mismos tamaños, ya que deben multiplicarse entre ellas por ambos lados.  
En este caso en específico, sólo hay dos particiones posibles distintas de las matrices originales, que son a) y:

$$
A_{11} = \begin{bmatrix} a_{11} & a_{12} \\\ a_{21} & a_{22} \end{bmatrix}, A_{12} = \begin{bmatrix} a_{13} \\\ a_{23} \end{bmatrix}, A_{21} = \begin{bmatrix} a_{31} & a_{32} \end{bmatrix}, A_{22} = \begin{bmatrix} a_{33} \end{bmatrix}
$$

$$
B_{11} = \begin{bmatrix} b_{11} & b_{12} \\\ b_{21} & b_{22} \end{bmatrix}, B_{12} = \begin{bmatrix} b_{13} \\\ b_{23} \end{bmatrix}, B_{21} = \begin{bmatrix} b_{31} & b_{32} \end{bmatrix}, B_{22} = \begin{bmatrix} b_{33} \end{bmatrix}
$$

### Guía práctica 1 - Ejercicio 3

#### **3) a.**

Si $\forall x \in \mathbb{R}^n \Rightarrow Ax = Bx$, específicamente para $e_1,...,e_n$ vectores canónicos de $\mathbb{R}^n$, también vale.  
Luego, $Ae_1 = Be_1,...,Ae_n=Be_n$. Pero, para cualquier matriz $C \in \mathbb{R}^{nxn}, Ce_i = \text{columna i de C}$.  
Por lo tanto, $\forall c_i \text{ columna i de } A, \text{ vale que } c_i \text{ es igual a la columna i de } B$.  
Por lo tanto, si todas sus columnas son iguales, son la misma matriz.

#### **3) b.**

Miremos $a_1 b_1^t$.

$$
a_1 b_1^t =
\begin{bmatrix}
  a_{11} b_{11} & a_{11} b_{12} & ... & a_{11} b_{1n} \\\
  a_{21} b_{11} & a_{21} b_{12} & ... & a_{21} b_{1n} \\\
  : & : & : & : \\\
  a_{n1} b_{11} & ... & ... & a_{n1} b_{1n}
\end{bmatrix}
$$

Ahora veamos para el caso general

$$
a_i b_i^t =
\begin{bmatrix}
  a_{1i} b_{i1} & a_{1i} b_{i2} & ... & a_{1i} b_{in} \\\
  a_{2i} b_{i1} & a_{2i} b_{i2} & ... & a_{2i} b_{in} \\\
  : & : & : & : \\\
  a_{ni} b_{i1} & ... & ... & a_{ni} b_{in}
\end{bmatrix}
$$

Entonces, tenemos que

$$
\sum_{i=1}^{n} a_i b_i^t =
$$

$$
\begin{bmatrix}
  a_{11} b_{11} & a_{11} b_{12} & ... & a_{11} b_{1n} \\\
  a_{21} b_{11} & a_{21} b_{12} & ... & a_{21} b_{1n} \\\
  : & : & : & : \\\
  a_{n1} b_{11} & ... & ... & a_{n1} b_{1n}
\end{bmatrix}
$$

$$+ ... +$$

$$
\begin{bmatrix}
  a_{1i} b_{i1} & a_{1i} b_{i2} & ... & a_{1i} b_{in} \\\
  a_{2i} b_{i1} & a_{2i} b_{i2} & ... & a_{2i} b_{in} \\\
  : & : & : & : \\\
  a_{ni} b_{i1} & ... & ... & a_{ni} b_{in}
\end{bmatrix}
$$

$$ + ... + $$

$$
\begin{bmatrix}
  a_{1n} b_{n1} & a_{1n} b_{n2} & ... & a_{1n} b_{nn} \\\
  a_{2n} b_{n1} & a_{2n} b_{n2} & ... & a_{2n} b_{nn} \\\
  : & : & : & : \\\
  a_{nn} b_{n1} & ... & ... & a_{nn} b_{nn}
\end{bmatrix}
$$

Por ende, si nos enfocamos en cada posición de manera individual,

$$
AB_{ij} = a_{i1} b_{1j} + ... + a_{ii} b_{ij} + ... + a_{in} b_{nj}
$$

Que es exactamente lo mismo que el resultado tradicional de $AB_{ij}$.

### Guía práctica 1 - Ejercicio 4

#### **4) a.**

$$
n = 2,
A = \begin{bmatrix}
  1 & 0 \\\
  1 & 0
\end{bmatrix},
B = \begin{bmatrix}
  1 & 0 \\\
  0 & 0
\end{bmatrix}
$$

$$
AB = \begin{bmatrix}
  1 & 0 \\\
  1 & 0
\end{bmatrix}
$$

$$
BA = \begin{bmatrix}
  1 & 0 \\\
  0 & 0
\end{bmatrix}
$$

#### **4) b.**

$$
n = 3,
A = \begin{bmatrix}
  8 & 0 & 0 \\\
  0 & 9 & 0 \\\
  0 & 0 & 5
\end{bmatrix},
B = \begin{bmatrix}
  1 & 0 & 0 \\\
  0 & 0 & 0 \\\
  0 & 0 & 0
\end{bmatrix}
$$

$$
tr(A)tr(b) = 22*1 = 22
$$

$$
AB = \begin{bmatrix}
  8 & 0 & 0 \\\
  0 & 0 & 0 \\\
  0 & 0 & 0
\end{bmatrix}
$$

$$
tr(AB) = 8 \neq 22 = tr(A)*tr(B)
$$

### Guía práctica 1 - Ejercicio 5

Falso.

$$
A = \begin{bmatrix}
  1 & 0 \\\
  0 & 0
\end{bmatrix},
B = \begin{bmatrix}
  0 & 0 \\\
  0 & 1
\end{bmatrix}
$$

$$
AB = 0
$$

### Práctica 1 - Ejercicio 20

#### **20) a.**

$\forall x \in Nu(B) \Rightarrow Bx = 0$  
Luego, $ABx = A(Bx) = A*0 = 0$. Por lo tanto, $x \in Nu(AB)$.

#### **20) b.**

$\forall x \in Im(AB) \Rightarrow \exists v / ABv = x$.  
Luego, $\forall x \Rightarrow \exists w = Bv / A(Bv) = x = Aw$.  
Entonces, $x \in Im(A)$.

#### **20) c.**

Si $AB = 0$, entonces $\forall x \Rightarrow ABx = 0x = 0$.  
Sin embargo, el producto es conmutativo, por lo tanto $\forall x ~ ABx = A(Bx) = 0$.  
Pero $Im(B) = \{v / Bx = v\}$.  
Luego, $\forall v \in Im(B) \Rightarrow Av = 0$.  
Por lo tanto, $Im(B) \subseteq Nu(A)$

[^1]: _Extensión de VSCode sugerida para editar y previsualizar: [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-n-one). Con Ctrl+K V abre preview._
[^2]: _Para visualizar las notas al pie en VSCode: [Markdown Footnotes](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-footnotes)_
