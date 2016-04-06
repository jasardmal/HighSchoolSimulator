    label firstSchoolDay:
        
        scene img_1832 with Dissolve(1.0)
        "*Bell Rings*"
        $ thephase = 3;

        pa "Welcome to the first day of school at Ketsu High School! Here, we…."

        mc "That guy, there in the back? {w} That’s me. {w} I just moved here from Utah. {w} This is my first day at Ketsu High, and I don’t know anyone. {w} This day is gonna be such a drag."

        pa "....... And that is how the Cougars roar! Have a wonderful day, students!"

        mc "Ugh. {w} When I moved here, I thought that not really knowing anyone might be nice. {w} My parents are always gone on some trip or another, {w} so I don’t really have any actual 
            interactions. {w} This year, I thought that maybe, {w} just maybe, {w} I could find someone who would actually be my friend."

        #Desk Slams Forward

        show marcw
        mw "Watch yourself! {w} Keep talking and maybe, {w} someday you'll say something intelligent!"
        hide marcw

        s1 "If you weren’t so easy to make fun of, {w} I wouldn’t! {w} You’re just a little baby."

        show marcw
        mw "Says the brat who's about to cry like one!"

        #Punches other student
        
        #Fight Ensues
        
        #Wipes Chin

        mw "I told you not to insult me. {w} Idiot."
        hide marcw

        #Teacher comes in
        
        mh "Hey! {w} What’s going on? {w} How dare you engage in classroom violence! {w} Don’t you know that fights are against school rules? {w} Both of you, {w} to the dean’s office!"

        #Marc and other student leave

        mh "You! {w} New student! {w} You were the closest and probably saw what happened the best. {w} Go to the deans office with them to fill out an incident report!"

        mc "But, wait, {w} no…."

        mh "Don’t argue, {w} just do it! {w} Don’t keep what you know to yourself! {w} Go to the Dean’s office!"
        
        #Sighs

        mc "F-Fine..."
        
        #Grumbling as you leave
        
        mh "Back in my day, {w} when we had to fight over things, {w} we waited until after school...."

        #CHANGE SCENES WOO DEAN'S OFFICE TIME

        #MC Standing outside door about to walk in
        scene img_1831 with Dissolve(1.0)

        show dean
        de "Now, {w} you both know better! {w} I can’t believe that it hasn’t even been a day into the school year and you have already begun fighting! {w} Shame on both of you! {w}
            Have you no dignity?!?!"
        hide dean

        show marcw
        co "Sorry, Mr Dean. It won’t happen again."
        hide marcw
        
        #Under his breath

        show marcw
        mw "Fat lard."
        hide marcw
        
        s1 "Excuse me? {w} What did you call me?"

        show marcw
        mw "Nothing, {w} I was talking about your mother."
        hide marcw

        show dean
        de "Both of you! {w} Behave! {w} Do you have ANY deceny? {w} You haven’t even left my office! {w} Marc, {w} stay here, and let him go."
        hide dean
        
        $mwname = "Marc"

        show marcw
        mw "Fine. {w} But he’s still a fat lard."
        hide marcw

        show dean
        de "One more word out of you and I will suspend you!"
        hide dean
        
        show marcw
        mw "..."
        hide marcw
        
        #Walks in

        show dean
        de "Who are you?"
        
        mc "I’m a new student. {w} I just moved here a few weeks ago. {w} Mr. Hart told me to come down here because I was closest to the fight, {w} so that I can fill out a report."

        show dean
        de "Oh. Well, {w} in that case, {w} let me get one of those for you."
        
        #Rummages through cabinet file
        
        label firstdayschoolchoice1:

            mc "What did I see?"

            #OPTIONS
            
            menu:

                "Marc started it":
                    $ toldonmarc = True
                    jump firstSchoolC1O1
                
                "Marc didn't start it":
                    $ toldonmarc = False
                    jump firstSchoolC1O2


        label firstSchoolC1O1:
            #MARC STARTED IT
            mc "It looked to me like that student (Marc) was antagonizing the other student. {w} I’m not sure what was said, {w} but one minute I was waiting for class to start, {w} 
                and the next those two were duking it out by my desk."

            de "Well, {w} are you sure you didn't see anything else?"
        
            mc "All I know is the two were fighting. {w} I don’t know enough about either of them to tell."
            
            de "Well, {w} all right then. {w} Get back to class."
            
            mc "Yes, sir."

            de "On your way back out, {w} call Marc back in."
            
            mc "Which one is Marc?"

            de "The one who probably started the fight."
            hide dean

            mc "Oh, alright."

            #Walks out

            mc "Marc? {w} The dean wants to see you."
            
            show marcw
            mw "Ugh, {w} finally. {w} I wish this would just be over… {w} I can’t stand it when people insult me and get away with it."
            hide marcw
            
            #Marc goes to office

            #Goes to class
            jump firstSchoolPath

        label firstSchoolC1O2:
            #MARC DIDN'T START IT

            mc "Well… {w} To be honest, {w} it seemed to me like the one who is still sitting outside was the victim. {w} The other one had made some rude comments about him, {w} and he didn’t like it."
            
            de "Is that right? {w} Well, {w} so far, {w} that’s not what I’ve heard. Are you sure?"
            
            mc "Yes, Sir. {w} I’m sure."
            
            de "Hmm… {w} Alright. Go back to class… {w} Thank you for your help."
            
            mc "Yes, sir."
            
            de "On your way back out, {w} call Marc back in."
            hide dean
            
            #To himself

            mc "Marc must be the one who is still in the foyer. {w} Ok."

            #Walks out

            mc "Marc? {w} The dean wants to see you."

            show marcw
            mw "Ugh, {w} finally. {w} I wish this would just be over… {w} I can’t stand it when people insult me and get away with it."
            hide marcw

            #Marc goes to office

            #Goes to class
            jump firstSchoolPath

        label firstSchoolPath:
        #AFTER BOTH VERSIONS:
        scene img_1832 with Dissolve(1.0)
        
        mh "Welcome back!"

        #Bell Rings

        #Slams book closed dramatically
        
        mh "Alright, {w} Class Dismissed."
        
        #To Himself
        scene img_1831 with Dissolve(1.0)

        mc "I should probably get to my next class. {w} It’s no good to dawdle. Looks like my next class is… {w}"
            
        #Shift to picture of the schedule
            
        mc "... History."

        "*Bell rings*"
        $ thephase = 4

        mc "Oh no! {w} I’m late!"

        #Enter Class
        scene img_1832 with Dissolve(1.0)

        mc "Sorry I’m late, Mrs. Ong."

        mo "The Nerve! {w} In my day, {w} if we were late, {w} we would be paddled! {w} With a wooden spoon! {w} Sit down, before I get any angrier. {w} Now, class. {w} What is the…"

        #Brain wandering off*

        mo "Mr. [mcname], {w} can you tell me what the capital of Texas is?"

        mc "Er… {w} Is it Houston?"

        mo "Actually, {w} it’s Austin. {w} Now, {w} if you would stop dozing off in class, {w} maybe you would learn something. {w} In my day, {w} we were whipped if we fell asleep in class!"

        mc "Urgh… yes, Mrs. Ong."

        mo "Now, class. {w} To start off the year, {w} we will be researching how civilizations in the fertile crescent rose to power. {w} By Friday, {w} 
            I want an essay no longer than 750 words on this subject. {w} If you do not do this assignment, {w} it will severely impact your grade at this, {w} 
            the beginning of the school year!"
            
        "*Bell rings*" 
                      
        mo "Dismissed!"
        
        #In the hallway
        scene img_1831 with Dissolve(1.0)
        
        #Groan

        mc "I can’t believe I got homework on the first day of school. {w} What kind of sick place is this?"
        
        #Shoulder bumps into MC

        show frederickh:
            xalign 0.5 yalign 0.01
        fh "Hey, freshie, {w} if you can’t take the heat get out of the kitchen."
        hide frederickh
        
        #Hurries off"

        mc "What? {w} Whatever…"
        $ thephase = 5
        jump period
        
        #Initiate end of day 1
        label firstSchoolDayEnd:
            
            scene img_1801 with Dissolve(1.0)
        
            mc ">Walking Home"

            show marcw
            mw "Hey, {w} wait up!"

            mc "!?"

            mw "I wanted to thank you for helping me out. {w} I’ve never seen you before. {w} What’s your name?"

            mc "Uh… {w} No problem… {w} my name is [mcname]... {w} hey..."

            mw "If you ever need anything, {w} let me know. {w} I’ll return the favor." 

            mc "Oh, uh, {w} ok… {w} Thanks..."

            mw "Cya round."

            mc "Um, Ok. See ya." 

            #*At home*
            scene img_black with Dissolve(1.0)
            $ location = 2
            $ thephase = 11
            
            label firstdayschoolchoice2:
                
                mc "*Phone is ringing*"
                
                menu:
                    
                    "Pick up the phone":
                        jump firstdayschoolC2O1
                    
                    "Don't pick up the phone":
                        jump firstdayschoolC2O2

            #Pick up the phone
            label firstdayschoolC2O1:

                mc "Hello?"

                mom "Hey honey! {w} How was the first day of school?"

                mc "Oh, {w} it was alright I guess."

                mom "Make any new friends?"

                mc "Erm, {w} Maybe."

                mom "Well, {w} that's something. {w} You should try to be friends with more people, like your sister."

                mc "Ok, Mom. {w} I’ll try."

                mom "Don’t try, {w} do! {w} *Sigh* {w} Love you, hun."

                mc "Love you too, Mom. {w} *Click*"

                mc "It’d be nice if Mom or Dad was home for once..."
                
                #*End scene*
                
                $ thephase = 11 + 1
                $ isfirstschoolday = False
                $ issecondschoolday = True
                jump startDecider
                
            #Don't pick up the phone
            label firstdayschoolC2O2:
                mc "Ugh! {w} I wonder who it is. {w} Well, {w} they can wait. {w} I need to sleep… {w} Today was busy..."

                #*End scene*
                
                $ thephase = 11 + 1
                $ isfirstschoolday = False
                $ issecondschoolday = True
                jump startDecider
            
    label secondSchoolDay:
        
        scene img_black with Dissolve(1.0)
            
        #*Alarm rings*

        mc "Urgh… {w} My head…"

        #Alarm rings again

        mc "Fine, {w} I’ll get up. {w} Where’s my toothbrush?"

        #*Screen shakes because he's looking for stuff*

        #OBTAINED TOOTHBRUSH

        mc "Aha! Here we go."

        #*KNOCK KNOCK KNOCK*

        mc "What? {w} Who’s here? {w} Who even knows I live here?"
        
        show marcw
        mw "OI! {w} YOU READY FOR SCHOOL?"

        mc "Marc?!?!?!?!?!?! {w} Wha-"

        mw "YOU’RE GUNNA BE LATE BRO!"
        hide marcw

        mc "Ok, ok! {w} I just got out of bed! {w} Let me put on some clothes first, jeez!"
        
        #*Puts on clothes*

        #*Runs out of door*

        #*Out of breath*
        
        scene img_1801 with Dissolve(1.0)

        mc "Alright, Marc, {w} I’m here. {w} How did you figure out where I live?"

        show marcw
        mw "You dropped your wallet. {w} Your address was inside."

        mc "......Oh......"

        mw "You probably want this back." 

        #*Hands over wallet*

        #*OBTAINED WALLET*

        mw "Now we’re even."

        mc "Even?"

        mw "Yeah, {w} for when you had my back at the dean’s."
        
        if toldonmarc == False:
            
            mc "Oh, {w} Right."
            
        else:
            
            mc "Oh, Uh, {w} Right, {w} Sure."

        mw "Sooo… Shall we? {w} If we stand here any longer, we’ll be late for school."

        mc "Oh! {w} Let’s go."

        #Arrives at school
        scene img_1831 with Dissolve(1.0)

        mw "Hey, {w} [mcname]. {w} Can I talk to you for a sec?"

        mc "Uh, {w} sure Marc. {w} What’s up?"

        mw "Since you’re new in town, {w} you probably don’t know nothin ‘bout anything. {w} If you want to get through the year, {w} you’ll need someone to show you around. {w} I can do that for you."

