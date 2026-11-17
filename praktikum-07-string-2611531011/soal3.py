# Name: Muhammad Dzaky Yazid
# NIM: 2611531011
# Question 3 (A)
text = "Algoritma dan Pemrograman"
count = 0
for char in text.lower():
    if char in "aiueo":
        count = count + 1
print("Vowels:", count)
