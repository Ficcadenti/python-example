import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

print('Machine Learning - Regressione lineare (1 variabile indipendente) !!!!')


df = pd.DataFrame({'stud': [1,2,3,4,5,6,4,1,2,1,3],'red':[12000,23000,35000,47000,55000,67000,43000,15000, 25000,15000,31500]})
print(df)

plt.plot(df['stud'],df['red'],'ro')
plt.show()

mat=np.matrix(df)
x=mat[:,0]
y=mat[:,1]
print(mat)
print('x=',x)
print('y=',y)

lr = LinearRegression()
print(lr.fit(x,y))
print(lr.score(x, y))
print('Intercept=',lr.intercept_)
print('Coefficente=',lr.coef_)

# Predizione per titolo di studio liv=4
print('Predizione stipendio per titolo di studio liv=4 --> ',lr.predict([[4]]))
print('Predizione stipendio per titolo di studio liv=2 --> ',lr.predict([[2]]))


