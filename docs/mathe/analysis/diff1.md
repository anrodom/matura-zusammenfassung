# Differentialrechnung I

## Allgemein

### Differenzenquotient

$$\frac{\Delta y}{\Delta x}=\frac{f(x+\Delta x)-f(x)}{\Delta x}$$

### Differenzialquotient / Ableitung y'

Die Ableitung $y'$ hat den folgenden (Grenz-)Wert:

$$\lim_{\Delta x\to 0}\frac{\Delta y}{\Delta x}=\lim_{\Delta x\to 0}\frac{f(x+\Delta x)-f(x)}{\Delta x}$$

### Leibnizschreibweise

Oft schreibt man für $y'$ auch:

$$y'=\frac{dy}{dx}$$

## y'-Bestimmungen

$y=3x^2$:

$$\begin{align}
  y'&=\lim_{\Delta x\to 0}\frac{3(x+\Delta x)^2-3x^2}{\Delta x}\\
  &=\lim_{\Delta x\to 0}\frac{\cancel{3x^2}+6x\cancel{\Delta x}+3\Delta x^{\cancel{2}}\cancel{-3x^2}}{\cancel{\Delta x}}\\
  &=\lim_{\Delta x\to 0}6x+3\Delta x\\
  &=6x
\end{align}$$

$y=\sqrt{x}$:

$$\begin{align}
  y'&=\lim_{\Delta x\to 0}\frac{\sqrt{x+\Delta x}-\sqrt{x}}{\Delta x}\cdot\frac{\sqrt{x+\Delta x}+\sqrt{x}}{\sqrt{x+\Delta x}+\sqrt{x}}\\
  &=\lim_{\Delta x\to 0}\frac{\cancel{\Delta x}}{\cancel{\Delta x}(\sqrt{x+\Delta x}+\sqrt{x})}\\
  &=\lim_{\Delta x\to 0}\frac{1}{\sqrt{x+\Delta x}+\sqrt{x}}\\
  &=\frac{1}{2\sqrt{x}}
\end{align}$$

$y=\sin(x)$ (Voraussetzungen siehe Kapitel "Neue Grenzwerte" in [Repetition Funktionen und Ergänzungen](repF&E.md)):

$$\begin{align}
  y'&=\lim_{\Delta x\to 0}\frac{\sin(x+\Delta x)-\sin(x)}{\Delta x}\\
  &=\lim_{\Delta x\to 0}\frac{\sin(x)\cos(\Delta x)+\cos(x)\sin(\Delta x)-\sin(x)}{\Delta x}\\
  &=\lim_{\Delta x\to 0}\frac{\cos(x)\sin(\Delta x)}{\Delta x}+\frac{\sin(x)(\cos(\Delta x)-1)}{\Delta x}\\
  &=\cos(x)
\end{align}$$

$y=\cos(x)$:

$$\begin{align}
  y'&=\lim_{\Delta x\to 0}\frac{\cos(x+\Delta x)-\cos(x)}{\Delta x}\\
  &=\lim_{\Delta x\to 0}\frac{\cos(x)\cos(\Delta x)+\sin(x)\sin(\Delta x)-\cos(x)}{\Delta x}\\
  &=\lim_{\Delta x\to 0}-\frac{\sin(x)\sin(\Delta x)}{\Delta x}+\frac{\cos(x)(\cos(\Delta x)-1)}{\Delta x}\\
  &=-\sin(x)
\end{align}$$

$y=\ln(x)$:

$$\begin{align}
  y'&=\lim_{\Delta x\to 0}\frac{\ln(x+\Delta x)-\ln(x)}{\Delta x}\\
  &=\lim_{\Delta x\to 0}\frac{1}{\Delta x}\ln(\frac{x+\Delta x}{\Delta x})\\
  &=\lim_{\Delta x\to 0}\ln[(\frac{x+\Delta x}{\Delta x})^{\frac{1}{\Delta x}}]\;\;(\textrm{Substitution:}\;n=\frac{x}{\Delta x})\\
  &=\lim_{n\to\infty}\ln[((\frac{x+\Delta x}{\Delta x})^n)^{\frac{1}{x}}]\\
  &=\frac{1}{x}\ln(e)\\
  &=\frac{1}{x}
\end{align}$$

$y=e^x$ bzw. $ln(y)=x$:

$$\begin{align}
  \lim_{\Delta y\to 0}\frac{\Delta x}{\Delta y}&=\frac{1}{y}\\
  \lim_{\Delta x\to 0}\frac{1}{\frac{\Delta y}{\Delta x}}&=\frac{1}{\lim_{\Delta x\to 0}{\frac{\Delta y}{\Delta x}}}=\frac{1}{y'}\\
  &\Downarrow\\
  y&=y'
\end{align}$$



## Erste Regeln beim Ableiten

I.  Potenzregel (Beweis in [Differentialrechnung II](diff2.md))

$$y=x^n\;\textrm{hat}\;y'=nx^{n-1}$$

II.  Faktor- und Konstanten-Regel

$$\begin{align}
  (ky+C)'&=\lim_{\Delta x\to 0}\frac{[kf(x+\Delta x)+C]-[kf(x)+C]}{\Delta x}\\
  &=\lim_{\Delta x\to 0}\frac{k[f(x+\Delta x)-f(x)]}{\Delta x}\\
  &=k\cdot\lim_{\Delta x\to 0}\frac{f(x+\Delta x)-f(x)}{\Delta x}\\
  &=k\cdot y'
\end{align}$$

III.  Differenzen- und Summen-Regel

$$\begin{align}
  (f(x)\pm q(x))'&=\lim_{\Delta x\to 0}\frac{[f(x+\Delta x)\pm q(x+\Delta x)]-[f(x)\pm q(x)]}{\Delta x}\\
  &=\lim_{\Delta x\to 0}\frac{f(x+\Delta x)-f(x)}{\Delta x}\pm\lim_{\Delta x\to 0}\frac{q(x+\Delta x)-q(x)}{\Delta x}\\
  &=f'(x)\pm q'(x)
\end{align}$$

IV.  Noch keine Regeln für Verkettungen, Quotienten, Produkte


## Tangente an Stelle S der Funktion f(x)

1.  $m$ ist $f(2)'$
2.  $q$ mit berechnetem $m$ und dem Punkt $S$ für $t:\;y=mx+q$ berechnen

## Scheitelpunkt einer Parabel

$$(f'(x_0)=0|f(x_0))$$

## Schnittwinkel zweier Funktionen

$$\tan(\alpha)=|\frac{y_2'-y_1'}{1+y_1'y_2'}|$$

## Tangente t durch P an Funktion f(x)

$m$ der Tangente und Schnittpunkt bei $x_0$ mit folgenden 2 Gleichungen berechnen:

1.  $$t(x_0)=f(x_0)$$
2.  $$m=f'(x_0)$$