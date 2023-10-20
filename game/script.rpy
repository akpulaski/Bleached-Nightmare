label start: 
    $ pName = renpy.input("What is your name?", length = 32)
    $ pName = pName.strip() #remove whitespace 
    #set a default name if players didn't enter anything 
    if not pName: 
        $ pName = "Sam"
    "You hear a knock at the door."
    "It goes on for several seconds, but as it stops you hear a familiar voice speaking to you."
    i "Hello {pName}, are you going to come out and play today."
    "It’s Ivo, your friend for as long as you can remember."
    mc "Of course, just give me a minute to go and change."
    "Some minutes later as you’re ready to leave your sister stops you."
    e "And where are you going?"
    mc "Out to play with Ivo."
    e "Oh no you don’t!"
    e "Mum said to wait for her here until she comes home again tomorrow."
    mc "Come on! Isn’t there anything I can do to not tell on me?"
    e "You can take me with you, I don’t want to stay in hear, plus Ivo is my friend too."
    e "I don’t tell on you & you don’t tell on me. How does that sound?"
    mc "Fine, you don’t need to make such a big deal about it."
    "You’re finally ready to go."
    menu: 
        "But will you?"
        "Go out with Ivo and Eliška.": 
            jump A1
        "Stay in.": 
            jump A2

label A1: #go out with Ivo and Eliska 
    i "Finally, what took you so long?"
    e "He just doesn’t know how to tie his shoes."
    i "Wait, REALLY!!!"
    i "HAHAHAHAHA!"
    mc "You promised me you’d never tell anyone."
    e "Sorry, not sorry."
    i "Can we play now?"
    mc "Okay, what do you want to do?"
    "Just as you finished that sentence he runs to you and nose."
    i "Now you’re it! Catch me if you can!"
    mc "I’ll catch you alright!"
    e "Hey! Wait for me!"
    "And so you play with your friends for hours without a care in the word."
    "But as you run through the village’s market you bump into someone."
    im "Hello there {pName} and Eliška, what are you doing here?"
    mc "Just playing around, Miss Ivo’s mum."
    i "Hi, mum!"
    im "Hi, sweetie, how are you doing?"
    i "Good!"
    im "Do you need me to buy you anything while I’m in the market?"
    i "Candy!"
    im "Something that isn’t candy?"
    i "Non-candycal candy…?"
    im "What is that you said? Vegetables?"
    i "No!"
    im "Okay then, I’ll take the freshest vegetables just for you."
    #SFX: Kid crying 
    i "Fine..."
    mc "By the way, Miss Ivo’s Mum, me and Eliška are supposed to be home now, so don’t snitch on as, okay?"
    im "Okay, I won’t tell."
    im "Eliška, please make sure to take care of them."
    e "Already doing that."
    im "Well, I have to go now, bye."
    i "Bye!"
    "So you continue playing together."
    "Running left, right, up and down the village like there’s no tomorrow."
    "Until…"
    "You find yourselves in front of a towering building."
    i "W-what is that?"
    mc "I don’t know, but it gives me the creeps."
    e "It’s the old church, once our parents used to come here."
    e "Until \"it\" got too close."
    mc "Do you think \"it\" will ever go away?"
    e "I…"
    e "Of course it will, we will find a way."
    e "(Probably…)"
    mc "!?!"
    mc "Wait a minute!"
    mc "Where is Ivo!"
    e "Oh no! He must have left while we were talking!"
    e "What are we going to do? What are we going to do?"
    mc "Look!"
    mc "Wasn’t that door closed a moment ago?"
    mc "Do you think he got in?"
    e "He was always too curious."
    e "And he probably got bored by us talking about the sand."
    mc "We…"
    mc "We need to go and save him!"
    e "Are you crazy!?"
    e "It’s too dangerous, we need to go and tell an adult."
    mc "Are you nuts!"
    mc "Who knows what can happen to him at any second."
    mc "He could get hurt or even worse, get corrupted."
    mc "We can’t waste our time."
    menu: 
        "What do you think is the better course of action?"
        "Go and save him.": 
            jump A1_1
        "Tell an adult.": 
            jump A1_2

label A1_1: #Go save him
    "Ok then, hope you like hell because heaven doesn’t accept suicidals."
    e "I guess you’re right."
    e "Time is of the essence."
    e "Let’s go and save him."
    mc "I’m always right."
    e "I regret this already."
    "You and your sister make you way in front of the building’s door."
    "The pure scale itself gives you a feeling of dread."
    e "Once we walk in, there in no going back."
    e "You got that?"
    mc "Yea..."
    "You slowly walk inside your tombs."
    mc "This place is even bigger on the inside."
    e "We better stay close."
    menu: 
        "Where do you want to go?"
        "Second floor.": 
            jump A1_1_1
        "North Aisle.": 
            jump A1_1_2
        "Nave.": 
            jump A1_1_3
        "South Aisle.": 
            jump A1_1_4

