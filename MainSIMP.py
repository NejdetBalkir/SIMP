import numpy as np


def SIMP(nelx, nely, volfrac, penal, rmin):
    # INITIALIZATION
    x = volfrac * np.ones((nely,nelx)) # distributing material evenly in the design domain
    print(x)
    loop = 0
    change = 1
    dc = np.empty([nely,nelx]) # initialize the sensitivity of the compliance

    # START ITERATION
    while change > 0.01:
        loop = loop + 1
        xold = x.copy()

        # FE-ANALYSIS
        from FeAnalysis import FE
        U = FE(nelx, nely, x,penal)

        from stiffness import stiffness
        KE = stiffness() #global stiffness tensor

        c = 0 # initialize the compliance

        for ely in range(0,nely):
            for elx in range(0,nelx):
                print('ely:', ely)
                print('type(ely):', type(ely))
                n1 = (nely+1)*elx+ely # index of upper left corner of the element
                n2 = (nely+1)* (elx+1) + ely  # index of upper right corner of the element
                edof = np.array([2*n1, 2*n1+1, 2*n2, 2*n2+1, 2*n2+2, 2*n2+3, 2*n1+2, 2*n1+3])
                Ue = U[edof] # extract the displacement of the element
                print('Ue:' , Ue)
                c = c + x[ely,elx]**penal*np.dot(np.dot(Ue.T, KE), Ue) # calculate and accumulate the compliance
                dc[ely,elx] = -penal*x[ely,elx]**(penal-1)*np.dot(np.dot(Ue.T, KE), Ue) # calculate the derivative of the compliance (sensitivity of compliance)

        # SENSITIVITY FILTERING
        from SF import sensitivity_filter # type: ignore
        dc = sensitivity_filter(nelx, nely, rmin, x, dc)

        from OC import optimality_criteria # type: ignore
        x = optimality_criteria(nelx, nely, x, volfrac, dc)

        # Print Results
        change = np.max(np.abs(x - xold))
        volume = np.sum(x) / (nelx * nely)
        volume = volume.item()
        print('type change:', type(change))
        print('type volume:', type(volume))
        print('type c:', type(c))
        print('type loop:', type(loop))
        # print(f"It.: {loop} Obj.: {c:10.4f} Vol.: {np.sum(x) / (nelx * nely):6.3f} ch.: {change:6.3f}")
        print(f" It.: {loop:4d} Obj.: {c.item():10.4f} Vol.: {volume:6.3f} ch.: {change:6.3f}")

        print('x:',x)
        #Plot Densities
        import matplotlib.pyplot as plt
        plt.imshow(-x, cmap='gray', aspect='equal')
        plt.axis('off')  # Turn off axis
        plt.tight_layout()  # Tight layout to minimize padding
        plt.pause(1e-6)  # Pause for a brief moment
        plt.show()  # Display the plot
        plt.close()

        