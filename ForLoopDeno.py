x=[1,2,'Yogesh',55.5]
for i in x:
    print(i)

for i in range(1,10):
    print(i,end=",")

#   # # # #
#   # # # #
#   # # # #
#   # # # #
print()

for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print()

    ##########################################
    #
    # #
    # # #
    # # # #

for i in range(4):
    for j in range(i+1):
        print("#",end=" ")
    print()
    
print()

for i in range(4):
    for j in range(i,4):
        print("#", end=" ")
    print()