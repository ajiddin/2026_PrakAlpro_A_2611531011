PASS_SCORE = 65

n = int(input("Number of students: "))
while n < 1:
    print("Invalid!")
    n = int(input("Number of students: "))

total = 0       
passed = 0      
lowest = 100    


for i in range(1, n + 1):
    print("Student", i)
    score = int(input("Enter score: "))

    
    while score < 0 or score > 100:
        print("Invalid score!")
        score = int(input("Enter score: "))

    total += score

    
    if score >= PASS_SCORE:
        passed += 1

    
    if score < lowest:
        lowest = score

average = total / n

print(f"Total score: {total}, Average score: {round(average, 2)}")
print(f"Passed: {passed}")
print(f"Lowest score: {lowest}")