#13 დაწერე პროგრამა, რომელიც ამოწმებს, არის თუ არა რიცხვი უარყოფითი ან  ლუწი.
num = int(input("enter number: "))
if num <= 0 or num % 2 == 0:
    print(True)
