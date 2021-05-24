# Mechanik

## Kinematik

Alle Beziehungen zwischen $x$, $v$, $a$ und $t$ ohne Berücksichtigung von $m$ und $t$ sind Teil der Kinematik. Wichtig sind im Grunde die Beziehungen $v=\frac{x}{t}$ und $a=\frac{v}{t}$. Alle weiteren Formeln sind Ableitungen dieser Grundgesetze. Alle anderen Formeln sind Ableitungen davon. 

## Kräfte

### Gewichtskraft

$$G=m\cdot g$$

### Normalkraft

Auf stabilem Untergrund heben sich die Gewichtskraft und die Komponente der Normalkraft in entgegengesetzter Richtung auf.

$$\vec{N_y}=-\vec{G}$$

### Reibungskräfte

#### Haftreibung

Die Haftreibung verhindert das Rutschen. Für die maximal möglich Haftreibung $R_{\textrm{H,max}}$ gilt:

$$R_{\textrm{H,max}}=\mu_H\cdot N$$

#### Gleitreibung

Die von der Geschwindigkeit unabhängige, bremsende Kraft bei bewegten Körpern:

$$R_{\textrm{G,max}}=\mu_G\cdot N$$

### Feder

Die Kraft $F$ einer Feder wird mit der Federkonstante $D$ und der erreichten Verlängerung $x$ beschrieben:

$$F=D\cdot x$$

### Gravitationskraft

$$F_{\textrm{Grav}}=G\cdot\frac{m_1\cdot m_2}{r^2}$$

## Newtonschen Prinzipien

### Trägheitsprinzip

Körper ohne Krafteinwirkung führen gleichförmige Bewegungen aus oder bleiben in Ruhe

### Aktionsprinzip

Die Verknüpfung von Kinematik und Kräften

$$F=m\cdot a$$

Daraus folgt auch:

$$\vec{F}\cdot\Delta t=m\cdot\Delta v$$

### Wechselwirkungsprinzip

Actio gleich reactio. 

## Impuls

Der Impuls wird wie folgt definiert:

$$\vec{p}=m\cdot \vec{v}$$

Es gilt zusätzlich die Impulserhaltung:

$$\sum p_{\textrm{vorher}} = \sum p_{\textrm{nachher}}$$

## Arbeit, Energie und Leistung

### Arbeit

Die Arbeit $W$ wird wie folgt definiert:

$$W=F\cdot \Delta x$$

### Energie

Die Definitionen der Energien folgen aus Umformungen der Arbeit.

#### Kinetische Energie

$$E_{\textrm{kin}}=\frac{m}{2}v^2$$

Daraus folgt der Energiesatz:

$$W_{\textrm{tot}}=F_{\textrm{res,x}}\cdot\Delta x=E_{\textrm{kin,Ende}}-E_{\textrm{kin,Anfang}}=\frac{m}{2}v_{\textrm{x,Ende}}^2-\frac{m}{2}v_{\textrm{x,Anfang}}^2$$

Wichtig für z. B. Bremsweg, weil sie auch mit Reibung gilt.

Bei elastischen Stössen bleibt zudem die kinetische Energie erhalten.

#### Potenzielle Energie

$$E_{\textrm{pot}}=F\cdot h=m\cdot g\cdot h$$

#### Deformationsenergie

$$E_{\textrm{D}}=\frac{D}{2}x^2$$

#### Energieerhaltung

Gilt nur, wenn keine Reibung im Spiel ist:

$$\sum E_{\textrm{vorher}} =\sum E_{\textrm{nachher}}$$

### Leistung

Für die Leistung $P$ gilt:

$$P=\frac{W}{t}=\frac{E}{t}$$

### Wirkungsgrad

Für den Wirkungsgrad $\eta$ gilt:

$$\eta=\frac{E_{\textrm{nützlich}}}{E_{\textrm{aufgewandt}}}=\frac{P_{\textrm{nützlich}}}{P_{\textrm{aufgewandt}}}$$

## Kreisbewegung

Die Winkelgeschwindigkeit $\omega$ wird als zurückgelegte Winkel $\Delta\varphi$ (in Bogenmass) pro Zeiteinheit $\Delta t$ definiert:

$$\omega=\frac{\Delta\varphi}{\Delta t}$$

Für die Geschwindigkeit $v$ über Strecke $s$ gilt dann:

$$v=\frac{\Delta s}{\Delta t}=r\cdot \frac{\Delta\varphi}{\Delta t}=r\cdot\omega$$

Die Periode $T$ hat:

$$T=\frac{2\pi}{\omega}$$

Und die Frequenz $f$ hat:

$$f=\frac{1}{T}$$

Für die resultierende Kraft in radialer Richtung gilt:

$$F_{\textrm{res,rad}}=m\cdot a_{\textrm{rad}}=m\cdot\frac{v^2}{r}$$

