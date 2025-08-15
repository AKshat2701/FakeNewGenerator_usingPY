# import random module 
import random 

#Create subject
subjects = [
            "shahrukh Khan", 
            "Virat Kohli",
            "Nirmala Sitaraman",
            " A Mumbai cat",
            "A group of monkey",
            "Prime Minister Modi",
            "Auto Rikshaw Driver from delhi"
            ]
 
actions = [
    "launches",
    "cancels",
    "Dances with",
    "eats",
    "declare wars on",
    "Orders",
    "celebrates"
]

places_or_things = [
    "At red fort",
    "Mumbai local train",
    "a plate of samosa",
    "inside parliament",
    "at ganga ghat",
    "during IPL match",
    "at india gate"
]
#start the headline generation loop

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\n Do you want another headline? (Yes/No).strip()")
    if user_input == "No":
        break 
 
 #print goodbye message
print("\nTHanks for using the fake news Headline generator , have a fun time")