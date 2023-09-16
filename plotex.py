#### I make a trivial modification to plotex.py code##########
#### September 16th ##
import matplotlib.pyplot as plt

def my_plotex(cxs,cys,dxs,dys):
    plt.xlabel('x', fontsize=20)
    plt.ylabel('f(x)', fontsize=20)
    plt.plot(cxs, cys, 'r-', label='one function')
    plt.plot(dxs, dys, 'b--^', label='other function')
    plt.legend()
    plt.show()

cxs = [0.1*i for i in range(60)]
cys = [x**3 + x**2 for x in cxs]
dxs = [i for i in range(7)]
dys = [x**2 + 4 for x in dxs]

my_plotex(cxs, cys, dxs, dys)
