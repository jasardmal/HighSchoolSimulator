
#Characters

define h = Character('Mr. Hart', color="#c8ffc8")
define k = Character('Mr. Kelly', color="#c8ffc8")
define g = Character('Mrs. Galvin', color="#c8ffc8")
define o = Character('Mrs. Ong', color="#c8ffc8")
define v = Character('Mr. V', color="#c8ffc8")
define d = Character('Danny DeVito', color="#c8ffc8")
define m = Character('Marc', color="#c8ffc8")
define s = Character('Sarah', color="#c8ffc8")
define b = Character('Becka', color="#c8ffc8")
define c = Character('Cynthia', color="#c8ffc8")
define n = Character('Natalie', color="#c8ffc8")
define a = Character('Agnes', color="#c8ffc8")
define i = Character('Ivor', color="#c8ffc8")
define f = Character('Fredrick', color="#c8ffc8")
define who = Character('???', color="#c8ffc8")
define dean = Character('Dean', color="#c8ffc8")
define ran = Character('Other Student', color="#c8ffc8")
define pov = Character("You", color ="#c8ffc8")
define mom = Character('Mom', color="#c8ffc8")

image basicdanny = "dannybasic.png"
image basickolby = "kolbybasic.png"
image basicmarc = "marcbasic.png"

