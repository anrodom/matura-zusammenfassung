# Kurzzusammenfassung Mathematik

## Logarithmen und Exponentielles Wachstum

### Theorie

- Exponentielle Zunahme hat *multiplikativen* Wachstumsfaktor.

### Techniken

- Benutze Logarithmusgesetze und $\log_{b}a=\frac{\log a}{\log b}$.

- Exponentielle Zunahme: 

  - Prozentuale Zunahme $\pm p\%$ entspricht Wachstumsfaktor $b=1\pm\frac{p}{100}$.
  - Wachstumsfaktor $\color{cyan}{b}$ <span style="color: cyan">pro Zeit</span> $\color{cyan}{\Delta t}$ entspricht dem Wachstumsfaktor $\color{cyan}{b^{k}}$ <span style="color: cyan">pro Zeit</span> $\color{cyan}{ k\Delta t}$.
  - $A(t)=A_{0}b^{t}=A_{0}e^{t\ln{b}}$
  - Für die Halbwertszeit $\lambda$ gilt: $b^{\lambda}=\frac{1}{2}$.

## Vektorgeometrie

### Theorie

- Vektoren haben keine Position.
- Linearkombination $\vec{v}=\displaystyle{\sum_{i=1}^{N}v_{i}\vec{e}_{i}}$.
- Skalarprodukt als Projektion zwischen zwei Vektoren.
- Vektorprodukt als Normalvektor zu zwei Vektoren mit der Länge gleich dem Flächeninhalt des von den Vektoren aufgespannten Parallelogramms.
- Spatprodukt als Volumen des von drei Vektoren aufgespannten Spats mit Vorzeichen je nach Rechts-/Linkssystem.
- Geraden mit Vektoren dargestellt: $\vec{g}=\vec{u}+t\vec{v}$.
- Ebenen mit Vektoren dargestellt: $\vec{e}=\vec{u}+t\vec{v}+s\vec{w}$.

### Techniken

- Skalarprodukt:

  - Geometrische und elementweise Berechnung.
  - $\vec{a}^{2}=a^{2}$.
  - Falls $\vec{a}\vec{b}=0$, dann sind $\vec{a},\vec{b}\neq\vec{0}$ *senkrecht* zueinander.

- Kreuzprodukt:

  - $\begin{pmatrix} a_{1} \\ a_{2} \\ a_{3} \end{pmatrix} \times \begin{pmatrix}  b_{1} \\ b{2} \\ b_{3} \end{pmatrix} = \begin{pmatrix} a_{2}b_{3}-a_{3}b_{2} \\ a_{3}b_{1}-a_{1}b_{3} \\ a_{1}b_{2}-a_{2}b_{1} \end{pmatrix}$
  - $\vec{a}\times\vec{b}=-\vec{b}\times\vec{a}$
  - Falls $\vec{a}\times\vec{b}=0$, dann sind $\vec{a},\vec{b}\neq\vec{0}$ *kollinear* zueinander.

- Spatprodukt:

  - $\vec{a}\times\vec{b}\cdot\vec{c}=[\vec{a},\vec{b},\vec{c}]$ (Berechnung entspricht Determinante).
  - Falls $[\vec{a},\vec{b},\vec{c}]>0$ : Vektoren bilden ein Rechtssystem.
  - Falls $[\vec{a},\vec{b},\vec{c}]<0$ : Vektoren bilden ein Linkssystem.
  - Falls $[\vec{a},\vec{b},\vec{c}]=0$ : Vektoren sind komplanar.

- |                 | Skalarprodukt | Kreuzprodukt |
  | --------------- | ------------- | ------------ |
  | Kommutativität  | &#x2714;      | &#x2718;     |
  | Distributivität | &#x2714;      | &#x2714;     |
  | Assoziativität  | &#x2718;      | &#x2718;     |

- Für kollineare Vektoren $\vec{v},\vec{w}$ gilt $\bbox[3px, border:2px]{\vec{v}=\lambda\vec{w}}$ und $\bbox[3px, border:2px]{v=\lambda w}$.

