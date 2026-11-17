# Name: Muhammad Dzaky Yazid
# NIM: 2611531011
# Question 7
name = input("name: ")
nim = input("nim: ")
username = name.strip().lower()[:8] + nim[-3:]
intake = "20" + nim[:2]

print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print(f"{'Name':10}" + ": ", name.title())
print(f"{'Nim':10}" + ": ", nim)
print(f"{'Username':10}" + ": ", username)
print(f"{'Intake':10}" + ": ", intake)
print("=" * 30)