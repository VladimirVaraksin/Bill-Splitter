import random

people = int(input("Enter the number of friends joining (including you): "))
if people < 1:
    print("No one is joining for the party")
else:
    friends_dict = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for x in range(people):
        friends_dict[input()] = 0
    bill = int(input("Enter the total bill value: "))
    pers_bill = round(bill / people, 2)
    for friend in friends_dict.keys():
        friends_dict[friend] = pers_bill
    lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    if lucky_feature == "Yes":
        index = random.randint(0, people-1)
        person = list(friends_dict.keys())[index]
        print(person + " is the lucky one!")
        pers_bill = round(bill / (people-1), 2)
        for friend in friends_dict.keys():
            if friend == person:
                friends_dict[friend] = 0
            else:
                friends_dict[friend] = pers_bill
    else:
        print("No one is going to be lucky")
    print(friends_dict)