#        label seconddayschoolchoice1:
        
#            menu:
                
#                "You Could? That’d be great!": #(+affection)
#                    jump seconddayschoolC1O1
#                "I think I would rather do it on my own.": #(- affection)
#                    jump seconddayschoolC1O2
#                "Uh, sure....":
#                    jump seconddayschoolC1O3
                    
                    
#        label seconddayschoolC1O1:
#            mw "Alright, meet me after school in the courtyard, ok? See you in class!"
#            jump secondSchoolDayPath1
#        label seconddayschoolC1O2:
#            mw "Oh, ok. Well, let me know if you need anything then. See you in class."
#            jump secondSchoolDayPath1
#        label seconddayschoolC1O3:
#            mw "‘Kay. Cya Round."
#            jump secondSchoolDayPath1
            
#    label secondSchoolDayPath1:        
                
#        Scene Change MATH CLASS

#        mk "Ok Class! Take your seats! One… One… Two… Three… Five… Eight… Thirteen… Twenty one…"

#        Continues mumbling (LEAVE RESOLUTION OF JOKE UNTIL THE END OF THE YEAR, TELLS STUDENTS THAT IT’S THE FIBONACCI SEQUENCE)

#        nm "........" 

#        nm "*Scribble scribble*"

#        mk  "Now, class. I know that you hate homework on the first day, but I want to get you all learned up by the end of the year."

