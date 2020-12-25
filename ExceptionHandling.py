a = 5
b = 0

try:
    print("resouce is opened")
    k =int(input("Please enter second number"))
    print(a/b)

except ZeroDivisionError as zde:
    print(zde.__repr__())
    print("You can not devide  by 0",zde)
except ValueError as ve:
    print("invalid input",ve)
except Exception as e:
    print("Other error"+e)
    print(e.with_traceback().__format__())

finally:
    print("resource closed")


