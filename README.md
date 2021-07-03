This repository complements the paper titled "Pairwise Comparison Evolutionary Dynamics with Strategy-Dependent Revision Rates: Stability and $\delta$-Passivity", and accommodates two Python files. 

The first file, named "RM_Smith_upper_bound.py", comprises the code that numerically approximates the upper bound given in Theorem 1 for the worst case revision rate ratios under which the RM-Smith protocol is $\delta$-passive. In order to get the upper bound for a desired value of number of strategies ($n$), set the value of 'n' to the desired value in the file named RM_Smith_upper_bound.py and run the code.

The second file, named "Find_NE_of_HPG.py", contains the code that finds the Nash equilibria of the HPG for the DRAM market constructed in Section VI-A. In order to verify that this Nash equilibria is the singleton given by $\{x = ((0,1,0),(0,0,1))\}$, run the code in the file named Find_NE_of_HPG.py by following the steps specified in its comments.
