numbers = []
for i in range(5):
    num = float(input(f"please enter your scores {i+1} : "))
    numbers.append(num)

avrage = sum(numbers) / len(numbers)
minimal = min(numbers)
maximal = max(numbers)

print(f"your avrage : {avrage}")
print(f"your minimal : {minimal}")
print(f"your maximal : {maximal}")

# varince 

variance = 0

for grade in numbers:
    variance += (grade - avrage)**2

variance = variance / len(numbers)
print(f" your variance : {variance}")
