""""create dictionary with 5 name & money
then sum the money of the first & last name and print it too the screen
after add a new name with the sum of the money you calculated before
in the end, print the number of entries and check if "idan" is inside.
"""

name_money={"ayelet":100000,"shaul":75000,"yael":50000,"roni":90000,"avi":40000}
print(name_money)
name_money2=(name_money["ayelet"]+name_money["avi"])
#print("sum money ayelet and avi: "+ str(name_money["ayelet"]+name_money["avi"]))
print("sum money ayelet and avi: "+str(name_money2))
name_money.update({"noam":name_money2})
print(name_money)
print("sum entries: "+str(len(name_money)))
print("idan" in  name_money)
