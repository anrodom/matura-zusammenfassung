# Differentialrechnung II

## Neue Ableitungsregeln

### Produktregel

$$\begin{align}
  (f(x)\cdot g(x))'&=\lim_{\Delta x\to 0}\frac{f(x+\Delta x)\cdot g(x+\Delta x)-f(x)\cdot g(x)}{\Delta x}\\
  &=\lim_{\Delta x\to 0}\frac{f(x+\Delta x)\cdot g(x+\Delta x)-f(x)\cdot g(x+\Delta x)+f(x)\cdot g(x+\Delta x)-f(x)\cdot g(x)}{\Delta x}\\
  &=\lim_{\Delta x\to 0}\frac{f(x+\Delta x)\cdot g(x+\Delta x)-f(x)\cdot g(x+\Delta x)}{\Delta x}+\lim_{\Delta x\to 0}\frac{f(x)\cdot g(x+\Delta x)-f(x)\cdot g(x)}{\Delta x}\\
  &=\lim_{\Delta x\to 0}\frac{g(x+\Delta x)\cdot[f(x+\Delta x) -f(x)]}{\Delta x}+\lim_{\Delta x\to 0}\frac{f(x)\cdot[g(x+\Delta x) -g(x)]}{\Delta x}\\
  &=\lim_{\Delta x\to 0}(g(x+\Delta x))\cdot\lim_{\Delta x\to 0}\frac{f(x+\Delta x) -f(x)}{\Delta x}+\lim_{\Delta x\to 0}(f(x))\cdot\lim_{\Delta x\to 0}\frac{g(x+\Delta x) -g(x)}{\Delta x}\\
  &=g(x)\cdot f'(x)+g'(x)\cdot f(x)
\end{align}$$

### Kettenregel

$$\begin{align}
  (f(g(x)))'&=\lim_{\Delta x\to 0}\frac{f(g(x+\Delta x))-f(g(x))}{\Delta x}\\
  &=\lim_{\Delta x\to 0}\frac{f(u+\Delta u)-f(u)}{\Delta x}\\
  &=\lim_{\Delta x\to 0}\frac{f(u+\Delta u)-f(u)}{\Delta x}\cdot\frac{\Delta u}{\Delta u}\\
  &=\lim_{\Delta x\to 0}\frac{f(u+\Delta u)-f(u)}{\Delta u}\cdot\lim_{\Delta x\to 0}\frac{\Delta u}{\Delta x}\\
  &=\lim_{\Delta u\to 0}\frac{f(u+\Delta u)-f(u)}{\Delta u}\cdot\lim_{\Delta x\to 0}\frac{\Delta u}{\Delta x}\\
  &=f'(u)\cdot g'(x)\\
  &=f'(g(x))\cdot g'(x)
\end{align}$$

### Quotientenregel

$$\begin{align}
  \left( \frac{f(x)}{g(x)}\right)'&=\left( f(x)\cdot\frac{1}{g(x)}\right)'\\
  &=f'(x)\cdot\frac{1}{g(x)}+f(x)\cdot\frac{-1}{g^2(x)}\cdot g'(x)\\
  &=\frac{f'(x)\cdot g(x)-f(x)\cdot g'(x)}{g^2(x)}
\end{align}$$

### Beweis der alten Ableitungsregel (Vollständige Induktion)

Ver. (n=1):

$$y=x^1\;\Rightarrow\;y'=1\cdot x^0=1$$

Vor.:

$$y=x^k\;\Rightarrow\;y'=kx^{k-1}$$

Z. z.:

$$\begin{align}
  y&=x^{k+1}\;\Rightarrow\;y'=(k+1)x^{k}\\
  y&=x^{k+1}\\
  &=x^k\cdot x\\
  y'&=k\cdot x^{k-1}\cdot x +x^k\\
  &=(k+1)x^k
\end{align}$$

Es gilt also:

$$y=x^n\;\textrm{hat}\;y'=n\cdot x^{n-1}$$

## De L'Hospital

### Regel 1

Wenn für ein bestimmtes $a$ für Funktionen $f(a)=g(a)=0$ gilt, dann gilt Folgendes für den Quotienten:

$$\begin{align}
  \lim_{x\to a}\frac{f(x)}{g(x)}&=\lim_{x\to a}\frac{f(x)-f(a)}{g(x)-g(a)}\\
  &=\lim_{x\to a}\frac{\frac{f(x)-f(a)}{x-a}}{\frac{g(x)-g(a)}{x-a}}\\
  &=\lim_{x\to a}\frac{f'(x)}{g'(x)}
\end{align}$$

### Regel 2

