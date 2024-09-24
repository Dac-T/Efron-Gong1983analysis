# Efron-Gong1983analysis
The goal is to reproduces the main results of _Efron and Gong, The American Statistician, 1983_ for a master project (PCBS2, Cogmaster, ENS-Ulm).
The paper take a look at different nonparametrical strategies to determinate the standard deviation $\sigma$ of a data set with an unknown probability of distribution F.

## Code and Modularity
The file code.py reproduces the main results of Efron and Gong. You can comment or decomment the printing of the different estimates of standard error.
I did not only manage to reproduce the results but to define functions corresponding to given equations in the paper so that the bootstrap estimate and the jackknife estimate could be used on any dataset (you just have to type it into the code, or to add a line for reading datafiles).

## Results
I computed the bootstrap estimate $\sigma_B$, the jackknife estimate $\sigma_J$ and the standard estimate, and compared their value to those given in _Efron and Gong (1983)_. I used the data sample given on figure 1.
![Figure_1.png](/Figure_1.png?raw=true "Figure 1")

Running the code gave me those values:
- $\sigma_B = 0.121$
- $\sigma_J = 0.126$
- $\sigma_{Norm} = 0.117$

The paper gave for this datasample:
- $\sigma_B = 0.127$
- $\sigma_{Norm} = 0.115$

Therefore I noted that the simulated results were consistents with those published, and I reproduced the figure 2, that displays an histogram of 1000 bootstrap replication, to observe a high similarity in the figures's shape.

![Figure_2.png](/Figure_2.png?raw=true "Figure 2")


## To be extended?
It would have been interesting to deeper study the possibles results for bootstrap, modelize uniform smoothed bootstrap and bend over infinitesimal jackknife and cross-validation.
