# Exponentielles Wachstum und Logarithmus

## Allgemein

Der Logarithmus $\log_{b}(x)$ ist die Umkehrfunktion zu $b^x$. D. h.:

$$x=\log_{b}(b^x)=b^{\log_{b}(x)}$$

Für $\log_{b}(x)$ gilt $\mathbb{W}=\mathbb{R}^{+}$, $\mathbb{D}=\mathbb{R}$ und für die Basis $b$ sind nur Werte aus $]0;\infty[\setminus\{1\}$ erlaubt, weil nur diese zu stetigen Funktionen führen.

Folgende Abkürzungen werden oft verwendet:

$$\begin{align}
  \log_{10}(x)=\lg(x)\\
  \log_{e}(x)=\ln(x)
\end{align}$$

## Logarithmusgesetze

$$\begin{align}
  &\textrm{I.}\:\log_{b}(m\cdot n)=\log_{b}(m)+\log_{b}(n)\\
  &\textrm{II.}\:\log_{b}\left(\frac{m}{n}\right)=\log_{b}(m)-\log_{b}(n)\\
  &\textrm{III.}\:\log_{b}(m^n)=n\cdot\log_{b}(m)\\
  &\textrm{IV.}\:\log_{b}(c)=\frac{\log_{a}(c)}{\log_{a}(b)}\\
\end{align}$$

## Prozentrechnen

Es sei $A(0)$ der Anfangsbetrag/bestand, $p$ der prozentuale Wachstum pro Zeiteinheit und $b=1+p$ der Wachstumsfaktor. Für den Betrag $A(t)$ nach $t$ Zeit gilt:

$$A(t)=A(0)\cdot(p+1)^t=A(0)\cdot b^t$$

In den Naturwissenschaften (z. B. für Halbwertszeit) schreibt man es als $e^x$-Funktion mit $k=\ln(b)$:

$$N(t)=N(0)\cdot e^{\ln(b)t} = N(0)\cdot e^{kt}$$