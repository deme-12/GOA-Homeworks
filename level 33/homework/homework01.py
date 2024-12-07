#A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?

# Return true if yes, false otherwise :)


def hero(bullets, dragons):
    bullets_needed = dragons * 2  # აქ განვაახლეთ ცვლადი რომელსაც მივანიჭეთ ახალი მნიშვნელობა dragons * 2  ტყვიების რაოდენობა უნდა იყოს დრაკონების რაოდენობაზე 2 ჯერ მეტი
    if bullets >= bullets_needed: # ვადარებთ თუ ტყვიების რაოდენობა არის დრაკონების რაოდენობაზე მეტი ან ტოლი, (bullet_needed)  ამ შემტხვევაში hero გადარჩება, და return დაბრუნდება True სხვა შემთხვევაში დაბრუნდება False
        return True
    else:
        return False
    




