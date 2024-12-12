def fizz_buzz(n):
   
    for i in range(1, n + 1):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if output == "":
            print(i)
        else:
            print(output)



fizz_buzz(17)