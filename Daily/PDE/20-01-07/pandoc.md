Sobolev’s Inequality
====================

\[Seminorms\]
For $1\le p<\infty$ and for integers $j,0\le j\le m$, we introduce functionals $\left| \cdot  \right| _{j,p}$ on $W^{m,p}$ as follows:
$$\left| u \right| _{j,p}=\left| u \right| _{j,p,\Omega}=\left( \int_{\Omega}\sum_{\left| \alpha \right| =j} \left| D^{\alpha}u(x) \right| ^{p}\mathrm{d}x \right) ^{\frac{1}{p}}
  .$$
Clearly $\left| u \right| _{0,p}=\|u\|_{0,p}=\|u\|_{p}$ is the norm on $L^{p}\left( \Omega \right) $ and
$$\|u\|_{m,p}=\left( \int_{\Omega}\sum_{j=0}^{m} \left| u \right| _{j,p}^{p} \right) ^{\frac{1}{p}}
  .$$
If $j\ge 1$, we call $\left| \cdot  \right| _{j,p}$ a <span>*seminorm*</span>. It has all the properties of a norm excerpt that $\left| u \right| _{j,p}=0$ need not imply $u=0$ in $W^{m,p}\left( \Omega \right) $.

\[An Averaging Lemma\]
Let $\Omega$ be a domain in $\mathbb{R}^{n}$ where $n\ge 2$. Let $k$ be an integer satisfying $1\le k\le n$, and let $\kappa=\left( \kappa_1,\cdots,\kappa_k \right) $ be a $k$-tuple of integers satisfying $1\le \kappa_1<\kappa_2<\cdots\kappa_k\le n$. Let $S$ be the set of all $\binom{n}{k}$ such $k$-tuples. Given $x\in \mathbb{R}^{n}$, let $x_\kappa$ denote the point $\left( x_{\kappa_1},\cdots,x_{\kappa_k} \right) $ in $\mathbb{R}^{k}$ and let $\mathrm{d}x_{\kappa}$ denote $\mathrm{d}x_{\kappa_1}\cdots\mathrm{d}x_{\kappa_k}$.\
For $\kappa \in S$ let $E_{\kappa}$ be the $k$-dimensional plane in $\mathbb{R}^{n}$ spanned by the coordinate axes corresponding to the components of $x_{\kappa}$ :
$$E_{\kappa}=\left\{ x\in \mathbb{R}^{n}: x_{i}=0 \text{ if }i\not\in \kappa \right\}$$
and let $\Omega_k$ be the projection of $\Omega$ onto $E_k$ :
$$\Omega_{\kappa}=\left\{ x\in E_{\kappa}:x_{\kappa}=y_{\kappa}\text{ for some }y\in \Omega \right\} .$$
Let $F_{\kappa}(x_{\kappa})$ be a function depending only on the $k$ components of $x_{\kappa} $ and belong to $L^{\lambda}\left( \Omega_{\kappa} \right) $, where $\lambda = \binom{n-1}{k-1}$. Then the function $F$ defined by
$$F(x)=\prod F_{\kappa}(x_{\kappa})$$
belongs to $L^{1}\left( \Omega \right) $, and $\|F\|_{1,\Omega}\le \prod_{\kappa \in S}\|F_{\kappa}\|_{\lambda,\Omega}$, that is,
$$\left( \int_{\Omega}\left| F(x) \right| \mathrm{d}x \right) ^{\lambda}\le \prod_{\kappa \in  S}\int_{\Omega_\kappa}\left| F_{\kappa}\left( x_{\kappa} \right)  \right| ^{\lambda}\mathrm{d}x_{\kappa}.$$

