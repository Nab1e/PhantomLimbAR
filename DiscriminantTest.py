import numpy as np
import pandas as pd
df = pd.read_csv('coeff_dataa.csv')
#type = df['type']  # Replace 'ColumnName' with the actual column name
const = df['Const']
K = np.array(const)
#lin1 = df['linear_1']

#L = [[l1, l2, l3] for l1 in lin1 for l2 in lin2 for l3 in lin3]

columns = [f'Linear_{i}' for i in range(1, 13)]
linear_data = df[columns]

# Convert the data to a list of lists (matrix)
matrix = linear_data.values.tolist()
print("matrixx")
L = np.array(matrix)
nM = 10

L = L.reshape(nM , nM , 12)
K = K.reshape(10,10)

def DiscriminantTest(tSet):
    nM = 10
    tempRes = np.zeros((nM, nM))
    tSet = np.transpose(np.reshape(tSet, (3, 4)))
    #print(K.shape)
    #print(L.shape)
    #print(tSet.shape)
    print("dsds")
    print(tSet)
    #print(tSet.ravel())


    #for k in range(nM*nM): 
   #     print("shapes")
   #     print(L[k].shape)
   #     print(tSet.shape)
   #     print("shapes")
    for i in range(nM):
        for j in range(nM):
            if(np.isnan(K[i][j])):
                K[i][j] = 0
                L[i][j] = 0
            tempRes[i][j] = K[i][j] + np.dot(tSet.ravel(), L[i][j])  # k + f1*L1 + f2*L2 ......

       # tempRes[k] = K[k] + np.dot(tSet.ravel(), L[k])  # k + f1*L1 + f2*L2 ......
    #tempRes = np.reshape(tempRes, (nM, nM))



    outVector = np.sum(tempRes, axis=1)
    outMov = np.argmax(outVector)
    maxV = outVector[outMov]
    print(outVector)
    print("predd")
    print(outMov)
    print(maxV)
    #print("predd")

    return outMov, outVector