# create 2 variables: string of your full name, another string of your mail.
# create variable of your age (integer)
# print all of them to the screen.

# then print your name from the eand to the beginning and print it only with your age*3

# then check if your full name is stored inside this full string:
# "ayelet ben dudu yoval shimon gal shahar yana"

a="ayelet leiman"
b="mosheayelet@gmail.com"
c=40
d="ayelet"
e="ayelet ben dudu yoval shimon gal shahar yana"

print("full name: "+"a" + "\nyor mail: "+"b"+ "\nyor age:"+str(c*3))
print(".......")
print(d[::-1])
print(".......")
print("ayelet" in e)
