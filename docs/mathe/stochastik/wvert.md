# Wahrscheinlichkeitsverteilung

## Begriffe

### Zufallsgrösse und Wahrscheinlichkeitsverteilung

Wir verwenden von nun an $X$ für die Zufallsgrösse (z. B. "Gewürfelte Augenzahl"), wobei die Verteilung der Wahrscheinlichkeiten $p(X)$ als Wahrscheinlichkeitsverteilung beschrieben wird.

Sind alle $p(X)$ gleich, spricht man von Gleichverteilung

### Erwartungswert

Der Erwartungswert (der durchschnittlich zu erwartende Wert) $E(X)$ oder $\mu$ wird wie folgt berechnet:

$$E(X)=\mu=\sum_{k=1}^{n}x_kp(X = x_k)$$

### Andere Zufallsgrössen (Gewinn / Runs)

Oft bezeichnet man Erwartungswerte, wie denn des Gewinnes in einem Spiel mit $Y$. Faire Spiele haben $E(Y)=0$

Auch die Anzahl Runs (wie oft wechselt der eigentliche Erwartungswert) wird oft mit $Y$ bezeichnet. Hier muss wieder mit Tupeln gerechnet werden.
Für $E(Y)$ mit $n$ als Anzahl möglicher Wechsel (immer 1 weniger als die Anzahl der z. B. Würfe), $k$ als Anzahl der Wechsel und $p$ als als Wahrscheinlichkeit eines Wechsels gilt also:

$$\begin{align}
E(Y)&=1\cdot{n\choose 0}p^{(n+1)}+2\cdot{n\choose 1}p^{(n+1)}+3\cdot{n\choose 2}p^{(n+1)}+...+(n+1)\cdot{n\choose n}p^{(n+1)}\\
  &=p^{(n+1)}[\sum_{k=0}^{n}(k+1){n\choose k}]
\end{align}$$

### Varianz / Standardabweichung

Beim Vergleichen zweier Zufallsgrössen $X$ und $Y$ können die Erwartungswerte $E(X)$ und $E(Y)$ gleich sein, die Streuung / Varianz sich aber unterscheiden. Für die Varianz einer Zufallsgrösse verwenden wir $V(X)$. Sie berechnet sich wie folgt:

$$V(X)=\sum_{k=1}^{n}p(X = x_k)\cdot(x_k-\mu)^2$$

Da wir hier quadrieren, gibt es auch die Standardabweichung $\sigma$:

$$\sigma=\sqrt{V(X)}$$

## Binomialverteilung

### Voraussetzung

Wenn bei einem Baum lediglich eine Wahrscheinlichkeit $p$ und eine $q=1-p$ vorhanden sind, spricht man von einer Binomialverteilung.

### Berechnung

$n$ sei die Anzahl Stufen / Versuche, $p$ die Wahrscheinlichkeit ($q=1-p$) für einen Treffer und $k$ die Anzahl Treffer.

#### Formel von Bernoulli

$$p(X = k)={n\choose k}\cdot p^k\cdot q^{n-k}$$

####  binomialpdf

$$p(X = k)=\textrm{binomialpdf}(n,p,k)$$

#### binomialcdf

$$p(X \leq k)=\textrm{binomialcdf}(n,p,k)$$

#### E(X)

$$E(X)=\sigma=n\cdot p$$

#### V(X)

$$V(X)=n\cdot p\cdot q$$

#### Standardabweichung

$$\sigma=\sqrt{V(X)}=\sqrt{n\cdot p\cdot q}$$

#### Unendliche viele Werte

> !Achtung: Immer noch Binomialverteilung! (Unendliche Bäume, die nicht binomial verteilt sind, mit Hilfe der Formeln in [Endliche Folgen und Reihen](../analysis/endlF&R.md).)


Vorbemerkung:

$$1+2x+3x^2+4x^3+...=\frac{1}{(1-x)^2}$$

Beispiel: Wie oft muss gewürfelt werfen, bis zum 1ten Mal eine 5 kommt?

$$E(X)=\frac{1}{6}\left[1+2\cdot\frac{5}{6}+3\cdot\left(\frac{5}{6}\right)^2+...\right]=\frac{1}{6}\cdot\frac{1}{\left(1-\frac{5}{6}\right)^2}=6$$

Allgemein:

$$E(X)=p\cdot\frac{1}{(1-q)^2}=\frac{1}{p}$$

## Normalverteilung

Die Normalverteilung ist im Grunde eine Annäherung an die Binomialverteilung, um diese als Funktion auszudrücken. Zudem ermöglicht sie, dass Zahlen aus $\mathbb{R}$ verwendet werden können.