label A1_1_1: #Second Floor
    $ visitedSecondFloor = True 
    "You make your way up the stairs to the second floor."
    "But as you walk you see something blocking your path."
    "A \"sand’s child\" as your village calls them standing were you want to go."
    "As you see it you immediately stop and hold your hands up your mouth."
    "And you slowly go back down the stairs."
    "Usually I would say that you misstepped and it turned around and ripped your insides."
    "But both of you didn’t make any noise, so good job on that."
    e "We must find a way to make him go away, but how?"
    mc "Maybe there’s something in here to help us."
    e "Probably, but where?"
    mc "The sacristy? (I always wanted to see what was behind one of those.)"
    e "That can work."
    e "We will need to be careful though."
    e "There is never just one of them."
    menu: 
        "From where do you want to go?"
        "North Aisle." if not visitedNorthAisle: 
            jump A1_1_2
        "Nave." if not visitedNave: 
            jump A1_1_3
        "South Aisle." if not visitedSouthAisle: 
            jump A1_1_4

label A1_1_2: #North Aisle
    $ visitedNorthAisle = True 
    "You thought to make your way to the north aisle sins most of the \"sand’s children\" are in the nave."
    "But, some of them are in there with you."
    "You go back and try again."
    menu: 
        "Where do you want to go?"
        "Second Floor." if not visitedSecondFloor: 
            jump A1_1_1
        "Nave." if not visitedNave: 
            jump A1_1_3
        "South Aisle." if not visitedSouthAisle: 
            jump A1_1_4

label A1_1_3: #Nave
    $ visitedNave = True 
    "You make your way to the nave."
    "You try to hide between the chairs but there are too many of \"them\"."
    "One of them saw you."
    "As you stared into each others eyes..."
    "(Or at least what remained of them)..."
    "It made a loud noise that make you go deaf and alerted the others."
    "In just seconds they turn and run at you."
    "They begin to rip you apart even though they forgot how to devour and eat."
    "You should have listened to your sister."
    "But at least your mind will be spared from the sand."
    jump HallowEnd

label A1_1_4: #South Aisle
    $ visitedSouthAisle = True 
    "You thought to make your way to the south aisle sins most of the “sand’s children” are in the nave."
    "You see one of them roaming near so you hide behind a pillar barely before it can turn around."
    "Luckily the pillar is big enough to hide two fat children with ease."
    "You hear it leave but you can’t see to know for sure."
    menu: 
        "What do you do?"
        "Stay a bit longer, just to make sure.": 
            jump A1_1_4_1 
        "Run for your life.": 
            jump A1_1_4_2

label A1_1_4_1: #Stay a bit longer 
    "You decide to wait just a little bit to make sure it left and isn’t out of only your view."
    "But you forgot one little tiny thing..."
    "A pillar can only hide you from one viewpoint."
    "I don’t think I need to tell you what happened next."
    jump HallowEnd

label A1_1_4_2: #Run for your life. 
    "You decide to run in chance you take it by surprise and make it in the opposite end."
    "You grab your sister’s hand and without a second (or even first) warning you make a run for it."
    "As you run you make enough noise to alert everyone in this room."
    "But sadly, even if they didn’t have time to react at first."
    "You barely manage… to…"
    "Wait!? You actually managed to pull it off!?"
    "I guess I have to continue the story then."
    "Ok! This is actually getting interesting."
    "Lets do this!"
    "{i}Ahem.{/i}"
    "You run like there was no tomorrow."
    "And since the sacristy was barely some meters away..."
    "You made it and closed the door just in time."
    "But just a small door won’t hold them long enough."
    "Thinking smart and fast and then smart again (in that order) you throw a closer at the door."
    "But… you couldn’t do it sins you’re just a little, small, tiny, microscopic child."
    "Good think your sister remembered she’s a part of the story too and helped you."
    e "That should hold them for a while."
    mc "So this is what it looks from inside."
    mc "Disappointing."
    e "Stop playing around! We need to hurry."
    mc "Fine, fine."
    "You search the room for minutes and find two keys."
    "As you grab them, you hear the door breaking."
    menu: 
        "With only seconds to react you:"
        "Hide in the closet.": 
            jump A1_1_4_2_1
        "Sneak through the other door.": 
            jump A1_1_4_2_2

