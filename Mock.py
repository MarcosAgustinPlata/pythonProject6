def mo():
    while True :
        number = input( "Please give me a multiple of 6 numbers")
        number= int(number)
        if number % 6 ==0:
            return number
        print("That number is not a multiple of 6. Retry")