- Aufpassen: Für richtige Orientierungen bei Kreuz-/Spatprodukt: Rechtssystem ist positiv!

- Gegenseitige Lage der Geraden $f:\vec{p}+t\vec{u}$ und $\;g:\vec{q}+s\vec{v}$:

$$\begin{align*}
  & \qquad\qquad\quad\;\, \downarrow\\
  \bbox[5px,border:1px]{\text{windschief }} \; \overset{\text{Nein}}{\longleftarrow} \; & \bbox[5px,border:1px]{f\cap g} \overset{\text{Nein}}{\longleftarrow}  \bbox[5px,border:1px]{\vec{u}||\vec{v}} \overset{\text{Ja}}{\longrightarrow} \bbox[5px,border:1px]{\vec{p}\in f, \vec{q}\in g} \overset{\text{Ja}}{\longrightarrow} \bbox[5px,border:1px]{\text{identisch}} \\
  & \;\; \downarrow \scriptsize \text{Ja} \normalsize \qquad\qquad\qquad\quad\;\; \downarrow \scriptsize \text{Nein}\\
  &\bbox[5px,border:1px]{\text{sich schneidend}} \quad\;\;\; \bbox[5px,border:1px]{\text{parallel}} \\
  \end{align*}$$

- Ebenen dargestellt als Relation $ax+by+cz=d$ haben den Normalenvektor $\vec{n}=\begin{pmatrix}a\\b\\c\end{pmatrix}$. Mit einsetzen eines in der Ebene enthaltenen Punktes lässt sich $d$ bestimmen. Dieser Vektor bestimmt sich aus dem Kreuzprodukt der beiden Richtungsvektoren $\vec{n}=\vec{v}\times\vec{w}$ der Ebene.
-  Schneiden von Gerade $\vec{u}+t\vec{v}$ mit der Ebene $ax+by+cz=d$: Einsetzen der einzelnen Komponenten der Geradengleichung in die Ebenengleichung ($x=u_x+tv_x,\dots$) und auflösen nach $t$.
- Parallele Ebene mit kollinearen Normalenvektoren.
- Schnittpunkte einer Ebene mit den Achsen mithilfe der Achsenabschnittsgleichung (Gleichung normalisiert auf $D=1$).
- Winkel zwischen Vektor/Gerade und Ebene mit Normalenvektor und Richtungsvektor. Wenn der berechnete Winkel $\alpha$ zwischen dem Normalenvektor und dem Richtungsvektor
  - kleiner als 90° ist: $\beta=\frac{\pi}{2}-\alpha$,
  - grösser als 90° ist: $\beta=\pi-\alpha$.
- Winkel zwischen Ebenen mit Winkel zwischen Normalenvektoren.
- Abstand eines Punkts von einer Ebene: 
  - Gerade mit Richtungsvektor $\vec{n}$ und Ortsvektor gleich dem Punkt mit der Ebene schneiden um den Abstandsfusspunkt zu erhalten. Der Abstand wird durch den Vektor zwischen den Punkten bestimmt.
  - Mit Spatprodukt, Grundfläche und Höhe.
- Abstand eines Punkts von einer Gerade:
  - Mit Ebene normal zur Gerade und auf Höhe des Punkts.
  - Schnell mit Vektorprodukt, Grundseite und Höhe.
- Spiegeln eines Punkts an einer Ebene mit Normalenvektor als Richtungsvektor.
- Reflektion Vektor an Ebene: Vektor an Ebene spiegeln.

## Folgen, Reihen und Grenzwerte

### Theorie

- Eine *Reihe* ist die Summe der Glieder einer *Folge*.

- Aufeinanderfolgende Glieder einer **arithmetischen** Folge unterscheiden sich um eine **Konstante**.
  Aufeinanderfolgende Glieder einer **geometrischen** Folge unterscheiden sich um einen **Faktor**.

- Eine Folge hat einen Grenzwert, wenn in jeder $\varepsilon$-Umgebung des Grenzwertes $a$ einer Folge $a_{n}$ fast alle Glieder $a_{n}$ liegen.

$$\forall \varepsilon>0 \; \exists n_{0}:|a-a_{n}|<\varepsilon \; \forall n\geq n_{0}$$

