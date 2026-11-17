# Name: Muhammad Dzaky Yazid
# NIM: 2611531011
# Question 5
#username = input("Username: ")

#if (len(username)) < 5 :
#    print ("Invalid: at least 5 characters")
#elif not username.isalnum():
#    print ("Invalid: letters and digits only")
#elif not (username[0].isalpha()) :
#   print ("Invalid: must start with a letter")
#else :
#    print ("valid")

nim = input("Nim: ")

if (len(nim)) < 10 :
    print ("invalid nim")
elif not (nim.isnumeric()) :
    print ("invalid nim")
else :
    print ("Valid, intake year 20" + nim[:2])