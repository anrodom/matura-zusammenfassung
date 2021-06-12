# Beurteilende Statistik

## Grundgesamtheit

Eine unbekannte oder sehr grosse Grundgesamtheit hat einen unbekannten und abzuschätzenden Erwartungswert $\mu$ und eine Theoretische Standardabweichung $\sigma$:

$$\begin{align}
	\mu&=\frac{\sum_{i=1}^k x_i}{k}\\
	\sigma&=\sqrt{\frac{\sum_{i=1}^k (\mu-x_i)^2}{k}}
\end{align}$$

## Zufalsstichprobe

Eine Zufallsstrichprobe aus der Grundgesamtheit mit Umfang $n$ hat den Durchschnitt $\bar{x}$ und die empirische Standardabweichung $s$:

$$\begin{align}
	\bar{x}&=\frac{\sum_{i=1}^n x_i}{n}\\
	s&=\sqrt{\frac{\sum_{i=1}^n (\bar{x}-x_i)^2}{n-1}}
\end{align}$$

Diese Werte gelten als Abschätzungen zur Grundgesamtheit $\mu\approx\bar{x}$ und $\sigma\approx s$

## Unsicherheit bei der Zufalsstichprobe

Der Durchschnitt $\bar{x}$ der Stichprobe streut mit dem Standardfehler $s_n$:

$$s_n=\frac{s}{\sqrt{n}}$$

Eine besser Annäherung für den Erwartungswert ist also:

$$\mu\approx\bar{x}\pm s_n$$

Es gilt:

$$\begin{align}
	&\bar{x}\pm s_n &&(\textrm{68\% Sicherheit})\\
	&\bar{x}\pm 2s_n &&(\textrm{95\% Sicherheit})\\
	&\bar{x}\pm 3s_n &&(\textrm{99\% Sicherheit})
\end{align}$$

