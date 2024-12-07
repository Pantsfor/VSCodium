from colorama import Fore
from colorama import Style

# The purpose of this program is to find the sum of all numbers between 1 and 1000 that are multiple of 3 and 5
x = 1
eligible = []
while x < 1000:
    if ((x % 3) == 0) or ((x % 5) == 0):
        eligible.append(x)
        x += 1
    else:
        x +=1
sum = 0
for number in eligible:
    sum = sum + int(number)

print(f"{Fore.CYAN}The entire set of multiples of 3 or 5 below 1000 includes:\n{Style.RESET_ALL}" + str(eligible))
print(f"{Fore.CYAN}The number of elements that meet these qualifications are:\n{Style.RESET_ALL}" + str(len(eligible)))
print(f"{Fore.CYAN}The sum of all of these elements are:\n{Style.RESET_ALL}" + str(sum))