- Eine Folge ist **konvergent**, wenn sie einen Grenzwert hat (die obige Definition erfüllt.), **divergent** wenn nicht.

- **Summen** haben genau dann einen Grenzwert, wenn die **Folge der Partialsummen** einen Grenzwert hat.
### Techniken

- | Folgen:  | Arithmetisch         | Geometrisch                 |
  | -------- | -------------------- | --------------------------- |
  | Rekursiv | $a_{n+1}=a_{n}+d$    | $a_{n+1}=a_{n} \cdot q$     |
  | Explizit | $a_{n}=a_{1}+(n-1)d$ | $a_{n}=a_{1} \cdot q^{n-1}$ |

- | Reihen:   | Arithmetisch                                  | Geometrisch                                                  |
  | --------- | --------------------------------------------- | ------------------------------------------------------------ |
  | Endlich   | $s_{n}=\frac{n}{2}\left( a_{1}+a_{n} \right)$ | $s_{n}=a_{1}\frac{1-q^{n}}{1-q}$                             |
  | Unendlich | N/A                                           | $\displaystyle\lim_{n\rightarrow\infty}s_{n}=\frac{a_{1}}{1-q}\quad(-1\le q\le 1)$ |

- Exaktes Berechnen von Grenzwerten von Folgen mit **Ausklammern der Variable** und **Nullfolgen**.

- Grenzwertsätze:

  - $\lim a_{n}b_{n}=\lim a_{n} \lim b_{n}$
  - $\lim a_{n}b_{n}^{-1}=\lim a_{n} (\lim b_{n})^{-1}$
  - $\lim a_{n}\pm b_{n}=\lim a_{n} \pm \lim b_{n}$
  - $\lim a_{n}^{r}=(\lim a_{n})^{r}$
  - $\lim ka_{n}=k\lim a_{n}$

- Um von **rekursiver Definition** oder von **einem Beispiel** aus auf die **explizite Definition** zu schliessen: **Vermutung** aufstellen, mit **vollständiger Induktion** beweisen.

## Funktionen

### Theorie

- Die Funktion $f$ ist an der Stelle $s$ **stetig**, falls
$$\lim_{x\rightarrow s^+}f(x)=\lim_{x\rightarrow s^-}f(x)=f(s),$$
  kurz
$$\lim_{x\rightarrow s}f(x)=f(s)$$
  gilt.

- Die Funktion $f$ ist an der Stelle $s$ **differenzierbar**, falls $\frac{d f}{d x}$ existiert.

- Differenzierbar $\Rightarrow$ Stetig.

### Techniken

- Bei Umformungen von Funktionen sollten Definitionslücken beachtet und vererbt werden.

## Kurvendiskussion

### Theorie

- Kurvenrichtung:

  - $y''>0:$ Linkskurve.
  - $y''<0:$ Rechtskurve.
  - $y''=0:$ Wendepunkt.

### Techniken 