Wenn für ein bestimmtes $a$ für Funktionen $f(a)=g(a)=\pm\infty$ gilt, dann gilt Folgendes für den Quotienten:

$$\begin{align}
  \lim_{x\to a}\frac{f(x)}{g(x)}&=\lim_{x\to a}\frac{\frac{1}{g(x)}}{\frac{1}{f(x)}}\;\textrm{(Nenner und Zähler streben zu}\;\pm\infty\,\Rightarrow\textrm{Regel 1)}\\
  &=\lim_{x\to a}\frac{\frac{-1}{g^2(x)}\cdot g'(x)}{\frac{-1}{f^2(x)}\cdot f'(x)}\\
  &\Downarrow\\
  \lim_{x\to a}\frac{f(x)}{g(x)}&=\lim_{x\to a}\frac{f'(x)}{g'(x)}
\end{align}$$

### Erweiterung / Zusammenfassung

Mit einer Substitution von $x=\frac{1}{z}$ kann man zeigen, dass für $a$ auch $a=\pm\infty$ gelten darf.

Allgemein zusammengefasst gilt wenn $\lim_{x\to a}f(x)=\lim_{x\to a}g(x)=0\;(\textrm{oder}\;\pm\infty)$ für alle $a$ (auch $\pm\infty$):

$$\lim_{x\to a}\frac{f(x)}{g(x)}=\lim_{x\to a}\frac{f'(x)}{g'(x)}$$

## Hyperbolicus

Funktionen wie $\cosh(x)$,$\sinh(x)$ und $\tanh(x)$ haben nichts mit dem Kosinus, Sinus und Tangens zu tun. Für sie gilt:

$$\begin{align}
  \cosh(x)&=\frac{e^x+e^{-x}}{2}\\
  \sinh(x)&=\frac{e^x-e^{-x}}{2}\\
  \tanh(x)&=\frac{e^x-e^{-x}}{e^x+e^-x}
\end{align}$$

Mit folgenden Zusammenhängen:

$$\begin{align}
  \sinh'(x)&=\cosh(x)\\
  \tanh'(x)&=\frac{1}{\cosh^2(x)}\\
  \cosh^2(x)-\sinh^2(x)&=1
\end{align}$$

Für die Umkehrfunktionen $\textrm{arcosh}(x)$, $\textrm{arsinh}(x)$ und $\textrm{artanh}(x)$ gilt:

$$\begin{align}
  \textrm{arcosh}(x)&=\frac{1}{\sqrt{x^2-1}}\\
  \textrm{arsinh}(x)&=\frac{1}{\sqrt{x^2+1}}\\
  \textrm{artanh}(x)&=\frac{1}{1-x^2}
\end{align}$$

## Implizites Differenzieren

Funktionen kann man, anstatt sie direkt abzuleiten, zuerst umformen und anschliessend ableiten. Achten muss man dabei darauf, dass beim Ableiten des Teiles mit $y$, dieser mit $y'$ multipliziert wird. Bsp. :

$$\begin{align}
  y&=\sqrt[3]{2x+1}\\
  y^3&=2x+1\\
  3y^2y'&=2\\
  y'&=\frac{2}{3y^2}\\
  y'&=\frac{2}{3\cdot\sqrt[3]{2x+1}^2}
\end{align}$$

## Taylorreihen

### Allgemein

Wenn Funktionen $f(x)$  (z. B. $f(x)=\frac{1}{1-x}$) auf Konvergenz-Intervallen (in diesem Fall $]-1;1[$) durch ein Polynom $p(x)=\displaystyle\sum_{k=0}^{\infty} a_kx^k$ ersetzt werden kann (hier $p(x)=1+x+x^2+x^3+...$ ), dann nennt man $p(x)$ Potenzreihe oder Taylorreihe von $f(x)$ 



### Bestimmung p(x)

Oft erhält man Bedingungen für $p(x)$ und $p'(x)$ etc. Die Idee dort, ist die Koeffizienten zu vergleichen. Um zu beweisen, dass $p(x)$ dann auch einer Funktion $f(x)$ (z. B. $e^x$) entspricht, also $\frac{p(x)}{f(x)}=1$ gilt, zeigt man zuerst, dass $\left(\frac{p(x)}{f(x)}\right)'=0$ gilt. Daraus folgt nämlich, dass $\frac{p(x)}{f(x)}=C$ zumindest konstant ist. Man muss nur noch ein $x$ einsetzen und hoffen, dass $C=1$ das Resultat ist. 



### Der Satz von Taylor

