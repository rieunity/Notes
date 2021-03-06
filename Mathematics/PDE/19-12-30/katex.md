Second-order Elliptic Equations
===============================

Define the partial differential operator $L$ to be
$$Lu=-\sum_{i,j=1}^{n}a^{ij}(x)u_{x_ix_j}+\sum_{i=1}^{n} b^{i}(x)u_{x_i}+c(x)u.$$

We say $L$ is (uniformly) elliptic if there exists a constant $\theta>0$ such that
$$\sum_{i,j=1}^{n}a^{ij}(x)\xi_i\xi_j\ge \theta \left| \xi \right|^2 \label{uec}$$
for a.e. $x\in U$ and all $\xi \in \R^{n}$.

Maximum Principle
=================

Weak Maximum Principle
----------------------

In this case, we assume that $a^{ij},b^{i},c$ are bounded, continuous and the uniform ellipticity condition (\[uec\]) holds.

The maximum principle we talk about here is the classical condition.

\[Weak maximum principle\]
Assume $u\in C^2(U)\cap C(\overline{U})$ and
$$c\equiv 0 \text{ in } U$$

1.  If
    $$Lu\le 0 \text{ in }U,\label{3}$$
    then
    $$\max_{\overline{U}}u=\max_{\partial U}u.$$

2.  If
    $$Lu\ge 0 \text{ in }U,$$
    then
    $$\min_{\overline{U}}u=\min_{\partial U}u.$$

\[theorem1\]

1\. Suppose we have the strict inequality
$$Lu<0 \text{ in }U,$$
and there is a point $x_0\in U$ such that
$$u(x_0)=\max_{\overline{U}}u.$$
At this maximum point $x_0$, we have
$$Du(x_0)=0\label{7}$$
and
$$D^2u(x_0)\le 0.\label{less}$$
Since the matrix $A=\left( a^{ij}(x_0) \right) $ is symmetric and positive definite, there exists
an orthognal matrix $O=\left( o_{ij} \right) $ so that
$$OAO^{T}=\text{diag}\left( d_1,\cdots,d_n \right) , \quad O O^{T}=1,$$
with $d_k>0$ $\left( k=1,\cdots,n \right) $. Write $y=x_0+O(x-x_0)$. Then $x-x_0=O^{T}(y-x_0)$, and so
$$u_{x_i}=\sum_{k=1}^{n} u_{y_k}O_{ki}, u_{x_ix_j}=\sum_{k,l=1}^{n}u_{y_ky_l}O_{ki}O_{lj}\quad \left( i,j=1,\cdots,n \right).$$
Hence at the point $x_0$,
$$\begin{aligned}
  \sum_{i,j=1}^{n}a^{ij}u_{x_ix_j}=&\sum_{k,l=1}^{n} \sum_{i,j=1}^{n} a^{ij}u_{y_ky_l}o_{ki}o_{lj}\notag\\
  =& \sum_{k=1}^{n} d_ku_{y_ky_k}\le 0 \quad\text{ by (\ref{less})}\label{10}
.\end{aligned}$$
Thus at $x_0$
$$Lu=-\sum_{i,j=1}^{n} a^{ij}u_{x_ix_j}+\sum_{i=1}^{n} b^{i}u_{x_i}\ge 0$$
in light of (\[7\]) and (\[10\]). So we have a contradiction.
2. In general case that (ref<span>3</span>) holds, write
$$u^{\epsilon}(x):=u(x)+\epsilon e^{\lambda x_1} (x\in  U),$$
where $\lambda>0$ will be selected below and $\epsilon>0$. The uniform condition implies $a^{ii}(x)\ge \theta$ $i=1,\cdots,n,x\in U$. Therefore
$$\begin{aligned}
  Lu^{\epsilon }=&Lu+\epsilon L\left( e^{\lambda x_1} \right) \\
  \le & \epsilon e^{\lambda x_1}\left( -\lambda^2a^{11}+\lambda b^{1} \right) \\
  \le& \epsilon e^{\lambda x_1}\left( -\lambda^2\theta+\|\mathbf{b}\|_{L^{\infty}}\lambda \right)\\
  <&0\quad \text{ in }U,
