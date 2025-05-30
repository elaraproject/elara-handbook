# General Relativity, Part 2

Previously, we built up the idea of acceleration as being indistinguishable from gravitational force, and found the geodesic equation, which governs how objects move in curved spacetime. But to truly accurately describe relativity, we also need a mathematical description of what curvature in spacetime is. This will be what we'll explore in this section.


## The Covariant Derivative


As we've seen by this point, the laws of physics are primarily written in partial differential equations, and so it would be natural to think that General Relativity can be characterized by partial differential equations too. The issue is, consider a vector $\vec V = V^a e_a$. If we were to take its partial derivative, we'd have (using the product rule):


$$
\frac{\partial \vec V}{\partial x^b} = \frac{\partial V^a}{\partial x^b} e_a + \frac{\partial e_a}{\partial x^b} V^a
$$


But remember that tensors should transform like tensors, where each component is at most a partial derivative multiplied by the original tensor? The additional $\frac{\partial e_a}{\partial x^b} V^a$ term means that the regular partial derivative doesn't transform like a tensor. So instead of partial derivatives, we need to define a new type of derivative, the **covariant derivative**, which compensates for the additional term in the partial derivative. The covariant derivative takes the form:


$$
\nabla_b V^a = \frac{\partial V^a}{\partial x^b} + V^k \Gamma^a_{kb}
$$


for vectors (those with an upper index), and the form:


$$
\nabla_b V_a = \frac{\partial V_a}{\partial x^b} - V_k \Gamma^k_{ab}
$$


