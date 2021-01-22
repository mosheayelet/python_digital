num=4567

"""
Alafim = 4
Meot=5
Asarot=6
Ahadot=7
"""
# Alafim
print("Alafim = " +  str(num//1000))

#Meot
num//100
b=(num//100)%10
print("Meot = "+str(b))

#Asarot
c=(num//10)%10
print("Asarot = " + str(c))

#Ahadot
d=(num//1)%10
print("Ahadot = " + str(d))

#shura ahat
print("Alafim = " +  str(num//1000)+"\nMeot = "+str((num//100)%10)+"\nAsarot = " + str((num//10)%10)+"\nAhadot = " + str(d))

while num>0:
    sifra=num%10
    num=num//10
    print (sifra)

