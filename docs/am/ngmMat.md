# Nichtgeometrische Anwendungen von Matrizen

## Allgemein

Eigentlich können sowohl Matrizen für Mengen / Preisen und Populationen als auch stochastische Matrizen (auch Markov-Ketten) nach dem gleichen Prinzip aufgestellt werden, wenn schon ein Übergangsgraph vorhanden ist. Es seien $A_1$, $B_1$, $C_1$ und $D_1$ die gesuchten Zahlen (Entwicklung nach einer Zeiteinheit, Endprodukt/Zwischenprodukt oder die nächsten Folgenglieder) und $A_0$, $B_0$, $C_0$ und $D_0$ die schon vorhandenen Zahlen (Anfangsbestand, Rohstoffe oder die ersten Folgenglieder). Übergänge werden mit z. B. $B_0\rightarrow A_1$ indiziert.

$$\begin{align}
	\begin{pmatrix}A_1\\B_1\\C_1\\D_1\end{pmatrix}&=\begin{pmatrix}A_0\rightarrow A_1 & B_0\rightarrow A_1 & C_0\rightarrow A_1 & D_0\rightarrow A_1\\  A_0\rightarrow B_1 & B_0\rightarrow B_1 & C_0\rightarrow B_1 & D_0\rightarrow B_1\\  A_0\rightarrow C_1 & B_0\rightarrow C_1 & C_0\rightarrow C_1 & D_0\rightarrow C_1\\  A_0\rightarrow D_1 & B_0\rightarrow D_1 & C_0\rightarrow D_1 & D_0\rightarrow D_1\end{pmatrix}\cdot\begin{pmatrix}A_0\\B_0\\C_0\\D_0\end{pmatrix}\\
	&\Downarrow\\
	M&=\begin{pmatrix}A_0\rightarrow A_1 & B_0\rightarrow A_1 & C_0\rightarrow A_1 & D_0\rightarrow A_1\\  A_0\rightarrow B_1 & B_0\rightarrow B_1 & C_0\rightarrow B_1 & D_0\rightarrow B_1\\  A_0\rightarrow C_1 & B_0\rightarrow C_1 & C_0\rightarrow C_1 & D_0\rightarrow C_1\\  A_0\rightarrow D_1 & B_0\rightarrow D_1 & C_0\rightarrow D_1 & D_0\rightarrow D_1\end{pmatrix}
\end{align}$$

## Zyklische Matrizen

Matrizen $A$ sind zyklisch, wenn es ein $n\in\mathbb{N}$ hat mit $A^n=A$

## Stochastische Matrizen

Stochastische Matrizen sind Matrizen, bei denen jede Spalte die Summe 1 aufweist.

## Grenzvektor

Für Grenzvektoren $\vec{v}=\begin{pmatrix}A\\B\\C\\D\end{pmatrix}$ einer Matrix $M$ mit $A+B+C+D=\textrm{Bestand}$ gilt:

$$\vec{v}=M\cdot\vec{v}$$

Ihre Existenz lässt sich mit Hilfe von EV und EW zeigen:

$$\lim_{n\to\infty}M^n\cdot\begin{pmatrix}A_0\\B_0\\C_0\\D_0\end{pmatrix}$$

## Explizite Definition

### Fibonacci-Folge

Die Fibonacci-Folge hat die Folgende rekursive Definition, welche sich mit vollständiger Induktion beweisen lässt:

$$\begin{pmatrix}a_{2n}\\a_{2n+1}\end{pmatrix}=\begin{pmatrix}1&1\\1&2\end{pmatrix}^n\cdot\begin{pmatrix}1\\1\end{pmatrix}$$



