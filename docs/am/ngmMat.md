# Nichtgeometrische Anwendungen von Matrizen

## Allgemein

Eigentlich können sowohl Matrizen für Mengen / Preise und Populationen als auch stochastische Matrizen (auch Markov-Ketten) nach dem gleichen Prinzip aufgestellt werden, wenn schon ein Übergangsgraph vorhanden ist. Es seien $A_1$, $B_1$, $C_1$ und $D_1$ die gesuchten Zahlen (Entwicklung nach einer Zeiteinheit, Endprodukt/Zwischenprodukt oder die nächsten Folgenglieder) und $A_0$, $B_0$, $C_0$ und $D_0$ die schon vorhandenen Zahlen (Anfangsbestand, Rohstoffe oder die ersten Folgenglieder). Übergänge werden mit z. B. $B_0\rightarrow A_1$ indiziert.

$$\begin{align}
	\begin{pmatrix}A_1\\B_1\\C_1\\D_1\end{pmatrix}&=\begin{pmatrix}A_0\rightarrow A_1 & B_0\rightarrow A_1 & C_0\rightarrow A_1 & D_0\rightarrow A_1\\  A_0\rightarrow B_1 & B_0\rightarrow B_1 & C_0\rightarrow B_1 & D_0\rightarrow B_1\\  A_0\rightarrow C_1 & B_0\rightarrow C_1 & C_0\rightarrow C_1 & D_0\rightarrow C_1\\  A_0\rightarrow D_1 & B_0\rightarrow D_1 & C_0\rightarrow D_1 & D_0\rightarrow D_1\end{pmatrix}\cdot\begin{pmatrix}A_0\\B_0\\C_0\\D_0\end{pmatrix}\\
	&\Downarrow\\
	M&=\begin{pmatrix}A_0\rightarrow A_1 & B_0\rightarrow A_1 & C_0\rightarrow A_1 & D_0\rightarrow A_1\\  A_0\rightarrow B_1 & B_0\rightarrow B_1 & C_0\rightarrow B_1 & D_0\rightarrow B_1\\  A_0\rightarrow C_1 & B_0\rightarrow C_1 & C_0\rightarrow C_1 & D_0\rightarrow C_1\\  A_0\rightarrow D_1 & B_0\rightarrow D_1 & C_0\rightarrow D_1 & D_0\rightarrow D_1\end{pmatrix}
\end{align}$$

## Zyklische Matrizen

Matrizen $A$ sind zyklisch, wenn es ein $n\in\mathbb{N}$ hat mit $A^n=A$

Damit eine Population nach $n$ Jahren $a$ mal Grösser wird, gilt:

$$M^n=\begin{pmatrix}a&0&0\\0&a&0\\0&0&a\end{pmatrix}$$ 

Wir haben uns aber nur Matrizen folgender Form (Populationsmatrizen) angeschaut:

$$M=\begin{pmatrix}0&0&0&v\\a&0&0&0\\0&b&0&0\\0&0&c&0\end{pmatrix}$$

$n\times n$-Matrizen dieser Form haben einen Zyklus von $n$ Jahren.

> Achtung, steht nicht in der Theorie, bei Fragen an Mikail (er ist ein absoluter Experte in Matrixen, vor allem wenn es um Populationen und Diagonal-Matrixen geht, kann ihm niemand das Wasser reichen) wenden.
> Soll nun ein Parameter $v$ der Populationsmatrix $M$ so verändert werden, dass nach $m$ Jahren die Population um $b$ grösser wird, wobei die Matrix eine Periode von $t$ hat (nach $t$ Jahren eine Diagonal-Matrix entsteht) bzw. eine Grösse von $t\times t$, gilt ($v_1$ ist der Wert von $v$, wenn die Population nach einer Periode gleich gross bleiben soll, eine Diagonal-Matrix mit 1):
>
$$\begin{align}
	v&=v_1\cdot\sqrt[n/t]{a}\\
	v_1&=\frac{v}{\sqrt[n/t]{a}}\\
	v_{\textrm{neu}}&=v_1\cdot\sqrt[m/t]{b}\\
	v_{\textrm{neu}}&=\frac{v}{\sqrt[n/t]a}\cdot\sqrt[m/t]{b}
\end{align}$$
> 
> Alternativ einfach $M^m=\begin{pmatrix}b&0&0\\0&b&0\\0&0&b\end{pmatrix}$ mit $v$ als Unbekannte in Mathematica eintippen.

## Stochastische Matrizen

Stochastische Matrizen sind Matrizen, bei denen jede Spalte die Summe 1 aufweist.

## Grenzvektor

### Bestimmung

Für Grenzvektoren $\vec{v}=\begin{pmatrix}A\\B\\C\\D\end{pmatrix}$ einer Matrix $M$ mit $A+B+C+D=\textrm{Bestand}$ gilt:

$$\vec{v}=M\cdot\vec{v}$$

### Existenz

Es sei eine Matrix $M=\begin{pmatrix}0.2&0.4\\0.8&0.6\end{pmatrix}$ und ein Startvektor $\begin{pmatrix}a_0\\b_0\end{pmatrix}$ mit $a_0+b_0=600$ gegeben. Die Matrix $M$ besitzt den Eigenvektor $\begin{pmatrix}1\\2\end{pmatrix}$ mit Eigenwert $1$ und den Eigenvektor $\begin{pmatrix}-1\\1\end{pmatrix}$ mit Eigenwert $-0.2$. Der Startvektor kann also mit Hilfe des Fixpunktes und der Eigenvektoren wie folgt aufgeschrieben:

$$\begin{pmatrix}a_0\\b_0\end{pmatrix}=\begin{pmatrix}200\\400\end{pmatrix}+C\cdot\begin{pmatrix}-1\\1\end{pmatrix}$$

Um die Existenz des Grenzwertes zu zeigen geht man wie folgt vor:

$$\begin{align}
	\lim_{n\to\infty}M^n\cdot\begin{pmatrix}a_0\\b_0\end{pmatrix}&=\lim_{n\to\infty}M^n\cdot\left(\begin{pmatrix}200\\400\end{pmatrix}+C\cdot\begin{pmatrix}-1\\1\end{pmatrix}\right)\\
	&=\lim_{n\to\infty}M^n\cdot\begin{pmatrix}200\\400\end{pmatrix}+M^n\cdot C\cdot\begin{pmatrix}-1\\1\end{pmatrix}\\
	&=\lim_{n\to\infty}\begin{pmatrix}200\\400\end{pmatrix}+C\cdot(-0.2)^n\cdot\begin{pmatrix}-1\\1\end{pmatrix}\\
	&=\begin{pmatrix}200\\400\end{pmatrix}
\end{align}$$

## Explizite Definition

### Fibonacci-Folge

Die Fibonacci-Folge hat die folgende rekursive Definition, welche sich mit vollständiger Induktion beweisen lässt:

$$\begin{pmatrix}a_{2n}\\a_{2n+1}\end{pmatrix}=\begin{pmatrix}1&1\\1&2\end{pmatrix}^n\cdot\begin{pmatrix}1\\1\end{pmatrix}$$