For each $\kappa \in S$, let $\mathbf{p}_\kappa$be the $n$-vector whose $i$th component is $\lambda$ if $i\in \kappa$ and $\infty$ if $i\not\in \kappa$. For each $i$, $1\le i\le n$, exactly $\left( k/ n \right) \binom{n}{k}=\lambda$ of the vectors $\mathbf{p}_{\kappa}$ have $i$th component equal to $\lambda$. Therefore,
$$\sum_{\kappa \in S}\frac{1}{\mathbf{p}_{\kappa}}=\frac{1}{\mathbf{w}},$$
where $\mathbf{w}$ is the $n$-vector $(1,1,\cdots,1)$.
Let $F_{\kappa}(x_{\kappa})$ be extended to be zero for $x_{\kappa}\not\in \Omega_{\kappa}$ and consider $F_{\kappa}$ to be defined on $\mathbb{R}^{n}$ but independent of $x_{j}$ if $j\not \in \kappa$. Then $F_{\kappa}$ is its own suprimum over those $x_{j}$ and
$$\|F_{\kappa}\|_{\lambda,\Omega_\kappa}=\|F_{\kappa}\|_{\mathbf{p}_\kappa,\mathbb{R}^{n}}.$$
From the mixed-norm Hölder inequality
$$\|F\|_{1,\Omega}\le \|F\|_{\mathbf{w},\mathbb{R}^{n}}\le \prod_{\kappa\in S}\|F_{\kappa}\|_{\mathbf{p}_\kappa,\mathbb{R}^{n}}=\prod_{\kappa \in S}\|F_{\kappa}\|_{\lambda,\Omega_\kappa}$$
as required.

The Sobolev imbedding theorem tells us that for all $\phi \in  C_0^{\infty}\left( \mathbb{R}^{n} \right) $ we have
$$\|\phi\|_q \le K \|\phi\|_{m,p}$$
for some $q$ and a constant $K$. We now want to replace $\|\cdot \|_{m,p}$ with $\left| \cdot  \right| _{m,p}$. That is, we want to esablish
$$\int_{\mathbb{R}^{n}}\left| \phi(x) \right| ^{q}\mathrm{d}x\le K^{q}\left( \sum_{\left| \alpha \right| =m} \int_{\mathbb{R}^{n}}\left| D^{\alpha}\phi(x) \right| ^{p}\mathrm{d}x \right) ^{\frac{q}{p}}
  .$$
