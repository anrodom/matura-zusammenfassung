# Endliche Folgen und Reihen

## Begriffe

### Folgen

Wenn Zahlen lediglich aufgelistet werden, dann nennt man dies Zahlenfolge:

$$a_1,\,a_2,\,a_3,\,...a_n,\,...$$


### Reihe

Reihen sind Aufsummierungen der einzelnen Glieder einer Folge:

$$s_n = a_1+a_2+a_3+...+a_n$$

### Rekursive Definition

Bei einer Rekursiven Definition wird das nächste Glied $a_{n+1}$ mit Hilfe eines oder mehreren der vorherigen Glieder $a_{n}$ bestimmt. Ein Startwert muss bekannt sein.

### Explizite Definition

Bei einer Expliziten Definition wird ein Glied $a_n$ mit Hilfe seines Index $n$ bestimmt. Die vorherigen Glieder (bis auf den Startwert) müssen also nicht bekannt sein.

## Arithmetische Folgen und Reihen

### Arithmetische Folge

Eine Zahlenfolge ist arithemtisch, wenn die Differenz $d$ zweier aufeinanderfolgender Glieder konstant ist. Sie hat folgende Definitionen:

#### Rekursiv

$$a_{n+1}=a_n+d$$

#### Explizit

$$a_{n}=a_1 + (n-1)\cdot d$$

### Arithmetische Reihe

Herleitung der Formel für $s_n$:

$$\begin{align}
  s_n&=a_1+a_2\;\;\;\:+a_3\;\;\;\,+...+a_{n-1}+a_n\\
  s_n&=a_n+a_{n-1}+a_{n-2}+...+a_2\;\;\;\:+a_1\\
  \underline{\phantom{+++}}&\underline{\phantom{+++++++++++++++++}}\\
  2s_n&=n(a_1 +a_n)\\
  s_n&=\frac{n}{2}(a_1+a_n)
\end{align}$$

## Geometrische Folgen und Reihen

### Geometrische Folge

Eine Zahlenfolge ist geometrisch, wenn der Quotient $q$ zweier aufeinanderfolgender Glieder konstant ist. Sie hat folgende Definitionen:

#### Rekursiv

$$a_{n+1}=a_n\cdot q$$

#### Explizit

$$a_{n}=a_1\cdot q^{n-1}$$

### Geometrische Reihe

Herleitung der Formel für $s_n$:

$$\begin{align}
  s_n&=a_1\;\;\;\;\;\;+\cancel{a_2}\;\;\;\;\,+...+\cancel{a_1\cdot q^{n-2}}+\cancel{a_1\cdot q^{n-1}}\\
  q\cdot s_n&=\cancel{a_1\cdot q}+\cancel{a_2\cdot q}+...+\cancel{a_1\cdot q^{n-1}}+a_1\cdot q^{n}\\
  \underline{\phantom{++++++}}&\underline{\phantom{+++++++++++++++++++++}}\\
  (1-q)s_n&=a_1-a_1\cdot q^n\\
  s_n&=a_1\frac{1-q^n}{1-q}
\end{align}$$