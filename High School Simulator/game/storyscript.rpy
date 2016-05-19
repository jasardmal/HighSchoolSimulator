    label firstSchoolDay:
        
        scene img_class with Dissolve(1.0)
        "*Bell Rings*"
        $ thephase = 3;

        pa "Welcome to the first day of school at Ketsu High School! Here, we...."

        mc "That guy, there in the back? {w} That’s me. {w} I just moved here from Utah. {w} This is my first day at Ketsu High, and I don’t know anyone. {w} This day is gonna be such a drag."

        pa "....... And that is how the Cougars roar! Have a wonderful day, students!"

        mc "Ugh. {w} When I moved here, I thought that not really knowing anyone might be nice. {w} My parents are always gone on some trip or another, {w} so I don’t really have any actual 
            interactions. {w} This year, I thought that maybe, {w} just maybe, {w} I could find someone who would actually be my friend."

        #Desk Slams Forward
        show img_class with hpunch

        show marcw with moveinright:
            xalign 0.0 yalign 1.0
        mw "Watch yourself! {w} Keep talking and maybe, {w} someday you'll say something intelligent!"

        s1 "If you weren’t so easy to make fun of, {w} I wouldn’t! {w} You’re just a little baby."

        show marcw with moveinleft:
            xalign 0.5 yalign 1.0
        mw "Says the brat who's about to cry like one!"

        #Punches other student
        show img_class with hpunch
        
        #Fight Ensues
        show img_class with hpunch
        show img_class with hpunch
        show img_class with vpunch
        show img_class with vpunch
        
        #Wipes Chin

        mw "I told you not to insult me. {w} Idiot."

        #Teacher comes in
        
        mh "Hey! {w} What’s going on? {w} How dare you engage in classroom violence! {w} Don’t you know that fights are against school rules? {w} Both of you, {w} to the dean’s office!"

        #Marc and other student leave
        show marcw with moveinleft:
            xalign 1.0 yalign 1.0
        hide marcw

        mh "You! {w} New student! {w} You were the closest and probably saw what happened the best. {w} Go to the deans office with them to fill out an incident report!"

        mc "But, wait, {w} no...."

        mh "Don’t argue, {w} just do it! {w} Don’t keep what you know to yourself! {w} Go to the Dean’s office!"
        
        #Sighs

        mc "F-Fine..."
        
        #Grumbling as you leave
        
        mh "Back in my day, {w} when we had to fight over things, {w} we waited until after school...."

        #CHANGE SCENES WOO DEAN'S OFFICE TIME
        #MC Standing outside door about to walk in
        scene img_hall with Dissolve(1.0)

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
        
        $ mwname = "Marc"

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
            mw "Ugh, {w} finally. {w} I wish this would just be over... {w} I can’t stand it when people insult me and get away with it."
            
            #Marc goes to office
            show marcw with moveinleft:
                xalign 1.0 yalign 1.0
            hide macw

            #Goes to class
            jump firstSchoolPath

        label firstSchoolC1O2:
            #MARC DIDN'T START IT

            mc "Well... {w} To be honest, {w} it seemed to me like the one who is still sitting outside was the victim. {w} The other one had made some rude comments about him, {w} and he didn’t like it."
            
            de "Is that right? {w} Well, {w} so far, {w} that’s not what I’ve heard. Are you sure?"
            
            mc "Yes, Sir. {w} I’m sure."
            
            de "Hmm... {w} Alright. Go back to class... {w} Thank you for your help."
            
            mc "Yes, sir."
            
            de "On your way back out, {w} call Marc back in."
            hide dean
            
            #To himself

            mc "Marc must be the one who is still in the foyer. {w} Ok."

            #Walks out

            mc "Marc? {w} The dean wants to see you."

            show marcw
            mw "Ugh, {w} finally. {w} I wish this would just be over... {w} I can’t stand it when people insult me and get away with it."

            #Marc goes to office
            show marcw with moveinleft:
                xalign 1.0 yalign 1.0
            hide macw

            #Goes to class
            jump firstSchoolPath

        label firstSchoolPath:
        #AFTER BOTH VERSIONS:
        scene img_class with Dissolve(1.0)
        
        mh "Welcome back!"

        #Bell Rings

        #Slams book closed dramatically
        
        mh "Alright, {w} Class Dismissed."
        
        #To Himself
        scene img_hall with Dissolve(1.0)

        mc "I should probably get to my next class. {w} It’s no good to dawdle. Looks like my next class is... {w}"
            
        #Shift to picture of the schedule
            
        mc "... History."

        "*Bell rings*"
        $ thephase = 4

        mc "Oh no! {w} I’m late!"

        #Enter Class
        scene img_class with Dissolve(1.0)

        mc "Sorry I’m late, Mrs. Ong."

        mo "The Nerve! {w} In my day, {w} if we were late, {w} we would be paddled! {w} With a wooden spoon! {w} Sit down, before I get any angrier. {w} Now, class. {w} What is the..."

        #Brain wandering off*

        mo "Mr. [mcname], {w} can you tell me what the capital of Texas is?"

        mc "Er... {w} Is it Houston?"

        mo "Actually, {w} it’s Austin. {w} Now, {w} if you would stop dozing off in class, {w} maybe you would learn something. {w} In my day, {w} we were whipped if we fell asleep in class!"

        mc "Urgh... yes, Mrs. Ong."

        mo "Now, class. {w} To start off the year, {w} we will be researching how civilizations in the fertile crescent rose to power. {w} By Friday, {w} 
            I want an essay no longer than 750 words on this subject. {w} If you do not do this assignment, {w} it will severely impact your grade at this, {w} 
            the beginning of the school year!"
            
        "*Bell rings*" 
                      
        mo "Dismissed!"
        
        #In the hallway
        scene img_hall with Dissolve(1.0)
        
        #Groan

        mc "I can’t believe I got homework on the first day of school. {w} What kind of sick place is this?"
        
        #Shoulder bumps into MC
        show img_hall with hpunch

        show frederickh with moveinright:
            xalign 0.5 yalign 0.0
        fh "Hey, freshie, {w} if you can’t take the heat get out of the kitchen."
        
        #Hurries off"
        show frederickh with moveinright:
            xalign 0.0 yalign 0.0
        hide frederickh

        mc "What? {w} Whatever..."
        $ thephase = 5
        jump period
        
        #Initiate end of day 1
        label firstSchoolDayEnd:
            
            scene img_nearhome with Dissolve(1.0)
        
            mc ">Walking Home"

            show marcw with moveinright:
                xalign 0.5 yalign 1.0
                
            mw "Hey, {w} wait up!"

            mc "!?"

            mw "I wanted to thank you for helping me out. {w} I’ve never seen you before. {w} What’s your name?"

            if toldonmarc == False:
                
                mc "Uh... {w} No problem... {w} my name is [mcname]... {w} hey..."
                
            else:
                
                mc "Uh... {w} No problem... {w} (Shoot, I told on him.) {w} my name is [mcname]... {w} hey..."

            mw "If you ever need anything, {w} let me know. {w} I’ll return the favor." 

            mc "Oh, uh, {w} ok... {w} Thanks..."

            mw "Cya round."

            mc "Um, Ok. See ya."
            
            show marcw with moveinright:
                xalign 0.0 yalign 1.0
            hide marcw
            
            $ hasmetmarc = True
            
            ">You can now view Marc's profile."

            #*At home*
            scene img_home with Dissolve(1.0)
            $ location = 2
            $ thephase = 11
            
            label firstdayschoolchoice2:
                
                mc "*Phone is ringing*"
                
                menu:
                    
                    "Pick up the phone":
                        jump firstdayC2O1
                    
                    "Don't pick up the phone":
                        jump firstdayC2O2

            #Pick up the phone
            label firstdayC2O1:

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
            label firstdayC2O2:
                mc "Ugh! {w} I wonder who it is. {w} Well, {w} they can wait. {w} I need to sleep... {w} Today was busy..."

                #*End scene*
                $ thephase = 11 + 1
                $ isfirstschoolday = False
                $ issecondschoolday = True
                jump startDecider
            
    label secondSchoolDay:
        
        scene img_home with Dissolve(1.0)
            
        #*Alarm rings*

        mc "Urgh... {w} My head..."

        #Alarm rings again

        mc "Fine, {w} I’ll get up. {w} Where’s my toothbrush?"

        #*Screen shakes because he's looking for stuff*
        show img_home with hpunch
        show img_home with vpunch

        #OBTAINED TOOTHBRUSH

        mc "Aha! Here we go."

        #*KNOCK KNOCK KNOCK*

        mc "What? {w} Who’s here? {w} Who even knows I live here?"
        
        show marcw with moveinright:
                xalign 0.5 yalign 1.0
        mw "OI! {w} YOU READY FOR SCHOOL?"

        mc "Marc?!?!?!?!?!?!"
        
        show img_home with hpunch
        show img_home with vpunch
        show img_home with hpunch
        show img_home with vpunch
        show img_home with hpunch
        show img_home with vpunch
        show img_home with hpunch
        show img_home with vpunch
        show img_home with hpunch
        show img_home with vpunch
        show img_home with hpunch
        show img_home with vpunch
        show img_home with hpunch
        show img_home with vpunch
        show img_home with hpunch
        show img_home with vpunch
        show img_home with hpunch
        show img_home with vpunch
        show img_home with hpunch
        show img_home with vpunch

        mw "YOU’RE GUNNA BE LATE BRO!"
        hide marcw

        mc "Ok, ok! {w} I just got out of bed! {w} Let me put on some clothes first, jeez!"
        
        #*Puts on clothes*
        
        #*Runs out of door*
        scene img_nearhome with Dissolve(1.0)

        #*Out of breath*

        mc "Alright, Marc, {w} I’m here. {w} How did you figure out where I live?"

        show marcw with moveinright:
                xalign 0.5 yalign 1.0
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

        mw "Sooo... Shall we? {w} If we stand here any longer, we’ll be late for school."

        mc "Oh! {w} Let’s go."
        
        show marcw with moveinright:
                xalign 0.0 yalign 1.0
        hide marcw

        #Arrives at school
        scene img_hall with Dissolve(1.0)
        $ thephase = thephase + 1
        $ location = 1
        
        show marcw with moveinleft:
                xalign 0.5 yalign 1.0
        mw "Hey, {w} [mcname]. {w} Can I talk to you for a sec?"
        
        mc "Uh, {w} sure Marc. {w} What’s up?"

        mw "Since you’re new in town, {w} you probably don’t know nothin ‘bout anything. {w} If you want to get through the year, {w} you’ll need someone to show you around. {w} I can do that for you."

        label seconddayschoolchoice1:
        
            menu:
                
                "You Could? That’d be great!": #(+affection)
                    $ marcprogression = marcprogression + 1
                    jump seconddayC1O1
                "I think I would rather do it on my own.": #(- affection)
                    $ marcprogression = marcprogression - 1
                    jump seconddayC1O2
                "Uh, sure....":
                    jump seconddayC1O3
                    
                    
        label seconddayC1O1:
            mw "Alright, {w} meet me after school in the courtyard, ok? {w} See you in class!"
            show marcw with moveinleft:
                xalign 1.0 yalign 1.0
            hide marcw
            jump period
        label seconddayC1O2:
            mw "Oh, {w} ok. {w} Well, {w} let me know if you need anything then. {w} See you in class."
            show marcw with moveinleft:
                xalign 1.0 yalign 1.0
            hide marcw
            jump period
        label seconddayC1O3:
            mw "‘Kay. {w} Cya Round."
            show marcw with moveinleft:
                xalign 1.0 yalign 1.0
            hide marcw
            jump period
            
    label secondDayPath1:
        scene img_class with Dissolve(1.0)
        $ thephase = 5
                
        mk "Ok Class! {w} Take your seats! {w} One... {w} One... {w} Two... {w} Three... {w} Five... {w} Eight... {w} Thirteen... {w} Twenty one..."

        #Continues mumbling (LEAVE RESOLUTION OF JOKE UNTIL THE END OF THE YEAR, TELLS STUDENTS THAT IT’S THE FIBONACCI SEQUENCE)

        nm "........" 

        nm "*Scribble scribble*"

        mk  "Now, class. {w} I know that you hate homework on the first day, {w} but I want to get you all learned up by the end of the year."

        #Collective groans

        mk "I will hand out your assignments on the way out. {w} For now, {w} there is a text book under everyone’s desk. {w} Pull it out and turn to page 394. {w} That is where we will start."

        #MORE GROANS

        mk "Today’s topic will be geometry. {w} You know, {w} I really like angles, {w} to a certain degree."

        mc "............ Was that a pun?"

        mc "What was that pun?"

        nm "*Doodles smiley faces*"

        mk "Ms. McNeil, {w} I don’t see you opening up your textbook. {w} Please don’t try to measure my patience."
        
        $ nmname = "Natalie Mcneil"

        nm "*Quickly sketches frowny face and shows it to Mr. Kelly*"

        mk "... Okaaaaaay Ms. McNeil, {w} I think you should put away your sketchbook now."

        nm "*Opens eyes really wide, vigorously shakes her head*"

        mk "I insist."

        nm "*Eyes tear up a bit, puts sketch book away and begins to sulk*"
        
        $ hasmetnatalie = True
        
        ">You can now view Natalie's profile."

        mk "That’s better."

        #Later in class
        scene img_class with Dissolve(1.0)

        mk ".... and that’s how these laws of geometry work. {w} You know, {w} it’s a shame parallel lines will never meet. {w} They have so much in common."

        #Class groans

        "*Bell rings*" 

        mk "Alright class, {w} you are dismissed."

        label seconddayschoolchoice2:
        
            menu:
                
                "Ask how Natalie's feeling":  #(+affection)
                    $ natalieprogression = natalieprogression + 1
                    jump seconddayC2O1
                "Question Natalie's behavior": #(-Affection)
                    $ natalieprogression = natalieprogression - 1
                    jump seconddayC2O2
                "Ignore Natalie":
                    jump seconddayC2O3
                    
        label seconddayC2O1:
            mc "Hey, {w} are you ok? {w} I couldn’t help but notice that you seemed upset."
            nm "*Blushes*"
            mc "Huh. {w} That was strange...."
            $ thephase = thephase + 1
            jump lunchSchool
        label seconddayC2O2:
            mc "Why didn’t you pay any attention in class? {w} Are you mute?"
            nm "*Makes an angry face*"
            mc "Huh. {w} That was strange...."
            $ thephase = thephase + 1
            jump lunchSchool
        label seconddayC2O3:
            $ thephase = thephase + 1
            jump lunchSchool
            
    label secondDayPath2:

        mc "My next class is science, {w} it looks like. {w} I’d better get there fast."

        #Scene change = ENTER SCIENCE
        scene img_class with Dissolve(1.0)
        $ thephase = thephase + 1

        mg "Before you sit down, {w} line up at the back of the room. {w} I have some important questions."

        mg "Since this is a science class, {w} we must observe the scientific method. {w} That means collecting questions. {w} Now, my first question is this:..."

        #Fade out

        mg "....Now, pick your partners. {w} We will begin our lectures tomorrow, and collect data. {w} Tonight, I want you to take notes on the first chapter of the textbook."
            
        mg "Before you leave, {w} let me know who you are sitting with. {w} If you don’t, {w} you will be randomly assigned with a partner. {w} Go!"

        mc "Uh... {w} Hey... {w} Anyone want to be my partner?"

        mc "Anyone? {w} Hey, you... {w} No? {w} Alright..."

        mc "Urgh... {w} Seems like no one is available..."

        mg "Now, {w} does anyone not have a partner yet?"

        #Looks around  

        mc "Uh, {w} I guess I don’t have a partner yet..."

        mg "Interesting. {w} Now, could you take a look around the room? {w} Can you tell me what you see?"

        mc "Uhm... {w} Oh." 

        #Looks at agnes 
        show agnesr with moveinbottom

        mc "Uh, {w} alright. {w} Hi..."

        ar "Hi."
        hide agnesr

        mg "Wonderful. {w} Now, {w} tomorrow’s lecture will be about the chapter in which you are currently engaged in notetaking. {w} Remember, {w} the chapter notes will be due at the end of every week. 
            The first chapter is rather short, {w} so if you do not have them completed, {w} there will be no excuse."

        #Staring at her phone, headphones in
        show agnesr

        mc "Um, {w} hi. {w} Er, {w} since we are working together and everything, {w} I was wondering..."

        ar "Hmmm?"

        mc "Oh, {w} I was just wondering..."

        ar "Agnes. {w} But don’t call me that. {w} I prefer..."
        
        $ arname = "Agnes Rocco"

        ar ".... {w} Novahawk."

        mc "Uh... {w} Right... {w} Novahawk... {w} ok..."

        ar "Mhm. {w} Now get outta here."
        
        $ hasmetagnes = True

        #Agnes leaves
        show agnesr with moveinleft:
                xalign 1.0
        hide agnesr
        
        ">You can now view Agnes's profile."
        
        scene img_hall with Dissolve(1.0)

        mc ".........Huh."

        mc "I guess it’s time for the electives now. {w} Let’s see what Marc is up to."

        #*Insert Elective here*
        scene img_class with Dissolve(1.0)
        $ thephase = thephase + 1

        show marcw
        mw "...And that’s how you disguise your phone number."

        mc "Oh, {w} cool... {w} What would I use that for?"

        mw "Probably nothing, {w} but hey, {w} the more you know."
        show marcw with moveinright:
                xalign 1.0 yalign 1.0
        hide marcw
        
        scene img_hall with Dissolve(1.0)
        $ thephase = thephase + 1
        
        jump period

    label secondDayPath3:
        
        if marcprogression >= 5:
            
            show marcw with moveinright:
                xalign 0.5 yalign 1.0
            mw "Hey! {w} Ready for me to show you around town?"
        
            mc "Oh, {w} uh, {w} sure."
            show marcw with moveinright:
                xalign 0.0 yalign 1.0
            hide marcw
            
            scene img_town with Dissolve(1.0)
            $ location = 3
            
            ">You spend after school letting Marc show you around town."

            show marcw with moveinright:
                xalign 0.5 yalign 1.0
            mw ".... And that’s why Marcy’s is cheaper than Jenny’s. {w} Good way to save your money on clothes."

            mc "Oh ok, {w} thanks for letting me know."

            mw "So I was thinkin’, {w} there’s this place up by the Cafe that I hang around, {w} got a bunch a’ video games and stuff. {w} Wanna hit it, see if there’s something ya wanna play?" 

            mc "Er, {w} sure. {w} What kinds of games are there?"

            mw "Oh ya know, {w} things like fighting games, racing games, shooters. {w} All kinds. {w} It’s right over here, let’s get going."

            mc "Uh yeah, {w} let’s go..."
            show marcw with moveinright:
                xalign 0.0 yalign 1.0
            hide marcw

            #*In Arcade*
            scene img_mall with Dissolve(1.0)

            show marcw with moveinright:
                xalign 0.5 yalign 1.0
            mw "Check out this game, dude!"

            mc "Erm, {w} alright... {w} What game is this?"

            mw "It’s the hottest game in the arcade! {w} You HAVE to try it."

            mc "Oh, {w} okay cool... {w} What do I do?"

            mw "Well, first, {w} you start by..."

            mw "... And that’s how you can use the combos to get higher scores."

            mc "You know, {w} this game is pretty fun!"

            mw "That’s awesome! {w} This is my favorite game in the arcade."

            mw "Hey are you feeling hungry? {w} My stomach just started to growl."
            
            show img_mall with vpunch

            mc "Oh! {w} I’m feeling hungry too. {w} Do you know any good places to eat?"
            
            mw "Actually I do, {w} there’s a place not too far from here that’s super popular with the students at our school. {w} A senior named Frederick runs the place, and a friend of mine works there."

            mc "Ok cool, {w} let’s go."
            show marcw with moveinright:
                xalign 0.0 yalign 1.0
            hide marcw

            #*Outside Cafe*
            scene img_cafe with Dissolve(1.0)

            show marcw
            mw "Here’s the place. {w} Roland’s Sweet Honey Cafe."

            mc "Looks nice."

            mw "I’m starving, {w} let’s go in and get some food."
            hide marcw

            #*Inside Cafe*
            scene img_cafe with Dissolve(1.0)

            mc "There’s a lot of people here."
            
            show marcw with moveinright
            mw "Yea, {w} almost everyone comes here after school to hang out and unwind."
            show marcw with moveinright:
                xalign 0.0 yalign 1.0

            show frederickh with moveinbottom:
                xalign 0.5 yalign 0.0
            fh "Well, if it isn’t the freshie who can’t take a bit of homework."
            
            mw "Excuse me Frederick!?!?!?!"
            
            $ fhname = "Frederick Hobson"

            fh "No, not you, {w} your friend here."

            mc "W-w-what? {w} W-what do you mean?"

            fh "Forgetful, are we? {w} Just yesterday I caught you complaining about homework on the first day. {w} I told you to grow a pair."

            #*Snickers*

            mc "Marc!"

            mw "Sorry, it is a little funny. {w} You probably shouldn’t complain too much."

            mc "Y-you’re one to talk!"

            mw "Yeah, probably. {w} But still, {w} that was FUNNY."
            
            show beckak with moveinright:
                xalign 1.0 yalign 1.0

            bk "Frederick, {w} that’s no way to treat new customers. {w} You know better."

            fh "Becka!! {w} My apologies. You’re right. {w} It was just that... {w} he was being whiny yesterday and it bothered me, {w} I mean, he hasn’t even been to any higher level classes..."

            bk "Shush. {w} You were exactly the same way. {w} As were most of the members of our class, if I recall correctly."

            fh "Well I Ne-..."

            bk "Now apologize to your customer."
            
            #*BLUSHING*

            fh "You do not own this cafe! {w} I do! Argh!" 

            fh "But, you are right. {w} I must be more... professional."
            
            #*Turns to MC and Marc*
            hide frederickh
            show frederickhprofile:
                xalign 0.5 yalign 0.0
            
            fh "As a consolation, your drinks are on the house. {w} You are welcome."

            bk "Now, that wasn’t so hard was it?"

            fh "Oh for heaven’s sake!"

            #*Frederick and Becka leave*
            hide beckak
            hide frederickhprofile
            show frederickh:
                xalign 0.5 yalign 0.0
            show frederickh with moveinright:
                xalign 1.0 yalign 0.0
            hide frederickh
            
            $ hasmetfrederick = True
            $ hasmetbecka = True
            
            ">You can now view Frederick's and Becka's profiles."
            
            show marcw with moveinright:
                xalign 0.5 yalign 1.0
            
            mw "Huh. Anyway, {w} let’s go sit somewhere."

            mc "Uh... okay, {w} that sounds good to me."
            
            show marcw with moveinright:
                xalign 0.0 yalign 1.0
            show sarahg with moveinright:
                xalign 0.5 yalign 1.0

            sg "Hey Marc! {w} How’s it goin?"

            mw "Sarah! {w} How’s business today?"
            
            $ sgname = "Sarah Granger"

            sg "Oh, you know, {w} it’s been pretty busy, being the first few days in the school year and all... {w} What can I get for you guys?"

            mw "I’ll have the usual. {w} Frederick said we get free drinks today."

            sg "Did he now? {w} Well, alright, I trust you. {w} And who’s this?"

            mw "This is [mcname]! {w} He just moved into town. He’s a freshman, like me. {w} In fact, he lives in our neighborhood!"

            sg "Oh? And how would you know? {w} Did you follow him home?"

            mw "... Something like that."

            mc "Uhh..."

            mw "Don’t worry about it. {w} What are you gonna order?"

            mc "Err, what does the chef recommend?"

            sg "Today we have a special on Caesar Salads. {w} Comes with grilled chicken and garlic bread."

            mc "Sounds good, I’ll have that."

            sg "Then I’ll be back in a jiffy."
            
            show sarahg with moveinright:
                xalign 1.0 yalign 1.0
            hide sarahg
            
            show marcw with moveinright:
                xalign 0.5 yalign 1.0
            
            mw "Thanks!"

            mc "So... {w} How do you and Sarah know each other...?"

            mw "Oh, me and Sarah? {w} We go way back. Grew up together, almost."

            mc "Really? {w} That’s cool..."
            
            show marcw with moveinright:
                xalign 0.0 yalign 1.0
            
            show sarahg with moveinright:
                xalign 0.5 yalign 1.0

            sg "Hey guys! Here are your drinks. {w} I’ll be back in a sec with your food."

            mw "Thanks! {w} Do you have a minute to sit with us after that?"

            sg "Oh, no, sorry. {w} Not today. We are up to our elbows in customers, haha."

            mw "Alright, maybe next time then."

            sg "See you later!"
            
            show sarahg with moveinright:
                xalign 1.0 yalign 1.0
                
            show marcw with moveinright:
                xalign 0.5 yalign 1.0

            mw "Hey wait! {w} How is your leg doing?"

            sg "Oh, well, {w} I’ve been doing better... {w} Healing a broken bone doesn’t happen overnight, you know?"

            mw "True, true. {w} Well, get better soon! The team needs you."

            sg "Haha, thanks. I’ll see you around."
            
            hide sarahg
            
            $ hasmetsarah = True
            
            ">You can now view Sarah's profile."
            
            mc "...I didn’t notice her cast. {w} What happened?"

            mw "It’s a bit of a nasty story. {w} Let’s just say there was a really, really bad accident." 

            mc "Oh... {w} Uh, how long has she had the cast?"

            mw "Too long. The whole summer, and then some. {w} It was really bad." 

            mw "Thinking about this is depressing. {w} Let’s finish up and get out of here."

            mc "Uhhh, sure."

            #*Dining room noises*

            mw "That was really good! {w} I always enjoy eating here. Are you done?"

            mc "Yeah, I think I’m finished. {w} Let’s go."

            mw "Sweet. I'll see you tomorrow."

            #*scene transition*
            jump secondDayPath4

        else:

            mc "Well school’s out now, I wonder what I should do... Looks like a bunch of students are going over to that cafe over there, I think I’ll go check it out."

            #*walks over to the cafe*

            mc "Roland’s Sweet Honey Cafe... weird name..."

            #*walks in*

            #*Inside Cafe*

            mc "There’s a lot of people here." 

            s1 "Well, if it isn’t the freshie who can’t take a bit of homework."

            mc "W-w-what? W-what do you mean?"

            fh "Forgetful, are we? Just yesterday I caught you complaining about homework on the first day. I told you to grow a pair."

            mc "H-hey! G-get out of my face!"

            fh "Why, you insolent..."

            bk "Frederick, that’s no way to treat new customers. You know better."

            fh "Becka!! My apologies. You’re right. It was just that... he was being whiny yesterday and it bothered me, I mean, he hasn’t even been to any higher level classes..."

            bk "Shush. You were exactly the same way. As were most of the members of our class, if I recall correctly."

            fh "Well I Ne-..."

            bk "Now apologize to your customer."

            fh "*BLUSHING* You do not own this cafe! I do! Argh!" 

            fh "But, you are right. I must be more... professional. *turns to MC* As a consolation, your drink is on the house. You are welcome."

            bk "Now, that wasn’t so hard was it?"

            fh "Oh for heaven’s sake!" 

            #*frederick and becka leave*

            mc "Jeez... what’s his problem..."

            #*scene cut to Marc talking to some girl (Sarah)*

            mw ".... And that’s how I avoided getting into trouble with the dean."

            sg "...You aren’t serious."

            mw "Yes I am! Look, at school tomorrow I’ll have you meet the guy."

            sg "Uh huh."

            mw "Well, speak of the devil and he shall appear! He’s right there!"

            mc "h-huh?! Excuse me? W-what’s going on?"

            mw "Oh, I was just telling my friend Sarah here how I met you yesterday. So, how’s solo explorin’ going?"

            mc "G-good, I guess..." 

            sg "So, what’ll it be? I assume you *are* here to eat."
            
            mw "I’ll have the usual. Oh, by the way, have you met MC? He just moved to town. He even lives in our neighborhood!"

            sg "Oh? And how would you know? Did you follow him home?"

            mw "... Something like that."

            mc "Uhh..."

            mw "Don’t worry about it. *to MC* What are you gonna order?"

            mc "Err, what does the chef recommend?"

            sg "Today we have a special on Caesar Salads. Comes with grilled chicken and garlic bread."

            mc "Sounds good, I’ll have that." 

            sg "Then I’ll be back in a jiffy."

            mw "Thanks!"

            mc "So... How do you and Sarah know each other...?" 

            mw "Oh, me and Sarah? We go way back. Grew up together, almost."

            mc "Really? That’s cool..."

            sg "Hey guys! Here are your drinks. By the way, Frederick said that you get a free drink, MC. I’ll be back in a sec with your food."

            mw "Thanks! Do you have a minute to sit with us after that?"

            sg "Oh, no, sorry. Not today. We are up to our elbows in customers, haha."

            mw "Alright, maybe next time then."

            sg "See you later!"

            mw "Hey wait! How is your leg doing?" 

            sg "Oh, well, I’ve been doing better... Healing a broken bone doesn’t happen overnight, you know?"

            mw "True, true. Well, get better soon! The team needs you."

            sg "Haha, thanks. I’ll see you around."

            mc "...I didn’t notice her cast. What happened?"

            mw "It’s a bit of a nasty story. Let’s just say there was a really, really bad accident." 

            mc "Oh... Uh, how long has she had the cast?"

            mw "Too long. The whole summer, and then some. It was really bad." 

            mw "Thinking about this is depressing. Let’s finish up and get out of here."

            mc "Uhhh, sure." 

            jump secondDayPath3

    label secondDayPath4:

        #*Scene Change Home*
        scene img_home with Dissolve(1.0)
        $ location = 2
        $ thephase = thephase + 1

        #RING RING RING RING RING

        mc "Wow! {w} As soon as I get home, someone else is calling me. {w} Is it going to be like this every night?"

        mc "I had probably better pick up the call..."

        mc "Oh. Look. {w} It’s my sister."

        sis "Hey little bro! {w} How was your first few days of school?"

        mc "Oh! Hey, Jackie! {w} It’s been a while."

        sis "Yeah, well, you know, {w} college and all that. {w} How’s my socially awkward padawan learner?"

        mc "Urgh, I’m doing fine... {w} Why do you always reference that movie?"

        sis "Because it’s *our* favorite, and don’t you forget that."

        mc "But you know I don’t..."

        sis "Shush, yes you do. {w} Anyways, do you have a girlfriend yet?"

        mc "What?!?! {w} I literally just got here and..."

        sis "No excuses! {w} Get moving, casanova!"

        mc "Argh! {w} I don’t even know anyone yet!"

        sis "Sure you don’t, Romeo." 

        mc "Okay, fine, I’ve met a grand total of 6 people. {w} None of whom I know very well."

        sis "Any girls?"

        mc "...Three. But..."

        sis "Are they pretty?"

        mc "...What? Wait... {w} No, that doesn’t... {w} leave me alone!"

        sis "Alright, Valentine. {w} I’ll keep cupid off your back... for now. {w} Don’t be surprised if you find an arrow in your butt later in the year."

        mc "An arrow?"

        sis "You know, the arrow of love? {w} Nevermind, loverboy. I’ll talk to you later. {w} Don’t forget to give mom and dad a call every now and then!"

        mc "Ok, I’ll do that. {w} Don’t you have college things to do?"

        sis "Yeah probably. Oh, and by the way, {w} I looked at your school’s website and it looks like homecoming is coming up soon. {w} So, like I said, get a date. Cupid will watch over you."

        mc "...Uh, Ok... {w} Sure..."

        sis "See ya round!"
        
        #*Hangs up*

        mc "Jeez... That was really something... {w} I’d better get some sleep..."

        #*End Day*
        $ thephase = 11 + 1
        $ issecondschoolday = False
        jump startDecider