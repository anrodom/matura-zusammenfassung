# Kombinatorik

## Menge vs. Tupel

Bei Mengen spielt die Reihenfolge **keine** Rolle

$$\{a_1, a_2, a_3\}=\{a_3, a_2, a_1\}$$

Bei Tupeln spielt die Reihenfolge **eine** Rolle

$$(a_1, a_2, a_3)\neq(a_3, a_2, a_1)$$

## Tupel mit und ohne Wiederholung der Elemente

Tupel berechnet man allgemein mit dem Produktsatz. Man multipliziert also die Anzahl Möglichkeiten pro Position. Achten muss man dabei aber ob sich die Elemente wiederholen können (Bsp. 3-stellige Zahlen: $(3, 8, 8)=9\cdot10\cdot10=900$) oder nicht (Bsp. Schlussranglisten bei 5 Personen: $(D,C,A,B,E)=5\cdot4\cdot3\cdot2\cdot1=120$)

> Spezialfall Personen an rundem Tisch:
>
> Wenn Sitzordnungen mit gleichen Nachbaren als Duplikate gezählt werden, muss man noch durch die Wiederholungen teilen. Bei 5 Personen $(A, B, C, D, E)$ gibt es wieder $5\cdot4\cdot3\cdot2\cdot1=120$ Fälle. Allerdings müssen die 5 Rotationen um den Tisch und das Spiegeln des Tisches beachtet werden. Es gilt also für die Anzahl der Sitzordnungen $\frac{120}{5\cdot2}=12$. Oder allgemein für n Personen $\frac{(n-1)!}{2}$ (Für Fakultät siehe nächstes Kapitel).

## Fakultät

Bei z. B. Schlussranglisten mit mehr als 5 Personen wird die Berechnung mühsam. Deswegen gibt es aber Fakultäten:

$$n! = \prod_{k=1}^n k$$

Man schreibt also $5! = 5\cdot4\cdot3\cdot2\cdot1 = 120$

## n tief k

### Mengenaufgaben

Bei Mengen zählt man normalerweise die Tupel und dividiert aufgrund der Unbedeutsamkeit der Reihenfolge durch die Anzahl Duplikate. Bei 4-Mengen von 7 Personen: $\frac{7\cdot6\cdot5\cdot4}{4\cdot3\cdot2\cdot1}=35$.

### Definition

Auch das ist aufwendig aufzuschreiben (selbst mit Fakultäten) also definiert man "n tief k":

$$\frac{n(n-1)...(n-k+1)}{k!}=\frac{n!}{k!(n-k)!}={n\choose k}$$

### Bei Tupelaufgaben

Sobald Positionen auf Tupeln ins Spiel kommen, verwendet man auch ${n\choose k}$.

Bsp. Kawasaki-Problem: Anzahl neuer Wörter (Permutationen). Man hat das Tupel $(K,K,W,A,S,A,I,A)$ also 2 $K$ und 3 $A$ die sich wiederholen. Man schaut sich also zuerst an, wie viele Positionen man den beiden $K$ zuordnen kann ${8\choose 2}$. Das gleiche für die $A$ und den übrig gebliebenen Positionen ${6\choose 3}$. Schliesslich bleiben noch $3!$ für den Rest übrig. Insgesamt also ${8\choose 2}{6\choose 3}3! = 3360$

## Gesetze zu n tief k

Wichtig für grosse $n$:

$${n\choose k}={n\choose n-k}$$

Weiter:

$${n\choose k} + {n\choose k+1} = {n+1\choose k+1}$$

## Kombinatorik und das Pascaldreieck

Bei z. B. $(a+b)^5 = (a+b)(a+b)(a+b)(a+b)(a+b)$ findet man $a^3b^2$ 10-mal vor, was ${5\choose 3}$ bzw. ${5\choose 2}$ entspricht. Mit anderen Worten 3 Klammer aus denen man $a$ nimmt und 2 mit $b$.

Demnach gilt für $n\in\mathbb{N}$:

$$(a+b)^n = \sum_{k=0}^{n}{n\choose k}a^kb^{n-k}$$

## Kombinatorik und e

### e als Summe