- Extremalpunke:

  - Tiefpunkt: $y'=0,y''>0$.
  - Hochpunkt: $y'=0,y''<0$.
  - Wendepunkt: $y''=0,(y'''\ne 0)$.
  - Sattelpunkt: $y'=0,y''=0$.
- Vollständige Kurvendiskussion:
  1. $y',y''$ berechnen.
  2. Nullstellen mit $y=0$ berechnen.
  3. Stellen mit $y'=0$ bestimmen und mit $y''$ in Hoch-/Tief-/Sattelpunkt einteilen.
  4. Wendepunkte mit $y''=0$ bestimmen.
  5. Grenzwerte mit $\displaystyle\lim_{x\rightarrow\pm\infty}y$ bestimmen.
- Bestimmung von Parabeln bei $n$ Bedingungen mit Parabel $n+1$er Ordnung.
- Bei der Bestimmung von Extremalstellen können Funktionen mit einfacher ableitbaren Funktionen ersetzt werden, falls sie die gleichen Extremalstellen haben.



## Differenzialrechnung

### Theorie

- Differentialquotient:
$$\newcommand{\d}{\text{d}} \\\frac{\d y}{\d x}=\lim_{\Delta x\rightarrow0}\frac{f(x+\Delta x)-f(x)}{\Delta x}.$$

### Techniken

- Ableitungsregeln:

  - $(kf)'=kf'$.
  - $(f\pm c)'=f'$.
  - $(f\pm g)'=f'\pm g'.$
  - $(fg)'=f'g+fg'$.
  - $\left(\frac{f}{g}\right)'=\frac{f'g-fg'}{g^{2}}$.
  - $(f(g))'=f'(g)g'$.
- Schnittwinkel zweier Tangenten mit $\tan\alpha=\left| \frac{f'-g'}{f'g'+1} \right|$.
- Ableiten nach Leibniz mit $f(x+\d x)=f(x)+\d y$.

  - Rechnen mit Differenzialen:
    - $\d x+a=a$
    - $\d x\d y +a\d x=a\d x$
    - $\d x^{2}-ax+b\d y=-ax$
- **Regeln von De L'Hôpital**: Für zwei Funktionen $f(x),g(x)$ gilt
$$\lim_{x\rightarrow a}\frac{f(x)}{g(x)}=\lim_{x\rightarrow a}\frac{f'(x)}{g'(x)},$$

​        wenn $f(a)=g(a)=0$ (Regel 1) oder $f(a)=g(a)\rightarrow\pm\infty$ (Regel 2).

- **Implizites Ableiten**: Wenn eine Funktion nicht direkt abgeleitet werden kann, können auch beide Seiten so umgeformt werden, dass sie ableitbar sind und dann auf beiden Seiten abgeleitet werden. Die gesuchte Ableitung sollte als Folge der Kettenregel entstehen. 
- **Satz von Taylor**:
  - $f(x)=\displaystyle\sum_{k=0}^{\infty}\frac{f^{(k)}(x_{0})}{k!}(x-x_{0})^{k}\quad(\mathbb{D}=\mathbb{I})$. Die Taylor-Entwicklung von $f(x)$ an der Stelle $x=x_{0}$ entspricht der Funktion $f(x)$ über dem Konvergenzintervall $\mathbb{I}$.
  - $f(x)=\displaystyle\sum_{k=0}^{n}\frac{f^{(k)}(x_{0})}{k!}(x-x_{0})^{k}+R_{n}(x)\quad(\mathbb{D}=\mathbb{I})$. Das Taylor-Polynom $p_{n}(x)$ plus dem Restglied $R_{n}(x)$ entspricht ebenfalls der Funktion $f(x)$ über dem Konvergenzintervall $\mathbb{I}$.
  - Benutze das Taylorpolynom $p_{n}(x)$, um eine Funktion anzunähern (z.B. um einfacher zu integrieren).

## Integralrechnung

### Theorie

- Streifenmethode durch Bestimmung des Grenzwerts der Obersumme mit Intervallbreite $b$ und Streifenanzahl $n$.
- Für die Integralfunktion $I(x)=\displaystyle\int_{0}^{x}f(u)\;\d u$ gilt $\frac{\d I}{\d x}=f(x)$.
- Die Stammfunktion ist definiert als $F(x)=I(x)+C$ und beschreibt somit **jede** Funktion mit $F'=f$.
- Für bestimmte Integrale gilt $\displaystyle\int_{a}^{b}f(x)\;\d x=F(b)-F(a)$.

### Techniken

- Integralsätze:
  - $\displaystyle\int cf(x)\;\d x=c\int f(x)\;\d x$.
  - $\displaystyle\int_{a}^{b}f(x)\;\d x=-\int_{b}^{a}f(x)\;\d x$.
  - $\displaystyle\int_{a}^{b}f(x)\;\d x=\displaystyle\int_{a}^{c}f(x)\;\d x+\displaystyle\int_{c}^{b}f(x)\;\d x$.
  - $\displaystyle\int f(x)\pm g(x)\;\d x=\int f(x)\;\d x\pm\int g(x)\;\d x$.
- Bei Flächenberechnungen auf Nullstellen und Vorzeichen achten.
- Integrationsmethoden:
  - Umgekehrte Kettenregel: Wenn im Integrand das Vielfache einer inneren Ableitung vorkommt.
  - Substitutionsmethode: Formale Anwendung der umgekehrten Kettenregel.
    - $\displaystyle\int f(u)u'\;\d x=\int f(u)\;\d u$.
    - 1. Wähle ein $u$ aus.
      2. Bilde $\frac{\d u}{\d x}=u'$ und forme so um, dass das im Integrand vorhandene Vielfache von $u'\d x$ auf einer Seite entsteht.
      3. Ersetze im Integrand mit der anderen Seite aus 2.
      4. Integriere nach $u$.
      5. Ersetze $u$ wieder mit dem ursprünglichen Term.
    - Bestimmte Integrale bestimmen sich auf zwei Arten:
      1. Bilde das unbestimmte Integral und setze die Grenzen am Schluss ein.
      2. Konvertiere die Grenzen von $x$ zu $u$ und berechne die Grenzen ohne zurücksubstituieren.
  - Aktive Substitution: Wenn die Kriterien für die umgekehrte Kettenregel und die Substitutionsmethode nicht erfüllt sind, hilft manchmal aktive Substitution. Dabei ersetzt man so, dass sich der Integrand vereinfacht. Beispiele:
    - Bei $\displaystyle\int\frac{1}{\sqrt{1-x^{2}}}\;\d x$ kann mit $x=\sin{t}$ substituiert werden.
    - Bei $\displaystyle\int\frac{x}{x+4}\;\d x$ kann mit $z=x+4$ substituiert werden.
  - Partialbruchzerlegung: Wenn ein Bruch durch keine der vorherigen Integrationsmethoden integriert werden kann, lassen sich Brüche in gewissen Situationen in Partialbrüche aufteilen und so integrieren.
    - Bei Brüchen, die im Nenner ein ausklammerbares Polynom wie z. B. $\frac{-2x-22}{x^{2}-2x-15}=\frac{-2x-22}{(x+3)(x-5)}$ haben, können zur einfach integrierbaren Summe der Teilbrüche $\frac{A}{x+3}+\frac{B}{x-5}$ umgeformt werden. Man kann $A,B$ durch Koeffizientenvergleich bestimmen.
    - Wenn im Nenner ein Polynom mit doppelter Nullstelle $x=a$ vorkommt, sind drei Teilbrüche gefordert: $\frac{\alpha}{x(x-a)^{2}}=\frac{A}{x}+\frac{B}{x-a}+\frac{C}{(x-a)^{2}}$.
    - Wenn der Grad des Zählers grösser oder gleich dem Grad des Nenners ist, wende zuerst Polynomdivision an.
  - Partielle Integration: Mit dieser Methode lassen sich Integrale oft in einfachere Integrale umwandeln oder sonst umformen.
    - $\displaystyle\int u'v\;\d x=uv-\int uv'\;\d x$.
    - Bei der Bestimmung vom $u$ und vom $v$ sollte das $v$ eine einfache Ableitung haben.
    - Manchmal entsteht auch das gleiche Integral nochmal. Dann können beide auf eine Seite genommen und durch 2 geteilt werden.
    - Bei bestimmten Integralen gilt: $\displaystyle\int_{a}^{b} u'v\;\d x=\left.uv\right|_{a}^{b}-\int_{a}^{b} uv'\;\d x$.
    - Bei uneigentlichen Integralen sollte die generelle Lösung für Grenzwerte $a,b$ gesucht werden und dann der Grenzwert genommen.

## Kombinatorik

### Theorie

- $(a+b)^{n}=\displaystyle\sum_{k=0}^{n}\binom{n}{k}a^{k}b^{n-k}\quad(n\in\mathbb{N})$.

### Techniken

- Rechenregeln für Fakultäten:

  - $\frac{(n+1)!}{(n-1)!}=n(n+1)$.
  - $\frac{1}{(n+1)!}+\frac{1}{(n+2)!}=\frac{n+3}{(n+2)!}$.
- Rechenregeln für Binomialkoeffizienten:

  - $\binom{n}{k}=\binom{n}{n-k}=\frac{n!}{k!(n-k)!}$.
  - $\binom{n}{0}=1\quad(n\in\mathbb{N})$.
  - $\binom{n}{n}=1\quad(n\in\mathbb{N})$.
  - $\binom{n}{k}+\binom{n}{k+1}+\binom{n+1}{k+1}$.
  - $\displaystyle\sum_{k=0}^{n}\binom{n}{k}=2^{n}$.
- Merkregel:
  Ist die Reihenfolge wichtig? / Gibt es eine Zuordnung?
    	<span style="color:green"><b>Ja:</b></span> Tupel $\Rightarrow$ Produktsatz. Sind Wiederholungen erlaubt?
					<span style="color:green"><b>Ja:</b></span> $k^n$
					<span style="color:red"><b>Nein:</b></span> $k!$
    ​	<span style="color:red"><b>Nein:</b></span> Mengen $\Rightarrow\binom{n}{k}$

## Wahrscheinlichkeitsrechnung

### Theorie

- Laplace-Wahrscheinlichkeit: Wenn **alle Elementarereignisse $\omega$ gleichverteilt** sind, hat das Ereignis $E$ mit $k$ Elementen im Ergebnisraum $\Omega$ mit $n$ Elementen die Wahrscheinlichkeit $p(E)=\frac{|E|}{|\Omega|}=\frac{k}{n}$.

### Techniken

- Zähle **gleichwahrscheinliche** Tupel/Mengen, um $k$ und $n$ zu bestimmen und/oder erstelle ein Baumdiagramm. Manchmal hilft auch ein Mengendiagramm.

- Manchmal ist es einfacher mit dem Gegenereignis $\overline{E}$ zu rechnen: $p(E)=1-p(\overline{E})$.

- Bei Baumdiagrammen: 
  - Versuche, Bäume mit zwei Ästen zu erstellen. Am besten sollte immer das gesuchte Elementarereignisse und alle Gegenfälle zusammengefasst gewählt werden.
  - Die Wahrscheinlichkeit eines **Elementarereignisses** in einem **mehrstufigen** Experiment ist das Produkt der Wahrscheinlichkeiten der einzelnen Experimente.
  - Die Wahrscheinlichkeit des **gesuchten Ereignisses** ist die Summe der Wahrscheinlichkeiten der Elementarereignisse.
  
- Bedingte Wahrscheinlichkeiten:
  - $p(A|B)=\frac{|A\cap B|}{|B|}=\frac{p(A\wedge B)}{p(B)}$.
  - $p(A\wedge B)=p(B\and A)\Rightarrow p(A|B)p(B)=p(B|A)p(A)$.
  - Die Ereignisse $A,B$ sind unabhängig, wenn $p(A|B)=p(A)$ oder $p(A\wedge B)=p(A)p(B)$.
  - $p(A)$ ist die Wahrscheinlichkeit, dass $A$ eintritt.
    $p(A\wedge B)$ ist die Wahrscheinlichkeit, dass $B$ und dann $A$ eintritt.
    $p(A|B)$ ist die Wahrscheinlichkeit, dass $A$ eintritt, wenn $B$ eingetreten ist.
## Wahrscheinlichkeitsverteilungen

### Theorie

- Wie sich Wahrscheinlichkeiten einer Zufallsgrösse verteilen, nennt man Wahrscheinlichkeitsverteilung.

  - Eine Wahrscheinlichkeitsverteilung, wo jeder Wert einer Zufallsgrösse die gleiche Wahrscheinlichkeit hat, nennt man **Gleichverteilung**.
  - Eine Wahrscheinlichkeitsverteilung, bei der die der Anzahl Treffer entsprechende Zufallsgrösse mit einem Baum mit jeweils 2 Ästen und gleichbleibenden Wahrscheinlichkeiten ($n$ Versuche mit Wahrscheinlichkeit $p$ für Treffer und Wahrscheinlichkeit $q=p-1$ für Nieten) dargestellt werden kann, nennt man **Binomialverteilung**.
  - Die Binomialverteilung kann durch eine sogenannte **Normalverteilung** mittels einer Dichtefunktion $\varphi$ angenähert werden. Diese Verteilung ist nicht nur weniger rechenaufwändig, sondern kann auch kontinuierliche Zufallsgrössen beschreiben. Aus der Binomialverteilung entspringen für die Dichtefunktion 4 Anforderungen:
    - $\displaystyle\lim_{x\rightarrow\pm\infty}\varphi(x)=0$.
    - $\displaystyle\int_{-\infty}^{\infty}\varphi(x)\;\d x=1$.
    - $\displaystyle\int_{-\infty}^{\infty}x\varphi(x)\;\d x=\mu$.
    - $\displaystyle\int_{-\infty}^{\infty}(\mu-x)^{2}\varphi(x)\;\d x=\sigma^{2}$.

- Für die Annäherung einer Binomialverteilung mit einer Normalverteilung kann man genauere Ergebnisse erhalten, wenn man eine Stetigkeitskorrektur vornimmt. Dabei addiert man den Wert der Zufallsgrösse mit $0.5$.

- Der durchschnittlich zu erwartende Wert nennt man **Erwartungswert**. Er entspricht nur bei **Gleichverteilungen dem Durchschnitt**.

- Faire Spiele haben den Erwartungswert 0 für die dem Gewinn entsprechende Zufallsgrösse.

- Bei zwei Zufallsgrössen $X,Y$, für welche $Y=\frac{1}{n}X$ gilt, gilt auch folgendes:

  - $\mu_{Y}=\frac{1}{n}\mu_{X}=p$.
  - $V(Y)=\frac{1}{n^{2}}V(X)$.
  - $\sigma_{Y}=\frac{1}{n}\sigma_{X}=\sqrt{\frac{pq}{n}}$.

  Die Zufallsgrösse $X$ ist dabei die absolute Verteilung und $Y$ die relative. Die mit $Y$ assoziierten Masszahlen eignen sich, um die Fehlerhaftigkeit zwischen verschieden grossen Umfragen zu vergleichen.

### Techniken

- Erwartungswert: $E(X)=\mu_{X}=\displaystyle\sum_{k=1}^{n}x_{k}p(x=x_{k})$.
  - Bei Gleichverteilungen: $E(X)=\frac{1}{n}\displaystyle\sum_{k=1}^{n}x_{k}$.
  - Bei Binomialverteilungen: $E(X)=np$.
  - Bei Normalverteilungen: $E(X)=\displaystyle\int_{-\infty}^{\infty}x\varphi(x)\;\d x$.
- Varianz: $V(X)=\displaystyle\sum_{k=1}^{n}(\mu-x_{k})^{2}p(x=x_{k})$.
  - Bei Binomialverteilungen: $V(X)=npq$.
  - Bei Normalverteilungen: $V(X)=\displaystyle\int_{-\infty}^{\infty}(\mu-x)^{2}\varphi(x)\;\d x$.
- Standardabweichung: $\sigma_{X}=\sqrt{V(X)}$.
  - Bei Binomialverteilungen: $\mu_{X}=\sqrt{npq}$.
  - Bei Normalverteilungen: $\sigma_{X}=\left(\displaystyle\int_{-\infty}^{\infty}(\mu-x)^{2}\varphi(x)\;\d x\right)^{\frac{1}{2}}$.
- Wahrscheinlichkeit:
  - Bei Binomialverteilungen: $p(X=k)=\binom{n}{k}p^{k}q^{n-k}$.
    $\mathrm{binomialpdf}(n,p,k)=p(X=k)$.
    $\mathrm{binomialcdf}(n,p,k)=p(X\le k)$.
  - Bei Normalverteilungen: $p(a\le X\le b)=\displaystyle\int_{a}^{b}\varphi(x)\;\d x$.
    $\mathrm{normalpdf}(\mu,\sigma,x)=\varphi(x)$. (Keine Wahrscheinlichkeit!)
    $\mathrm{normalcdf}(\mu,\sigma,a,b)=p(a\le X\le b)$.
    $\mathrm{invnorm}(\mu,\sigma,p)=b$ für $p=p(X\le b)$.
    $\mathrm{invnorm}(\mu,\sigma,1-p)=a$ für $p=p(a\le X)$.
- Bei einer Zufallsgrösse, die unendlich viele Werte annimmt: Geometrische Reihe aus dem Erwartungswert bilden und den Grenzwert bestimmen.
- Eine Normalverteilung lässt sich standardisieren ($\mu=0,\sigma=1$) mit $Y=\frac{X-\mu}{\sigma}$. Die Standardisierung ist eine flächentreue Abbildung $\Rightarrow p(a\le X\le b)=p(a'\le Y\le b')$ mit $a'=\frac{a-\mu}{\sigma},b'=\frac{b-\mu}{\sigma}$. Damit können Gleichungssysteme gebildet werden, z. B., wenn ein Vertrauensintervall bekannt ist. Dabei hilft auch der $\mathrm{invnorm}$-Befehl.
- Vertrauensintervalle bei Standardnormalverteilungen:
  - $[\mu-\sigma;\mu+\sigma]:68.27%$
  - $[\mu-2\sigma;\mu+2\sigma]:95.45%$
  - $[\mu-3\sigma;\mu+3\sigma]:99.73%$

## Differenzialgleichungen

### Theorie

- Differenzialgleichung **1. Ordnung**: Gleichung mit der Funktion $y(x),x$ und der 1. Ableitung $y'$.
- Einfache Differenzialgleichungen für $N(t)$.
  - $N'(t)=k\Rightarrow$ lineares Wachstum (Zunahme konstant).
    Lösung: $N(t)=C+kt$.
  - $N'(t)=kN(t)\Rightarrow$ exponentielles Wachstum (Zunahme proportional zum Wert).
    Lösung: $N(t)=Ce^{kt}$. 
  - $N'(t)=k(G-N(t))\Rightarrow$ begrenztes Wachstum 
    Lösung: $N(t)=Ce^{-kt}+G$.
  - $N'(t)=kN(t)(G-N(t))\Rightarrow$ logistisches Wachstum 
    Lösung: $N(t)=\frac{G}{Ce^{-kGt}+1}$.
- Weber-Fechner-Gesetz:
  - $y'=\frac{k}{x}$ mit $A(x_0;0)$.
  - $y=k\ln{\frac{x}{x_0}}$.
- Bei Überlagerungen von Wachstumsmodellen können die Wachstumsraten addiert werden:
  $y=f(t)$ und gleichzeitig $y=g(t)\Rightarrow y'=f'(t)+g'(t)$.

### Techniken

- Der Wachstumsfaktor $b$ entspricht **nicht** dem Faktor $k$ in $y'=ky$, sondern $e^{k}$. Generell sollte $k$ bestimmt werden, indem die Funktion für das relevante Wachstum nach $k$ aufgelöst wird.
- Separation der Variablen: Forme so um, dass beim Integrieren $y'$ verschwindet. Dabei sollten auf einer Seite $y$-und $y'$-Terme sein und auf der anderen Seite $x$-Terme. Beispiele:
  - $y^{n} {\color{red}y'} \xrightarrow{\int}\frac{1}{n+1}y^{n+1}$.
  - $\frac{\color{red}y'}{y}\xrightarrow{\int}\ln{y}$.
- Bei gegebener Anfangsbedingung $(x_0;y_0)$ kann einfach eingesetzt und nach $C$ aufgelöst werden.
- In Fällen wie $y'=c-ky$ darf die Konstante sowie der Faktor mit auf die linke Seite genommen werden.
- Bei Differenzialgleichungen der Form $y'=y(c-y)$ kann man entweder Partialbruchzerlegung oder Substitution anwenden.
  - Ansatz $\frac{y'}{y(19-y)}=\frac{Ay'}{y}+\frac{By'}{10-y}$.
  - Substitution $z=\frac{1}{y}$ und $z'=-\frac{1}{y^2}y'\Rightarrow y'=-y^2 z'$.  Zuerst $y'$ ersetzen und dann umformen bis $\frac{1}{y}$ und somit $z$ entsteht. Anschliessend nach $z$ auflösen und mit $\frac{1}{y}$ ersetzen.

