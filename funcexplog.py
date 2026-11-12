import math
import os
if os.name=='nt':
 clear = lambda: os.system('cls')
else:
 clear = lambda: os.system('clear')
dados=[-3.0,-2.0,-1.0,0.0,1.0,2.0,3.0]
opcao = '0'
clear()
while True:   
 print("Opções:")
 print("1)Função exponencial")
 print("2)Função logarítmica")
 print("3)Ambas as funções")
 print("4)Sair") 
 if opcao=='4':
   clear()
   break
 fx = []
 gx = []
 for x in dados:
    p=pow(2,x)
    fx.append([x,p])
    gx.append([p,math.log(p,2)])
 if opcao=='1' or opcao=='3': 
  print(" ")
  print("-" * 20)
  print(f"{'f(x)=2\u02e3':<5}")
  print("-" * 20)
  print(f"{'x':<10} {'f(x)':<10}")
  print("-" * 20)
  for row in fx:
    print(f"{row[0]:<10} {row[1]:<10}")
 if opcao=='2' or opcao=='3':    
  print(" ")
  print("-" * 20)
  print(f"{'g(x)=log\u2082x':<5}")
  print("-" * 20)
  print(f"{'x':<10} {'g(x)':<10}")
  print("-" * 20)
  for row in gx:
    print(f"{row[0]:<10} {row[1]:<10}")
 print(" ")
 opcao = input("Digite a opção desejada: ") 
 clear()