Als Funktion wird dabei die Dichtefunktion $\varphi(x)$ von Gauss:

$$\varphi(x)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$

Wahrscheinlichkeiten $p(x)$ sind also die Flächen unter dem Integral, weswegen sie also mit dem Integral der Dichtefunktion berechnet werden.

### Berechnung

#### normalcdf

$$p(k_1\leq x\leq k_2)=\textrm{normalcdf}(\mu,\sigma,k_1,k_2)=\int_{k_1}^{k_2} \varphi(x) \,dx$$

#### normalpdf

Macht eigentlich wenig Sinn, da Fläche unter einzelnen Werten ja 0 sind. Es wird also verwendet, um die Dichtefunktion zu berechnen.

$$p(x)=\textrm{normalpdf}(x,\mu,\sigma)=\varphi(x)$$

#### invNorm

Um von einer gegeben Wahrscheinlichkeit $p_0=p(x\leq x_0)$ das $x_0$ zu finden, wird der Befehl invNorm verwendet:

$$x_0 = \textrm{invNorm}(p_0,\mu,\sigma)$$

### Stetigkeitskorrektur

Falls eine Zufallsgrösse $X$ normalverteilt ist aber nur ganzzahlige Werte annehmen kann, besteht die Möglichkeit eine Stetigkeitskorrektur durchzuführen:

$$p(x\leq k)\rightarrow p(x\leq k+0.5)$$


## Standardnormalverteilung

Die Standardnormalverteilung ist Normalverteilung mit den Werten $\mu=0$ und $\sigma=1$. Sie ist somit zur y-Achse symmetrisch.

### Standardisierung einer Normalverteilung

Um von einem normalverteilten Zufallsgrösse $X$ mit $\mu_x$ und $\sigma_x$ auf die standardisierte Zufallsgrösse $Y$ zu kommen, rechnet man Folgendes:

$$Y=\frac{X-\mu_x}{\sigma_x}$$

Dann bleiben die Wahrscheinlichkeiten gleich. (Beweis mit Substitutionsmethode mit $Y$)

Umgekehrt lassen sich auch $\mu_x$ und $\sigma_x$ aus dem standardisierten $Y$ berechnen, indem man zuerst die Grenzen anhand der gegebenen Wahrscheinlichkeiten $p$ standardisiert und $\mu_x$ und $\sigma_x$ dann mit der obigen Formel berechnet.

## Umgebungen

$$\begin{align}
  p(\mu-\sigma\leq X\leq\mu+\sigma)&\approx 68.3\% \\
  p(\mu-2\sigma\leq X\leq\mu+2\sigma)&\approx 95.4\% \\
  p(\mu-3\sigma\leq X\leq\mu+3\sigma)&\approx 99.7\%
\end{align}$$

## Umfang n einer Stichprobe bestimmen

Um von einer absoluten Zufallsgrösse $X$ zu einer relativen $Y$ zu kommen, brauchen wir die Umwandlung $Y=\frac{X}{n}$. Wir wollen nun mit einer bestimmten Sicherheit $\lambda\sigma_y$ (wir wählen eine Umgebung aus siehe vorheriges Kapitel) auf $g$ genau bestimmen (z. B. Anteil Personen mit Blutgruppe B auf 0.02 genau).

Es gelten nun:

$$\begin{align}
  \lambda\sigma_y&=g\\
  \sigma_y&=\frac{\sigma_x}{n}=\sqrt{\frac{pq}{n}}
\end{align}$$

Folgende Gleichung ergibt sich:

$$\sqrt{\frac{pq}{n}}=\frac{g}{\lambda}$$

Falls ungefähre $p$ und $q$ nicht bekannt sind, müssen wir eine zusätzliche Abschätzung machen:

$$\begin{align}
  p(1-p)&=p-p^2\\
  &=\frac{1}{4}-\left(\frac{1}{4}-p+p^2\right)\\
  &=\frac{1}{4}-\left(\frac{1}{2}-p\right)^2\leq\frac{1}{4}
\end{align}$$

Wir verwenden also $pq\leq\frac{1}{4}$. Würde man wissen, dass sich $p$ bei etwa 10% befindet hätten wir $pq\approx 0.09$.

Aus der Gleichung entsteht nun:

$$\begin{align}
  \sqrt{\frac{1/4}{n}}&\leq\frac{g}{\lambda}\\
  \frac{1}{4n}&\leq\left(\frac{g}{\lambda}\right)^2\\
  n&\geq\frac{1}{4(\frac{g}{\lambda})^2}
\end{align}$$

