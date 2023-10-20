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

label A1: 
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
    