try:
    n1 = int(input("enter first number:"))
    n2 = int(input("enter second number:"))
    n3 = n1 / n2
    print("output is:", n3)
except Exception as ex:
    print(ex)


# except ZeroDivisionError as er:
#     print(er)
# except ValueError as er:
#   print(er)