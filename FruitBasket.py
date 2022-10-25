basket = []

print("Catch and eat any of these fruits: ('apple', 'orange', 'mango', 'guava')")
catch = int(input("How many fruits would you like to catch?: "))
print("Choose a fruit to catch. Press A, O, M, or G.")

for i in range(catch):
    i+=1
    a = input("Fruit " + str(i) + " of " + str(catch) + ": ")
    if str.upper(a) == 'A':
        basket.append("apple")
        
    elif str.upper(a) == 'O':
        basket.append("orange")
            
    elif str.upper(a) == 'M':
        basket.append("mango")
            
    elif str.upper(a) == 'G':
        basket.append("guava")
            
    else:
        print("Invalid input")
        
print("Your basket now has: ", basket)

while True:
    eat = input("Press E to eat Fruit: ")
    
    if eat.upper() == 'E':
        basket.pop()
        
        if not basket:
            print("No more Fruits.")
            break
        print("Fruit(s) in the basket: ", basket)