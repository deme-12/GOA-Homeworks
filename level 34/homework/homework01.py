# ## დაასრულეთ საკლასო დავალებები: 
# ```1) შექმენით manual_replace ფუნქცია, რომელიც იქნება .replace() ფუნქციის კლონი. ამ ფუნქციამ სთრინგში არსებული sapce-ები უნდა შეცვალოს ტირეებად.
# არ გამოიყენოთ ჩაშენებული ფუნქციები და კომენტარებით ახსენით მე-4 დავალება```

def manual_replace(string1):
    new_string = ""
    for letters in string1:
        if letters == " ":
            new_string += "-"
        else:
            new_string += letters
    return new_string

print(manual_replace("daad ada ada da ad"))

