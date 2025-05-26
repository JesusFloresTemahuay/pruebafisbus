print("Programa FizBuz hasta el 1,000")

fiz = "FiZZ"
buz = "Buzz"
salida = ""
for counter in range(1, 1000):
    div3 = counter % 3 == 0
    div5 = counter % 5 == 0
    if(div3 or div5):
        if(div3):
            salida = salida + fiz
        if(div5):
            salida = salida + buz
        print(salida)
    else:
        print(counter)
    salida = ""
        