$$\begin{align}
  e&=\lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n\\
  &=\lim_{n\to\infty}\sum_{k=0}^{n}{n\choose k}\left(\frac{1}{n}\right)^k1^{n-k}\\
  &=\lim_{n\to\infty}\sum_{k=0}^{n}\frac{n(n-1)...(n-k+1)}{k!}\frac{1}{n^k}\\
  &=\sum_{k=0}^{\infty}\frac{1}{k!}
\end{align}$$

### e ist irrational

Aus dem Vorherigen folgt:

$$\begin{align}
  \frac{1}{0!}+\frac{1}{1!}+...+\frac{1}{n!}&<e=\frac{1}{0!}+\frac{1}{1!}+...+\frac{1}{n!}+\frac{1}{(n+1)!}+\frac{1}{(n+2)!}+...\\
  \frac{1}{0!}+\frac{1}{1!}+...+\frac{1}{n!}&<e=\frac{1}{0!}+\frac{1}{1!}+...+\frac{1}{n!}+\frac{1}{n!}\left[\frac{1}{n+1}+\frac{1}{(n+1)(n+2)}+...\right]\\
  \frac{1}{0!}+\frac{1}{1!}+...+\frac{1}{n!}&<e<\frac{1}{0!}+\frac{1}{1!}+...+\frac{1}{n!}+\frac{1}{n!}\left[\frac{1}{2}+\frac{1}{4}+...\right]\\
  \frac{1}{0!}+\frac{1}{1!}+...+\frac{1}{n!}&<e<\frac{1}{0!}+\frac{1}{1!}+...+\frac{1}{n!}+\frac{1}{n!}[1]\\
  \frac{1}{0!}+\frac{1}{1!}+...+\frac{1}{n!}+\frac{0}{n!}&<e<\frac{1}{0!}+\frac{1}{1!}+...+\frac{1}{n!}+\frac{1}{n!}\\
\end{align}$$

Für $e$ gilt also mit $0<\lambda<1$:

$$e=\frac{1}{0!}+\frac{1}{1!}+...+\frac{1}{n!}+\frac{\lambda}{n!}$$

Wenn $e=\frac{p}{q}$ mit $p,q\in\mathbb{N}$:

$$\frac{p}{q}=\frac{1}{0!}+\frac{1}{1!}+...+\frac{1}{n!}+\frac{\lambda}{n!}$$

Wählt man nun $n=q$ und multipliziert mit $q!$:

$$[p(q-1)!]=[q! + q! + ... + 1] + \lambda$$

Das ist ein Widerspruch, da es sich bei den Zahlen in $[...]$ um ganze Zahlen handelt und für $\lambda$ zwingend $0<\lambda<1$ gilt!


## Neue Binomialkoeffizienten

Aus der Tatsache, dass in z. B. $(a+b)^{\frac{1}{2}} = \sqrt{a+b}$ auch rationale Zahlen eingesetzt werden können, müssen auch rationale Werte für $n$ in ${n\choose k}$ Sinn ergeben:

$$\begin{align}
  {\frac{1}{2}\choose 0}&=1\\
  {\frac{1}{2}\choose 1}&=\frac{1}{2}\\
  {\frac{1}{2}\choose 2}&=\frac{\frac{1}{2}\cdot(-\frac{1}{2})}{2!}=-\frac{1}{8}\\
  {\frac{1}{2}\choose 3}&=\frac{\frac{1}{2}\cdot(-\frac{1}{2})\cdot(-\frac{3}{2})}{3!}=\frac{1}{16}\\
\end{align}$$


## Merkregel Kombinatorik

*  Spielt Reihenfolge eine Rolle?
    *  **Ja** --> Tupel
        *  Produktsatz
        *  Dürfen Elemente mehrmals vorkommen?
            *  **Ja** --> Zähle mit $k\cdot k\cdot k\cdot...$
            *  **Nein** --> Zähle mit $k\cdot(k-1)\cdot(k-2)\cdot...$
        *  Spezialfall Positionen auf Tupel --> ${n\choose k}$
    *  **Nein** --> Mengen
        *  Zähle mit ${n\choose k}$