#        Collective groans

#        mk "I will hand out your assignments on the way out. For now, there is a text book under everyone’s desk. Pull it out and turn to page 394. That is where we will start."

#        #MORE GROANS

#        mk "Today’s topic will be geometry. You know, I really like angles, to a certain degree."

#        mc "............ was that a pun"

#        mc "What was that pun"

#        nm "*Doodles smiley faces*"

#        mk "Ms. McNeil, I don’t see you opening up your textbook. Please don’t try to measure my patience."

#        nm "*Quickly sketches frowny face and shows it to Mr. Kelly*"

#        mk "... Okaaaaaay Ms. McNeil, I think you should put away your sketchbook now."

#        nm "*Opens eyes really wide, vigorously shakes her head*"

#        mk "I insist."

#        nm "*Eyes tear up a bit, puts sketch book away and begins to sulk*"

#        mk "That’s better."

#        Later in class

#        mk ".... and that’s how these laws of geometry work. You, know, it’s a shame parallel lines will never meet. They have so much in common."

#        Class groans

#        Bell rings 

#        mk "Alright class, you are dismissed."

#        label seconddayschoolchoice2:
        
#            menu:
                
#                "Ask how she's feeling":  #(+affection)
#                    jump seconddayschoolC2O1
#                "Question her behavior": #(-Affection)
#                    jump seconddayschoolC2O2
#                "Ignore her":
#                    jump seconddayschoolC2O3
                    
                    
#        label seconddayschoolC2O1:
#            mc "Hey, are you ok? I couldn’t help but notice that you seemed upset."
#            nm "*Blushes"
#            jump secondSchoolDayPath2
#        label seconddayschoolC2O2:
#            mc "Why didn’t you pay any attention in class? Are you mute?"
#            nm "*Makes an angry face*"
#            jump secondSchoolDayPath2
#        label seconddayschoolC2O3:
#            jump secondSchoolDayPath2
            
#    label secondSchoolDayPath2:
        
#        mc "Huh. That was strange…."

#        mc "My next class is science, it looks like. I’d better get there fast."


#        Scene change = ENTER SCIENCE

