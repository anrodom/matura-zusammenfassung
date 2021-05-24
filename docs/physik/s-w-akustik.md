# Schwingungen und Wellen, Akustik

## Schwingungen

### Allgemein

Schwingungen entstehen, wenn eine rücktreibende Kraft vorhanden ist. Bei aperiodischen Schwingungen wiederholt sich der Vorgang nicht. Bei periodischen Schwingungen hingegen schon. Beschrieben werden diese mit der Zeit $T$ zwischen zwei Wiederholungen und der Anzahl Schwingungen pro Sekund bzw. Frequenz $f$:

$$f=\frac{1}{T}$$

Bei echt periodischen Schwingungen bleibt die maximale Auslenkung also Amplitude konstant, es geht keine Energie verloren und man spricht von ungedämpften Schwingungen. Falls die Auslenkung mit Hilfe von $\sin$ und $\cos$ beschrieben werden kann, die rücktreibende Kraft proportional zur Auslenkung ist, spricht man von harmonischen Schwingungen

### Mathematische Beschreibung

#### Allgemein

Schwingungen lassen sich als Kreisbewegungen projizieren. Es gibt also eine Winkelgeschwindigkeit $\omega=2\pi\cdot f$ des Winkels $\varphi$ und der Radius entspricht der Amplitude $x_0$:

$$\begin{align}
	x(t)&=x_0\cdot\sin(\omega\cdot t)\\
	v_x(t)=x'(t)&=x_0\cdot\omega\cdot\sin(\omega\cdot t)&&(\textrm{Geschwindigkeitsamplitude:}\,x_0\cdot\omega)\\
	a_x(t)=x''(t)&=-x_0\cdot\omega^2\cdot\sin(\omega\cdot t)=-\omega^2\cdot x(t)&&(\textrm{Beschleunigungsamplitude:}\,x_0\cdot\omega^2)\\
	F_{\textrm{res}}&=-m\cdot\omega^2\cdot x(t)
\end{align}$$

#### Das Fadenpendel

Für die Position $x(t)$ auf der Kreislinie mit Länge $l$ des Fadens gilt:

$$x(t)=\varphi(t)\cdot l$$

mit 

$$\varphi(t)=\varphi_0\cdot\sin(\omega\cdot t)$$

Geschwindigkeit und Beschleunigung können dementsprechend berechnet werden. Nehmen wir jetzt als rücktreibende Kraft die Gravitation ergibt sich:

$$\begin{align}
	-G\cdot\sin(\varphi(t))&=m\cdot a_x(t)\\
	-m\cdot g\cdot\sin(\varphi(t))&=m\cdot l\cdot \varphi''(t)\\
	\varphi''(t)&=\frac{g}{l}\cdot\sin(\varphi(t))\\
	\varphi''(t)&\approx\frac{g}{l}\cdot\varphi(t)
\end{align}$$

Für die Winkelgeschwindigkeit $\omega$ eines Fadenpendels gilt für kleine Winkel ($\sin(\varphi(t)))\approx\varphi(t)$:

$$\omega=\sqrt{\frac{g}{l}}$$

#### Das Federpendel

Beim Federpendel ist die Federkraft die rücktreibende Kraft:

$$\begin{align}
	-D\cdot x(t)&=m\cdot a_x(t)\\
	x''(t)&=-\frac{D}{m}\cdot x(t)
\end{align}$$

Für die Winkelgeschwindigkeit $\omega$ eines Federpendels gilt:

$$\omega=\sqrt{\frac{D}{m}}$$

### Resonanz

Die Amplitude bleibt aufgrund von Energieverlusten normalerweise nicht konstant, sondern sie wird abgedämpft. Will man, dass sie das bleibt, muss periodisch Energie hinzugefügt werden (Z. B. Anstossen Schaukel). Die Amplitude bleibt also konstant, weil die Energiezufuhr dem Energieverlust entspricht. Sie hängt von der Anregungsfrequenz und der Eigenfrequenz ab und ist am grössten, wenn diese übereinstimmen. Man spricht dann von Resonanz.


## Wellen

### Allgemein

### Harmonische Wellen

### Schwebungen

### Überlagerung und Interferenz



## Akustik

