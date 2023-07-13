print ("""salários abaixo de 128.000.00 percentagem é de 20%
salários entre 128.000.00 a 500.000.00 aumento é de 15%
salários entre 500.000.00 a 1.000.000.00 o ajuste é de 10%
salário acima de 1.000.000.00 tem um ajuste de 5%""")

salário=float(input("informe o seu salário: "))
if salário < 128000:
   percentagem=0.2
   aumento=salário*percentagem
   novo_salário=salário+aumento
elif salário>=128000 or salário<=500000:
     percentagem=0.15
     aumento=salário*percentagem
     novo_salário=salário+aumento
elif salário>=500000 or salário<=1000000:
    percentagem=0.1
    aumento=salário*percentagem
    novo_salário=salário+aumento
else:
    percentagem =0.05
    aumento=salário*percentagem
    novo_salário+aumento
print("Salário antes do reajustes",salário)
print ("percentagem:",percentagem)
print ("Aumento ao ser aplicado:",aumento)
print ("Novo salário",novo_salário)
        
     
