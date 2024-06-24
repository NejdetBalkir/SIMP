import numpy as np
from scipy.sparse import csr_matrix
from scipy.linalg import solve
from stiffness import stiffness 

def FE(nelx, nely, x, penal):
    KE = stiffness()
    print('KE:',KE)
    print('size of KE:',KE.shape)
    K = csr_matrix((2*(nelx+1)*(nely+1), 2*(nelx+1)*(nely+1)))
    F = csr_matrix((2*(nely+1)*(nelx+1), 1))
    print('size of F:',F.shape)
    U = np.zeros((2*(nely+1)*(nelx+1), 1))
    print('size of U:',U.shape)

    for elx in range(0, nelx):
        for ely in range(0, nely):
            print('elx:',elx)
            print('ely:',ely)
            n1 = (nely+1)*(elx) + ely
            n2 = (nely+1)*(elx+1) + ely
            print('n1:',n1)
            print('n2:',n2)
            edof = np.array([2*n1, 2*n1+1, 2*n2, 2*n2+1, 2*n2+2, 2*n2+3, 2*n1+2, 2*n1+3])
            print('edof:',edof)
            K[edof[:, None], edof] = K[edof[:, None], edof] + x[ely, elx]**penal * KE

    # Define loads and supports (half MBB-beam)
    F[2*(nely+1)*(nelx+1)-1,0] = -5
    # fixeddofs = np.union1d(np.arange(0, 2*(nely+1)*(nelx+1), 1), [2*(nelx+1)*(nely+1)-1])
    fixeddofs = np.arange(0,2*(nely+1),1)
    print('fixeddofs:',fixeddofs)
    alldofs = np.arange(0, 2*(nely+1)*(nelx+1))
    print('alldofs:',alldofs)
    freedofs = np.setdiff1d(alldofs, fixeddofs)
    print('freedofs:',freedofs)
    print('type K:', type(K))
    print('K:' , K.toarray())
    print('size of K:', K.toarray().shape)
    print('F:',F.toarray())

    # Solving
    U[freedofs, :] = np.linalg.solve(K[freedofs][:, freedofs].toarray(), F[freedofs].toarray())
    # U[freedofs, :] = solve(K[freedofs][:, freedofs].toarray(), F[freedofs].toarray())
    U[fixeddofs, :] = 0

    print('U:',U)

    return U