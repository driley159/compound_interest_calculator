# compound interect calculator
principle = 0
rate = 0
time = 0
#asks for priciniple input and resets code if there is an improper entry
while int(principle) <= 0:
    principle = input("enter the principle amount: ")
    if not int(principle) > 0:
        print("principle can't be less the zero, please try again")
# asks for desired rate and resets if there is an impropr entry
while int(rate) <= 0:
    rate = input("enter rate amount: ")
    if not int(rate) > 0:
        print("rate cannot be less then or equal to zero")
        rate = input("enter rate amount: ")
# asks for desired time and resets if there is an impropr entry
while int(time) <= 0:
    time = input("enter time amount: ")
    if not int(time) > 0:
        print("time cannot be less then or equal to zero")
        time = input("enter time amount: ")
# shows the amount you would have after the desired time:
total = principle * pow((1 + rate / 100), time)
print("Your final total is: " + total)
