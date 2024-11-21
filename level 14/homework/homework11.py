# )დაწერეთ ისეთი პროგრამა რომელიც მომხმარებელს უპრინტავს კვირის დღეს მომხმარებლის შემოტანილი რიცხვის მიხედვით (1 არის ორშაბათი, 2 სამშაბათი და ა.შ) გამოიყენეთ if elif else

day = int(input("enter  number "))
if day == 1:
    print("monday")
elif day == 2:
    print("tuesday")
elif day == 3:
    print("wednesday")
elif day == 4:
    print("thuesday")
elif day == 5:
    print("friday")
elif day == 6:
    print("saturday")
elif day == 7:
    print("sunday")
else:
    print("try again")