Eine Funktion $f(x)$ nähert man mit $p(x)=a_0+a_1x+a_2x^2+a_3x^3+...+a_nx^n$ in der Umgebung von $x=0$ an, indem man $a_0,\,a_1x,\,a_2x^2,\,a_3x^3,\,...,\,a_nx^n$ mit $p(0)=f(0),\,p'(0)=f'(0),\,p''(0)=f''(0),\,...,\,p^{(n)}(0)=f^{(n)}(0)$ bestimmt. Allgemein gilt für $a_n$ also Folgendes:

$$a_n=\frac{f^{(n)}(0)}{n!}$$

Und für das Polynom $p(x)$:

$$p(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}x^n$$

Alle wichtigen Potenzreihen stehen im Formelbuch auf S.31

### Beispiel Newton Binomialreihe

Es gilt:

$$\begin{align}
	y&=(1+x)^a\\
	y'&=a(1+x)^{(a-1)}\\
	y''&=a(a-1)(1+x)^{(a-2)}\\
	y'''&=a(a-1)(a-2)(1+x)^{(a-3)}\\
\end{align}$$

Wenn nun jeweils $x=0$ eingesetzt wird, erhält man für die Polynomreihe:

$$(1+x)^a=\sum_{n=0}^{\infty}{a\choose n}x^n$$

### Das Basel-Problem

Ziel ist die Lösung der folgenden Reihe:

$$1+\frac{1}{1^2}+\frac{1}{2^2}+\frac{1}{3^2}+...$$

Wir schreiben dafür zuerst $\sin(x)$ als unendliches Polynom mit denselben Nullstellen:

$$\begin{align}
	\sin(x)&=Cx\left(1-\frac{x^2}{\pi^2}\right)\left(1-\frac{x^2}{(2\pi)^2}\right)\left(1-\frac{x^2}{(3\pi)^2}\right)...\\
	\frac{\sin(x)}{x}&=C\left(1-\frac{x^2}{\pi^2}\right)\left(1-\frac{x^2}{(2\pi)^2}\right)\left(1-\frac{x^2}{(3\pi)^2}\right)...\\
	\lim_{x\to 0}\frac{\sin(x)}{x}&=C\lim_{x\to 0}\left(1-\frac{x^2}{\pi^2}\right)\left(1-\frac{x^2}{(2\pi)^2}\right)\left(1-\frac{x^2}{(3\pi)^2}\right)...\\
	1&=C\\
	&\Downarrow\\
	\sin(x)&=x\left(1-\frac{x^2}{\pi^2}\right)\left(1-\frac{x^2}{(2\pi)^2}\right)\left(1-\frac{x^2}{(3\pi)^2}\right)...
\end{align}$$

Es ergibt sich also Folgendes:

$$x-\frac{x^3}{3!}+\frac{x^5}{5!}-...=x\left(1-\frac{x^2}{\pi^2}\right)\left(1-\frac{x^2}{(2\pi)^2}\right)\left(1-\frac{x^2}{(3\pi)^2}\right)...$$

Wenn wir nun einen Koeffizientenvergleich für $x^3$ machen, erhalten wir:

$$\begin{align}
	-\frac{1}{6}&=-\frac{1}{\pi^2}-\frac{1}{(2\pi)^2}-\frac{1}{(3\pi)^2}-\frac{1}{(4\pi)^2}-...\\
	\frac{\pi^2}{6}&=\frac{1}{1^2}+\frac{1}{2^2}+\frac{1}{3^2}+...
\end{align}$$

### Euler und Primzahlen

Für Primzahlen $p$ gilt:

$$1+\frac{1}{p^2}+\frac{1}{p^4}+\frac{1}{p^6}+...=\frac{1}{1-\frac{1}{p^2}}=\frac{p^2}{p^2-1}$$

Für das Produkt aller solcher Primzahlfolgen gilt:

$$\begin{align}
	\prod_{p\;\textrm{prim}}\frac{p^2}{p^2-1}&=\left(1+\frac{1}{2^2}+\frac{1}{2^4}+...\right)\left(1+\frac{1}{3^2}+\frac{1}{3^4}+...\right)\left(1+\frac{1}{5^2}+\frac{1}{5^4}+...\right)...\\
	&=1+\frac{1}{2^2}+\frac{1}{3^2}+\frac{1}{4^2}+\frac{1}{5^2}+\frac{1}{6^2}+...\\
	&=\frac{\pi^2}{6}
\end{align}$$


### Der allgemeine Satz von Taylor

Will man Funktionen $f(x)$ an einer Stelle $x_0$, in der diese unendlich oft differenzierbar sind, als Polynom $p(x)$ aufschreiben, dann verschiebt man die Funktion zuerst zu $x=0$, bestimmt dort die Entwicklung und verschiebt zurück. Für $f(x)$ gilt dann:

$$f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n$$

