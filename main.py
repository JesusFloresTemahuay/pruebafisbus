print("Programa FizBuz hasta el 1,000")

FIZZ = "FiZZ"
BUZZ = "Buzz"
out = ""

for counter in range(1, 1000):

    is_divisible_3 = counter % 3 == 0
    is_divisible_5 = counter % 5 == 0

    if(is_divisible_3):
        out = out + FIZZ

    if(is_divisible_5):
        out = out + BUZZ
    
    if(len(out) > 0):
        print(out)
    else:
        print(counter)

    out = ""
        
