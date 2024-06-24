import numpy as np

def optimality_criteria(nelx, nely, x, volfrac, dc):
    # This function optimizes the design using the optimality criteria method
    # Inputs:
    # nelx: number of elements in the x direction
    # nely: number of elements in the y direction
    # x: design variable
    # volfrac: volume fraction
    # dc: derivative of the compliance
    # Outputs:
    # xnew: new design variable

    l1 = 0 # lower bound of Lagrange multiplier
    l2 = 100000 # upper bound of Lagrange multiplier
    move = 0.2 # maximum change of design variable
    xmin = 0.001 # minimum value of design variable

    # Apply Bi-section method to find the Lagrange multiplier
    while (l2-l1) > 1e-4: # loop until the Lagrange multiplier converges
        lmid = 0.5*(l2+l1) # middle value of Lagrange multiplier
        xnew = np.maximum(xmin, np.maximum(x-move, \
                    np.minimum(1,np.minimum(x+move, x*np.sqrt(-dc/lmid)))))
        
        if np.sum(xnew) - volfrac*(nelx*nely) > 0:
            l1 = lmid
        else:
            l2 = lmid
        

    return xnew
    