#        mg "Before you sit down, line up at the back of the room. I have some important questions."

#        mg "Since this is a science class, we must observe the scientific method. That means collecting questions. Now, my first question is this:…"

#        Fade out

#        mc "....Now, pick your partners. We will begin our lectures tomorrow, and collect data. Tonight, I want you to take notes on the first chapter of the textbook. Before you leave, let me know who you are sitting with. If you don’t, you will be randomly assigned with a partner. Go!"

#        mc "Uh… Hey… Anyone want to be my partner?"

#        mc "Anyone? Hey, you… No? Alright…"

#        mc "Urgh… Seems like no one is available…"

#        mg "Now, does anyone not have a partner yet?"

#        Looks around  

#        mc "Uh, I guess I don’t have a partner yet…"

#        mg "Interesting. Now, could you take a look around the room? Can you tell me what you see?"

#        mc "Uhm… Oh." 

#        Looks at agnes 

#        mc "Uh, alright. Hi…"

#        ar "Hi."

#        mg " Wonderful. Now, tomorrow’s lecture will be about the chapter in which you are currently engaged in notetaking. Remember, the chapter notes will be due at the end of every week. The first chapter is rather short, so if you do not have them completed, there will be no excuse."

#        Staring at her phone, headphones in

#        mc "Um, hi. Er, since we are working together and everything, I was wondering…"

#        ar "Hmmm?"

#        mc " Oh, I was just wondering…"

#        ar "Agnes. But don’t call me that. I prefer..."

#        ar ".... Novahawk."

#        mc " Uh… Right… Novahawk… ok…"

#        ar " Mhm. Now get outta here."

#        Agnes leaves 

#        mc ".........Huh."

#        mc "I guess it’s time for the electives now. Let’s see what Marc is up to."

#        Insert Elective here*

#        mw "...And that’s how you disguise your phone number."

#        mc "Oh, cool… What would I use that for?"

#        mw "Probably nothing, but hey, the more you know."

#        #OPTION ⅓-  Marc shows you around, takes you to where Sarah works
#        #Player discovers more places, affection with Marc goes up

#        mw ".... And that’s why Marcy’s is cheaper than Jenny’s. Good way to save your money on clothes."

#        mc "Oh ok, thanks for letting me know."

#        mw "So I was thinkin’, there’s this place up by the Cafe that I hang around, got a bunch a’ video games and stuff. Wanna hit it, see if there’s something ya wanna play?" 

#        mc "Er, sure. What kinds of games are there?"

#        mw "Oh ya know, things like fighting games, racing games, shooters. All kinds. It’s right over here, let’s get going."

#        mc "Uh yeah, let’s go..."

#        *In Arcade*

#        mw "Check out this game, dude!"

#        mc "Erm, alright… What game is this?"

#        mw "It’s the hottest game in the arcade! You HAVE to try it."

#        mc "Oh, okay cool… What do I do?"

#        mw "Well, first, you start by..."
        
#        *minigame tutorial, insert minigame here*

#        mw "... And that’s how you can use the combos to get higher scores."

#       ### mc  "You know, this game is 1) pretty fun! [small increase in affection] 2) pretty lame. 3) not too bad."

#       ### mw 1) That’s awesome! This is my favorite game in the arcade.
#       ###           2-3) Oh well, to each their own. I really like it myself.

#        mw "Hey are you feeling hungry? My stomach just started to growl."

#        mc "*STOMACH GROWLS, SCREEN SHAKES AS REPRESENTATION* Oh! I’m feeling hungry too. Do you know any good places to eat?"
        
#        mw "Actually I do, there’s a place not too far from here that’s super popular with the students at our school. A senior named Fredrick runs the place, and a friend of mine works there."

#        mc "Ok cool, let’s go."

#        *Outside Cafe*

#        mw "Here’s the place. Roland’s Sweet Honey Cafe."

#        mc "Looks nice."

#        mw "I’m starving, let’s go in and get some food."

#        *Inside Cafe*

#        mc "There’s a lot of people here." 

#        mw "Yea, almost everyone comes here after school to hang out and unwind."

#        ???(Fred) "Well, if it isn’t the freshie who can’t take a bit of homework."

#        mw "Excuse me Fredrick!?!?!?!"

#        fh "No, not you, your friend here."

#        mc "W-w-what? W-what do you mean?"

#        fh "Forgetful, are we? Just yesterday I caught you complaining about homework on the first day. I told you to grow a pair."

#        mw "*Snickers*"

#        mc "Marc!"

#        mw "Sorry, it is a little funny. You probably shouldn’t complain too much."

#        mc "Y-you’re one to talk!"

#        mw "Yeah, probably. But still, that was FUNNY."

#        bk "Frederick, that’s no way to treat new customers. You know better."

#        fh "Becka!! My apologies. You’re right. It was just that… he was being whiny yesterday and it bothered me, I mean, he hasn’t even been to any higher level classes..."

#        bk "Shush. You were exactly the same way. As were most of the members of our class, if I recall correctly."

#        fh "Well I Ne-..."

#        bk "Now apologize to your customer."

#        fh "*BLUSHING* You do not own this cafe! I do! Argh!" 

#        fh "But, you are right. I must be more… professional. *turns to MC and Marc* As a consolation, your drinks are on the house. You are welcome."

