# Grenzwerte und unendliche Prozesse

## Grenzwerte


### Allgemein

#### Konvergent / Divergent

Eine Folge wie z. B. $a_n=\frac{n-2}{n}$ nähert sich immer mehr der kleinsten oberen Schranke 1. Obwohl diese theoretisch nie wirklich erreicht wird, sagen wir, dass wenn $n$ zu $\infty$ geht $a_n$ zu 1 wird, sie also den Grenzwert 1 hat. Oder:

$$\lim_{n\to\infty}a_n=1$$

Die Folge konvergiert. Wenn dies nicht der Fall ist und die Folge zu $\infty$ oder $-\infty$ strebt, dann divergiert diese.

#### Umgebung

Grenzwerte werden formell mit $\varepsilon$-Umgebungen definiert. Egal wie gross /klein eine Umgebung (ein Bereich um den Grenzwert $a$) gewählt wird, ab einem bestimmten $n_0$ liegen alle weiteren (immer noch unendlich viele) $a_n$ in dieser Umgebung. Genau:

> Für alle $\varepsilon$>0 gibt es ein $n_0$ mit $|a_n-a|<\varepsilon$ für alle $n\geq n_0$

Oder noch kürzer:

> $\forall\varepsilon>0,\;\exists n_0$ mit $|a_n-a|<\varepsilon, \;\forall n\geq n_0$

#### Ideen

1.  $$\lim_{n\to\infty}\frac{a^n}{an}=\infty$$

2.  $$\begin{align}
    \lim_{n\to\infty}\frac{an+b}{cn+d}&=\lim_{n\to\infty}\frac{n\left(a+\frac{b}{n}\right)}{n\left(c+\frac{d}{n}\right)}\\
    &=\lim_{n\to\infty}\frac{a+\frac{b}{n}}{c+\frac{d}{n}}\\
    &=\frac{a}{c}
    \end{align}$$

### Folgen und Reihen

#### Allgemein

Unendliche Reihen haben dann einen Grenzwert $s$, wenn die Folge der Partialreihen $s_n$ einen Grenzwert haben.

#### Geometrische Reihe

Der mögliche Grenzwert von $$s=a_1\frac{1-q^n}{1-q}$$ lässt sich auf zwei Arten bestimmen. Die erste lässt sich auch auf andere Beweise anwenden.

Erste Art:

$$\begin{align}
  s &= a_1 + a_1q + a_1q^2+...\\
  s &= a_1 + q[a_1 + a_1q + a_1q^2+...]\\
  s &= a_1 + q\cdot s\\
  s(1-q)&=a_1\\
  s&=\frac{a_1}{1-q}
\end{align}$$

(Achtung: Beweis gilt nur, wenn $s$ auch einen Wert hat, es konvergiert: $-1<q<1$)

Zweite Art:

$$\begin{align}
  s &= \lim_{n\to\infty}s_n\\
  &= \lim_{n\to\infty}\left(a_1\frac{1-q^n}{1-q}\right)\\
  &= \frac{a_1}{1-q}\;\;(\textrm{Wenn}\,|q|<1)
\end{align}$$

### Grenzwertsätze

1.  $$\lim_{n\to\infty}(a_n\cdot b_n)=\lim_{n\to\infty}(a_n)\cdot\lim_{n\to\infty}(b_n)=a\cdot b$$
2.  $$\lim_{n\to\infty}\left(\frac{a_n}{b_n}\right)=\frac{\lim_{n\to\infty}(a_n)}{\lim_{n\to\infty}(b_n)}=\frac{a}{b}$$
3.  $$\lim_{n\to\infty}(a_n\pm b_n)=\lim_{n\to\infty}(a_n)\pm\lim_{n\to\infty}(b_n)=a\pm b$$
4.  $$\lim_{n\to\infty}[(a_n)^r]=[\lim_{n\to\infty}(a_n)]^r=a^r$$
5.  $$\lim_{n\to\infty}(r\cdot a_n)=r\cdot\lim_{n\to\infty}(a_n)=r\cdot a$$

### Intervallschachtelung

Wenn für eine Folge von ineinander verschachtelten Intervallen $[a_n;b_n]$ die Aussage $\lim_{n\to\infty}(b_n-a_n)=0$ gilt, spricht man von einer Intervallschachtelung. D. h. eine Folge $a_n$ nähert sich dem Grenzwert $x$ von unten und eine Folge $b_n$ von oben, sprich $\lim_{n\to\infty}a_n=\lim_{n\to\infty}b_n=x$.

### Auflistung der reellen Zahlen

Könnte man alle Zahlen $r\in\mathbb{R}$ im Intervall $[0;1$ als Punkte in einer Liste ${r_1,r_2,r_3,...}$ auflisten, dann kann die Grösse dieser Punkte beliebig klein (z. B. $\frac{1}{1\cdot10^6},\frac{1}{2\cdot10^6},\frac{1}{4\cdot10^6},...$) gewählt werden, was dazu führt, dass alle Punkte in der Liste unter einer beliebig kleinen Umgebung (z. B. $\frac{1}{1\cdot10^6}+\frac{1}{2\cdot10^6}+\frac{1}{4\cdot10^6}+...=\frac{2}{10^6}$ Platz hätten. Dies macht keinen Sinn, da wir wissen, dass diese Punkte insgesamt die Länge 1 ergeben müssten. D. h., dass die reellen Zahlen nicht aufgelistet werden können.

### Harmonische Reihe

Eine sehr wichtige Reihe ist die sogenannte Harmonische Reihe:

$$s=\sum_{k=0}^{\infty}\frac{1}{k}=\frac{1}{1}+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+...$$

Um den Grenzwert zu bestimmen, verwendet man wieder eine Idee (Gruppieren), die bei vielen Beweisen verwendet wird:

$$\begin{align}
  s&=\frac{1}{1}+\frac{1}{2}+\left(\frac{1}{3}+\frac{1}{4}\right)+\left(\frac{1}{5}+\frac{1}{6}+\frac{1}{7}+\frac{1}{8}\right)+...\\
  &\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;>\frac{1}{2}\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\;\,\:>\frac{1}{2}\\
  s&>\lim_{n\to\infty}\left(1+n\cdot\frac{1}{2}\right)=\infty
\end{align}$$

## Vollständige Induktion

Die Logik bei der Induktion ist vom Speziellen zum Allgemeinen zu schliessen. (Gegenteil von Deduktion)

Folgendes Vorgehen wird für den Beweis verwendet, nach dem eine Behauptung (meistens mit $n$) aufgestellt hat:

1.  Verankerung: Kleinsten speziellen Fall finden, für welchen die Behauptung gilt.
2.  Voraussetzung: Die Behauptung erneut für ein (meistens) $k$ formuliert.
3.  Zu Zeigen: Aus den vorherigen Schritten, muss gezeigt werden, dass die Behauptung für $k+1$ gilt.