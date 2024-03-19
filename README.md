# **Métodos Numéricos** - 1er Cuatrimestre 2024 [^1][^2] <!-- omit in toc -->

# Apuntes de Juan Cruz Barcos <!-- omit in toc -->

[Tabla de contenidos](#métodos-numéricos---1er-cuatrimestre-2024-1)- [Apuntes de clases](#apuntes-de-clases)
- [Apuntes de clases](#apuntes-de-clases)
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
    - [**Tarea**](#tarea)

# Apuntes de clases

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
\left(\begin{array}{cc}
a_{11} & a_{12} & ... & a_{1n} \\
a_{21} & a_{22} & ... & a_{2n} \\
... & ... & ... & ... \\
a_{i1} & a_{i2} & ... & a_{in} \\
... & ... & ... & ... \\
a_{m1} & a_{m2} & ... & a_{mn}
\end{array}Right)
$$

#### **Suma**
Intruición: suma lugar a lugar.  
Definida si $m = p, n = q$  
$C = A + B$ con $c_{ij} = a_{ij} + b_{ij}$ para $i = 1,...,m$, $j = 1,...,n.$  
$C \in R^{mxn}$ (conmutativa, asociativa)

#### **Producto por escalar**
Intuición: multiplica cada elemento de la matriz por el escalar.  
$C = \alpha A$ con $c_{ij} = \alpha a_{ij}$ para $i = 1,...,m$,  $j = 1,...,n$, $C \in R^{mxn}$

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
$a_{11} x_1 + a_{12} x_2 + ... + a_{1n} x_n = b_1$  
$a_{21} x_1 + a_{22} x_2 + ... + a_{2n} x_n = b_2$  
...  
$a_{n1} x_1 + a_{n2} x_2 + ... + a_{nn} x_n = b_n$

$A \in R^{mxn}$
$$
A = 
\left(\begin{array}{cc}
a_{11} & a_{12} & ... & a_{1n} \\
a_{21} & a_{22} & ... & a_{2n} \\
... & ... & ... & ... \\
a_{i1} & a_{i2} & ... & a_{in} \\
... & ... & ... & ... \\
a_{m1} & a_{m2} & ... & a_{mn}
\end{array}Right)
$$

$$
x = 
\left(\begin{array}{cc}
x_{11} & x_{12} & ... & x_{1n}
\end{array}Right)
$$

$$
b = 
\left(\begin{array}{cc}
b_{11} & b_{12} & ... & b_{1n}
\end{array}Right) \\

Ax = b
$$


### **Tarea**
- Demostrar que el producto de dos matrices inferiores es una matriz inferior (ídem superior).  
- Demostrar que la inversa (si existe) de una matriz triangular inferior es matriz triangular inferior. (ídem superior).  

[^1]: _Extensión de VSCode sugerida para editar y previsualizar: [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-n-one). Con Ctrl+K V abre preview._
[^2]: _Para visualizar las notas al pie en VSCode: [Markdown Footnotes](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-footnotes)_
