import numpy as np
from sys_identfy import *
import pandas as pd
import matplotlib.pyplot as plt


non_degree = 2
ylag = 2
ulag = 2
ntp = 10
porcent=70
y_caminho='y1.txt'
u_caminho='u1.txt'

[y_ident_,u_ident_,y_valid_,u_valid_] = sys_identfy.prepare_data(y_caminho,u_caminho,porcent)


y=y_ident_
u=u_ident_


model1=sys_identfy(non_degree,ylag,ulag)
w=model1.get_regressmatrx(y,u)
[model, errr, pivv, psi] = model1.ERR(y,w,ntp)
theta=model1.last_squares(psi,y)
reg_code_=model1.reg_code

#print(reg_code_)
#print(w[0:10,0:4])

#yy=psi@theta
#print(theta)
print(model)
print(errr)
print(pivv)
print(theta)
#================================================

"""
y_livre = y[0:model1.max_lag]
for i in range((model1.max_lag),u.size):
    y_livre=np.append(y_livre,theta[0]*y_livre[i-1]+theta[1]*y_livre[i-2]+theta[2]*u[i-1]+theta[3]*y_livre[i-1]*u[i-1]+theta[4]*u[i-2]+theta[5]*y_livre[i-2]*u[i-1]+theta[6]*y_livre[i-1]*u[i-2]+theta[7]*y_livre[i-2]*u[i-2]+theta[8]*y_livre[i-1]*y_livre[i-1]+theta[9]*y_livre[i-2]*y_livre[i-2])
print(y_livre)

y_livre = np.zeros(u.size)
y_livre[0:model1.max_lag] = np.copy(y[0:model1.max_lag])

for i in range((model1.max_lag),u.size):
    y_livre[i]=theta[0]*y_livre[i-1]+theta[1]*y_livre[i-2]+theta[2]*u[i-1]+theta[3]*y_livre[i-1]*u[i-1]+theta[4]*u[i-2]+theta[5]*y_livre[i-2]*u[i-1]+theta[6]*y_livre[i-1]*u[i-2]+theta[7]*y_livre[i-2]*u[i-2]+theta[8]*y_livre[i-1]*y_livre[i-1]+theta[9]*y_livre[i-2]*y_livre[i-2]
print(y_livre)
plt.plot(y_livre)
plt.show()

"""



