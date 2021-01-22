"""
create a list with 4 details about you: name, age, mail, phone and print it to the screen
then create another list with 2 IPs, then add 3 more IPs, pop the 3rd IP and print how many
IPs do we have and print them.
"""

details=["ayelet",41,"mosheayelet@gmail.com","052-888888"]
print("name:" +details[0] + "\nage:"+str(details [1])+ "\nmail:"+ details[2]+ "\nphone: " + details[3])
ips=[23232323,45454545]
print("too ips: "+str(ips))
ips.append(67676767)
ips.append(99999999)
ips.append(77777777)
print("append three ips: "+str(ips))
ips.pop(2)
print("remov three ips: "+str(ips)+"\n"+str(len(ips)))