#        bk "Now, that wasn’t so hard was it?"

#        fh "Oh for heaven’s sake!" 

#        *frederick and becka leave*

#        mw "Huh. Anyway, let’s go sit somewhere."

#        mc "Uh… okay, that sounds good to me."

#        ???(sarah) "Hey Marc! How’s it goin?"

#        mw "Sarah! How’s business today?"

#        sg "Oh, you know, it’s been pretty busy, being the first few days in the school year and all... What can I get for you guys?"

#        mw "I’ll have the usual. Frederick said we get free drinks today."

#        sg "Did he now? Well, alright, I trust you. And who’s this?"

#        mw "This is (MC)! He just moved into town. He’s a freshman, like me. In fact, he lives in our neighborhood!"

#        sg "Oh? And how would you know? Did you follow him home?"

#        mw "... Something like that."

#        mc "Uhh..."

#        mw "Don’t worry about it. What are you gonna order?"

#        mc "Err, what does the chef recommend?"

#        sg "Today we have a special on Caesar Salads. Comes with grilled chicken and garlic bread."

#        mc "Sounds good, I’ll have that."

#        sg "Then I’ll be back in a jiffy."

#        mw "Thanks!"

#        mc "So… How do you and Sarah know each other...?"

#        mw "Oh, me and Sarah? We go way back. Grew up together, almost."

#        mc "Really? That’s cool..."

#        sg "Hey guys! Here are your drinks. I’ll be back in a sec with your food."

#        mw "Thanks! Do you have a minute to sit with us after that?"

#        sg "Oh, no, sorry. Not today. We are up to our elbows in customers, haha."

#        mw "Alright, maybe next time then."

#        sg "See you later!"

#        mw "Hey wait! How is your leg doing?"

#        sg "Oh, well, I’ve been doing better… Healing a broken bone doesn’t happen overnight, you know?"

#        mw "True, true. Well, get better soon! The team needs you."

#        sg "Haha, thanks. I’ll see you around."

#        mc "...I didn’t notice her cast. What happened?"

#        mw "It’s a bit of a nasty story. Let’s just say there was a really, really bad accident." 

#        mc "Oh… Uh, how long has she had the cast?"

#        mw "Too long. The whole summer, and then some. It was really bad." 

#        mw "Thinking about this is depressing. Let’s finish up and get out of here."

#        mc "Uhhh, sure." 

#        *Dining room noises*

#        mw "That was really good! I always enjoy eating here. Are you done?"

#        mc "Yeah, I think I’m finished. Let’s go."

#        mw "Sweet. I'll see you tomorrow."

#        *scene transition*



#       ######## #OPTION 2-  Player walks around on their own, ends up where Sarah works because hungry, Marc is there cracking a joke

#        mc "Well school’s out now, I wonder what I should do… Looks like a bunch of students are going over to that cafe over there, I think I’ll go check it out."

#        *walks over to the cafe*

#        mc "Roland’s Sweet Honey Cafe… weird name..."

#        *walks in*

#        *Inside Cafe*

#        mc "There’s a lot of people here." 

#        ???(Fred) "Well, if it isn’t the freshie who can’t take a bit of homework."

#        mc "W-w-what? W-what do you mean?"

#        fh "Forgetful, are we? Just yesterday I caught you complaining about homework on the first day. I told you to grow a pair."

#        mc "H-hey! G-get out of my face!"

#        fh "Why, you insolent..."

#        bk "Frederick, that’s no way to treat new customers. You know better."

#        fh "Becka!! My apologies. You’re right. It was just that… he was being whiny yesterday and it bothered me, I mean, he hasn’t even been to any higher level classes..."

#        bk "Shush. You were exactly the same way. As were most of the members of our class, if I recall correctly."

#        fh "Well I Ne-..."

#        bk "Now apologize to your customer."

#        fh "*BLUSHING* You do not own this cafe! I do! Argh!" 

#        fh "But, you are right. I must be more… professional. *turns to MC* As a consolation, your drink is on the house. You are welcome."

#        bk "Now, that wasn’t so hard was it?"

#        fh "Oh for heaven’s sake!" 

#        *frederick and becka leave*

#        mc "Jeez… what’s his problem..."

#        *scene cut to Marc talking to some girl (Sarah)*

#        mw ".... And that’s how I avoided getting into trouble with the dean."

#        sg "...You aren’t serious."

#        mw "Yes I am! Look, at school tomorrow I’ll have you meet the guy."

#        sg "Uh huh."

#        mw "Well, speak of the devil and he shall appear! He’s right there!"

#        mc "h-huh?! Excuse me? W-what’s going on?"

#        mw "Oh, I was just telling my friend Sarah here how I met you yesterday. So, how’s solo explorin’ going?"

#        mc "G-good, I guess..." 

#        sg "So, what’ll it be? I assume you *are* here to eat."
        
#        mw "I’ll have the usual. Oh, by the way, have you met MC? He just moved to town. He even lives in our neighborhood!"

#        sg "Oh? And how would you know? Did you follow him home?"

#        mw "... Something like that."

#        mc "Uhh..."

#        mw "Don’t worry about it. *to MC* What are you gonna order?"

#        mc "Err, what does the chef recommend?"

#        sg "Today we have a special on Caesar Salads. Comes with grilled chicken and garlic bread."

