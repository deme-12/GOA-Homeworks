# ლოგიკური ოპერატორები

# ლოგიკური გადაწყვეტილებები

# and - და
# or - ან

# true, false



print(True and True) # true
print(True and False) # false
print(False and True) # false
print(False and False) # false

print(True or True) # true
print(True or False) # true
print(False or True) # true
print(False or False) # true


print(10 > 5 and 10 > 7)
print(10 > 8 and 10 < 8)
print(10 >= 10 and 8 <= 8)
print(20 > 20 and 15 < 20)

print(10 > 20 or 10 > 5)
print(10 < 5 or 5 < 3)
print(20 > 15 or 20 > 25)
print(10 < 9 or 10 < 11)


# ინდენტაცია - კიდედან დაშორება

age = int(input("enter your number: "))

if age > 18:
    print("შენ ხარ სრულწლოვანი: ")
else:
    print("არხარ სრულწლოვანი")

# მომხმარებელს შევეკითხოთ რომელ აკადემიაში სწავლობს და შესაბამისად გავცეთ პასუხი

user_answer = input("რომელ აკადემიაში სწავლობ?: ")

if user_answer == "goa"  or user_answer == "goal-oriented-academy" or user_answer == "GOA":
    print("შენ ხარ chad!")
elif user_answer == "it step":
    print("")
else:
    print("virjin")
