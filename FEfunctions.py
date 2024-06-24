import numpy as np

def QuadStiffnessMatrix(E, nu):
    #OBJECTIVE: To obtain the stiffness matrix for a quadrilateral element
    #INPUTS:
        # E: Young's modulus
        # nu: Poisson's ratio
        # D: Constitutive matrix
    #OUTPUT:
        # K: Stiffness matrix

    #Formula for the element stiffness matrix:
    # K = B^T * C * B * det(J)
    # B: Strain-displacement matrix
    # C: Constitutive matrix
    # J: Jacobian matrix

    
    return K


def ConstitutiveRelation(E, nu):
    # E: Young's modulus
    # nu: Poisson's ratio
    # D: Constitutive matrix

    # CONSTITUTIVE RELATION FOR PLANE STRESS CONDITIONS
    C = E/(1-nu**2) * np.array([[1, nu, 0],
                                 [nu, 1, 0],
                                 [0, 0, (1-nu)/2]])
    
    return C

def ShapeFunctions(x1, x2):
    #OBJECTIVE: To obtain the shape functions for a quadrilateral element
    #INPUTS:
        # x1: Natural coordinate in the x-direction
        # x2: Natural coordinate in the y-direction
    #OUTPUT:
        # N: Shape functions

    #Shape functions for a quadrilateral element:
    N = 1/4 * [(1-x1)*(1-x2), 
               (1+x1)*(1-x2), 
               (1+x1)*(1+x2), 
               (1-x1)*(1+x2)]

    dN = 1/4 * [[(-1 + x2) , (-1 + x1)],
                [( 1 - x2) , (-1 - x1)],
                [( 1 + x2) , ( 1 + x1)],
                [(-1 - x2) , ( 1 - x1)] ]
    
    return N , dN

def JacobianMatrix(x1, x2, X):
    #OBJECTIVE: To obtain the Jacobian matrix for a quadrilateral element
    #INPUTS:
        # x1: Natural coordinate in the x-direction
        # x2: Natural coordinate in the y-direction
        # X: Nodal coordinates
    #OUTPUT:
        # J: Jacobian matrix

   
    J = 
    
    return J