#        mc "Sounds good, I’ll have that." 

#        sg "Then I’ll be back in a jiffy."

#        mw "Thanks!"

#        mc "So… How do you and Sarah know each other...?" 

#        mw "Oh, me and Sarah? We go way back. Grew up together, almost."

#        mc "Really? That’s cool..."

#        sg "Hey guys! Here are your drinks. By the way, Frederick said that you get a free drink, MC. I’ll be back in a sec with your food."

#        mw "Thanks! Do you have a minute to sit with us after that?"

#        sg "Oh, no, sorry. Not today. We are up to our elbows in customers, haha."

#        mw "Alright, maybe next time then."

#        sg "See you later!"

#        mw "Hey wait! How is your leg doing?" 

#        sg "Oh, well, I’ve been doing better… Healing a broken bone doesn’t happen overnight, you know?"

#        mw "True, true. Well, get better soon! The team needs you."

#        sg "Haha, thanks. I’ll see you around."

#        mc "...I didn’t notice her cast. What happened?"

#        mw "It’s a bit of a nasty story. Let’s just say there was a really, really bad accident." 

#        mc "Oh… Uh, how long has she had the cast?"

#        mw "Too long. The whole summer, and then some. It was really bad." 

#        mw "Thinking about this is depressing. Let’s finish up and get out of here."

#        mc "Uhhh, sure." 

#        *Dining room noises*
  
#        mw "That was really good! I always enjoy eating here. Are you done?"

#        mc "Yeah, I think I’m finished. Let’s go."

#        mw "Sweet. I'll see you tomorrow."

#        *Scene Change Home*

#        RING RING RING RING RING

#        mc "Wow! As soon as I get home, someone else is calling me. Is it going to be like this every night?"

#        mc "I had probably better pick up the call..."


#        mc 1. Pick up 2. Don’t

#        mc Oh. Look. It’s my sister.

#        Jackie "Hey little bro! How was your first few days of school?"

#        mc "Oh! Hey, Jackie! It’s been a while."

#        Jackie "Yeah, well, you know, college and all that. How’s my socially awkward padawan learner?"

#        mc "Urgh, I’m doing fine… Why do you always reference that movie?"

#        Jackie "Because it’s *our* favorite, and don’t you forget that."

#        mc "But you know I don’t..."

#        Jackie "Shush, yes you do. Anyways, do you have a girlfriend yet?"

#        mc "What?!?! I literally just got here and..."

#        Jackie "No excuses! Get moving, casanova!"

#        mc "Argh! I don’t even know anyone yet!"

#        Jackie "Sure you don’t, Romeo." 

#        mc "Okay, fine, I’ve met a grand total of 4 people. None of whom I know very well."

#        Jackie: Any girls?

#        mc "...Two. But..."

#        Jackie "Are they pretty?"

#        mc "...What? Wait… No, that doesn’t… leave me alone!"

#        Jackie "Alright, Valentine. I’ll keep cupid off your back... for now. Don’t be surprised if you find an arrow in your butt later in the year."

#        mc "An arrow?"

#        Jackie "You know, the arrow of love? Nevermind, loverboy. I’ll talk to you later. Don’t forget to give mom and dad a call every now and then!"

#        mc "Ok, I’ll do that. Don’t you have college things to do?"

#        Jackie "Yeah probably. Oh, and by the way, I looked at your school’s website and it looks like homecoming is coming up soon. So, like I said, get a date. Cupid will watch over you."

#        mc "...Uh, Ok... Sure..."

#        Jackie "See ya round! *hangs up*"

#        mc "Jeez... That was really something... I’d better get some sleep..."

#       *End Day* 

#       2) mc "Egh... It’s probably not important. You know, today was really long. I’m glad I met all these people, though. I hope they will be my friends... *Yawn* Wow, I’m tired. I should really get some sleep. I hope that call wasn’t important..."



###########################Homecoming#############################################################################


#*Cynthia gives Danny relationship advice, telling him to just *ask that girl* out, thinking that that girl is herself. She is shocked when it is in fact not.*


#cl "Heyy Dannyyy, what’s hangin, bangin?"

#dr "O-oh, hey Cynthia. It’s hangin."

#cl "That’s pretty sweet, sugar. You know, Homecoming is coming up soon. If there’s a girl you like, don’t you think that it’s about time for you to ask her out? *leans in too close*"

#dr "O-oh yeah, probably. I should do that."

#cl "Yeah, you should! I’ll see you around, darling."

#dr "A-alright. See you around!"

#*CL leaves*

#mc "Oh, homecoming is coming up soon…. I wonder if Marc and Sarah are going to go..."

#*bumps into DR*

#mc "Oh! Sorry. That was my fault."

#dr "No, it’s fine. Don’t worry about it."

#mc "Oh, alright. What is your name?"

#dr "My name is Danny. How about you?"

#mc "Oh, my name is __________. Who was that with you?"

#dr "Oh, her? That was Cynthia. She’s a cheerleader."

#mc "That’s cool. She seemed like she wanted something."

#dr "Huh? Nah, we’re just friends."

#mc "Ah, ok. Well, see you around."

#dr "Yep, see you."

#*Danny Leaves*

#mc "He’s totally clueless… Whatever. It’s not my business. Hmm… Looks like I have an A day today. That means… English and History. I should find Marc, and see what he’s up to. Where could he be? If I don’t find him soon, we could be late!"