for covectors (those with a lower index). To take the covariant derivative of tensors formed from both vectors and covectors, such as the metric tensor $g_{\mu \nu}$, we add a term for each upper index the tensor has and subtract a term for each lower index the tensor has (you'll see how this works in just a moment). For example, for the metric tensor, we first write out the covariant derivative as a partial derivative, plus an unknown term:


$$
\nabla_b g_{\mu \nu} = \frac{\partial g_{\mu \nu}}{\partial x^b} + \dots
$$


Then, we notice that the metric tensor has two lower indices, so we need two correction terms. The first correction term is for the index $\mu$, and the second correction term is for the index $\nu$. To emphasize which index each correction term is for, there is a little hat on that index:


$$
\nabla_b g_{\mu \nu} = \frac{\partial g_{\mu \nu}}{\partial x^b} - g_{\hat \mu \nu} A - g_{\mu \hat \nu} B
$$


Now comes the slightly bizarre part. We're going to replace whichever index we're interested in (the one with a hat on) with a dummy index $\alpha$. This is so that the rules of tensor algebra work out such that the covariant derivative transforms like a tensor. So:


$$
\frac{\partial g_{\mu \nu}}{\partial x^b} - g_{\alpha \nu} A - g_{\mu \alpha} B
$$


To figure out the correct index convention for $A$ and $B$, we use the rule that we multiply $\Gamma^\alpha_{\gamma b}$ for each lower index correction term, and multiply $\Gamma^\gamma_{\alpha b}$ for each upper index correction term. Here:

- $\alpha$ is the dummy index we're using
- $\gamma$ is the index of the term we're interested in
- $b$ is the index we take the covariant derivative with respect to. 

So $A = \Gamma^\alpha_{\mu b}$ and $B = \Gamma^\alpha_{\nu b}$. Thus we have:


$$
\nabla_b g_{\mu \nu} = \frac{\partial g_{\mu \nu}}{\partial x^b} - g_{\alpha \nu} \Gamma^\alpha_{\mu b} - g_{\mu \alpha} \Gamma^\alpha_{\nu b}
$$


Also, it should be noted that "covariant derivative" is a bit of a misnomer - here, the definition of the word "covariant" pre-dates the idea of contra- and covariant tensors (tensors with upper/lower indices), and referes to the earlier definition of "invariant". Thus, the covariant derivative is really just a fancy way of saying a derivative of a tensor that is invariant of the coordinates used.


Lastly, the covariant derivative of a field with respect to the same index as the index of the field is equal to simply the divergence:


$$
\nabla_b V^b = \nabla \cdot \vec V
$$


## The Riemann tensor


What can we use to measure the curvature of spacetime? We already know that with the covariant derivative, we can take fully-invariant derivatives in spacetime. But if spacetime is to be curved, then if we take a derivative of a vector along direction $\mu$, then another along direction $\nu$, we'd expect to get a different result than if we were to take a derivative along direction $\nu$, then along direction $\mu$. We can qualitatively describe this as:


$$
\nabla_\mu \nabla_\nu V^\alpha \neq \nabla_\nu \nabla_\mu V^\alpha
$$


The difference between the two sets of derivatives is going to tell us how much the curvature of spacetime varies between the two points. So we simply need to compute:


$$
\nabla_\mu \nabla_\nu V^\alpha - \nabla_\nu \nabla_\mu V^\alpha
$$


First, we expand out the covariant derivatives:


$$
\nabla_\mu (\nabla_\nu V^\alpha) - \nabla_\nu (\nabla_\mu V^\alpha)
$$


$$
\nabla_\mu (\partial_\nu V^\alpha + V^\sigma \Gamma^\alpha_{\sigma \nu}) - \nabla_\nu (\partial_\mu V^\alpha + V^\sigma \Gamma^\alpha_{\sigma \mu})
$$


Let's take this step by step, and we'll start with the first covariant derivative:


$$
\nabla_\mu (\partial_\nu V^\alpha + V^\sigma \Gamma^\alpha_{\sigma \nu})
$$


Notice that because $\sigma$ is a dummy index and contracts, we can rewrite the inside of the parentheses as another tensor:


$$
C^\alpha_\nu = \partial_\nu V^\alpha + V^\sigma \Gamma^\alpha_{\sigma \nu}
$$


If we take the covariant derivative of $C^\alpha_\nu$, we know that we have a partial derivative, plus several other correction terms::


$$
\nabla_\mu C^\alpha_\nu = \partial_\mu C^\alpha_\nu + \dots
$$


We can write out the remaining correction terms as the tensor multiplied by several coefficients (add correction term if upper index, subtract correction term if lower index), with hats indicating which terms we're interested in:


$$
\nabla_\mu C^\alpha_\nu = \partial_\mu C^\alpha_\nu + C^{\hat \alpha}_\nu A - C^\alpha_{\hat \nu} B
$$


We replace the hatted indices with our dummy index $\lambda$ (we chose a new variable so as not to cause confusion with the existing variables):


$$
\nabla_\mu C^\alpha_\nu = \partial_\mu C^\alpha_\nu + C^\lambda_\nu A - C^\alpha_\lambda B
$$


Using the correction term coefficient rule described earlier for the Christoffel symbols, we recall that:

- For an upper index coefficient term we have the dummy index on the bottom and the interested index on the top
- For a lower index coefficient term we have the dummy index on top and the interested index on the bottom
- The rightmost lower term on the coefficient is always the index we're taking the covariant derivative with respect to (in our case $\mu$)

So we can figure out that $A = \Gamma^\alpha_{\lambda \mu}$, and $B = \Gamma^\lambda_{\nu \mu}$. So:


$$
\nabla_\mu C^\alpha_\nu = \partial_\mu C^\alpha_\nu + C^\lambda_\nu \Gamma^\alpha_{\lambda \mu} - C^\alpha_\lambda \Gamma^\lambda_{\nu \mu}
$$


But recall that:


$$
C^\alpha_\nu = \partial_\nu V^\alpha + V^\sigma \Gamma^\alpha_{\sigma \nu}
$$


From which we can perform index substitutions on every index to get:


$$
C^\lambda_\nu = \partial_\nu V^\lambda + V^\sigma \Gamma^\lambda_{\sigma \nu}
$$


$$
C^\alpha_\lambda = \partial_\lambda V^\alpha + V^\sigma \Gamma^\alpha_{\sigma \lambda}
$$


```{note}
The last two were obtained by changing the indices $\alpha \to \lambda$ and $\nu \to \lambda$. Shouldn't this be illegal in tensor algebra, where we're not supposed to swap free indices in the same equation? There is a nuance here - we can swap free indices **only** if we subtitute each and every index with a corresponding different index. That, is, if you have an equation $x^i = g^{ij} b_j$, you can't simply say "I want to swap $j \to i$ and make the equation $x^i = g^{ii} b_i$". Here, you're selectively substituting $j \to i$ without making a substitution for $i$, so the equation is wrong! But you can say that "I'll rewrite the equation using different indices, substituting $i \to a$ and $j \to b$, so I have $x^a = g^{ab} b_b$". Since we swapped _every_ index with a _unique_ different index, this is acceptable.
```


We can therefore rewrite the covariant derivative of $C^\alpha_\nu$ as:


$$
\nabla_\mu C^\alpha_\nu = \partial_\mu (\partial_\nu V^\alpha + V^\sigma \Gamma^\alpha_{\sigma \nu}) + (\partial_\nu V^\lambda + V^\sigma \Gamma^\lambda_{\sigma \nu}) \Gamma^\alpha_{\lambda \mu} - (\partial_\lambda V^\alpha + V^\sigma \Gamma^\alpha_{\sigma \lambda}) \Gamma^\lambda_{\nu \mu}
$$


Be careful! The second and third terms are just products, but the first term is a derivative, so we have to use the product rule to expand - $\partial_\mu (\partial_\nu V^\alpha + V^\sigma \Gamma^\alpha_{\sigma \nu}) = \partial_\mu \partial_\nu V^\alpha + \partial_\mu (V^\sigma \Gamma^\alpha_{\sigma \nu})$. Using that, and expanding the rest of the terms out, we get:


$$
\nabla_\mu \nabla_\nu V^\alpha = \nabla_\mu C^\alpha_\nu = \partial_\mu \partial_\nu V^\alpha + \partial_\mu (V^\sigma \Gamma^\alpha_{\sigma \nu}) + \Gamma^\alpha_{\lambda \mu} \partial_\nu V^\lambda + V^\sigma \Gamma^\lambda_{\sigma \nu} \Gamma^\alpha_{\lambda \mu} - \partial_\lambda V^\alpha \Gamma^\lambda_{\nu \mu} - V^\sigma \Gamma^\alpha_{\sigma \lambda} \Gamma^\lambda_{\nu \mu}
$$


Phew! We're almost there, just hang in there for the remaining derivation. Good news! Things are going to look simpler from this point on. We've already solved the left double covariant derivative, $\nabla_\mu \nabla_\nu V^\alpha$. The right double covariant derivative is just the left double covariant derivative with an index swap $\mu \leftrightarrow \nu$ (that means every time we see a $\mu$, we replace it with a $\nu$, and every time we see a $\nu$, we replace it with a $\mu$). So it is:


$$
\nabla_\nu \nabla_\mu V^\alpha = 
\partial_\nu \partial_\mu V^\alpha + \partial_\nu (V^\sigma \Gamma^\alpha_{\sigma \mu}) + \Gamma^\alpha_{\lambda \nu} \partial_\mu V^\lambda + V^\sigma \Gamma^\lambda_{\sigma \mu} \Gamma^\alpha_{\lambda \nu} - \partial_\lambda V^\alpha \Gamma^\lambda_{\mu \nu} - V^\sigma \Gamma^\alpha_{\sigma \lambda} \Gamma^\lambda_{\mu \nu}
$$


Now is the glorious part - when we subtract one from the other, the terms cancel each other out. Because second partial derivatives are equal no matter what order you take them, $\partial_\mu \partial_\nu = \partial_\nu \partial_\mu$, so those cancel. The last two terms are identical for both (given the symmetry of the Christoffel symbols, so they cancel as well. We're left with:


$$
\nabla_\mu \nabla_\nu V^\alpha - \nabla_\nu \nabla_\mu V^\alpha = (\partial_\mu (V^\sigma \Gamma^\alpha_{\sigma \nu}) + \Gamma^\alpha_{\lambda \mu} \partial_\nu V^\lambda - V^\sigma \Gamma^\lambda_{\sigma \nu} \Gamma^\alpha_{\lambda \mu}) - (\partial_\nu (V^\sigma \Gamma^\alpha_{\sigma \mu}) + \Gamma^\alpha_{\lambda \nu} \partial_\mu V^\lambda - V^\sigma \Gamma^\lambda_{\sigma \mu} \Gamma^\alpha_{\lambda \nu})
$$


Notice a third less obvious cancellation where $\partial_\mu (V^\sigma \Gamma^\alpha_{\sigma \nu}) = \partial_\mu V^\sigma \Gamma^\alpha_{\sigma \nu} + \partial_\mu \Gamma^\alpha_{\sigma \nu} V^\sigma$ which cancels out $\Gamma^\alpha_{\lambda \nu} \partial_\mu V^\lambda$ on the right (because dummy indices don't matter). This simplifies the expression to:


$$
\nabla_\mu \nabla_\nu V^\alpha - \nabla_\nu \nabla_\mu V^\alpha = \partial_\mu \Gamma^\alpha_{\sigma \nu} V^\sigma - \partial_\nu \Gamma^\alpha_{\sigma \mu} V^\sigma + V^\sigma \Gamma^\lambda_{\sigma \nu} \Gamma^\alpha_{\lambda \mu} - V^\sigma \Gamma^\lambda_{\sigma \mu} \Gamma^\alpha_{\lambda \nu}
$$


We can now finally (!!!) factor out the $V^\sigma$ from the expression, to get:


$$
\nabla_\mu \nabla_\nu V^\alpha - \nabla_\nu \nabla_\mu V^\alpha = V^\sigma [\partial_\mu \Gamma^\alpha_{\sigma \nu} - \partial_\nu \Gamma^\alpha_{\sigma \mu} + \Gamma^\lambda_{\sigma \nu} \Gamma^\alpha_{\lambda \mu} -  \Gamma^\lambda_{\sigma \mu} \Gamma^\alpha_{\lambda \nu}]
$$


The term in the brackets can be written as a new tensor:


$$
R^\alpha_{\sigma \mu \nu} = \partial_\mu \Gamma^\alpha_{\sigma \nu} - \partial_\nu \Gamma^\alpha_{\sigma \mu} + \Gamma^\lambda_{\sigma \nu} \Gamma^\alpha_{\lambda \mu} - \Gamma^\lambda_{\sigma \mu} \Gamma^\alpha_{\lambda \nu}
$$


The is the **Riemann curvature tensor**, and it measures how vectors diverge due to the curvature of space. It is a monster tensor - it has 256 components in 4D space, making it a $4 \times 4 \times 4 \times 4$ matrix.


To make this tensor easier to work with, we often contract it by making the 1st and 3rd indices identical, creating the **Ricci tensor**, which is defined by:


$$
R_{\sigma \nu} = R^\mu_{\sigma \mu \nu} = \partial_\mu \Gamma^\mu_{\sigma \nu} - \partial_\nu \Gamma^\mu_{\sigma \mu} + \Gamma^\lambda_{\sigma \nu} \Gamma^\mu_{\lambda \mu} - \Gamma^\lambda_{\sigma \mu} \Gamma^\mu_{\lambda \nu}
$$


We can further contract the Ricci tensor by multiplying it by the inverse metric, giving the **Ricci scalar**:


$$
R = g^{\mu \nu} R_{\mu \nu}
$$


We now have all the tensors we need to derive the ultimate equation - the **Einstein Field Equations**.