.\end{aligned}$$
provided we choose $\lambda>0$ sufficiently large. Then according step 1 above and let $\epsilon \to 0$ we get $\max_{\overline{U}}u=\max_{\partial U}u$.

\[Weak maximum principle for $c\ge 0$\]
Assume $u\in C^2(U)\cap C(\overline{U})$ and
$$c\ge 0 \text{ in }U.$$

1.  If
    $$Lu\le 0 \text{ in }U,$$
    then
    $$\max_{\overline{U}}\le \max_{\partial U}u^{+}.\label{11}$$

2.  Likewise, if
    $$Lu\ge 0 \text{ in }U,$$
    then
    $$\min_{\overline{U}}\ge -\max_{\partial U}u^-.$$

\[theorem2\]

1\. Let $u$ ve a subsolution and set $V:=\left\{ x\in U \lvert u(x)>0 \right\} $. Then
$$Ku:=Lu-cu\le -cu\le 0 \quad \text{ in }V.$$
The operator $K$ has no zeroth=order term and consequently Theorem \[theorem1\] implies $\max_{\overline{V}}u=\max_{\partial V}u=\max_{\partial U}u^+$. This gives (\[11\]) in the case that $V\neq \empty$. Otherwise $u\le 0$ everywhere in $U$,and (\[11\]) likewise follows.

2\. Assertion b follows from a applied to $-u$, once we observe that $\left( -u \right) ^+=u^-$.

Strong Maximum Principle
------------------------

\[Hopf’s Lemma\]
Assume $u\in C^{2}(U)\cap C^1(\overline{U})$ and
$$c\equiv 0 \text{ in } U.$$
Suppose further
$$Lu\le 0 \text{ in }U$$
and there exists a point $x^{0}\in \partial U$ such that
$$u(x^0)>u(x)\text{ for all }x\in U.$$
Assume finially that $U$ satisfies the interior ball condition at $x^{0}$ ; that is, there exists an open ball $B\subset U$ with $x^{0}\in \partial B$.

1.  Then
    $$\frac{\partial u}{\partial \nu} (x^{0})>0,$$
    where $\nu$ is the outer unit normal to $B$ at $x^{0}$.

2.  If
    $$c\ge 0 \text{ in }U$$
    the same conclusion holds provided
    $$u(x^{0})\ge 0.$$

1\. Assume $c\ge 0$ and $B=B^{0}(0,r)$ for some radius $r>0$. Define
$$v(x):=e^{-\lambda\left| x \right| ^{2}}-e^{-\lambda r^{2}}\quad  \left( x\in B\left( 0,r \right)  \right)$$
for $\lambda>0$ as selected below. Then using the uniform condition, we compute
$$\begin{aligned}
  Lv=&-\sum_{i,j=1}^{n} a^{ij}v_{x_ix_j}+\sum_{i=1}^{n} b^iv_{x_i}=cv\\
  =& e^{-\lambda \left| x \right| ^{2}}\sum_{i,j=1}^{n} a^{ij}\left( -4\lambda^{2}x_ix_j+2\lambda \delta_{ij} \right) \\
  -& e^{-\lambda \left| x \right| ^2}\sum_{i=1}^{n} b^{i}2\lambda x_i +c\left( e^{-\lambda \left| x \right| ^{2}}-e^{-\lambda r^{2}} \right) \\
  \le  & e^{-\lambda \left| x \right| ^{2}}\left( -4\theta \lambda^2\left| x \right| ^2+2\lambda \text{tr}A+2\lambda \left| b \right| \left| x \right| +c \right) ,\end{aligned}$$