#Check the field(+add stress, +affection w/marc)
#Go to class



#OPTION 1:

#mc "I should probably check the field. Maybe he’s there!"

#*switch background to a sports-y field*

#*MC and Marc both appear on the screen*

#mw "Oh, hey MC. What’s up?"

#mc "Well, class is about to start… I didn’t see you on the way to school, so I thought I’d find you."

#mw "What, are you following me?"

#mc "Y-you’re one to talk!"

#mw "Touché. Well, let’s get to class. I wouldn’t want to be too late."

#----

#*MC and Marc walk into class*

#mh "Hey! You two, why are you both coming into class late?"

#mc "Uhh..."

#mw "There was an accident on the freeway."

#mh "There isn’t a freeway nearby!"

#mw "Oh, right, I mean the, uh, the intersection on uh 3rd and 5th."

#mh "There isn’t even an intersection there!"

#mw "6th. I meant 6th."

#mh "Whatever! I’ll hold you to your word. If you are lying, I suppose it doesn’t matter. Just get to your seats."

#mw "*under breath* …. next time I’ll remember to not come at all."

#mc "*also under the breath* Jeez, Marc, chill."

#mw "Nah."

#mh "Now, class, before we begin, I want you to listen very carefully..."
#______________


#Option 2

#*gets to class*
#mc "*searches the room* Huh… I guess Marc hasn’t gotten to class yet..."

#mh "Everyone! Please take your seats. I will take attendance quickly so we can get right to work. MC?"

#mc "Here."

#mh "Felicia? Aaron? Thomas? Quade? Emmalie? Gregory? Selina? Hm… Marc? He’s not here. MC, do you know where he is?"

#mc "N-no, I don’t. Sorry."

#mh "It’s fine. Well, let's begin."

#*DOOR OPENS LOUDLY* 

#mw "... And that’s why turtles are cooler than tortoises. I’ll catch you later."

#Voice "Peace."

#mh "Marc Waller, who was that?"

#mw "Nobody important."

#mh "Well, I dare say it is! What were you doing?"

#mw "Talkin’."

#mh "Yes, I know that. About what?"

#mw "Stuff."

#mh "*Sigh* Fine, go sit down."

#mw "Sir, yes sir."

#mh "Now, before we begin, I want you to listen very carefully..."

#-------------------------------------------------------

#mh "Good work today, class. We will continue our reading of A Midsummer Night’s Dream  when we meet next. Class dismissed!"

#mw "Sooooooooooooooooooooooooooooooo, MCCCCCCCCCCCCCCCCC. Are you going to ask anyone out to homecoming?"

#mc "Well, I mean, I wasn’t thinking about it..."

#mw "But everyone is going! *author's note: I’ve never been to a homecoming Q.Q*"

#mw "C’meon dude, ask someone out."

#mc "Well, who are you going with?"

#mw "Well, since couples tickets are cheaper, Sarah and I are going together. As friends."

#mc "*makes finger air quotes* “Friends”. Right. Ok."

#mw "Are you trying to tell me something?"

#mc "No, I’m not saying anything. “friends”. Uh-huh."

#mw "Pft, what do you know. You don’t even have a date."

#mc "You should be my date, then."

#mw "*blushes* No, it’s just cheaper to go together... As friends."

#mc "I’m not doing the whole “friends” conversation again. You’re dating me."

#mw "I AM NOT"

#mc "You are too"

#mw "STOP"

#mc "Ok, ok, calm down a bit"

#mw "It’s not my fault, you kept egging me on"

#mc "Yeah I know. I’ll see you around. Maybe I’ll even see you at homecoming *wink wink*"

#mw "GAH"

#_______________________________________________

#*HALLWAY*


#mc "You know, maybe going to homecoming would be fun..." 

#dr "H-hey, u-uh Agnes?"

#ar "Novahawk. Yes?"

#dr "W-would you, you know, maybe like to..."

#ar "Well, spit it out already!"

#dr "Uh, maybe, you would want to, er, go to, uh, homecoming with me?"

#ar "Sure."

#dr "O-oh really? Fantastic! I-I’ll call you… wait, but I need your number first… Can I have your phone number?"

#ar "Yeah… Give me your phone."

#dr "O-ok… Here."

#ar "There you go. I’ll see you around." 

#dr "S-sounds good. I’ll talk to you later."

#*THEY LEAVE*

#mc "That… that was awkward."

#cl "W-WHAT! HE WAS SUPPOSED TO ASK MEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE! W-what a jerk!"

#mc "I’m sure he has good intentions… do you even know if he likes you?"

#cl "Yes, he does! He just likes to play hard-to-get. There is no doubt in my mind that he loves me!"

#mc "... Right… Hard-to-get..."

#cl "S-shush! He does, I’m telling you! Maybe he doesn’t know it yet, but he does! I need to go and think!"

#mc "Great, I’ll talk to you later." 

#______________________________________________

#*Lunch*

#mw "Hey who you are going to homecoming with?"

#mc "I.. uh… I’m not even sure if I’m going yet."

#mw "Well, you better figure out who you are going with because I got you a ticket."

#*MC Obtains Homecoming Ticket*

#mc "Wait... Uh... but..." 

