## Rooms
# Hallway
def hallway():
    pass

# Master Bedroom
def master_bedroom():
    print("""\n    You enter the master bedroom. Looking around, you see a partially open drawer at a 
    bedside table, a bottle poking out from under a pillow, and a laptop on the edge of the bed.""")
    options = {"drawer", "bottle", "laptop"}

    choice = input("\n    Do you wish to examine the drawer, bottle or laptop first? > ").strip().lower()
    if choice in options:
        options.remove(choice)
        if choice == "drawer":
            drawer()
        elif choice == "bottle":
            bottle()
        elif choice == "laptop":
            laptop()
        
        while True:
            next_choice = input(f"\n    Do you wish to examine the {' or '.join(options)} next? > ").strip().lower()
            if next_choice in options:
                options.remove(next_choice)
                if next_choice == "drawer":
                    drawer()
                elif next_choice == "bottle":
                    bottle()
                elif next_choice == "laptop":
                    laptop()
                
                final_choice = options.pop()
                print(f"\n    You now examine the {final_choice}.")
                if final_choice == "drawer":
                    drawer()
                elif final_choice == "bottle":
                    bottle()
                elif final_choice == "laptop":
                    laptop()
                break
            else:
                print(f"\n    Invalid choice, type either {' or '.join(options)}.")
    else:
        print("\n    Invalid choice, type either 'drawer', 'bottle', or 'laptop'.")
        master_bedroom()

# Bathroom
def bathroom():
    print("""\n    The bathroom is cold and you catch faint red stains in the bathtub. A metallic hydrogen 
    peroxide smell lingers in the air. You spot a towel in the corner and shreds of paper in the bin. """)
    options = {"towel", "bin"}

    choice = input("\n    Do you wish to examine the towel or bin first? > ").strip().lower()
    if choice in options:
        if choice == "towel":
            towel()
            print(f"\n    You now examine the bin.")
            bin()
        elif choice == "bin":
            bin()
            print(f"\n    You now examine the towel.")
            towel()
    else:
        print("\n    Invalid choice, type either 'towel' or 'bin'.")
        bathroom()

# Bedroom
def bedroom():
    print("""\n    The air in Emily's bedroom feels thick and heavy. A journal sits atop her desk, and 
    infront of it is a corkboard filled with photos. You also spot her phone face-down on the bed.""")
    options = {"journal", "corkboard", "phone"}

    choice = input("\n    Do you wish to examine the journal, corkboard or phone first? > ").strip().lower()
    if choice in options:
        options.remove(choice)
        if choice == "journal":
            journal()
        elif choice == "corkboard":
            corkboard()
        elif choice == "phone":
            phone()
        
        while True:
            next_choice = input(f"\n    Do you wish to examine the {' or '.join(options)} next? > ").strip().lower()
            if next_choice in options:
                options.remove(next_choice)
                if next_choice == "journal":
                    journal()
                elif next_choice == "corkboard":
                    corkboard()
                elif next_choice == "phone":
                    phone()
                
                final_choice = options.pop()
                print(f"\n    You now examine the {final_choice}.")
                if final_choice == "journal":
                    journal()
                elif final_choice == "corkboard":
                    corkboard()
                elif final_choice == "phone":
                    phone()
                break
            else:
                print(f"\n    Invalid choice, type either {' or '.join(options)}.")
    else:
        print("\n    Invalid choice, type either 'journal', 'corkboard', or 'phone'.")
        bedroom()
# Kitchen
def kitchen():
    print("""\n    The kitchen is warm and inviting, with the faint aroma of coffee lingering in the air. 
    A knife block sits backfacing on the counter, and a receipt is found on the dining table.""")
    options = {"knife block", "receipt"}

    choice = input("\n    Do you wish to examine the knife block or receipt first? > ").strip().lower()
    if choice in options:
        if choice == "knife block":
            knife_block()
            print(f"\n    You now examine the receipt.")
            receipt()
        elif choice == "receipt":
            receipt()
            print(f"\n    You now examine the knife block.")
            knife_block()
    else:
        print("\n    Invalid choice, type either 'receipt' or 'knife block'.")
        kitchen()

