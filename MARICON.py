import random
import numpy as np
import pandas as pd

## empty list to append 
x=random.sample(range(1, 10000), 10)

  
  
df = pd.DataFrame(np.random.randint(0,10000,size=(10,500)))

da=[]
for i in range(0,10):
  for j in range(0,500):
    da.append(df.iloc[int(i),int(j)]>x[i])

da2=np.reshape(da,(10,500))

pdata=pd.DataFrame(data=da2)


