#The purpose of this program is to find the sum of all even valued elements of the fibonacci sequence up to four million.
digits = [1,2]
while(digits[-1] + digits[-2] < 4000000):
    digits.append(digits[-1]+digits[-2])
    print(digits[-1])
print(digits)
final_sum = 0
for number in digits:
    if number % 2 == 0:
        print(f"{number}")
        final_sum = final_sum + number
print(final_sum)