# Wahrscheinlichkeitsrechnung

Bemerkung: Die meisten Aufgaben können auch mit Baumdiagrammen, statt klassischer Kombinatorik gelöst werden.

## Begriffe / Schreibkonventionen

### Ereignis

Ereignisse werden als $E$ aufgeschrieben. Die Anzahl Elemente $k$ in $E$ sind $|E|$.

### Wahrscheinlichkeit

Wahrscheinlichkeit eines Ereignisses E: $p(E)$

### Ergebnisraum

Alle möglichen Ergebnisse: $\Omega$. Die Anzahl Elemente $n$ in $\Omega$ sind $|\Omega|$

### Elementarereignisse

Einziges Element des Ergebnisraumes: $\omega$

### Gegenereignis

Das Gegenereignis von $E$ heisst $\bar{E}$ ("E quer"). Es hat den Wert $\bar{E}=1-E$

## Laplace-Wahrscheinlichkeit

Wenn alle Elementarereignisse $\omega$ die gleiche Wahrscheinlichkeit haben, gilt:

$$p(E)=\frac{|E|}{|\Omega|}=\frac{k}{n}$$

## Bedingte Wahrscheinlichkeiten

Ein Ergebnis kann unter einer bestimmten Bedingung auftauchen (Beim Baum hängt das unterste Ereignis von den oben angesetzten Bedingungen ab). Man schreibt für die Wahrscheinlichkeit: $p(E|Bedingung)$ oder allgemein: $p(A|B)$. Die Wahrscheinlichkeit, dass sowohl $A$ als auch $B$ eintreten wird $p(A\wedge B)$ oder in der Mengenlehre $A\cap B$ aufgeschrieben. Sie entspricht also der Multiplikation der Zahlen eines Astes beim Baum oder:

$$\begin{align}
  p(A\wedge B) &= p(A|B)\cdot p(B)\\
  p(A|B)&=\frac{p(A\wedge B)}{p(B)}
\end{align}$$


Für die umgekehrte Bedingung $p(B|A)$ können wir (klarer mit Mengenlehre) Folgendes genau so gut schreiben:

$$p(B|A)=\frac{p(A\wedge B)}{p(A)} = \frac{p(A|B)\cdot p(B)}{p(A)}$$


Ereignisse gelten als unabhängig, wenn eines der Folgenden gilt:

1.  $$p(A|B)=p(A)$$
2.  $$p(A\wedge B)=p(A)\cdot p(B)$$
3.  $$p(A|B)=p(A|\textrm{n} B)$$
4.  $$p(\textrm{n} A\wedge B)=p(\textrm{n} A)\cdot p(B)$$
5.  ...

Umgekehrt sind $A$ und $B$ abhängig, wenn etwas nicht gilt.

## Beispiel für unendliche Bäume

Jemand will sich mit 90% Wahrscheinlichkeit sicher sein, dass mindestens ein Tier einen Gendefekt aufweist, der bei 5% der Tiere auftritt. Wie viele Tiere $n$ braucht er?

Die Wahrscheinlichkeit, dass kein Tier einen Defekt aufweist ist $p(\bar{E}) = 0.95^n$. D. h.:

$$\begin{align}
  p(E)= 1 - 0.95^n&\geq 0.9\\
  0.1&\geq 0.95^n\\
  n&\geq 44.89\rightarrow 45
\end{align}$$

Oder allgemein:

$$n = \log_{p(\textrm{kein Deffekt})}(1-p(\textrm{mind. Sicherheit}))$$


## Primzahlsatz

Abschätzung für $\frac{1}{1}+\frac{1}{2}+..+\frac{1}{n}$:

$$\begin{align}
  \int_{1}^{n}\frac{1}{x}\,dx+\frac{1}{n}&<\frac{1}{1}+\frac{1}{2}+..+\frac{1}{n}\\
  \ln(n)+\frac{1}{n}&<\frac{1}{1}+\frac{1}{2}+..+\frac{1}{n}\\
  \ln(n)&\approx\frac{1}{1}+\frac{1}{2}+..+\frac{1}{n}
\end{align}$$

Abschätzung für $\prod_{p\leq x}(1-\frac{1}{p})$ wobei $p$ prim ist:

$$\begin{align}
  \prod_{p\leq x}(1-\frac{1}{p})&=(1-\frac{1}{2})(1-\frac{1}{3})(1-\frac{1}{5})...(1-\frac{1}{p})\\
  &=(1+\frac{1}{2}+\frac{1}{4}+...)(1+\frac{1}{3}+\frac{1}{9}+...)(1+\frac{1}{5}+\frac{1}{25}+...)...(1+\frac{1}{p}+\frac{1}{p^2}+...)\\
  &=1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\frac{1}{5}+...+\frac{1}{p}+...+\frac{1}{x}...\textrm{Rest}\\
  \prod_{p\leq x}(1-\frac{1}{p})&\approx\frac{1}{\frac{1}{1}+\frac{1}{2}+...+\frac{1}{x}}
\end{align}$$

Beweis für die Anzahl Primzahlen kleiner/gleich $x$ oder $\pi(x)$ mit der Wahrscheinlichkeit p(x), dass eine Zahl zwischen 1 und $x$ prim ist:

$$\begin{align}
  p(x)&=\frac{\pi(x)}{x}\\
  \pi(x)&=xp(x)\\
  &\approx x[(1-\frac{1}{2})(1-\frac{1}{3})(1-\frac{1}{5})...(1-\frac{1}{p})]\\
  &\approx x[\frac{1}{\frac{1}{1}+\frac{1}{2}+...+\frac{1}{x}}] \approx x[\frac{1}{\ln(x)}]\\
  p(x)&\approx\frac{x}{\ln(x)}
\end{align}$$