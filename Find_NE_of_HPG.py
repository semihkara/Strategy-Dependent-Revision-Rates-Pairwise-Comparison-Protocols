from z3 import *

# Author: Semih Kara
# Date: 07.01.2021
# Description:
# This code verifies that ((0,1,0),(0,0,1)) is the unique Nash equilibrium of the HPG for the DRAM market with the
# parameters selected in Section VI-A of the paper. In order to compile, the Z3 solver and the Z3Py (the Z3 API in
# Python) are required to be installed and properly set up. For installation and set up information on Z3 and its
# bindings, see https://github.com/Z3Prover/z3.

# We create real valued variables in z3, where the 'xri' below represents the component of the social state
# corresponding to population $r\{1,2\}$ and strategy $i\in\{1,2,3\}$.
x11 = Real('x11')
x12 = Real('x12')
x13 = Real('x13')
x21 = Real('x21')
x22 = Real('x22')
x23 = Real('x23')

# Then, we enter the payoff to each population and strategy as determined by the DRAM HPG with the parameters selected
# in Section VI-A of the paper. The 'Fri' below represents the component of the payoff corresponding to population
# $r\{1,2\}$ and strategy $i\in\{1,2,3\}$.
F11 = -11-(x11+2*x21)**2
F12 = -9.2-(x12+2*x22)**2
F13 = -7.5-(x13+2*x23)**2
F21 = -11-(x11+2*x21)**2
F22 = -10.2-(x12+2*x22)**2
F23 = -6.5-(x13+2*x23)**2

# We create a z3 solver.
s = Solver()

# We introduce to the solver the constraint that the population state belongs to the simplex.
s.add(0 <= x11, x11 <= 1, 0 <= x12, x12 <= 1, 0 <= x13, x13 <= 1, 0 <= x21, x21 <= 1, 0 <= x22, x22 <= 1, 0 <= x23, x23 <= 1)
s.add(x11+x12+x13 == 1, x21+x22+x23 == 1)

# Now we introduce the conditions that define the Nash equilibria (see section III-A) to the solver. Hence, the
# variables x11,...,x23 that belong to the simplex and satisfy the below conditions are Nash equilibria of the HPG for
# the DRAM market with the parameters selected in Section VI-A of the paper.
s.add(Or(x11 == 0, And(F11 >= F12, F11 >= F13)))
s.add(Or(x12 == 0, And(F12 >= F11, F12 >= F13)))
s.add(Or(x13 == 0, And(F13 >= F11, F13 >= F12)))
s.add(Or(x21 == 0, And(F21 >= F22, F21 >= F23)))
s.add(Or(x22 == 0, And(F22 >= F21, F22 >= F23)))
s.add(Or(x23 == 0, And(F23 >= F21, F23 >= F22)))

# Running the code with the line 's.add(Or(x23 != 1, x12 != 1))' commented produces the output: 'sat
# [x12 = 1, x13 = 0, x22 = 0, x23 = 1, x21 = 0, x11 = 0]' in the command window. This means that the social state
# ((0,1,0),(0,0,1)) is a Nash equilibrium of the DRAM HPG with the parameters selected in Section VI-A of the paper. In
# order to see that this the unique Nash equilibrium, we enforce the condition to the solver that the social state is
# not equal to ((0,1,0),(0,0,1)), and run the resulting code. The condition that the social is not equal to
# ((0,1,0),(0,0,1)) can be enforced by uncommenting the line below.
# s.add(Or(x23 != 1, x12 != 1))

# Uncommenting 's.add(Or(x23 != 1, x12 != 1))' and running the code produces an output message with 'unsat' in the
# command window, which implies that the HPG with the parameters selected in Section VI-A of the paper has no Nash
# equilibrium other than ((0,1,0),(0,0,1)).

print(s.check())
print(s.model())
