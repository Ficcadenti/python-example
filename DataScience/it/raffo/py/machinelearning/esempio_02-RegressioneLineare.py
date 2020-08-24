import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import r2_score

'''
https://archive.ics.uci.edu/ml/machine-learning-databases/housing/
'''

print('Machine Learning - Regressione lineare (2 variabile indipendente) !!!!')

from sklearn.datasets import load_boston
boston=load_boston()

print(boston.data)
print(boston.target)
print(boston.DESCR)

boston2=pd.DataFrame(boston.data)
boston2.columns=boston.feature_names
print(boston2.head(5))

price=pd.DataFrame(boston.target)
print(price.head(5))
'''
plt.hist(price[0],bins=20)
plt.xlabel('Prezzo delle case')
plt.ylabel('Numero di case')
'''


print(boston2.shape)
print(price.shape)

df=pd.concat([boston2,price],axis=1)
df=df.rename(columns={0:'price'})
print(df.head(5))

lr=LinearRegression()
x_train, x_test, y_train, y_test = train_test_split(df.iloc[:, :13], df['price'], test_size = 0.3)


lr.fit(x_train,y_train)
pred = lr.predict(x_test)
plt.scatter(y_test,pred)

plt.plot(y_test,'b*')
plt.plot(pred,'g^')
plt.show()
print(lr.coef_)

coefficienti = pd.DataFrame(lr.coef_, boston2.columns, columns=['coefficienti'])

print('train: ',x_train.shape,y_train.shape,x_test.shape,y_test.shape)
print('coefficienti : ',coefficienti)
print('MAE:', metrics.mean_absolute_error(y_test, pred))
print('MSE:', metrics.mean_squared_error(y_test, pred))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, pred)))

r2=r2_score(y_test,pred)
print('R^2 : ',r2)



