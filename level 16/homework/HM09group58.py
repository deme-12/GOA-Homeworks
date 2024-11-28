# 10) შექმენით პროგრამა, რომელიც მომხარებელს შემოატანინებს წელს და დაპრინტავს რომელი საუკუნეა ის 
years = int(input("enter year"))

century = years // 100
remaining_years = years % 100

if remaining_years == 0:
    print(century)
else:
    print(century)
