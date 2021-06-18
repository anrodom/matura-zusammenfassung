# Erstes Rechnen mit Matrizen

## Allgemein

### Schreibweise

Matrizen sind im Grunde Tabellen für Abbildungen:

$$\begin{pmatrix}a_{11}&a_{12}&a_{13}\\a_{21}&a_{22}&a_{23}\end{pmatrix}=\textrm{2x3-Matrix}=\textrm{Zeilen x Spalten}$$

### Quadratische Matrix

Matrizen mit gleicher Anzahl an Zeilen und Spalten.

### Einheitsmatrix

Für eine Einheitsmatrix $E$ gilt $M\cdot E=M$:

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\cdot\begin{pmatrix}1&0\\0&1\end{pmatrix}=\begin{pmatrix}a&b\\c&d\end{pmatrix}$$

### Inverse Matrix

Es gilt:

$$\begin{align}
	A&=\begin{pmatrix}a&b\\c&d\end{pmatrix}\\
	A^{-1}&=\frac{1}{\Delta}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}\\
	A\cdot A^{-1}&=A^{-1}\cdot A
\end{align}$$

### Diagonal Matrix

$$\begin{pmatrix}a&0&0\\0&b&0\\0&0&c\end{pmatrix}$$

### Symmetrische Matrix

$$\begin{pmatrix}a&b&c\\b&d&e\\c&e&f\end{pmatrix}$$

### Permutationsmatrix

$$\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}$$

### Transponible Matrix

Zeilen und Spalten werden vertauscht:

$$\begin{align}
	M&=\begin{pmatrix}a&b&c\\d&e&f\\g&h&i\end{pmatrix}\\
	M^{T}&=\begin{pmatrix}a&d&g\\b&e&h\\c&f&i\end{pmatrix}
\end{align}$$

## Multiplikation/Division

Für die Multiplikation zweier Matrizen gilt:

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\cdot\begin{pmatrix}e&f\\g&h\end{pmatrix}=\begin{pmatrix}ae+bg&af+bh\\ce+dg&cf+dh\end{pmatrix}$$

Die Multiplikation ist nicht kommutativ ($AB\not=BA$)

Die Division ist nicht eindeutig, deshalb muss mit der inversen Matrix multipliziert werden.

## Basistransformation

### Allgemein

Will man z. B. an einer Gerade spiegeln (kann man auch mit herkömmlichen linearen Abbildung), können Basistransformationen den Prozess erleichtern. Man stellt zuerst eine Transformationsmatrix $T$ auf, welche die Basen $\vec{e_1}$, $\vec{e_2}$ so verändert $\vec{f_1}$, $\vec{f_2}$ (sie müssen nur linear unabhängig sein, Länge und Winkel sind egal), dass das Problem erleichtert wird (Bei einer Spiegelung also so, dass man anschliessend an der x-Achse spiegelt). Dann führt man die Spiegelung $B$ durch und transformiert wieder zurück mit $T^{-1}$. Für die Abbildung $A$ gilt demnach:

$$A=T\cdot B\cdot T^{-1}$$

Wobei für $T$ gilt:

$$T=\begin{pmatrix}\vec{f_1}&\vec{f_2}\end{pmatrix}$$

### Beispiel

Spiegelung an einer Geraden durch den Nullpunkt und Steigung $m$.

Eine gute Transformationsmatrix wäre:

$$T=\begin{pmatrix}1&m\\m&-1\end{pmatrix}$$

Spiegelungen an der x-Achse haben $B$:

$$B=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$$

Für die Abbildung $A$ gilt also:

$$\begin{align}
	A&=T\cdot B\cdot T^{-1}\\
	&=\begin{pmatrix}1&m\\m&-1\end{pmatrix}\cdot\begin{pmatrix}1&0\\0&-1\end{pmatrix}\cdot\frac{1}{-1-m^2}\begin{pmatrix}-1&-m\\-m&1\end{pmatrix}
\end{align}$$

