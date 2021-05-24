# Die Gerade im Raum

## Parameterform von Geraden

Jeder Punkt $P$ auf einer Geraden kann durch eine Kombination eines Ortsvektor $\vec{a}$ (Vektor zu einem bekannten Punkt auf der Geraden) und einem Richtungsvektor $\vec{b}$ (Vektor, der in die Richtung der Geraden zeigt) beschrieben werden:

$$\begin{align}
  \vec{OP}&=\vec{a}+t\vec{b}\\
  \left(\begin{array}{c}P_x\\P_y\\P_z \end{array}\right)&=\left(\begin{array}{c}a_x\\a_y\\a_z \end{array}\right) + t\left(\begin{array}{c}b_x\\b_y\\b_z \end{array}\right)
\end{align}$$

## Spezielle Geraden

*  Gerade durch den Origo

$$\left(\begin{array}{c}P_x\\P_y\\P_z \end{array}\right)=\left(\begin{array}{c}0\\0\\0 \end{array}\right) + t\left(\begin{array}{c}b_x\\b_y\\b_z \end{array}\right)$$

*  In der xz-Ebene

$$\left(\begin{array}{c}P_x\\P_y\\P_z \end{array}\right)=\left(\begin{array}{c}a_x\\0\\a_z \end{array}\right) + t\left(\begin{array}{c}b_x\\0\\b_z \end{array}\right)$$

*  Parallel zur xz-Ebenen

$$\left(\begin{array}{c}P_x\\P_y\\P_z \end{array}\right)=\left(\begin{array}{c}a_x\\a_y\neq0\\a_z \end{array}\right) + t\left(\begin{array}{c}b_x\\0\\b_z \end{array}\right)$$


*  Schnittwinkel einer Gerade und einer Ebene wird in ["Die Ebene im Raum"](eImRaum.md) besprochen.
*  Schnittpunkte mit den xy-, yz- und xz-Ebenen werden Spurpunkte $G_1$, $G_2$ und $G_3$ genannt.

## Vorgehen zur Lage zweier Geraden

Gegeben seien Geraden $f: \vec{p} + t\vec{u}$ und $g: \vec{q} + s\vec{v}$

*  $\vec{u}$ und $\vec{v}$ kollinear?
    *  **Ja** --> Liegt $\vec{p}$ auf $g$?
        *  **Ja** --> $f=g$
        *  **Nein** --> $f||g$
    *  **Nein** --> Schneidet $f$ $g$?
        *  **Ja** --> $f$ schneidet $g$
        *  **Nein** --> windschief