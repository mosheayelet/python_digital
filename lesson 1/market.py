# a program that get a shopping basket from the outside and consider how much it costs.
# tomato cucumber kola chicken
# the program calculate the price payment after value tax And no residue.
tax = 1.17
tomato = 3
cucumber = 2
kola = 5
chicken = 20
print("Cost of products in Market" + "\n........."+"\ntomato= 3"+"\ncucumber= 2"+"\nkola= 5"+"\nchicken= 20"+"\n.........\nyor order:" )
amount_tomato = int(input("enter amount of tomato: "))
amount_cucumber = int(input("enter amount of cucumber:  "))
amount_kola = int(input("enter amount of kola:  "))
amount_chicken = int(input("enter amount of chicken:  "))
print ("You nid to pay: NIS " + str(((amount_tomato*tomato)+(amount_cucumber*cucumber)+(amount_kola*kola)+(amount_chicken*chicken))))
print ("You nid to pay and tax: NIS " + str(((amount_tomato*tomato)+(amount_cucumber*cucumber)+(amount_kola*kola)+(amount_chicken*chicken))*tax//1))
