while True:
    try:
        n = int(input("Please enter an integer: "))
        break
    except IOError:
        print("Not an integer! Please again")
    except ValueError:
        print("Not an integer! Please again")

print("You successfully entered an integer!")