label start:
    
    #Initialize Calendar/Time/Location
    $ clock = True#make false to hide the calendar
    $ theweekday = 2#monday, the number of the weekday, this automatically changes but must be initially assigned
    $ themonth = 8#august, the number of the month, this automatically changes but must be initially assigned
    $ theday = 24#this automatically changes but must be initially assigned
    $ theyear = 2015#this automatically changes but must be initially assigned
    $ dayofyear = 236#you must calculate this properly, this automatically changes
    $ yearlim = 365#initially define it as 265 or 366, whichever is correct, this gets changed automatically later
    $ daylim = 31#initially define it as 28, 29, 30, or 31, whichever is correct, this gets changed automatically later
    $ stringweekday = "Monday"#2, the string of the weekday, this automatically changes but must be initially assigned
    $ stringmonth = "August"#8, the string of the month, this automatically changes but must be initially assigned
    $ thephase = 1#early morning, the phase of the day, this automatically changes but must be initially assigned
    $ stringphase = "Morning"#2, the phase of the day, this automatically changes but must be initially assigned
    $ location = 2#home, the current location, this automatically changes but must be initially assigned
    $ stringlocation = "Home"#2, the current location, this automatically changes but must be initially assigned
    
    #Initialize Stats
    $ charismasub = 0
    $ charisma = 0
    
    $ couragesub = 0
    $ courage = 0
    
    $ intelligencesub = 0
    $ intelligence = 0
    
    $ staminasub = 3
    $ staminasubcurrentlim = 5
    $ staminasubfuturelim = 5
    $ stamina = 3
    
    $ stresssub = 3
    $ stress = 3
    
    #Start week

    pov "I have no clue how I’m going to find any information about what happened at homecoming with Christina and Kolby. Speaking of those two, I don’t see either of them in class today."
    
    show basicdanny at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    #show basiccynthia at Position(xpos = 1.0, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    
    d "Christina made a big scene at prom… I wish I could have seen it."
    
    c "I know, right? I think almost everyone in the school heard her yelling. Everyone’s curious about what happened between Christina and Kolby."
    
    d "I guess he was with some other girl since she yelled, “You Cheater!” before she stormed out."
    
    hide basicdanny
    #hide basiccynthia
    
    #Lunch
    
    #show basicbecka at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    #show basicfredrick at Position(xpos = 1.0, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    
    b "What a loss. Christina and Kolby obviously broke up yesterday."
    
    f "Of course Christina would make a scene at homecoming - she always wants to be in the limelight."
    
    b "Christina seems like the person who wouldn’t want a break up to be a fast “we’re over” sort of deal. She seems like the type that would want a more intimate break up."
    
    f "It seemed obvious that she wanted to cause some sort of scene yesterday."
    
    #hide basicbecka
    #hide basicfredrick
    
    pov "Wouldn’t want a fast break up? I wonder…"
    
    #5th Period
    
    #show basicagnes at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    #show basicivor at Position(xpos = 1.0, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    
    a "You heard about what happened between the two love birds yesterday, right?"
    
    i "All I know is that Christina was very upset about something yesterday and left. I would rather not make assumptions about her relationship with Kolby."
    
    a "I heard Christina say, “I’m breaking up with you. Our relationship is done for,” before leaving."
    
    #hide basicagnes
    #hide basicivor
    
    pov "That’s quite the huge statement from Christina."
    
    #Tuesday
    #Before School: Hallway
    
    #show basicagnes at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    #show basiccynthia at Position(xpos = 1.0, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    
    a "Is it true that you were the one who kissed Kolby during homecoming, Cynthia?"
    
    c "OF COURSE NOT! WHO TOLD YOU THAT?!"
    
    a "Oh, well, I heard from some people who said you were looking around for a “partner.”"
    
    c "I am not doing anything of the sort!"
    
    #hide basiccynthia
    
    #Cynthia storms off
    
    #hide basicagnes
    
    pov "I wonder if what Agnes said is true."
    
    #3rd Period
    
    #show basicivor at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    #show basicbecka at Position(xpos = 1.0, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    
    i "I’ve been hearing rumors that Cynthia was seeing Kolby."
    
    b "Cynthia doesn’t have enough time for a partner that would be too high a loss of profit for her."

    i "What do you mean?"

    b "I doubt the money she makes working two jobs would go to anyone but her family."
    
    #hide basicivor
    #hide basicbecka

    pov" Well, that’s an interesting take on the price of relationships. Oh, Marc is texting me to meet him in the Gym after school. I wonder what he’s up to."

    #After School: Gym
    
    pov "Why does Marc want to meet me here? I will probably never know."
    
    show basicdanny at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    show basicmarc at Position(xpos = 1.0, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)

    m "You know Cynthia well. Now tell me why she is trying to steal Christina’s boyfriend."

    d "I have no clue what you’re talking about. Christina isn’t even interested in Kolby!"

    m "You’ve heard the talk around school. Everyone says Cynthia is trying to get with Kolby."

    d "The whole rumor is a lie. Everyone just wants to make up stories."  

    m "You obviously have some important information and if you're not willing to give it, I’m not afraid to resort to force."
    
    
    menu:
        
        pov "What should I do?"
        
        "Ask Marc to tone it down":
            jump marcToneDown
            
        "Ask Marc to leave":
            jump marcLeave
        
    
    
    #[Ask Marc to tone it down]
    
    label marcToneDown:
        
        pov "Marc, I thought I told you about keeping the violence low."

        m "Don’t tell me about keeping it down. I’m going to beat this kid down if he doesn’t want to tell me what I want to hear."

        pov "This is ridiculous Marc, you can’t just threaten people and EXPECT them to do as you say."

        m "I have my methods, you have yours. Now let me get back to… HE’S GONE, THE SNEAKY LITTLE-"

        pov "*Sigh* Well, we lost a potential lead." 
        
        jump marcDone


    #[Ask Marc to leave]
    
    label marcLeave:

        pov "Marc, just leave it to the two of us for a bit. I’ll talk to you later."

        m "Hmph! Fine. I’ll be waiting outside."

        #Marc leaves
        hide basicmarc

        pov "Sorry about that Danny. Marc can go overboard sometimes."

        d "The dude just tried to beat me up - how the hell are you even friends with him?"

        pov "Eh, I wonder how that happened too sometimes, but let’s get down to business. So can you tell me what you know about Christina and the rumor around school?"

        d "They’re all false. I know Christina well and she’s not that kind of person. She doesn’t have the time for that; she works two jobs, for crying out loud." 

        pov "That would make sense."

        d " Also she’s not even interested in getting into a relationship. Supporting her family is a lot more important to her."

        pov "Danny, thank you for this information. It helps me a lot. If you ever need a favor, just let me know. Also, I’ll make sure Marc doesn’t try to kill you."

        d "Heh, thanks man."

        #You both leave the gym.
        hide basicdanny
        
        show basicmarc at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
        
        m "So what did you find out?"

        pov "Some important information. I think I’m onto something here. Try to get Christina and Kolby to meet me at the park on Saturday, if you can. I’ll clear up any false information about the two."

        m "I guess I can do this for you. Good luck."
        
        hide basicmarc
        
        jump marcDone
        
    label marcDone:
    
    #Wednesday
    #2nd Period
    
    #show basicbecka at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    #show basicivor at Position(xpos = 1.0, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    
    b "Hey Ivor, here is your cut of the money for your performance."

    i "Thank you. I’m surprised you were able to get people to pay a decent amount to see my performance. Also, thank you for finding me a willing volunteer for my performance."

    b "“Willing” is a far stretch to describe Frederick being your dummy for those magic tricks. I have to give him a cut of our profit sadly."

    i "It’s not that big of a deal. I wasn’t even expecting to make money off of it."

    b "Ivor, one day you have to learn about the joys of making a profit, but we could have made so much more if Ms. Stage Crazy wasn’t also performing. I think you, Frederick, and I did a good job attracting and profiting from the performance." 

    #hide basicbecka
    #hide basicivor

    pov "So much was going on during homecoming, I didn’t even get to see any of the performances!"

    #4th Period
    
    show basicdanny at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    #show basiccynthia at Position(xpos = 1.0, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    
    c "Hey Danny, thanks for spending homecoming with me."

    d "Yea, no problem."

    c "It was nice to spend the time with just the two of us."

    #*Phone Rings*
    
    pov "Oh, Sarah texted me."

    s "Hey, can you meet me at the rooftop after school?"

    pov "I wonder what she has to say."
    
    #hide basiccynthia
    hide basicdanny
    
    #After School: Rooftop
    
    #show basicsarah at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    
    pov "Hey Sarah, what’s up?"

    s "Oh, hey you’re here…"

    #.......

    pov "We’re  just standing here staring out at the city."

    s "Marc told me what you’re up to. You’re a good friend."

    pov "Oh, uh, um, thanks…"

    s "I know Marc just dragged you around everywhere during homecoming so you weren’t able to enjoy it."

    pov "Uh, it wasn’t really like that."

    s "If you say so, but the point is you might have missed something important during homecoming." 

    pov "What do you think that is?"

    s "Well, you were probably busy, but Natalie, Marc, and I were watching Christina’s performance." 

    pov "Oh yeah, she had a performance. I missed it, but how is that important?"

    s "Someone was missing who should have been there."

    pov "And then it dawned on me."

    pov "KOLBY WASN’T AT HER PERFORMANCE!"

    s "Exactly. I hope this information will come of use."

    pov "Yeah, I’ll make sure of it. Thank you, Sarah."

    s "No problem. (sad smile)"
    
    #hide basicsarah
    
    #Thursday

    #Natalie Confirmation Art Room Haven’t talked to

    #Morning Before School In Front of School
    
    show basicmarc at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    
    pov "I think I’ve heard from almost everyone who was at homecoming but Natalie. I think I’ll find her and talk to her. I’ll ask Marc - maybe he’ll know where to find her."

    pov "Hey Marc, do you know where I could find Natalie?"

    m "Oh, the silent girl. I think she can usually be found in the art room when she’s not in class."

    pov "Thanks, Marc!"
    
    hide basicmarc

    #Morning Before School Art Room

    pov "This room is pretty empty. Wait, there’s someone here.. I think that’s Natalie." 
    
    #show basicnatalie at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)

    pov "Hey, you’re Natalie right?"

    n "*Nods her head*"

    pov "Do you know any information on the Kolby and Christina fight that isn’t a rumor?"

    n "*Nods her head again*"

    pov "Well, I see why Marc calls her the silent girl."

    pov "Can you tell me about it?"

    n "*Starts scribbling in her notebook*"

    pov "Wait, this looks like when all the performances were going on at homecoming."

    pov "This is during the performances. How is it significant?"

    n "*Furrows her eyebrows and keeps drawing*"

    pov "This drawing… is this Kolby? It looks like he’s surprised that he is being kissed, but who is the girl in the picture?"

    pov "Who is the girl kissing Kolby?"

    n "*Frowns and continues drawing*"

    pov "It’s a laptop. What does it mean?"

    n "*Stops drawing and stares*"

    pov "This is probably important." 

    pov "Is there anything else you can tell me?"

    n "*Nods her head no*"

    pov "Thank you Natalie. I think this is important."
    
    #hide basicnatalie

    #Agnes Confession emotional not real relationship /w Kolby
    #After School in Hallway 

    who "*Waahhhhhhhh*"

    pov "What’s that noise?"

    who "*Waahhhh*"

    pov "It sounds like it's coming from this way."

    pov "Oh, here it is. Looks like someone is crying here."

    who "*Wahhhh*"

    pov "Wait, this is… *remembers picture from Natalie* AGNES WAS THE ONE WHO KISSED KOLBY."

    #[Comfort Her]
    
    #show basicagnes at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)

    pov "Hey Agnes, are you ok?"

    a "Huh? Oh, what does it look like?"

    pov "Obviously that something went wrong. What happened?"

    a "Kolby dumped me."

    pov "She really thought she had something with him? Oh my…"

    pov "Think about it, you weren’t in a relationship with him at all."

    a "But-but-but… we kissed."

    pov "Relationships don’t just happen by smooching with someone." 

    a "*sob* *sob* No one's going to ever love me!"

    pov "You know, Kolby wouldn’t have been a good match for you anyway. There are tons of people out there in the world. I’m sure you will find that special someone."

    a "Do you really think that?"

    pov "Yeah."

    a "*sobs* But-but now everyone in the school will hate me and call me terrible things for trying to get between Christina and Kolby’s relationship."

    #[Tell Agnes to apologize to Christina and Kolby]

    pov "There’s a way you can fix this, Agnes."

    a "How?"

    pov "I’m meeting up with Christina and Kolby at the park tomorrow to tell them the truth. How about you join us and apologize to them?"

    a "Do you really think that would be a good idea?"

    pov "Sure. If you really mean it, I’m sure they can understand a tad bit."

    a "Ok then… if you say so."

    pov "Ok, we’ll all meet up at the park tomorrow. I hope you’re feeling better, Agnes."

    a "… I … am … thank you."

    #[Lie for Agnes]

    pov "There’s something I can do to clear your name."

    a "What is it?"

    pov "I’m meeting up with Christina and Kolby at the park tomorrow to tell them the truth. How about I just ‘change’ the truth a tad bit and it’ll be like you were never involved in this?"

    a "You can do that? Thank you so much!"

    #// I’m thinking about making it so you can demand something from her in return.

    pov "Just don’t do something like this again."

    a "I won’t, I promise."

    #[Insult Her]

    pov "Your crying is horrific.  It’s like you’re a wailing banshee."

    a "What do you know?"

    pov "That your reputation at this school is going to be ruined because I’m going to reveal to the school you’re a [insert words here]."

    a "Just leave me alone!"

    #[Make a deal with Agnes]

    pov "Actually, I have a way to clear your name."

    a "You can do that?"

    pov "Yeah. It will just be a small cost."

    a "What would that be?"

    pov "You’ll owe me a favor sometime."

    a "Oh, ok."

    #[Leave]

    pov "Have fun with the whole school knowing what you are."
    
    #Friday Park

    #[Agnes apologizes route]

    pov "Ok, I’m here at the park. Now time to find Agnes, Marc, Christina, and Kolby. Oh, I think I see Agnes."

    pov "Hey, Agnes! Over here."

    a "Hi… "

    pov "You ready?"

    a "Maybe this isn’t a good idea, maybe I should leave..."

    pov "No, no, no, you’re staying here and you’re going to face them."

    pov "I think I see the rest of them over there. Christina looks like she wants to kill Kolby right now. I better hurry up over there."

    pov "Hey guys."
    
    #hide basicagnes
    
    show basickolby at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    #show basicchristina at Position(xpos = 0.75, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    show basicmarc at Position(xpos = 1.0, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    
    #Marc, Christina, Kolby: "Hey."

    pov "This is getting pretty tense."

    m "Who's that behind you?"

    pov "Oh yeah - I asked Agnes to come here. She has something to say about the homecoming fiasco."

    pov "So far so good, but Kolby looks a bit concerned."
    
    hide basickolby
    #hide basicchristina
    hide basicmarc

    #show basicagnes at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    #show basicchristina at Position(xpos = 1.0, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)

    a "I’ve come here to apologize to the both of you, Christina and Kolby."

    c "Are you implying what I’m thinking?"

    a "YES, I’M THE ONE WHO KISSED KOLBY AND I’M SORRY."

    c "Go away. No one wants you here."

    pov "Agnes is looking kinda scared, like she might actually leave."

    #[Tell them to let Agnes explain herself]

    pov "Christina, please, just hear Agnes out."

    c "Fine."

    a "Thank you, [your name]..."

    a "I’m sorry that I came between your relationship. I thought…."

    a "*sobs* I thought I could make a relationship for myself out of nothing and I’m sorry."

    a "I’ve learned my lesson and I hope you guys can forgive me, but especially forgive each other for what I’ve done."

    #Christina and Kolby: "*whisper* *whisper*"
    
    #hide basicagnes
    #hide basicchristina
    
    show basicmarc at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)

    m "*whispers* Do you really think this is a good idea?"

    pov "I’m sure everything will be ok."
    
    hide basicmarc
    
    show basickolby at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    #show basicchristina at Position(xpos = 1.0, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)

    k "Agnes... thank you for coming here today. I promise we won’t reveal anything about this."

    c "Just make sure to stay away from my boyfriend or I. WILL. DESTROY. YOU."

    pov "Sheesh, Christina can be terrifying."
    
    hide basickolby
    #hide basicchristina
    
    #show basicagnes at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    
    a "I promise. Thank you so much for understanding, especially you, [your name]. You’ve taught me a lot. I’m not sure how I’ll ever repay you."

    pov "We’ll see if that ever comes up, but I’m just glad everything’s ok now and we can move on."

    #[Epilogue]

    pov "And everything went well from there. We had a nice picnic and everyone was able to move on from homecoming. I worry about the stability of Christina and Kolby’s relationship, but I’m sure they can work it out."

    #[Let Agnes leave]

    a "Yeah… you’re right, I should leave. I hope you guys can find the best in each other."

    pov "Well, that could have gone worse. Now time to make sure Christina and Kolby are ok."

    pov "So Christina, Kolby, you guys ok with this?"
    
    show basickolby at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    #show basicchristina at Position(xpos = 1.0, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)

    #Christina and Kolby: "*whisper* *whisper* *whisper*"

    k "I think everything’s ok now, but I don’t think Agnes is going to be ok after this."

    c "Yeah, everyone will hear about her and her reputation will be ruined."
    
    hide basickolby
    #hide basicchristina

    #[Epilogue]

    pov "And everything went well from there. The picnic was nice, but there still felt like a rift between Christina and Kolby. I worry about the stability of Christina and Kolby’s relationship. I hope they can work it out. I hope that Christina will rethink her decision about Agnes, but it looks like everyone will see the worse in her."

    #[Lie Route]

    pov "Ok, I’m here at the park. Now time to find Marc, Christina, and Kolby. I’m going to cover for Agnes and figure out how to make Christina and Kolby get together."

    #[Reveal Agnes]

    pov "Ok, I’m here at the park. Now time to find Marc, Christina, and Kolby. It's time to reveal to them that Agnes is the culprit here!"

    pov "I think I see them over there. Christina looks like she wants to kill Kolby right now. I better hurry up over there."

    pov "Hey guys!"
    
    show basickolby at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    #show basicchristina at Position(xpos = 0.75, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    show basicmarc at Position(xpos = 1.0, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)

    #Christina, Kolby, Marc: "Hey."

    pov "So you guys are probably wonder why you are here."

    c "I don’t see why you brought me here to see HIM." 

    pov "I brought you here to tell you the truth."

    c "The truth that Kolby is a dirty player?"

    pov "No, the truth that Kolby is innocent here. Kolby was grabbed by Agnes by surprise and she kissed him. She wanted to make you jealous just so that this fight would happen."
    
    hide basickolby
    #hide basicchristina
    hide basicmarc
    
    
    #START DAY
    
    
    pa "*Bell Rings*"

    pa "Welcome to the first day of school at __________ high school! Here, we…."

    pov "That guy, there in the back? That’s me. I just moved here from __________________. This is my first day at __________ High, and I don’t know anyone. This day is gonna be such a drag."

    pa "....... And that is how the Cougars roar! Have a wonderful day, students!"

    pov "Ugh."

    pov "When I moved here, I thought that not really knowing anyone might be nice. My parents are always gone on some trip or another, so I don’t really have any actual interactions. This year, I thought that maybe, just maybe, I could find someone who would actually be my friend." 

    pov "*Desk slams forward*"

    who "Watch yourself! Keep talking, someday you'll say something intelligent!"

    ran "If you weren’t so easy to make fun of, I wouldn’t! You’re just a little baby."

    who "How many times do I have to flush before you go away? *punches other student*"

    pov "*A fight ensues*"

    who "*wipes chin* I told you not to insult me. Idiot."

    pov "Teacher comes in, it’s Mr. Hart(English)"
         
    h "Hey! What’s going on? How dare you engage in classroom violence! Don’t you know that fights are against school rules? Both of you, to the dean’s office!"

    pov "*marc and other student leave*"

    h "You! New student! You were the closest and probably saw what happened the best. go to the deans office with them to fill out an incident report!"

    pov "But, wait, no..."

    h "Don’t argue, just do it! Don’t let your experiences be memories! Go to the Dean’s office!"

    pov "*sighs* F-Fine..."
    
    h "*grumbling as you leave* Back in my day, when we had to fight over things, we waited until after school...."


    #*CHANGE SCENES WOO DEAN'S OFFICE TIME*


    dean "Now, you both know better! I can’t believe that it hasn’t even been a day into the school year and you have already begun fighting! Shame on both of you! have you no dignity?!?!"

    who "Sorry, Mr. Dean. It won’t happen again."

    who "*under his breath* Fat lard."

    ran "Excuse me? What did you call me?"

    who "Nothing, I was talking about your mother."

    dean "Both of you! Behave! Have you no decency? You haven’t even left my office! marc, stay here, and let him go."

    who "Fine. But he’s still a fat lard."

    dean "One more word out of you and I will suspend you!"

    who "..."

    pov "*MC walks in*"

    dean "Who are you?"

    pov "I’m a new student. I just moved here a few weeks ago. Mr. Hart told me to come down here because I was closest to the fight, so that I can fill out a report."

    dean "Oh. Well, in that case, let me get one of those for you. *rummages in file cabinet*"

    dean "Fill this out. what did you see?"

    #OPTIONS

    #-Marc Started it
    #-Marc didnt start it
    #-idk    -------> blame teacher
    
    
    #MARC STARTED IT


    pov "It looked to me like that student was antagonizing the other student. I’m not sure what was said, but one minute I was waiting for class to start, and the next those two were duking it out by my desk." 

    dean "Well, are you sure you didn't see anything else?"

    who "All I know is the two were fighting. I don’t know enough about either of them to tell."

    dean "Well, all right then. Get back to class."

    pov "Yes, sir."

    dean "On your way back out, call Marc back in."

    pov "Which one is Marc?"

    dean "The one who probably started the fight."

    pov "Oh, alright." 

    pov "*Walks out*"

    pov "Marc? The dean wants to see you."

    m "Ugh, finally. I wish this would just be over… I can’t stand it when people insult me and get away with it." 

    pov "*Marc goes to office*"

    pov "*Goes to class*"

    h "Welcome back!"

    pov "*End Scene*"


    #MARC DIDN'T START IT

    pov "Well… To be honest, it seemed to me like the one who is still sitting outside was the victim. The other one had made some rude comments about him, and he didn’t like it."
                                                                                                                                                                                      
    dean "Is that right? Well, so far, that’s not what I’ve heard. Are you sure?"

    pov "Yes, Sir. I’m Sure."    

    dean "Hmm… Alright. Go back to class… Thank you for your help."

    pov "Yes, sir."

    dean "On your way back out, call Marc back in."

    pov "*to himself* Marc must be the one who is still in the foyer.* Ok."

    pov "*Walks out*"

    pov "Marc? The dean wants to see you."

    m "Ugh, finally. I wish this would just be over… I can’t stand it when people insult me and get away with it." 

    pov "*Marc goes to office*"

    pov "*Goes to class*"

    h "Welcome back!"

    pov "*End Scene*"




    #AFTER BOTH VERSIONS:

    pov "*Bell Rings*"

    h "Alright, Class Dismissed. *slams book closed dramatically.*"

    pov "*To Himself* I should probably get to my next class. It’s no good to dawdle. Looks like my next class is…*shift to picture of the schedule*... History."

    pov "*bell rings*"

    pov "Oh no! I’m late!"

    pov "*enter Class*"

    pov "Sorry I’m late, Mrs. Ong."

    o "The Nerve! In my day, if we were late, we would be paddled! With a wooden spoon! Sit down, before I get any angrier. Now, class. What is the..."

    pov "*brain wandering off*"


    o "Mr MC can you tell me what the capital of Texas is?"

    pov "Er… Is it Houston."

    o "Actually, it’s Austin. Now, if you would stop dozing off in class, maybe you would learn something. In my day, we were whipped if we fell asleep in class!" 

    pov "Urgh… yes, Mrs Ong."

    o "Now, class. To start off the year, we will be researching how civilizations in the fertile crescent rose to power. By Friday, I want an essay no longer than 750 words on this subject. If you do not do this assignment, it will severely impact your grade at this, the beginning of the school year! *Bell rings* Dismissed!"

    pov "*In the hallway* *Groan* I can’t believe I got homework on the first day of school. What kind of sick place is this?" 

    who "*shoulder bumps into MC* Hey, freshie, if you can’t take the heat get out of the oven. *Hurries off*"

    pov "What? Whatever… *end scene*"












    #INSERT ELECTIVES HERE






















    #END ELECTIVE HERE



    #*Initiate end of day 1*
    #*Walking Home*

    m "Hey, wait up!"

    pov "!?"

    m "I wanted to thank you for helping me out. I’ve never seen you before. What’s your name?"

    pov "Uh… No problem… my name is *tells him name*... hey…"

    m "If you ever need anything, let me know. I’ll return the favor." 

    pov "Oh, uh, ok… Thanks..."

    m "Cya round."
    
    pov "Um, Ok. Cya." 


    "*At home*"

    "*Phone is ringing*"

    #PICK UP THE PHONE

    pov "Hello?"

    mom "Hey honey! How was the first day of school?"

    pov "Oh, it was alright I guess."

    mom "Make any new friends?"

    pov "Erm, Maybe."

    mom "*sigh* Well, that's something. You should try to be friends with more people, like your sister."

    pov "Ok, Mom. I’ll try."

    mom "Don’t try, do! *sigh* Love you, hun."

    pov "Love you too, mom. *click*"

    pov "*Sigh* It’d be nice if mom or dad was home for once..."

    pov "*end scene*"



    #DONT PICK UP THE PHONE


    pov "*groan* Ugh! I wonder who it is. Well, they can wait. I need to sleep... Today was busy..."

    pov "*end scene*"

        
        
        
        
        
        
        
        
        
        
        
        
    return
