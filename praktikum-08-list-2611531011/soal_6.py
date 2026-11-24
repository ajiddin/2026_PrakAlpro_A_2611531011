LAST_DIGIT = 1  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code below
for day in range(1,8):
    expense = int(input(f"Day{day}: "))
    expenses.append(expense)

total = 0
highest = 1
above = 0

for i in range(7    ):
    total += expenses[i]

    if expenses[i] > highest:
        highest = expenses[i]
        highest_day = i + 1

    if expenses[i] > daily_limit:
        above += 1

average = total / 7

print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest})")
print(f"Days above limit: {above}")