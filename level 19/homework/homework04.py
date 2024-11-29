# 4) შექმენით ცვლადი სადაც შეინახავთ სთრინგს და გაიგეთ, არის თუ არა ის პალინდრომი(პალინდრომი არის ისეთი სიტყვა, რომელიც ორივე მხრიდან ერთნაირად იკითხება, მაგალითად, "ana"...)

name = "deme"

if name == name[::-1]:
    print("palidrome")
else:
    print("not palidrome")


name = "ana"

if name == name[::-1]:
    print("palidrome")
else:
    print("not palidrome")
