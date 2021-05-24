# Gewöhnliche Differentialgleichungen

## Begriffe

Bei Differenzen-Gleichungen arbeitet man mit Relativen Zunahmen:

$$\frac{\Delta y}{\Delta x}$$

Bei Differenzial-Gleichungen arbeitet man mit Momentane Zunahme:

$$\lim_{\Delta x\to 0}\frac{\Delta y}{\Delta x}=\frac{dy}{dx}$$

## Lineares Wachstum

Relative und Momentane Zunahme sind konstant.

$$\frac{\Delta y}{\Delta x}=\textrm{konst.}\;\textrm{und}\;\frac{dy}{dx}=\textrm{konst.}$$

## Exponentielles Wachstum

Die Momentane Zunahme ist proportional zum Funktionswert/vorhandenen Anzahl:

$$\frac{\frac{dy}{dx}}{y}=\frac{y'}{y}=\textrm{konst.}$$

## Begrenztes Wachstum

Die Momentane Zunahme ist proportional zum Funktionswert/vorhandenen Anzahl subtrahiert von einer Grenze $G$:

$$\frac{y'}{G-y}=k$$

## Logistisches Wachstum

$$y'=k\cdot y(G-y)$$

## Berechnung von DG's

### Allgemein

Die wichtigste Methode beim Lösen von DG's ist die sogenannte Separation der Variablen. Das bedeutet, dass man alle $y$ und $y'$ auf die eine Seite bringt und den Rest auf der anderen. Wichtig dabei ist, dass zu jedem $y$ auch ein $y'$ vorhanden ist, damit integriert werden kann.

Beim Integrieren entsteht die Integrationskonstante $C$. Es gibt also unendlich viele Funktionen als Lösung. Man braucht also eine Anfangsbedingung, um das jeweilige $C$ zu finden.

Logistisches Wachstum, also $y'=k\cdot y(G-y)$, kann zum Integrieren mit der Partialbruchzerlegung (siehe [Integrations-Methoden](gewDiff.md)) oder mit einer Substitution $z=\frac{1}{y}$ und $y'=-y^2z'$ bestimmt werden (siehe nachfolgende Beispiele)

### Beispiele

$y'=2y$:

$$\begin{align}
	y'&=2y\\
	\frac{y'}{y}&=2\\
	\ln(y)&=2x+C\\
	y&=e^{2x+C}\\
	y&=C\cdot e^{2x}
\end{align}$$

$y'x=\frac{1}{y^2}$:

$$\begin{align}
	y'x&=\frac{1}{y^2}\\
	y'y^2&=\frac{1}{x}\\
	\frac{y^3}{3}&=\ln(x)+C\\
	y&=\sqrt[3]{3\ln(x)+C}
\end{align}$$

$y'=k\cdot y(G-y)$ mit $z=\frac{1}{y}$ und $y'=-y^2z'$:

$$\begin{align}
	y'&=k\cdot y(G-y)\\
	-y^2z'&=k\cdot y(G-y)\\
	-z'&=k(\frac{G}{y}-1)\\
	z'&=-k(G\cdot z-1)\\
	\frac{z'}{z-\frac{1}{G}}&=-kG\\
	\ln\left(z-\frac{1}{G}\right)&=-kGx+C\\
	z&=C\cdot e^{-kGx}+\frac{1}{G}\\
	y&=\frac{1}{C\cdot e^{-kGx}+\frac{1}{G}}
\end{align}$$

### Energie

$$\begin{align}
	\vec{F}&=-G\frac{mM}{x^2(t)}\\
	m\cdot a&=-G\frac{mM}{x^2(t)}\\
	\ddot{x}(t)m&=-G\frac{mM}{x^2(t)}\\
	\dot{x}(t)\ddot{x}(t)m&=-G\frac{mM}{x^2(t)}\dot{x}(t)\\
	m\frac{\dot{x}^2(t)}{2}&=GmM\frac{1}{x(t)}+C\\
	C&=\frac{m}{2}v^2+\vec{F}x(t)\\
	\textrm{Energie}&=E_{\textrm{kin}}+E_{\textrm{pot}}
\end{align}$$

## Bemerkungen

### Eindeutigkeit

Gibt es andere Funktion $g(x)$ ausser $f(x)=C\cdot e^{kx}$ für die DG $y'=y\cdot k$ ?

Für die Ableitung des Quotienten gilt:

$$\begin{align}
	\left(\frac{f(x}{g(x}\right)'&=\frac{f'(x)g(x)-f(x)g'(x)}{g^2(x)}\\
	&=\frac{kf(x)g(x)-kf(x)g(x)}{g^2(x)}\\
	&=0
\end{align}$$

Für den Quotienten gilt:

$$\frac{f(x)}{g(x)}=C$$

Mit gleicher Anfangsbedingung:

$$\frac{f(a)}{g(a)}=1$$

Dies bedeutet, dass $f(x)$ und $g(x)$ identisch sein müssen.

### Komplexe DG

Mit $y'=y\cdot i$ soll gezeigt werden, dass $e^{xi}=\cos(x)+i\sin(x)$ gilt:

Wir haben also:

$$\begin{align}
	f(x)&=\cos(x)+i\sin(x)\\
	g(x)&=e^{xi}\\
	f(0)&=g(0)=0
\end{align}$$

Es folgt:

$$\begin{align}
	f'(x)&=e^{xi}\cdot i=f(x)\cdot i\\
	&\textrm{und}\\
	g(x)\cdot i&=i\cos(x)+i^2\sin(x)\\
	&=-sin(x)+i\cos(x)\\
	&=g'(x)
\end{align}$$

Es handelt sich also um dieselbe DG $\Rightarrow\;e^{xi}=\cos(x)+i\sin(x)$

## Überlagerung von Wachstum

Falls Bedingungen verschiedener Wachstumsarten gegeben sind, können die jeweiligen Momentanen Zunahmen zusammenaddiert werden, um die DG für das ganze Modell zu erhalten.



