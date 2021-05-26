# Integrations-Methoden

Anfänglich reichen die umgekehrten Ableitungsregeln. Es gibt aber oft kompliziertere Integrale, die andere Methoden verlangen. 

## Substitutions-Methode

Wenn die innere Ableitung bis auf einen Faktor gegeben ist, dann kann man $u$ substituieren, so dass $u'=\frac{du}{dx}$ gilt:

$$\int f(u)\cdot u'\,dx=\int f(u)\,du$$

Bei der Substitution eines bestimmten Integrals ändern sich die Grenzen, weswegen man entweder unbestimmt nach $u$ integriert und dann wieder zurück substituiert oder die Grenzen für $u$ neu berechnet.

Falls bei einem Integral der Faktor nicht ersichtlich ist, dann kann man auch aktiv substituieren. Beispiel für $\int\frac{1}{\sqrt{1-x^2}}\,dx$ mit $x=\sin(t)$ und $\frac{dx}{dt}=\cos(t)$:

$$\begin{align}
	\int\frac{1}{\sqrt{1-x^2}}\,dx&=\int\frac{1}{\sqrt{1-\sin(t)^2}}\cos(t)\,dt\\
	&=\int\frac{1}{\cos(t)}\cos(t)\,dt\\
	&=\int 1\,dt\\
	&=t+C\\
	&=\arcsin(x)+C
\end{align}$$

## Partialbruchzerlegung

### Allgemein

Die Partialbruchzerlegung wird bei Funktionen $f(x)=\frac{P(x)}{Q(x)}$ angewandt. Nach folgendem Schema wird vorgegangen:

2.	Wenn der Zähler $P(x)$ einen gleichen oder höheren Grad als der Nenner $Q(x)$ hat, dann muss zuerst die Polynomdivision angewandt werden. Für die nächsten Schritte wird dann nur der entstanden Rest $R$ (der auch ein Bruch sein wird) verwendet. ($P(x):Q(x)=a_0x^n+a_1x^{n-1}+...+R$)
2.	Nun müssen $P(x)$ und $Q(x)$ als Nullstellen aufgeschrieben werden . ($(x+2)(x+3)$ statt $x^2+5x+6$)
3.	Das Ziel ist diesen Bruch als eine Summe von Brüchen pro Nullstelle aufzuschreiben. ($\frac{x+2}{(x+2)(x+3)}=\frac{A}{x+1}+\frac{B}{x+3}$)
4.	Achtung bei doppelten Nullstellen wie $(x+2)^2$. N-fache Nullstellen sind für sich selbst Summen von Brüchen $\sum_{k=1}^n\frac{A_k}{(x-x_k)^n}$. (Im Fall $\frac{1}{(x+2)^2}$ also $\frac{1}{(x+2)^2}=\frac{A_1}{x+2}+\frac{A_2}{(x+2)^2}$)
5.	Die Gleichung wird nun so umgeformt, dass ein Koeffizientenvergleich auf die gesuchten $A_n$ führt. (Mit z. B. dem Bruch aus 3: $x+1=(A+B)x+3A+B$ mit $A+B=1$ und $3A+B=2$)
6.	Anschliessend integriert man alle entstandenen Glieder (die aus der Polynomdivision falls vorhanden nicht vergessen!). Man kann sich zusätzlich merken, dass aus z. B. $\frac{A_1}{x+2}$ nach dem Integrieren $A_1\ln(x+2)$ wird.

### Beispiel 

Gesucht sei $\int\frac{1+x^3}{x^3-4x^2+4x}\,dx$ :

1. Sowohl im Nenner als auch im Zähler haben wir $x^3\Rightarrow$ Polynomdivision: $(1+x^3):(x^3-4x^2+4x)=1+\frac{4x^2-4x+1}{x^3-4x^2+4x}$
2. $x^3-4x^2+4x=x(x-2)^2$
3. Doppelte Nullstellen! $\frac{4x^2-4x+1}{x(x-2)^2}=\frac{A}{x}+\frac{B}{x-2}+\frac{C}{(x-2)^2}$
4. Das ergibt folgende Gleichung $4x^2-4x+1=(A+B)x^2+(C-4A-2B)x+4A$ mit

$$\begin{align}
	\textrm{I.}\;\;\;\;\;\,4&=A+B\\
	\textrm{II.}-4&=C-4A-2B\\
	\textrm{III.}\;\;\;1&=4A\\
	&\Downarrow\\
	A&=\frac{1}{4}\\
	B&=\frac{15}{4}\\
	C&=\frac{9}{2}
\end{align}$$

Wir haben nun also folgendes Integral:

$$\int 1+\frac{\frac{1}{4}}{x}+\frac{\frac{15}{4}}{x-2}+\frac{\frac{9}{2}}{(x-2)^2}\,dx=x+\frac{1}{4}\ln(x)+\frac{15}{4}\ln(x-2)-\frac{9}{2(x-2)}+C$$

## Partielle Integration

Die Idee zur partiellen Integration folgt aus der umgekehrten Produktregel:

$$\begin{align}
	[u(x)\cdot v(x)]'&=u'(x)v(x)+u(x)v'(x)\\
	u(x)v(x)&=\int u'(x)v(x)\,dx+\int u(x)v'(x)\,dx
\end{align}$$

Die Hoffnung ist also aus einem nicht-integrierbarem Produkt ein integrierbares herauszubekommen:

$$\int u'v\,dx=uv-\int uv'\,dx$$

Oder bei bei bestimmten Integralen:

$$\int_a^b u'v\,dx=uv\left|_a^b\right.-\int_a^b uv'\,dx$$

## Die Euler-Gamma-Funktion

### Behauptung

Für die Gamma-Funktion $\Gamma(n)=\int_0^{\infty}t^{n-1}e^{-t}\,dt$ soll gelten:

$$\Gamma(n)=(n-1)!$$

Mit folgender rekursiver Definition:

$$\Gamma(n)=(n-1)\Gamma(n-1)$$

### Beweis

Verankerung:

$$\begin{align}
	\Gamma(1)&\stackrel{?}{=}0!\\
	\int_0^{\infty}t^{1-1}e^{-t}\,dt&\stackrel{?}{=}0!\\
	\int_0^{\infty}e^{-t}\,dt&\stackrel{?}{=}0!\\
	-e^{-t}\left|_{0}^{\infty}\right.&\stackrel{?}{=}1\\
	1&=1
\end{align}$$

Voraussetzung:

$$\Gamma(k)=(k-1)!$$

Zu Zeigen:

$$\begin{align}
	\Gamma(k+1)&=k!\\
	\Gamma(k+1)&=k\cdot (k-1)!\\
	\Gamma(k+1)&=k\cdot\Gamma(k)\;\textrm{(Rek. Def.)}
\end{align}$$

