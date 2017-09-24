# HofstaderButterfly
2D square lattice tight bind model, with external B field, Peierls substitution


# test.py
## (1)increase the system size L
L=8

## (2)increase the B field interval
BBins=64

## (3)half the size with symmetry
2*np.pi to np.pi


## graph
![8x8 lattice, 64 B fileds ](https://github.com/Jian2017/HofstaderButterfly/blob/master/plot.png?raw=true)


## another graph
![16x16 lattice, 256 B fileds ](https://github.com/Jian2017/HofstaderButterfly/blob/master/butterfly2.png?raw=true)


## larger system
![32x32 lattice](https://github.com/Jian2017/HofstaderButterfly/blob/master/butterfly.png?raw=true)

## bugs
the graphs do not look like the graph on the internetl, I am using open boundary condition,
perhaps Pierels substitution gets some bugs
