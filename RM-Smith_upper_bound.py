import numpy as np
from scipy.optimize import minimize
from scipy.optimize import LinearConstraint
from scipy.optimize import Bounds

# Author: Semih Kara
# Date: 07.01.2021
# Description:
# This code numerically approximates the $\bar{\lambda}(n)$ in equation (30) of the paper for the RM-Smith protocol.
# First note that $\bar{\lambda}(n)$ is equal to the solution of the optimization problem in (31). Moreover, note that
# $p_1\geq p_2\geq ... \geq p_n$ eliminates expressions of the form $\max(x,0)$ in the objective function and
# constraints, and yields an objective function that is a ratio of two polynomials in $p_i$'s. Hence, under
# $p_1\geq p_2\geq ... \geq p_n$, we get an objective function that is a fraction of two polynomials in $p_i$'s and this
# is a form that the optimization toolbox can handle. Additionally, due to the boundedness of the PDM or continuity of
# the static game, payoff is bounded. From the objective function we see that dividing all $p_j$ {j\in\{1,...,n\}} by
# $\max_{i\in\{1,...,n\}} |p_i|$ value of the objective function does not change, and we get an equivalent optimization
# problem in which $|p|\leq 1$. Therefore, without loss of generality we can assume $-1\leq p_j\leq 1$ for all
# $j\in\{1,...,n\}$. Plugging these in the optimization toolbox of scipy we get a numerical approximation of the
# minimization problem of interest. In order to get the approximation result for the desired $n$ value, set the value of
# 'n' below to the desired value.

# n is the number of strategies.
n = 3
# b is the bound on $|p_i|$ for all $i\in\{1,...,n\}$. We can set $b$ to be any positive value and we choose it to be 1.
b = 1
# v0 is the initial value of $p$ that we provide to the optimization toolbox. Any vector satisfying the bound and linear
# inequality constraints works.
v0 = np.linspace(b, -b, num=n)


# The following definition describes the objective function as a function of $p$.
def obj_after_con_smith(p):
    # We first define the numerator.
    num = sum((p-p[n-1])**2)*sum((p-p[n-1]))

    # Then we define the denominator.
    denom = 0
    for i in range(0, n):

        m = 0
        for k in range(0, i):
            m = m + (p[k]-p[i])**2

        denom = denom + (p[i]-p[n-1])*m

    obj = num/denom

    return obj


# Here we set the linear inequality constraint.
lin_const_mat = np.zeros(n)
lin_const_mat[0] = 1
lin_const_mat[1] = -1
lin_const_mat = np.append([lin_const_mat], [np.roll(lin_const_mat, 1)], axis=0)
for i in range(0, n - 3):
    lin_const_mat = np.append(lin_const_mat, [np.roll(lin_const_mat[1, :], i+1)], axis=0)

# Note that due to the bounds on $p_i$s we can also set the upper bound in the inequality constraint to be 2*b rather
# than np.inf.
lin_const_ub = np.ones(n-1)*2*b
lin_const_lb = np.zeros(n-1)

linear_constraint = LinearConstraint(lin_const_mat, lin_const_lb, lin_const_ub)

# We define the upper and lower bounds on $p$.
bounds = Bounds(-b*np.ones(n), b*np.ones(n))

# We pass the minimization problem with the determined constraints and the objective function to the optimization
# toolbox of scipy.
res = minimize(obj_after_con_smith, v0, method='trust-constr',
               constraints=[linear_constraint],
               options={'verbose': 1, 'maxiter': 3000}, bounds=bounds)

print(res.x)
print(obj_after_con_smith(res.x))