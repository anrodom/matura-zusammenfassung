# Physik mit Differential- und Integralrechnung
## Kinematik

Die Position eines Körpers als Vektor $\vec{r}$:

$$\vec{r}=\left(\begin{array}{c}x(t)\\y(t)\\z(t) \end{array}\right)$$

Für die Geschwindigkeit $\vec{v}$ und die Beschleunigung $\vec{a}$ folgen demnach:

$$\vec{v}=\left(\begin{array}{c}\dot{x}\\\dot{y}\\\dot{z} \end{array}\right)={\vec{r}'}$$

$$\vec{a}=\left(\begin{array}{c}\ddot{x}\\\ddot{y}\\\ddot{z} \end{array}\right)={\vec{r}''}$$

## Verknüpfung mit Kräften: Dynamik

Für das 2te Newton'sche Prinzip:

$$\vec{F}_{res}=m\cdot\vec{a}=m\cdot{\vec{r}''}$$

Wenn also z. B. $m$ und $\vec{F}_{res}$ gegeben sind, können $\vec{a}(t)$, $\vec{v}(t)$ und $\vec{r}(t)$ wie folgt berechnet werden:

$$\vec{a}=\frac{\vec{F}_{res}}{m}$$

$$\vec{v}(t)=\int \vec{a}(t) \,dt$$

$$\vec{r}(t)=\int \vec{v}(t) \,dt$$

Am Beispiel des Freien Falls mit $\vec{G}=m\cdot\vec{a}$ gilt demnach:

$$z(t)=-\frac{g}{2}t^2+v_0t+z_0$$

Wobei es sich bei $v_0$ und $z_0$ um die jeweiligen Integrationskonstanten handelt.

## Arbeit einer Kraft

Erinnerung: $W$ = "Kraft mal Weg" = "Kraftkomponente parallel zum Weg mal Weg", wenn die Kraft konstant ist. Sonst handelt es sich beim $W$ um eine Fläche (also einem Integral).

Einige Beispiele:

- Feder

$$W=\int_{0}^{x_0} Dx \,dx=\frac{D}{2}x^2$$

- Masse $m$ von Höhe $x_1$ auf $x_2$

$$W=\int_{x_1}^{x_2} mg \,dx=mg(x_2-x_1)$$

- Masse $m$ von Erdoberfläche auf Distanz $d$

$$W=\int_{r_E}^{d} G\cdot\frac{m_E\cdot m}{x^2} \,dx=G\cdot m_E\cdot m(\frac{1}{r_E}-\frac{1}{d})$$

> ### Exkurs Fluchtgeschwindigkeit
> Die Geschwindigkeit, die nötig ist, um dem Gravitationsfeld von der Oberfläche antriebslos zu entkommen. Man setzt also $E_{kin}$ dem Einfluss des Gravitationsfeld von der Oberfläche zu $\infty$:
>
> $$\int_{r_E}^{\infty} G\cdot\frac{m_E\cdot m}{x^2} \,dx$$
>
> Für $v_{Flucht}$ folgt also:
>
> $$v_{Flucht}=\sqrt{\frac{2Gm_E}{r_E}}$$
>
> Sobald man von $v=c$ ausgeht, nennt man den Radius $R_S$ Schwarzschildradius, dem Ereignishorizont eines schwarzen Loches.

- Coulombkraft $F_C=\frac{1}{4\pi\varepsilon_0}\cdot\frac{Q_1\cdot Q_2}{x^2}$ über den Weg des Protons

$$W=\int_{\infty}^{d} F_C \,dx$$

## Induktion

$$U_{ind}(t)=-\frac{d\phi}{dt}=-\frac{d[A(t)\cdot B(t)\cdot \cos(\alpha(t))]}{dt}$$