# Living Room
def living_room():
    print("""\n    The living room feels homely and lived in. A coffee table sits cluttered with papers, 
    and a mantle above the fireplace displays photographs and awards.""")
    options = {"coffee table", "photographs"}

    choice = input("\n    Do you wish to examine the coffee table or photographs first? > ").strip().lower()
    if choice in options:
        if choice == "coffee table":
            coffee_table()
            print(f"\n    You now examine the photographs.")
            photographs()
        elif choice == "photographs":
            photographs()
            print(f"\n    You now examine the table.")
            coffee_table()
    else:
        print("\n    Invalid choice, type either 'coffee_table' or 'photographs'.")
        living_room()

# Backyard
def backyard():
    print("""\n    The backyard is dimly lit, with overgrown grass rustling in the faint breeze. You feel 
    the air getting heavier; you're standing in front of the crime scene after all. You see bloodied grass 
    with a patch of disturbed soil beside it. \n    You take a step forward and gasp. A bloodied knife 
    pokes through the soil. 'So detective, who do you think it is?' You jump at a voice from behind, but 
    it's just the officer back to take your statement.""")
    options = {"john", "margaret", "lucas", "emily"}
    
    while True:
        choice = input("\n    Who was the murderer? > ").strip().lower()
        if choice in options:
            if choice == "john":
                print("""\n    Not quite. John had motive, but the evidence doesn't add up. The knife was buried 
            in the backyard and bloodied, pointing to a rushed cleanup effort. Combined with Emily's journal 
            and Lucas's text, Lucas was the one who took desperate measures to silence her.""")

            elif choice == "margaret":
                print("""\n    Nope. Apart from the prescription pills which Emily voluntarily stole and ate, and 
            the self-help book suggesting a strained mother-daughter relationship, nothing else suggests 
            that Margaret was the culprit.""")

            elif choice == "lucas":
                print("""\n    Bingo! He knew Emily would expose his role in John's crimes, and he probably couldn't 
            risk his entire future. His desperation led him to plan her murder as evidenced by the text and 
            Emily's journal.""")
                break
            else:
                print("""\n    You really thought Emily killed herself with the knife, buried her own body and then 
            the knife? Man, how did you get famous as a detective anyway?""")
        else:
            print("\n    Invalid choice, the murderer can only be any of the aforementioned character's names.")
    
    print("""\n    Thanks for playing!""")    
        


## Room choices and functions
rooms = {
    'Hallway': ['Master Bedroom', 'Bedroom'],
    'Master Bedroom': ['Bathroom', 'Hallway'],
    'Bathroom' : ['Master Bedroom'],
    'Bedroom': ['Hallway'],
    'Kitchen': ['Living Room', 'Hallway'],
    'Living Room': ['Kitchen', 'Backyard'],
    'Backyard': ['Living Room']
}

room_functions = {
    'Hallway': hallway,
    'Master Bedroom': master_bedroom,
    'Bathroom': bathroom,
    'Bedroom': bedroom,
    'Kitchen': kitchen,
    'Living Room': living_room,
    'Backyard': backyard
}

## Track visited rooms
visited_rooms = set()

## Room movement system
def prompt(current_room):
    
    if current_room not in visited_rooms:
        visited_rooms.add(current_room)
        room_functions[current_room]()

    if current_room == 'Hallway' and 'Master Bedroom' in visited_rooms and 'Bedroom' in visited_rooms:
        if 'Kitchen' not in rooms['Hallway']:
            rooms['Hallway'].append('Kitchen') 
            print("\n    You notice a door leading to the kitchen that you have not noticed before.")

    available_rooms = rooms[current_room]
    if len(available_rooms) == 1:
        next_room = available_rooms[0]
        print(f"\n    You see only one path to the {next_room} and walk in.")
        prompt(next_room)
    else:
        while True:
            if len(available_rooms) == 2:
                print(f"\n    There are doors leading to the {' or '.join(available_rooms)}.")
            else:
                print(f"\n    There are doors leading to {', '.join(available_rooms[:-1])}, or {available_rooms[-1]}.")

            choice = input(f"\n    Where do you want to go next? > ").strip().lower()
            for room in available_rooms:
                if choice == room.lower():
                    print(f"\n    You walk into the {room}.")
                    prompt(room)
                    return
            print("\n    Invalid choice, please choose a valid room.")



