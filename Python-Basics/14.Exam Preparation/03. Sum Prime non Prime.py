number = 0
prime = 0
nonprime = 0
while number != "stop":
    count = 0
    number = float(number)
    number = int(number)
    if number < 0:
        print("Number is negative.")
    else:
        if number < 0:
            print(f"Number is negative.")
            number = input()
            continue
        else:
            for i in range(2, number+1):
                if number % i == 0:
                    count += 1
            if count == 1:
                prime += number
            else:
                nonprime += number
            #number%2==0:
            #prime += number
        #else:
            #nonprime += number
    number = input()
print(f"Sum of all prime numbers is: {prime}")
print(f"Sum of all non prime numbers is: {nonprime}")