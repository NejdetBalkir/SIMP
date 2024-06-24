import numpy as np
def sensitivity_filter(nelx,nely,rmin,x,dc):
    # OBJECTIVE: filter the derivative of the compliance

    # INPUTS: 
        # nelx,nely: number of elements in the x and y directions
        # rmin: filter radius
        # x: density field
        # dc: derivative of the compliance
    # OUTPUTS:
        # dc: filtered derivative of the compliance

    dcn = np.zeros((nely,nelx)) # initialize the filtered derivative of the compliance

    for i in range(1,nelx+1):
        for j in range(1,nely+1):
            sum = 0
            for k in range( max(i-int(np.floor(rmin)),1), min(i+int(np.floor(rmin)),nelx)+1 ):
                for l in range(max(j-int(np.floor(rmin)),1), min(j+int(np.floor(rmin)),nely)+1):
                    fac = rmin - np.sqrt((i-k)**2+(j-l)**2)
                    sum += max(0,fac)
                    dcn[j-1,i-1] += max(0.0,fac)*x[l-1,k-1]*dc[l-1,k-1]
            dcn[j-1,i-1] = dcn[j-1,i-1]/(x[j-1,i-1]*sum)

    return dcn