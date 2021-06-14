# Affinitäten

## Allgemein

### Definition

Punktabbildungen $\alpha$ der folgenden Form nennt man Affinitäten:

$$\begin{align}
	x'&=a\cdot x + b\cdot y+e\\
	y'&=c\cdot x + d\cdot y+f\\
\end{align}$$

Es handelt sich also um die Verkettung $\beta\circ\gamma$ einer linearen Vektorabbildung $\gamma$ und einer Verschiebung $\beta$:

$$\begin{align}
	\gamma:&\;&&x'=a\cdot x + b\cdot y\\
	&\;&&y'=c\cdot x + d\cdot y\\
	&\;\\
	\beta:&\;&&x'=x + e\\
	&\;&&y'=y+f
\end{align}$$

auch hier muss $\Delta\not=0$ gelten.

### Determinanten

Die Folgen der Determinante sind die gleichen wie bei linearen Abbildungen, weil sie nur für die Vektorabbildung verwendet werden. Für Verkettungen $\alpha\circ\beta$ gilt auch:

$$\Delta_{\alpha}\cdot \Delta_{\beta}=\Delta_{\alpha\circ\beta}$$

Für die Umkehrabbildung:

$$\Delta_{\alpha^{-1}}=\frac{1}{\Delta_{\alpha}}$$

### Perspektivität

Abbildungen $\alpha$ mit einer Fixpunktgeraden $g$ und einer Affinitätsrichtung $\vec{PP'}$ nennt man perspektiv affin. Zur Bestimmung der Fixpunktgeraden, wird von den Gleichungen von Fixpunkten ausgegangen:

$$\begin{align}
	x&=a\cdot x + b\cdot y+e\\
	y&=c\cdot x + d\cdot y+f\\
\end{align}$$

Wenn also folgendes Gleichungssystem 

$$\begin{align}
	x&=(a-1)\cdot x + b\cdot y+e\\
	y&=c\cdot x + (d-1)\cdot y+f\\
\end{align}$$

eine allgemeingültige Lösung hat, z. B. $0=0$, dann können beide Gleichungen zur Gleichung der Fixpunktgeraden umgeformt werden.

Für die Affinitätsrichtung $\vec{PP'}$ gilt $\vec{OP'}-\vec{OP}=\vec{PP'}$:

$$\begin{pmatrix}a\cdot x + b\cdot y+e\\c\cdot x + d\cdot y+f\end{pmatrix}-\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}(a-1)\cdot x + b\cdot y+e\\c\cdot x + (d-1)\cdot y+f\end{pmatrix}$$

### Eigenvektoren und Eigenwerte

#### Allgemein

Vektoren $\vec{v}$ mit Vektorabbildung $\vec{\alpha}$ nennt man Eigenvektor mit Eigenwert $\lambda$, wenn folgendes gilt:

$$\vec{\alpha}(\vec{v})=\lambda\cdot\vec{v}$$

Eigenvektoren werden zu kollinearen Vektoren zum Eigenvektor abgebildet.

Umgekehrt gilt auch für alle zum Eigenvektor $\vec{v}$ kollinearen Vektoren $\vec{w}$:

$$\vec{\alpha}(\vec{w})=\vec{\alpha}(c\cdot\vec{v})=c\cdot\vec{\alpha}(\vec{v})=c\cdot\lambda\vec{v}=\lambda \vec{w}$$

Alle zum Eigenvektor kollinearen Vektoren sind Eigenvektoren zum Eigenwert $\lambda$.

#### Bestimmung

Folgendes Gleichungssystem muss gelten:

$$\begin{align}
	\lambda\cdot x&=a\cdot x + b\cdot y\\
	\lambda\cdot y&=c\cdot x + d\cdot y\\
\end{align}$$

Wegen des vorher gezeigten Zusammenhanges von Kollinearität und der Eigenvektoren, muss dieses Gleichungssystem $\infty$ viele Lösungen (kollineare Vektoren) haben. Die Determinante $\Delta$ muss also 0 sein:

$$(a-\lambda)(d-\lambda)-b\cdot c=0$$

Daraus entsteht auch das charakteristisches Polynom:

$$\lambda^2-(a+d)\lambda + ad - bc= \lambda^2-(a+d)\lambda + \Delta$$

Alle Eigenvektoren zum Eigenwert $\lambda$ (es gibt 2 weil quadratisch) sind Lösungen der vorherigen 2 Gleichungen, wobei die erhaltenen $\lambda$ eingesetzt werden.

### Fixgeraden

Fixgeraden sind Geraden, deren Abbildung auf sich selbst fällt, sprich dieselbe Gerade. Es muss also nicht zwingend jeder Punkt auf sich selbst fallen (Fixpunktgerade). 

Der Richtungsvektor $\vec{AA'}$ der Geraden ist kollinear zum Eigenvektor $\vec{v}$:

$$\begin{pmatrix}(a-1)\cdot x + b\cdot y+e\\c\cdot x + (d-1)\cdot y+f\end{pmatrix}=t\cdot \vec{v}$$

Aus diesen beiden Gleichungen kann man $t$ eliminieren und erhält die Gleichung der Fixgeraden, falls eine vorhanden ist.

## Spezielle Abbildungen

### Allgemeine zentrische Streckung

Eine Abbildung soll um den Faktor $\lambda$ mit Zentrum $(x_z|y_z)$ strecken:

$$\begin{align}
	x'&=\lambda(x-x_z) + x_z\\
	y'&=\lambda(y-y_z) + y_z
\end{align}$$

