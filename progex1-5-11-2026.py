#import numpy as np
import math
from prettytable import PrettyTable
from fractions import Fraction
dados=[-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0]
y = True
while y==True:
 print("Opções:")
 print("1)Função exponencial")
 print("2)Função logarítmica")
 print("3)Ambas as funções")
 print("4)Sair")
 opcao = input()
 if opcao=='4':
   y=False
 fx = PrettyTable()
 gx = PrettyTable()
 
 fx.field_names = ["x", "f(x)"]
 gx.field_names = ["x", "g(x)"]
 for x in dados:
    p=Fraction(pow(2,x))
    fx.add_row([x,p])
    gx.add_row([p,math.log(p,2)])
 if opcao=='1' or opcao=='3':
  print(fx)
 if opcao=='2' or opcao=='3':
  print(gx)
