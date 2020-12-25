

f = open("MyData", 'r')
print(f.read())


p = open("Passport.jpg", 'rb')
p1 = open("Passport_copy.jpg", 'wb')

for i in p:
    p1.write(i)


