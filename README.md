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
- [Clases prácticas](#clases-prácticas)
  - [Clase 1: 20 de marzo](#clase-1-20-de-marzo)
    - [**Guía práctica 1 - Ejercicio 1**](#guía-práctica-1---ejercicio-1)
      - [1) a.](#1-a)
      - [1) b.](#1-b)
      - [1) c.](#1-c)
      - [1) d.](#1-d)
    - [**Guía práctica 1 - Ejercicio 2**](#guía-práctica-1---ejercicio-2)
      - [2) a.](#2-a)
      - [2) b.](#2-b)
      - [3) c.](#3-c)
      - [3) ¿Qué otras particiones son posibles?](#3-qué-otras-particiones-son-posibles)
    - [**Vectores canónicos**](#vectores-canónicos)
    - [**Multiplicación de matrices por vectores canónicos**](#multiplicación-de-matrices-por-vectores-canónicos)

# Clases teóricas

## Clase 1: 18 de marzo

### 1. Vectores

#### **Definición**

$v \in R^n$ n-upla de coeficientes reales
$v = (v_{1},v_{2},...,v_{n})$

#### **Suma**

Intuición: suma lugar a lugar.  
$w = v + u$ con $w_i = v_i + u_i$ para $i = 1,...,n$ (conmutativa, asociativa).

#### **Multiplicación por escalar**

Intuición: Multiplica todos los números del vector por el escalar.  
Sea $a \in R$, $w = \alpha v$ con $w_{i} = \alpha v_{i}$ para $i = 1,...,n$

#### **Producto interno**

Intuición: Multiplicación lugar a lugar y \suma de los resultados.  
$<u, v> = \sum_{i=1}^{n} u_i v_i$

#### **Combinación lineal**

$w = \sum_{k=1}^{K} a_k v^k$

#### **Vectores linealmente independientes**

$\sum_{k=1}^{K} a_k v^k = 0 \to a_k = 0 \forall k = 1,...,K$

#### **Vectores linealmente dependientes**

Existen $a_k$ con $k = 1,...,K$ no todos nulos tal que $\sum_{k=1}^{K} a_k v^k = 0$

#### **Subespacio generado**

$S = {x \in R^n \text{ tal que } x = \sum_{k=1}^{K} \alpha_k v^k}$

#### **Dimensión de S**

Cantidad máxima de vectores linealmente independientes en S.

#### **Base de S**

Conjunto de vectores linealmente independientes que generan a S.

### 2. Matrices

#### **Definición**

$A \in R^{mxn}$

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
$C \in R^{mxn}$ (conmutativa, asociativa)

#### **Producto por escalar**

Intuición: multiplica cada elemento de la matriz por el escalar.  
$C = \alpha A$ con $c_{ij} = \alpha a_{ij}$ para $i = 1,...,m$, $j = 1,...,n$, $C \in R^{mxn}$

#### **Multiplicación**

Definida si $n = p$. $C = AB$ tal que
$A \in R^{mxn}$, $B \in R^{pxq}$
$c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}, para i = 1,...,m$, $j = 1,...,q$, $C \in R^{mxq}$
NO es conmutativa.

#### **Matriz identidad**

Intuición: Diagonal de unos y el resto ceros.  
$I \in R^{nxn}$ si
$I_{ii} = 1$, $I_{ij} = 0$ si $i \neq j$

#### **Matriz diagonal**

Intuición: Diagonal de números y el resto cero.  
$D \in R^{nxn}$ si
$D_{ii} = k_i, D_{ij} = 0$ si $i \neq j$

#### **Matriz triangular superior**

Intuición: De la diagonal para abajo es todo ceros.  
$U \in R^{nxn}$ con $u_{ij} = 0$ si $i > j$  
Producto de triangulares superiores es triangular superior.

#### **Matriz triangular inferior**

Intuición: De la diagonal para arriba es todo ceros.  
$L \in R^{nxn}$ con $l_{ij} = 0$ si $i < j$  
Producto de triangulares inferiores es triangular inferior.

#### **Rango de una matriz**

Cantidad máxima de columnas o filas linealmente independiente.

#### **Matriz inversa**

Definida si $m = n$. $A^{-1} \in R^{nxn}$.
$AA^{-1} = A^{-1}A = I$  
$A$ inversible $\iff rang(A) = n \iff det(A) \neq 0$  
La inversa (si existe) de una matriz diagonal es matriz diagonal.  
La inversa (si existe) de una matriz triangular inferior es matriz triangular inferior.  
La inversa (si existe) de una matriz triangular superior es matriz triangular superior.

#### **Matriz estrictamente diagonal dominante**

Intuición: Cada elemento de la diagonal es mayor a la suma del resto de los elementos de su fila (todo en valor absoluto).  
$A \in R^{nxn}$  
$|a_{ii}| > \sum_{j\neq i} |a_{ij}|$ $\forall 1,...,n$

#### **Matriz transpuesta**

Intuición: Las filas ahora son las columnas y las columnas las filas.  
$A^t \in R^{nxm}$  
$a^t_{ij} = a_{ji}$ para todo $i = 1,...,m$, $j = 1,...,n$  
$(A^t)^t = A$  
$(A + B)^t = A^t + B^t$  
$(AB)^t = B^t A^t$  
$(A^t)^{-1} = (A^{-1})^t$

#### **Matriz de permutación**

$P \in R^{nxn}$. Son una permutación de las filas (o columnas) de la matriz identidad.

#### **Multiplicar por matrices de permutación**

Intuición: Si multiplico con la matriz de permutación a izquierda, permuta las filas.  
Si multiplico con la matriz de permutación a derecha, permuta las columnas.

#### **Matriz elemental (tipo 1)**

$E \in R^{nxn}$. Matriz identidad con una fila multiplicada por un escalar no nulo.

#### **Multiplicar por matriz elemental (tipo 1)**

Intuición: Si multiplico con la matriz elemental a izquierda, multiplica la fila por el escalar.  
Si multiplico con la matriz elemental a derecha, multiplica la columna por el escalar.

#### **Matriz elemental (tipo 2)**

$E \in R^{nxn}$. Matriz identidad con un elemento no nulo fuera de la diagonal.

#### **Multiplicar por matriz elemental (tipo 2)**

Intuición: Si multiplico con la matriz elemental a izquierda con un escalar en $I_{ij}$, a la fila i le suma la fila j multiplicada por el escalar.  
Si multiplico con la matriz elemental a derecha con un escalar en $I_{ij}$, a la columna j le suma la columna i multiplicada por el escalar.

#### **Transformación linal**

Multiplicar una matriz $A \in R^{mxn}$ por un vector $x \in R^{nx1}$ y obtener $y \in R^{mx1}$

#### **Espacio imagen**

$Im(A) = {y \in R^m \text{ tal que existe } x \in R^n \text{ con } Ax = y}$

#### **Espacio nulo**

$N(A) = {x \in R^n \text{ tal que } Ax = 0}$  
$N(A) \neq {0} \iff \text{ las columnas de A son linealmente dependientes.}$

### 3. Sistemas de ecuaciones lineales

#### **Definición**

$a_{11} x_1 + a_{12} x_2 + ... + a_{1n} x_n = b_1$  
$a_{21} x_1 + a_{22} x_2 + ... + a_{2n} x_n = b_2$  
...  
$a_{n1} x_1 + a_{n2} x_2 + ... + a_{nn} x_n = b_n$

$A \in R^{mxn}$

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
\end{bmatrix} \\

Ax = b
$$

### Tarea

#### **Ejercicio 1**

Demostrar que el producto de dos matrices diagonales inferiores es una matriz diagonal inferior (ídem superior).

#### **Ejercicio 2**

Demostrar que la inversa (si existe) de una matriz triangular inferior es matriz triangular inferior. (ídem superior).

### Tarea resuelta

#### **Ejercicio 1**

Tomando dos matrices diagonales superiores genéricas $A$ y $B \in R^{nxn}$, veamos el resultado de $C = AB$.  
$c_{ij} = \sum_{k=1}^{n} a_{ik}*b_{kj}$  
Recordemos que, como ambas son matrices diagonales superiores, debajo de la diagonal, sus valores son 0. Por lo tanto, en $c_{ij}$, donde $i > j$, en la fila $i$ de $A$, tendremos exactamente $i - 1$ posiciones con valor 0, pues son aquellas posiciones donde $i > j$ y que, por definición, son 0. Además, en la columna $j$ de $B$, tendremos exactamente $n - j$ posiciones con valor 0, pues son las posiciones donde $i > j$ y, por definición, distintas de 0.  
Luego, para $\sum_{k=1}^{i-1} a_{ik}*b_{kj}$, $a_{ik}$ siempre será 0, por lo que la sumatoria será 0.  
Para $\sum_{k=i}^{n} a_{ik}*b_{kj}$, $b_{kj}$ siempre será 0, pues $k > j$, por comenzar siendo $i$, que es mayor a $j$, por lo que la sumatoria será 0.  
Por lo tanto, para todas las posiciones debajo de la diagonal, el valor resultante será 0.  
Luego, $C$ es diagonal superior. Ídem para diagonal inferior, invirtiendo el sentido.

#### **Ejercicio 2**

Sea $A \in R^{nxn}$ tiangular superior y $BA = I_n$.  
Teniendo en cuenta que $A$ es triangular superior, $b_{11} a_{11} = 1$ y $b_{j1} a_{11} = 0$. Por lo tanto, la primera columna de B es $\begin{bmatrix}a_{11}^{-1} \\ 0 \\ : \\ 0\end{bmatrix}$  
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
$(BA)_{jj}$ debe ser 1, luego,  
$b_{j1}a_{1j}+...+b_{jj}a_{jj}+...b_{jn}a_{nj} = 1$

Por inducción,  
$b_{j1} = ... = b_{jj-1} = 0$

Y por tiangularidad de $A$  
$a_{j+1j} = ... = a_{nj} = 0, k > j$

Se tiene  
$b_{jj}a_{jj} = 1$ y $b_{jj}=a_{jj}^{-1}$

$b_{kj}=0, k=j+1,...,n$:  
$(BA)_{kj} = 0$, luego  
$b_{k1}a_{1j}+...+{b_kj}a_{jj}+...+n_{jn}a_{nj} = 1$

Por inducción,  
$b_{k1} = ... = b_{kj-1} = 0$

Y por triangularidad de A  
$a_{j+1j} = ... = a_{nj} = 0, k > j$

Luego, $b_{kj}a_{jj} = 0$, puesto que $a_{jj}$ es no nulo, $b_{kj}$ debe serlo.

# Clases prácticas

## Clase 1: 20 de marzo

### **Guía práctica 1 - Ejercicio 1**

#### 1) a.

Falso. $A \in R^{nxm}$ y $z \in R^{nx1}$, por lo que no se pueden multiplicar.

#### 1) b.

Falso. El resultado de multiplicar $x \in R^{nx1}$ y $z^t \in R^{1xn}$ debe pertenecer a $R^{nxn}$, no a $R^{1x1}$.

#### 1) c.

Verdadero.

#### 1) d.

Verdadero.

### **Guía práctica 1 - Ejercicio 2**

#### 2) a.

$C_{11} = A_{11}B_{11} + A_{12}B_{21} = 1 + 9 = 10$ y $C_{11} \in R^{1x1}$

$C_{12} = A_{11}B_{12} + A_{12}B_{22} = [1, 1] + [0, 3] = [1,4]$ y $C_{12} \in R^{1x2}$

$C_{21} = A_{21}B_{11} + A_{22}B_{21} = [0,1]^t + [7,2]^t = [7,3]^t$ y $C_{21} \in R^{1x2}$

$C_{22} = A_{21}B_{12} + A_{22}B_{22} = \begin{bmatrix} 0 & 0 \\ 1 & 1 \\ \end{bmatrix} +  \begin{bmatrix} 0 & 5 \\ 0 & 2\end{bmatrix} = \begin{bmatrix} 0 & 5 \\ 1 & 2 \end{bmatrix}$ y $C_{22} \in R^{2x2}$

#### 2) b.

$C_{11} = A_{11}B_{11} + A_{12}B_{21}$ donde $A_{11} \in R^{1x2}$ y $B_{11} \in R^{1x1}$. Por lo tanto, no es posible.

#### 3) c.

$C_{11} = A_{11}B_{11} + A_{12}B_{21}$ donde $A_{12} \in R^{2x2}$ y $B_{21} \in R^{1x2}$. Por lo tanto, no es posible.

#### 3) ¿Qué otras particiones son posibles?

Son posibles todas aquellas particiones donde en la diagonal queden particiones cuadradas y de los mismos tamaños, ya que deben multiplicarse entre ellas por ambos lados.  
En este caso en específico, sólo hay dos particiones posibles distintas de las matrices originales, que son a) y:

$A_{11} = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}$, $A_{12} = \begin{bmatrix} a_{13} \\ a_{23} \end{bmatrix}$, $A_{21} = \begin{bmatrix} a_{31} & a_{32} \end{bmatrix}$, $A_{22} = \begin{bmatrix} a_{33} \end{bmatrix}$

$B_{11} = \begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix}$, $B_{12} = \begin{bmatrix} b_{13} \\ b_{23} \end{bmatrix}$, $B_{21} = \begin{bmatrix} b_{31} & b_{32} \end{bmatrix}$, $B_{22} = \begin{bmatrix} b_{33} \end{bmatrix}$

### **Vectores canónicos**

El vector canónico $e_i \in R^{nx1}$, es aquel que posee el valor 0 en todas sus posiciones, excepto por la posición $i$, donde vale 1.

### **Multiplicación de matrices por vectores canónicos**

$Ae_i$ es igual a la columna $i$ de $A$.  
$e_i^tA$ es igual a la fila $i$ de $A$.

[^1]: _Extensión de VSCode sugerida para editar y previsualizar: [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-n-one). Con Ctrl+K V abre preview._
[^2]: _Para visualizar las notas al pie en VSCode: [Markdown Footnotes](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-footnotes)_