#mw "Don’t worry you won’t have to pay me back. This is all on me."

#mc "Oh... but..."

#mw "Don’t worry about it! Homecoming will be fun, you won’t want to miss it!"

#sg "Wait... Mark, I thought we were going together?"

#mw "We ARE going together! But now we are bringing MC with us!"

#sg "Oh... Uh, awesome... It’ll be fun!"

#mw "I know right! Hey, I gotta go take care of something at my locker before lunch ends. I’ll cya later!"

#sg + mc "...See ya..."

#sg "Did you know he was going to do that?"

#mc "What? No! I wasn’t even sure yet, but I guess I’m going now..."

#sg "Ha, yeah, I guess so. I really thought… Nevermind. Whatever. I have to go." 

#mc "Um, alright. Bye."

#sg "..........."

#*end scene*

#*Next day*

#*in his house*

#mc "Well, tonight is homecoming I guess. I suppose I had better get ready..."

#*Phone rings*

#mc "Hello?"

#Jackie: "Heyy, bro! Are you going to Homecoming?"

#mc "Oh, uh, y-"

#Jackie: Well, you had better be! Otherwise I would have gotten you that expensive tuxedo for nothing.

#mc "Wait, what Tuxedo?"

#Jackie: Haven’t you gotten it yet? *Authors’ note: Jackie and Marc are in cahoots* You should have gotten it a few days ago!

#mc "Well, I-"

#Jackie: Go outside and check right now! It should be in a nice, tall package!

#mc "Um, alright..."

#Jackie: Is it there?

#*Giant package on the front door step*

#mc "Oh, wow, there it is."

#Jackie: Wonderful! Try it on! It should fit you perfectly. 

#mc "Uh, okay then. I’ll do that. Any other secret packages I should be looking for?"

#Jackie: Not right now! Don’t worry, though, the future holds great things.

#mc "...Thanks." 

#Jackie: No problem! Remember, have fun!

#mc "...Yeah, Thanks..."

#Jackie: Bye Bye, now!

#mc "...Bye..."

#*jackie hangs up*

#mc "Ugh. It’s like this was planned, or something..."

#*Knocking on door*

#mw "Hey! MC! Are you ready yet?"

#mc "...Marc? Hold on, I just got my tuxedo..."

#mw "Tuxedo!? Wow, Mr. Fancy. Dressin’ in a tux."

#mc "Please don’t. My sister got it for me."

#mw "Oh, ok. Sounds like your sister expected you to have a date."

#mc "Maybe she does. She’ll be awfully disappointed then."

#mw "Haha I bet. Well, hurry up and get dressed, we need to leave soon."

#mc "Don’t you need to go get Sarah or something?"

#mw "OH! Yeah. I’ll be back in a few."

#mc "...Bye."

#mc "...."

#mc "I can’t believe he forgot his date..."

#*Scene shift to outside the house*

#mc "Where are they? I’d better just go."

#mw "Hey! Wait Up!"

#sg "Wait, Marc, not so fast..."

#mw "Huh?" 

#sg "..."

#mw "Ookay. Well, the gang’s all here. Now lets go to homecoming!"

#sg "You look very nice today, MC."

#mc "Oh, uh, thanks Sarah."

#sg "*Nods*"

#mw "You DO look spiffy. Hopefully walking there won’t dirty it up any." 

#mc "Haha, yeah, that would suck."

#*A limo pulls up beside them, and the chauffeur gets out and opens the door for the three to get in.*

#Chauffeur: Sirs, Madam. I will take you to homecoming.

#mc "I think you have the wrong address..."

#Chauffeur: I assure you, I do not have the wrong address. I was hired by one Jackie (Whatever the mc’s last name is).

#mc "Oh. I see. Well, alright then… I guess we won’t have to walk after all." 

#mw "Nice! Now your tux won’t get dirty."

#mc "...Yeah. It won’t."

#sg "Well, quit sitting around and get in the car. Homecoming won’t wait for your sarcasm."

#mc "Sorry, sorry. After you two."

#*End Scene*

#*New Scene* 

#*At homecoming*

#mw "... And that’s why a bow tie is more useful than a long tie."

#sg "Mark, please. Not everyone thinks"

#Dean: Welcome, everyone! Congratulations on surviving school so far. We haven’t done you in yet! 

#*Nervous murmuring from the crowd*

#Dean: Aww, don’t be like that! We are here to have fun! Before we begin, I have one important announcement to make…

#mw "Hey! Dude! Over here!"

#mc "Wha…?"

#mw "There you are! When we walked in here, you got lost in the crowd! It’s all good though, I found you."

#mc "Um, yeah, thanks haha."

#mw "Anyways, now that you are here, maybe you could find a date after all. I’ve seen a bunch of girls who don’t have dates!"

#mc "How would you even know? Just looking doesn’t seem like enough to judge."

#mw "Oh, trust me, I know about these sort of things."

#sg "*HUff* Yeah, sure."

#mw "What? What’s wrong?"

#sg "Oh, nothing, don’t worry about it."

#mw "Well, all right then. Anyways, go and have fun. That’s what we are here for."

#mc "Sounds good. I’ll let you two get to dancing, then."

#mw "Ha! I don’t dance. But I appreciate the gesture."

#sg "You aren’t going to dance with me?"

#mw "Oh, uh, sure I am..."