## Objects
# Drawer
def drawer():
    print("""\n    A red nailpolish bottle and a hairbrush sit atop the bedside table. You pull open the 
    drawer and find a bookmark wedged in a tattered self-help book, 'Navigating estranged relationships 
    with your child'. The page is titled 'Accepting what you can't change'.""")
    
# Bottle
def bottle():
    print("""\n    Tucked under the pillow, you find a nearly empty bottle of prescription sleeping pills 
    labeled under Margaret's name.""")

# Laptop
def laptop():
    print("""\n    You poke around the laptop and stumble upon an unsent email draft addressed to Emily. 
    It reads: 'Emily, we need to talk. I know what you've been doing, and it has to stop. You're putting 
    us all in danger.""")

# Towel
def towel():
    print("""\n    A sharp chemical smell hits you the moment you pick up the towel. It reeks of bleach, 
    as if someone tried to scrub something away.""")

# Bin
def bin():
    print("""\n    Among the shreds of paper in the bin, you spot a piece with the logo of 'Westfield 
    Construction Company' with 'John Harrington, CEO' under it. Part of the letter reads: '... all 
    transactions must remain untraceable to avoid scrutiny. 'Untraceable funds?' you think to yourself.""")

# Journal
def journal():
    print("""\n    You flip to Emily's most recent journal entry. Her words are heavy with urgency: 'I 
    can't believe Lucas would do this to me. I can't sleep thinking about it and have to steal Mum's meds 
    almost every night just to fall asleep. I have to do something about it'.""")

# Corkboard
def corkboard():
    print("""\n    The corkboard is cluttered with photos, notes, and mementos, but one space is 
    conspicuously empty. On the desk, you find the missing picture a torn photo of Lucas and Emily, the 
    top edge jagged as if ripped out in anger.""")

# Phone
def phone():
    print("""\n    Upon picking it up, the screen unlocks to a text from Lucas the previous day: 'Meet 
    me at 11pm tonight. Call me back, please. Don't be rash.' The urgency in his words raises 
    more questions than answers.""")

# Knife Block
def knife_block():
    print("""\n    You turn the block around and find that one slot is conspicuously empty. The missing knife 
    sends a chill down your spine.""")

# Receipt
def receipt():
    print("""\n    You examine the crumpled receipt and see bleach and heavy-duty gloves among the items 
    purchased. The date matches the day before Emily's murder.""")

# Table
def coffee_table():
    print("""\n    Amongst the clutter, you spot a folder with loose pages sticking out. Curious, you open 
    it to find financial records. Several transactions are highlighted in red, with notes in the margin like, 
    'confirm with Lucas' and 're-route before audit'.""")

# Photographs
def photographs():
    print("""\n    On the mantle, a framed photo of John, Margaret, Emily, and Lucas catches your eye. Lucas 
    is holding a degree in Computer Science and a bouquet of flowers. 'They look so happy...' you sigh.""")



## Initialise main game
def main():
    print("""\n    The once lively Harrington estate now feels heavy with gloom. Emily Harrington, 
    19, was found brutally murdered in the backyard just days ago. She leaves behind her father, 
    John, her mother, Margaret, her brother, Ethan and her boyfriend, Lucas. A biopsy of her body 
    revealed sleeping pills in her bloodstream and subsequent fatal slashes around her neck. 
    As a skilled detective, you have been called to uncover the truth and find clues around 
    this house to unmask the killer.
          
    As you enter the dimly lit hallway, shadows flicker across family portraits, and you see 
    doors to the Master Bedroom and Emily's Bedroom. Choose your path, detective.""")
    prompt('Hallway')
    
if __name__ == "__main__":
    main()