for $A=\left( a_{ij} \right) $, $b=\left( b^{1},\cdots,b^{n} \right) $. Consider next the open annular region $R:=B^{0}\left( 0,r \right) -B\left( 0,\frac{r}{2} \right) $. We have
$$Lv\le 0\label{15}$$
in $R$, provided $\lambda$ is large enough.
2. In view of $u(x^{0})>u(x)$ for all $x\in U$, there exists a constant $\epsilon >0$ so small that
$$u(x^{0})\ge u(x)+\epsilon v(x)\quad \left( x\in \partial B(0,\frac{r}{2} \right) .\label{16}$$
In addition note
$$u(x^{0})\ge u(x)+\epsilon v(x)\quad\left( x\in \partial B(0,r) \right) ,\label{17}$$
since $v\equiv 0$ on $\partial B(0,r)$.

3\. From (\[15\]) we see
$$L\left( u+\epsilon v-u(x^{0}) \right) \le -cu(x^{0})\le 0 \quad \text{ in }R,$$
and from (\[16\]), (\[17\]) we observe
$$u+\epsilon v-u(x^{0})\le 0\quad \text{ in }\partial R,$$
In view of the weak maximum principle, Theorem \[theorem2\], we get $u+\epsilon v-u(x^{0})\le 0$ in $R$. But $u(x^{0})+\epsilon v(x^{0})-u(x^{0})=0$, and so
$$\frac{\partial u}{\partial \nu} (x^{0})+\epsilon \frac{\partial v}{\partial \nu} (x^{0})\ge 0.$$
Consequently
$$\frac{\partial u}{\partial \nu} \left( x^{0} \right) \ge -\epsilon  \frac{\partial v}{\partial \nu} \left( x^{0} \right) =-\frac{\epsilon }{r}Dv(x^{0})\cdot x^{0}=2\lambda \epsilon re^{-\lambda r^{2}}>0,$$
as required.

\[Strong maximum principle\]
Assume $u\in C^2\left( U \right) \cap C\left( \overline{U} \right) $ and
$$c\equiv 0 \quad \text {in }U.$$
Suppose also $U$ is connected, open and bounded.

1.  If
    $$Lu\le 0 \quad \text{ in }U$$
    and $u$ attains its minimum over $\overline{U}$ at an interior point, thenm $u$ is constant within $U$.

2.  Similarly, if
    $$Lu\ge 0\quad \text{ in }U$$
    and $u$ attains its minimum over $\overline{U}$ at an interior point, then $u$ is constant within $U$.

Write $M:=\max_{\overline{U}}u$ and $C:=\left\{ x\in U\lvert u(x)=M \right\} $. Then if $u\not\equiv M$, set
$$V:=\left\{ x\in U\lvert u(x)<M \right\} .$$
Choose a point $y\in V$ satisfying $\text{dist}\left( y,C \right) <\text{dist}\left( y,\partial U \right) $, and let $B$ denote the largest ball with center $y$ whose interior lies in $V$. Then there exists some point $x^{0}\in C$, with $x^{0}\in \partial B$. Clearly $V$ satisfies the interior ball condition at $x^{0}$, whence Hopf’s Lemma (a) implies
$$\frac{\partial u}{\partial \nu} \left( x^{0} \right) >0.$$
But this is a contradiction: since $u$ attains its maximum at $x^{0}\in U$, we have $Du(x^{0})=0$.

Similarly, we have the $c\ge 0$ version of the strong maximum principle, and the proof is like the above.

\[Strong maximum principle with $c\ge 0$\]
Assume $u\in C^{2}\left( U \right) \cap C\left( \overline{U} \right) $ and
$$c\ge 0 \quad \text{ in } U.$$
Suppose also $U$ is connect.

1.  If
    $$Lu\le 0 \quad \text{ in }U$$
    and $u$ attains a nonnegative maximum over $\overline{U}$ at an interior point, then u is constant with $U$.

2.  Similarly, if
    $$Lu\ge 0\quad \text{ in }U$$
    and $u$ attains a nonpositive minimum over $\overline{U}$ at an interior point, then $u$ is constant within $U$.