It must also holds for $\phi_{t}(x)=\phi(tx),0<t<\infty$. Since $\|\phi_t\|_{q}=t ^{-\frac{n}{q}}\|\phi\|_{q}$ and $\|D^{\alpha}\phi_t\|_{p}=t ^{m-(n/ p}\|D^{\alpha}\phi\|_{p}$. We must have
$$\int_{\mathbb{R}^{n}}\left| \phi(x) \right| ^{q}\mathrm{d}x\le K^{q}t ^{n+mq-(nq/ p)}\left( \sum_{\left| \alpha \right| =m} \left| D^{\alpha}\phi(x) \right| ^{p}\mathrm{d}x \right)^{\frac{q}{p}}.$$
It is posiible for all $t>0$ if and only if the exponent of $t$ is zero, that is, $q=p^{\ast}=np/(n-mp)$.

\[Sobolev’s Inequality\]
When $mp<n$, there exists a finite constant $K$ such that
$$\|\phi\|_{q,\mathbb{R}^{n}}\le K \left| \phi \right| _{m,p,\mathbb{R}^{n}}$$
holds for every $\phi$ in $C_0^{\infty}\left( \mathbb{R}^{n} \right) $ if and only if $q=p^{*}=np/\left( n-mp \right) $.

The “only if” part was demonstrated above. For the “if” part note first that it is sufficient to establish the inequality for $m=1$ as its validity for higher $m$ (with $mp<n $) can be confirmed by induction on $m$.\
Now we prove the case $m=1$, $p=1$, that is
$$\int_{\mathbb{R}^{n}}\left| \phi(x) \right| ^{n/(n-1)}\mathrm{d}x \le  K \left( \sum_{j=1}^{n}\int_{\mathbb{R}^{n}}\left| D_{j}\phi(x) \right| \mathrm{d}x \right) ^{n/(n-1)}
    .$$
Let $\phi \in C_0^{\infty}(\mathbb{R}^{n})$ and for $x\in \mathbb{R}^{n}$ and $1\le j\le n$ let $\hat{x}_{j}=\left( x_1,\cdots,x_{j-1},x_{j+1},\cdots,x_n \right) $. Let
$$u_{j}(\hat{x}_j)=\left( \int_{-\infty}^{\infty}\left| D\phi(x) \right| \mathrm{d}x_j \right)^{\frac{1}{n-1}}
    .$$
which is evidently independent of $x_j$ and satisfies
$$\left( \|u_j\|_{n-1,\mathbb{R}^{n-1}} \right)^{n-1}\le \left| \phi \right| _{1,1,\mathbb{R}^{n}}
  .$$
Since
$$\phi(x)=\int_{-\infty}^{x_1}D_1\phi(t,\hat{x}_1)\mathrm{d}t$$
we have
$$\left| \phi(x) \right| \le \int_{-\infty}^{\infty}\left| D_1\phi(t,\hat{x}_1) \right| \mathrm{d}t\le \left( u_1\left( \hat{x}_1 \right)  \right)^{n-1}.$$
Similarly, $\left| \phi(x) \right| \le \left( u_{j}\left( \hat{x}_j \right)  \right) ^{n-1}$. Applying the Lemma above with $k=n-1=\lambda$ we obtain
$$\begin{aligned}
  \int_{\mathbb{R}^{n}}\left| \phi(x) \right| ^{n/(n-1)}\mathrm{d}x\le & \int_{\mathbb{R}^{n}}\prod_{j=1}^{n}u_{j}(\hat{x}_j)\mathrm{d}x\\
  \le & \left( \prod_{j=1}^{n}\int_{\mathbb{R}^{n-1}}\left| u_j(\hat{x}_j) \right| ^{n-1}\mathrm{d}\hat{x}_j \right) ^{\frac{1}{n-1}}\\
  \le &\left| \phi\right| _{1,1,\mathbb{R}^{n}}^{n/(n-1)}
.\end{aligned}$$
For $1<p<n$ and $p^{\ast}=np/\left( n-p \right) $ we can apply the above inequality to $\left| \phi(x) \right| ^{s}$ where $s=(n-1)p^{\ast}/ n$ and obtain, using Hölder’s inequality,
$$\begin{aligned}
    \int_{\mathbb{R}^{n}}\left| \phi(x) \right| ^{p^{\ast}}\mathrm{d}x\le & K\left( \sum_{j=1}^{n}s\left| \phi(x) \right| ^{s-1}\left| D_{j}\phi(x) \right| \mathrm{d}x \right) ^{n/(n-1)}\\
    \le  & K_1 \left( \sum_{j=1}^{n}\|\phi\|^{s-1}_{(s-1)p'}\|D_{j}\phi\|_p \right) ^{n/(n-1)}
    .
  \end{aligned}$$
Since
$$\begin{aligned}
    (s-1)p'=&\left(\frac{(n-1)p^{\ast}}{n}-1\right) \frac{p}{p-1}=\left( \frac{n-1}{n}\cdot \frac{np}{n-p}-1 \right) \frac{p}{p-1}\\
    =& \left( \frac{(n-1)p}{n-p}-1 \right) \frac{p}{p-1}=\frac{np-p-n+p}{n-p}\cdot \frac{p}{p-1}\\
    =& \frac{n(p-1)}{n-p}\cdot \frac{p}{p-1}=\frac{np}{n-p}=p^{\ast}
  \end{aligned}$$
and
$$p^{\ast}-\frac{(s-1)n}{n-1}=\frac{n}{n-1},$$
it follows by cancellation that
$$\|\phi\|_{p^{\ast}}\le K_2 \left| \phi \right| _{1,p}.$$
For the case $m>1$, it can be proved by induction on $m$.

In the above proof, we used the given lemma to get the inequality
$$\int_{\mathbb{R}^{n}}\prod_{j=1}^{n}\phi_{j}(\hat{x}_j)\mathrm{d}x\le \int \left( \prod_{j=1}^{n}\int_{\mathbb{R}^{n-1}}\left| \phi_j(\hat{x}_j) \right| ^{n-1}\mathrm{d}\hat{x}_j \right) ^{\frac{1}{n-1}}.$$
In fact, this inequality can also be proved as follows:

First we have
$$\left| \phi(x) \right| ^{\frac{n}{n-1}}\le \prod_{j=1}^{n}\phi_j(\hat{x}_j).$$
To make the terms short and clear, we denote
$$\int_{\mathbb{R}}\left| D\phi \right| \mathrm{d}y_i=\int_{\mathbb{R}}\left| D\phi(x_1,\cdots,y_i,\cdots,x_n \right| \mathrm{d}y_i.$$
Integrate this inequality with respect to $x_1$:
$$\begin{aligned}
  \int_{\mathbb{R}}\left| \phi(x) \right| ^{\frac{n}{n-1}}\mathrm{d}x_1\le & \int_{\mathbb{R}}\prod_{i=1}^{n}\left( \int_{\mathbb{R}}\left| D \phi \right| \mathrm{d}y_{i} \right)^{\frac{1}{n-1}}\mathrm{d}x_1\\
  =& \left( \int_{\mathbb{R}}\left| D \phi \right|\mathrm{d}y_1  \right)^{\frac{1}{n-1}}\int_{\mathbb{R}}\prod_{i=2}^{n}\left( \int_{\mathbb{R}}\left| D\phi \right|\mathrm{d}y_i  \right) ^{\frac{1}{n-1}}\mathrm{d}x_1 \\
  \le& \left( \int_{\mathbb{R}}\left| D\phi \right| \mathrm{d}y_1 \right) ^{\frac{1}{n-1}}\left( \prod_{i=2}^{n}\int_{\mathbb{R}^{2}}\left| D\phi \right| \mathrm{d}x_1\mathrm{d}y_i \right)^{\frac{1}{n-1}}, \end{aligned}$$
the last inequality resulting from the general Hölder inequality.

Now integrate the above inequality with respect to $x_2$:
$$\int_{\mathbb{R}^{2}}\left| \phi \right| ^{\frac{n}{n-1}}\mathrm{d}x_1\mathrm{d}x_2\le \left( \int_{\mathbb{R}^{2}}\left| D\phi \right| \mathrm{d}x_1\mathrm{d}y_2 \right) ^{\frac{1}{n-1}}\int_{\mathbb{R}}\prod_{i=1,i\neq 2}^{n}I_i^{\frac{1}{n-1}}\mathrm{d}x_2,$$
for
$$I_1:=\int_{\mathbb{R}}\left| D\phi \right| \mathrm{d}y_1,\quad I_i:=\int_{\mathbb{R}^{2}}\left| D\phi \right| \mathrm{d}x_1\mathrm{d}y_i\quad \left( i=3,\cdots,n \right) .$$
Applying once more the extended Hölder inequality, we find
$$\begin{aligned}
  &\int_{\mathbb{R}^{2}}\left| \phi \right| ^{\frac{n}{n-1}}\mathrm{d}x_1\mathrm{d}x_2 \\
  \le &\left( \int_{\mathbb{R}^{2}}\left| D\phi \right| \mathrm{d}x_1\mathrm{d}y_2 \right) ^{\frac{1}{n-1}}\left( \int_{\mathbb{R}^{2}}\left| D\phi \right| \mathrm{d}y_1\mathrm{d}x_2 \right) ^{\frac{1}{n-1}}\prod_{i=3}^{n}\left( \int_{\mathbb{R}^{3}}\left| D\phi \right| \mathrm{d}x_1\mathrm{d}x_2\mathrm{d}y_i \right)^{\frac{1}{n-1}}. \end{aligned}$$
We continue by integrating with respect to $x_3,\cdots,x_n$, eventually to find
$$\int_{\mathbb{R}^{n}}\left| \phi \right| ^{\frac{n}{n-1}}\le \prod_{i=1}^{n}\left( \int_{\mathbb{R}^{n}}\left| D\phi \right| \mathrm{d}x_1\cdots\mathrm{d}y_i\cdots\mathrm{d}x_n \right)^{\frac{1}{n-1}}=\left( \int_{\mathbb{R}^{n}}\left| D\phi \right| \mathrm{d}x \right) ^{\frac{n}{n-1}}.$$
