# # # ჩატ-ბოტი არის პროგრამა, რომელიც არის შექმნილი ადამიანთან ურთიერთობისთვის. ის იყენებს ხელოვნურ ინტელექტს, რომ გაიგოს შეკითხვა და უპასუხოს მას. ჩატ ბოტემს შეუძლიათ შეკითხვებზე პასუხის გაცემა, პერსონალური რეკომენდაცია(თქვენი შეხედულების მიხედვით შემოგთავაზებენ სხვადასხვა პროდუქტებს და ა.შ)...A


# # თქვენი დავალებაა შექმნათ მარტივი ჩატ-ბოტი, რომელიც კოდის გაშვებისთანავე მიესალმება მომხარებელს და ჰკითხავს "How are your?", თუ მომხარებელი შეიყვანს, "Normal" დაბეჭდეთ "Bot:I hope you will get better", სხვა შემთხვევაში თუ შემოიყვანს "Great", დაუბეჭდეთ "Bot:Good! Have a nice day", ხოლო თუ შემოიყვანა "Sad" ან "Super Sad" დაუბეჭდეთ "Bot:It's sad". საბოლოოდ დაბეჭდეთ "Good bye!" და გათიშეთ while ციკლი. ამისათვის მას გადაეცით სწორი პირობა(მინიშნება: შექმენით ცვლადი რომლის მნიშვნელობა თავიდან იქნება False, while ციკლს პირობად გაუწერეთ ეს ცვლადი, თუ მომხარებელმა სწორი ინფორმაცია შემოიყვანა მისი ნიშვნელობა გახდება True და როცა ყველა პირობა შესრულდება while ციკლი გაითიშება).

# # თუ მომხარებელი შემოიყვანს ისეთ ინფორმაციას რაზეც თქვენი ბოტი არ არის დაპროგრამირებული, დაბეჭდეთ "Bot: Sorry, I didn't understand, repeat."(ამ შემთხვევაში while ციკლისთვის შექმნილი ცვლადის მნიშვნელობა არ იცვლება და ციკლი არ წყვეტს მუშაობას)

# # დაგჭირდებათ: while loop; input; if/else; and or.

# # თქვენი სურვილით დაამატეთ სხვა ფუნქციები და გააუმჯობესეთ ჩატ-ბოტი

# print("hello how are you")
# while True:
#     user_input = input("enter your response")
#     if user_input . lower() == "normal":
#         print("Bot:I hope you will get better")
#     elif user_input . lower() == "great":
#         print("Good have a nice day")
#     elif user_input . lower() == "super sad":
#         print("Bot: it's sad")
#     elif user_input . lower() == "how can i quit the chat?":
#         print("please enter exit")
#     elif user_input . lower() == "exit":
#         print("goodbye")
#         break
#     else:
#         print("sorry i didn't understand please repeat")


# print("hello how are you")
# chat_active = True
# while chat_active:
#     user_input = input("enter your response")
#     if user_input . lower() == "normal":
#         print("Bot:I hope you will get better")
#     elif user_input . lower() == "great":
#         print("Good have a nice day")
#     elif user_input . lower() == "super sad":
#         print("Bot: it's sad")
#     elif user_input . lower() == "how can i quit the chat?":
#         print("please enter exit")
#     elif user_input . lower() == "exit":
#         print("goodbye")
#         break
#     else:
#         print("sorry i didn't understand please repeat")