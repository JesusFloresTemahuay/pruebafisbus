print("Programa FizBuz hasta el 1,000")

fiz = "FiZZ"
buz = "Buzz"
salida = ""
for counter in range(1, 1000):
    
    is_div3 = counter % 3 == 0
    is_div5 = counter % 5 == 0

    if(is_div3):
        salida = salida + fiz
    if(is_div5):
        salida = salida + buz
    
    if(len(salida) > 0):
        print(salida)
    else:
        print(counter)

    salida = ""
        
