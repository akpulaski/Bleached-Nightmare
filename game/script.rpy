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

label A2: # don't go out. 
    """
    ...
    ...
    ...
    ...
    ...
    ...
    ...
    ...

    """
    jump EndIsNeverTheEnd

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

label A1_2: #Tell an adult 
    "Okay; you monster."
    "Hope you can sleep will yourself tonight."
    return

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

label A1_1_4_2_1: #Hide in the closet 
    "You decide to hide in the closet sins your little legs won’t get you far enough in time."
    "But since you’re the luckiest boy ever it’s locked."
    mc "Damn it!"
    mc "Why is this even locked!"
    e "Maybe you can unlock it with one of the keys."
    mc "Maybe."
    "They’re the same shape so you just pick one in random."
    mc "It unlocked!"
    "But it’s no use, they’re in."
    "You may wonder how you didn’t hear them break the door."
    "Well, just because they’re mindless zombies that are tearing you apart as I speak."
    "That doesn’t mean that they’re stupid idiots that don’t know how to pick a lock."
    "How rude of you thinking of them like that."
    "Oh yea, I was suppose to describe to you how they killed you in gruesome detail."
    "Well, that’s what you get for being a jerk."
    jump HallowEnd

label A1_1_4_2_2: #sneak through the other door
    "You decide to sneak through the other door."
    "As they got in you managed to get out."
    "They saw you get out but you blocked the door again just in time."
    "Your sister grabs your hand and before you can react she drags you as she runs quickly but quietly to the stairs of the second floor."
    "This time they did not see you go."
    "You make your way up the stairs to the second floor."
    "But as you walk you see something blocking your path."
    "One of them is standing were you want to go."
    e "(Well, we’re trapped until we find a way to get him out of here or one of them sees us.)"
    mc "(I think I know how to get us out.)"
    e "(What do you think you’re doing.)"
    mc "(Relax, just trust me and stay put.)"
    e "(Fine, just be careful.)"
    mc "(Don’t worry, I will.)"
    "So with your sister’s trust you try your idea."
    "You try to open the door of the closet but it was locked."
    "You take one of the keys you took earlier out of your pocket."
    "To your surprise, it actually works."
    "You didn’t think it would, but at least now you look smart."
    "Opening it, you see it’s full of clothes made of fabric."
    "You move them out of there and nodding at your sister."
    e "(Wait! You want me to go in there.)"
    mc "(Do it for Ivo.)"
    e "(For Ivo.)"
    "Somehow you made her to go inside that dirty closet."
    "You go in there too, closing the door."
    "Before you completely closed it, you throw the keys down the stairs."
    "You accidentally throw both keys, but that’s beside the point."
    "It follows the sounds and goes down the stairs."
    e "Finally! It’s gone."
    e "Okay, now give me the key so we can move on."
    mc "…"
    e "[pName]. The key, now."
    mc "I dropped it."
    e "I know that, I saw you throw it."
    e "Give me the second one."
    mc "I dropped that too."
    e "You what!"
    mc "Shh! It will hear us."
    e "(You what!)"
    mc "Don’t worry, everything is fine, 100% fine."
    mc "(She’s going to kill me!)"
    "As you speak like a politician you put your hand at the doorknob to look cooler."
    "But your stupidity proved useful since the door was never locked."
    mc "See, I told you."
    e "Whatever, let’s just go."
    "As you explore the church’s second floor you hear a voice coming behind a door."
    mc "Could that be Ivo."
    e "Who else could it be?"
    "Leaning closer tords the door you can hear that there’s another voice coming from in there."
    i "And then one of them saw me so I had to run, but it stopped at the stairs and I got away."
    p "Let’s hope it will stay there."
    e "(What are they saying?)"
    mc "(I don’t understand much.)"
    e "(Then move over so I can hear.)"
    "As you fight trying to lean closer on the door, you put too much pressure and fall in the room."
    i "[pName], Eliška, how did you make it here?"
    p "So those are your friends?"
    i "Yep."
    mc "Ivo, you’re okay! We were so worried about you!"
    e "Don’t ever do that again!"
    p "Don’t worry, I was looking out for him."
    e "And who are you!?"
    p "Oh, sorry for not formally introducing myself."
    $ priestName = "The Priest"
    p "I’m the priest of this church and my name is not important."
    i "And my new friend!"
    p "Yea, that too."
    e "I thought this place was abandoned."
    p "For your village, it is."
    e "What does that even mean?"
    p "Please sit down, this will be a big tale."
    "You and Eliška hesitate at first as the old man sits down slowly sits down."
    "(And Ivo sits down too, but who cares about him.)"
    p "Don’t worry, the floor doesn’t bite."
    i "Come on guys! I want to hear the story."
    mc "Fine fine, we’ll sit."
    p "So now that we’re all ready, let’s begin the exposition."
    p "First of all, what do you know about the \"white sand\"?"
    i "I’m tired of hearing about \"the sand\" all the time!"
    i "The sand this! The sand that!"
    i "I’m going back to the zombies."
    e "Wait, don’t go there!"
    i "Relax, I’m just gonna be just outside the room until you speak about something more original."
    i "Learn to understand when someone is making a joke in the meanwhile."
    "Ivo leaves in frustration as he slams the door behind him."
    p "Just let him be for now, it’s better not to lose his positive look on life this early on."
    p "Even in an environment like this."
    e "But he needs to grow up one day."
    p "That will be decided by events, not people."
    p "But enough of that, I promised you to tell you about the church’s and sand’s past."
    p "Some months or years ago this was your village’s church."
    p "Almost every day the people of the village wood come here and get a little bit of hope on those hard times."
    p "Everything was… better than now."
    p "The sand was spreading in the near villages and kingdoms."
    p "It consumed everything that got near it, not even the skies were safe."
    p "But we were doing fine at the moment."
    p "Until we were capable to see it from the horizon."
    p "Everyone panicked and run here for advice."
    p "Things got so bad that even the village chief came from time to time (and he’s not even religious)."
    p "After some days the chief had an idea."
    p "(It was more of hearing rumors and treating them as facts really, but who cares.)"
    p "It was something among the lines: \"The sand is spreading by consuming our beautiful land.\""
    p "\"So if we want to stop it we need to cut of its food supply.\""
    p "\"If we burn the flowers, the grass and trees near it then we should at least be able to delay it.\""
    p "And the villagers decided to do it since it was the only thing they had a chance at surviving."
    p "He organized a team of 10 -maybe more- people to do his bidding"
    p "They had to go slow and careful to not burn the village too, so they spend many weeks near it."
    p "And they succeeded!"
    p "The sand was slowed down and everyone wanted to party like never before."
    p "But that team didn’t returned like they left."
    p "We heard rumors that the sand corrupts bodies differently (and more easily) than inanimate things."
    p "But now we believed it."
    p "When they returned the end of their legs and/or hands weren’t behaving normal."
    p "Everyone was afraid that they would get their disease if they were near them."
    p "But now I’m a living proof that only the sand can do that."
    p "The chief decided to turn this church into a hospital-jail thing for them."
    p "\"It’s the perfect place,\" as he said."
    p "\"Far away from the village to have the villagers calm down.\""
    p "\"And close enough to keep an eye on them.\""
    p "Most people stopped coming here and after some time none."
    p "I stayed to keep an eye on the \"corrupted ones\" and the building itself."
    p "As time moved on the corruption was growing to the rest of the body."
    p "At one point they lost the ability to eat, sleep, breath and die."
    p "One of them couldn’t handle the idea of living like this."
    p "So he had the idea to blow his brain out before the corruption could reach it."
    p "But the corruption had already taken the rest of his body."
    p "And those parts stayed semi-factional."
    p "At first it remained still."
    p "Until one of the others tried to get near it."
    p "In an instant, it attacked and ripped everything it could from the others, until only the corrupted parts remained."
    p "The ones that they finished attacking started attacking too."
    p "I tried to run away but they were fast and I knew if I opened the door they would be the only ones to get out."
    p "Wait! You did close the door after you got in, right?"
    mc "Did we?"
    e "I think so…"
    mc "Ah yes, we did."
    mc "I remember it clearly now."
    p "100% sure?"
    mc "100% sure."
    mc "So, what happened next?"
    p "The only place I could run to was the second floor’s stairs."
    p "As I run, I noticed that they stopped in the middle of them."
    p "This floor is for staff only, so they weren’t allowed to go here before."
    p "So my theory is that they still have some basic and random parts of their memories."
    p "And I keep an eye on them ever since."
    mc "And why don’t you get out when they’re not looking?"
    p "Because I don’t know for how long until they’ll remember to how to open doors or break windows."
    p "And the sand is close enough now that I’m already starting to become corrupted."
    p "..."
    p "You should better leave before you catch the disease too."
    p "And help your parents too."
    p "They’re probably going to need help packing."
    mc "Packing what?"
    p "Your things before you leave far away from the village."
    mc "Why would we do that?"
    p "Because of the sand maybe?"
    e "Like our chief would ever do something that would require him to get up from his chair."
    e "Plus, the other villages would kill or imprison us because of our different religion."
    p "Better dead anywhere near it!"
    p "(better dead…?)"
    p "..."
    mc "Earth to priest, are you there?"
    p "Yeah…"
    p "You better leave sooner than later."
    e "I guess so."
    p "And don’t come back here!"
    e "I don’t plan to."
    "As you exit the room you see Ivo standing right next to the door."
    "He probably eavesdroped on the conversation, but you all had a rough day so you don’t bother him."
    e "Come on, let’s go."
    "Ivo follows you without muttering a word as you make your way out as quietly as posable."
    "When you get outside you come across a pitch-black night-sky."
    i "When did it go so dark?"
    e "We were outside for hours, even without counting the time we were in the church."
    i "I better go back home before my parents start to worry."
    e "We can walk you there."
    mc "We will?"
    e "..." 
    mc "I mean, of course we will!"
    i "Really guys, that would be awesome, thanks!"
    "So you make your way to Ivo’s house."
    "You knock at the door and wait."
    ip "Hello? Who’s there?"
    i "It’s me."
    ip "Ivo! We were worried sick about you."
    i "Sorry, I was playing with my friends and forgot to look at the time."
    e "I’m sorry too, as the oldest I should be more careful."
    ip "Since your friend took the responsibility I guess I won’t use the belt tonight, son. (I’m such a good father.)"
    "Now come on, your mother made a lot of food and I can’t eat it all alone."
    i "Coming! Bye Eliška, bye [pName]! See you tomorrow!"
    "After that you and your sister go home too, your parents didn’t returned yet so at least you’re lucky."
    "You immediately go to sleep after this exhausted day."
    centered "A few days later... {w=1}{nw}"
    return

label HallowEnd: 
    "Oops you turned into a hallow."
    return

label EndIsNeverTheEnd: 
    "Oops you made a bad choice."
    return