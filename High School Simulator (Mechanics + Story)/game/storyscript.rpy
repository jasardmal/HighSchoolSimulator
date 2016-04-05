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
            
            $ hasmetmarc = True
            
            ">You can now view Marc's profile."

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


