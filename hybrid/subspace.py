import numpy as np
from cvxpy import *
import matplotlib.pyplot as plt

def subspace(X, gt, set_gamma, set_K, norm_sub, plotter, printer):
    print('hello from subspace')
    
    ### Subspace Clustering ###
    # Solve for each point as a linear system with respect to all other points 
    # using convex optimization routines  
    # Basically, we express each point as a linear combination of the other points...
    # Here we try to minimize the dot-product between the coefficients.
    # Sparsity is only needed in dot-product space in-so-far as possible.

    # transpose X
    A = np.transpose(X)
    if printer: print('A =\n', A)    
    if printer: print('shape of A =', np.shape(A))
        
    # coefficent matrix
    coeff = np.zeros([np.shape(A)[1],np.shape(A)[1]])
    if printer: print('coeff =\n', coeff)

    if printer: print('\n************************************************' +
                      '\n            Solve for coefficents')    
    for i in range(np.shape(A)[1]):
        b = A[:,i]
        if printer: print('b =\n', b)

        # gamma must be positive due to DCP rules.
        # Can change to cvxpy.Parameter
        gamma = Parameter(nonneg="true")
        constraints = None

        # Construct the problem.
        x = Variable(np.shape(A)[1])
        if printer: print('x =\n', x)

        ## Lasso
        obj = Minimize(gamma*norm(A@x-b,2) + norm(x, 1))
        constraints = [x[i] == 0]
        if printer: print(constraints)
        ## constraints = [x[i] == 0, sum(x) == 1]

        ## L1-Perfect
        ## obj = Minimize(norm(x, 1))
        ## constraints = [A*x == b, x[i] == 0, sum(x) == 1]
        ## L1-Noisy
        ## obj = Minimize(norm(x, 1))
        ## constraints = [ A*x - b <= gamma, x[i] == 0, sum(x) == 1 ]

        if [constraints == None]:
            prob = Problem(obj)
        else:
            prob = Problem(obj, constraints)

        ## From the original code
        gamma.value = set_gamma
        prob.solve(solver='ECOS')

        coeff[:,i] = np.transpose(x.value)
        if printer: print('coeff =\n', coeff)
            
    if printer: print('\n************************************************' +
                      '\n         Done solving for coefficents\n')

    ## Refine results...
    ## Only use magnitude of the coefficients (no negative values)
    coeff = np.abs(coeff)
    if printer: print('abs of coeff =\n', coeff)
    
#     ## Normalize each row - not needed but doesn't hurt on most examples
#     if norm_sub: coeff = coeff / np.apply_along_axis(np.max,1,coeff)[:,None]
#     if printer: print('norm of coeff =\n', coeff)
        
    ## Symmetrize
    coeff = coeff + np.transpose(coeff)
    if printer: print('symmetrize coeff =\n', coeff)
        
    if set_K == 0:
        K = np.shape(A)[1]
    else:
        if set_K > np.shape(A)[1]:
            print('Max K =', np.shape(A)[1], ', please set K to a lower value.')
        else:
            K = set_K
    if printer: print('K =', K)

    # Select the top K coefficients
    newcoeff = np.zeros(np.shape(coeff))
    if printer: print('newcoeff =\n', newcoeff)
    
    if printer: print('coeff =\n', coeff)
        
    indices = np.apply_along_axis(lambda x: np.argsort(x)[::-1],1,coeff)[:,range(K)]
    if printer: print('indices =\n', indices)

    for x in range(np.shape(coeff)[0]):
        newcoeff[x,indices[x,:]] = coeff[x,indices[x,:]]
    if printer: print('newcoeff =\n', newcoeff)
        
#     # Normalize each row - again, not really needed
#     newcoeff = newcoeff / np.apply_along_axis(np.max,1,newcoeff)[:,None]
#     if printer: print('norm newcoeff =\n', newcoeff)
    
    ## Symmetrize
    newcoeff = newcoeff + np.transpose(newcoeff)
    if printer: print('symmetrize newcoeff =\n', newcoeff)

    ## Standard...
    sub_aff = newcoeff
    
    ## Get row sums
    sub_aff_D = np.diagflat(1.0 / np.sqrt(np.apply_along_axis(np.sum,0,sub_aff)))
    if printer: print('sub_aff_D =\n', sub_aff_D)
    
    ## Normalization
    sub_norm = np.matmul(np.matmul(sub_aff_D,sub_aff),sub_aff_D)
    if printer: print('sub_norm =\n', sub_norm)
        
    if norm_sub:
        aff_sub = sub_norm
    else:
        aff_sub = sub_aff
    if printer: print('aff_sub =\n', aff_sub)
        
    #######################################################################
    # plotting the strenghts
#     print(X)
    if plotter:
        if X.shape[1] == 2:
            for i in range(X.shape[0]):
                for j in range(X.shape[0]):
                    if i==j: continue
                    print(i,j)
                    print(aff_sub[i,j])
                    if gt[i] == 0:
                        plt.plot(X[[i,j],0],X[[i,j],1], color='red', alpha=aff_sub[i,j])
                    else:
                        plt.plot(X[[i,j],0],X[[i,j],1], color='blue', alpha=aff_sub[i,j])
#                     plt.plot(X[[i,j],0],X[[i,j],1], color='red', alpha=aff_sub[i,j])
            plt.scatter(X[:,0], X[:,1], color = [["red", "blue"][i] for i in gt])
#             plt.title('Ground Truth: ' + problem )
            plt.title('Subspace Connections' )
            plt.ylabel('y')
            plt.xlabel('x')
            plt.show()
            
    if plotter:
        plt.imshow(aff_sub)
        plt.show()
        
    return(aff_sub)
