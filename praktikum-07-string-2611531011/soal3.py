# Name: Muhammad Dzaky Yazid
# NIM: 2611531011
# Question 3 (B)
text = "Muhammad Dzaky Yazid"
count = 0
for char in text:
    if char in "AIUEOaiueo":
        count = count + 1
print("Vowels:", count)
