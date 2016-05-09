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

        #*Out of breath*
        
        scene img_nearhome with Dissolve(1.0)

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

        mc "Okay, fine, I’ve met a grand total of 6 people. None of whom I know very well."

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

###########################Homecoming#############################################################################

    label homecomingarc:
        
        #*Cynthia gives Danny relationship advice, telling him to just *ask that girl* out, thinking that that girl is herself. She is shocked when it is in fact not.*

        cl "Heyy Dannyyy, what’s hangin, bangin?"

        dr "O-oh, hey Cynthia. It’s hangin."

        cl "That’s pretty sweet, sugar. You know, Homecoming is coming up soon. If there’s a girl you like, don’t you think that it’s about time for you to ask her out? *leans in too close*"

        dr "O-oh yeah, probably. I should do that."

        cl "Yeah, you should! I’ll see you around, darling."

        dr "A-alright. See you around!"

        #*CL leaves*

        mc "Oh, homecoming is coming up soon.... I wonder if Marc and Sarah are going to go..."

        #*bumps into DR*

        mc "Oh! Sorry. That was my fault."

        dr "No, it’s fine. Don’t worry about it."

        mc "Oh, alright. What is your name?"

        dr "My name is Danny. How about you?"

        mc "Oh, my name is __________. Who was that with you?"

        dr "Oh, her? That was Cynthia. She’s a cheerleader."

        mc "That’s cool. She seemed like she wanted something."

        dr "Huh? Nah, we’re just friends."

        mc "Ah, ok. Well, see you around."

        dr "Yep, see you."

        #*Danny Leaves*

        mc "He’s totally clueless... Whatever. It’s not my business. Hmm... Looks like I have an A day today. That means... English and History. I should find Marc, and see what he’s up to. Where could he be? If I don’t find him soon, we could be late!"

        label homecomingChoice1:
            
            menu:
                
                "I should probably check the field. Maybe he’s there!":
                    $ marcprogression = marcprogression + 1
                    jump homecomingC1O1
                "I think I would rather do it on my own.":
                    jump homecomingC1O2

        label homecomingC1O1:

            mc "I should probably check the field. Maybe he’s there!"

            #*switch background to a sports-y field*

            #*MC and Marc both appear on the screen*

            mw "Oh, hey MC. What’s up?"

            mc "Well, class is about to start... I didn’t see you on the way to school, so I thought I’d find you."

            mw "What, are you following me?"

            mc "Y-you’re one to talk!"

            mw "Touché. Well, let’s get to class. I wouldn’t want to be too late."

            #----

            #*MC and Marc walk into class*

            mh "Hey! You two, why are you both coming into class late?"

            mc "Uhh..."

            mw "There was an accident on the freeway."

            mh "There isn’t a freeway nearby!"

            mw "Oh, right, I mean the, uh, the intersection on uh 3rd and 5th."

            mh "There isn’t even an intersection there!"

            mw "6th. I meant 6th."

            mh "Whatever! I’ll hold you to your word. If you are lying, I suppose it doesn’t matter. Just get to your seats."

            mw "*under breath* .... next time I’ll remember to not come at all."

            mc "*also under the breath* Jeez, Marc, chill."

            mw "Nah."

            mh "Now, class, before we begin, I want you to listen very carefully..."
            
            #jump homecomingPath1
            
            #______________


        label homecomingC1O2:

            #*gets to class*

            mc "*searches the room* Huh... I guess Marc hasn’t gotten to class yet..."

            mh "Everyone! Please take your seats. I will take attendance quickly so we can get right to work. MC?"

            mc "Here."

            mh "Felicia? Aaron? Thomas? Quade? Emmalie? Gregory? Selina? Hm... Marc? He’s not here. MC, do you know where he is?"

            mc "N-no, I don’t. Sorry."

            mh "It’s fine. Well, let's begin."

            #*DOOR OPENS LOUDLY* 

            mw "... And that’s why turtles are cooler than tortoises. I’ll catch you later."

            s1 "Peace."

            mh "Marc Waller, who was that?"

            mw "Nobody important."

            mh "Well, I dare say it is! What were you doing?"

            mw "Talkin’."

            mh "Yes, I know that. About what?"

            mw "Stuff."

            mh "*Sigh* Fine, go sit down."

            mw "Sir, yes sir."

            mh "Now, before we begin, I want you to listen very carefully..."
            
            jump homecomingPath1

            #-------------------------------------------------------
        
    label homecomingPath1:
    
#        mh "Good work today, class. We will continue our reading of A Midsummer Night’s Dream  when we meet next. Class dismissed!"

#        mw "Sooooooooooooooooooooooooooooooo, MCCCCCCCCCCCCCCCCC. Are you going to ask anyone out to homecoming?"

#        mc "Well, I mean, I wasn’t thinking about it..."

#        mw "But everyone is going!"

#        mw "C’meon dude, ask someone out."

#        mc "Well, who are you going with?"

#        mw "Well, since couples tickets are cheaper, Sarah and I are going together. As friends."

#        mc "*makes finger air quotes* "Friends". Right. Ok."

#        mw "Are you trying to tell me something?"

#        mc "No, I’m not saying anything. "Friends". Uh-huh."

#        mw "Pft, what do you know. You don’t even have a date."

#        mc "You should be my date, then."

#        mw "*blushes* No, it’s just cheaper to go together... As friends."

#        mc "I’m not doing the whole "friends" conversation again. You’re dating me."

#        mw "I AM NOT"

#        mc "You are too"

#        mw "STOP"

#        mc "Ok, ok, calm down a bit"

#        mw "It’s not my fault, you kept egging me on"

#        mc "Yeah I know. I’ll see you around. Maybe I’ll even see you at homecoming *wink wink*"

#        mw "GAH"

#        #_______________________________________________

#        #*HALLWAY*

#        mc "You know, maybe going to homecoming would be fun..." 

#        dr "H-hey, u-uh Agnes?"

#        ar "Novahawk. Yes?"

#        dr "W-would you, you know, maybe like to..."

#        ar "Well, spit it out already!"

#        dr "Uh, maybe, you would want to, er, go to, uh, homecoming with me?"

#        ar "Sure."

#        dr "O-oh really? Fantastic! I-I’ll call you... wait, but I need your number first... Can I have your phone number?"

#        ar "Yeah... Give me your phone."

#        dr "O-ok... Here."

#        ar "There you go. I’ll see you around." 

#        dr "S-sounds good. I’ll talk to you later."

#        #*THEY LEAVE*

#        mc "That... that was awkward."

#        cl "W-WHAT! HE WAS SUPPOSED TO ASK MEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE! W-what a jerk!"

#        mc "I’m sure he has good intentions... do you even know if he likes you?"

#        cl "Yes, he does! He just likes to play hard-to-get. There is no doubt in my mind that he loves me!"

#        mc "... Right... Hard-to-get..."

#        cl "S-shush! He does, I’m telling you! Maybe he doesn’t know it yet, but he does! I need to go and think!"

#        mc "Great, I’ll talk to you later." 

#        #______________________________________________

#        #*Lunch*

#        mw "Hey who you are going to homecoming with?"

#        mc "I.. uh... I’m not even sure if I’m going yet."

#        mw "Well, you better figure out who you are going with because I got you a ticket."

#        #*MC Obtains Homecoming Ticket*

#        mc "Wait... Uh... but..." 

#        mw "Don’t worry you won’t have to pay me back. This is all on me."

#        mc "Oh... but..."

#        mw "Don’t worry about it! Homecoming will be fun, you won’t want to miss it!"

#        sg "Wait... Mark, I thought we were going together?"

#        mw "We ARE going together! But now we are bringing MC with us!"

#        sg "Oh... Uh, awesome... It’ll be fun!"

#        mw "I know right! Hey, I gotta go take care of something at my locker before lunch ends. I’ll cya later!"

#        coname "...See ya..."

#        sg "Did you know he was going to do that?"

#        mc "What? No! I wasn’t even sure yet, but I guess I’m going now..."

#        sg "Ha, yeah, I guess so. I really thought... Nevermind. Whatever. I have to go." 

#        mc "Um, alright. Bye."

#        sg "..........."

#        #*end scene*

#        #*Next day*

#        #*in his house*

#        mc "Well, tonight is homecoming I guess. I suppose I had better get ready..."

#        #*Phone rings*

#        mc "Hello?"

#        sis "Heyy, bro! Are you going to Homecoming?"

#        mc "Oh, uh, y-"

#        sis "Well, you had better be! Otherwise I would have gotten you that expensive tuxedo for nothing."

#        mc "Wait, what Tuxedo?"

#        sis "Haven’t you gotten it yet? *Authors’ note: Jackie and Marc are in cahoots* You should have gotten it a few days ago!"

#        mc "Well, I-"

#        sis "Go outside and check right now! It should be in a nice, tall package!"

#        mc "Um, alright..."

#        sis "Is it there?"

#        #*Giant package on the front door step*

#        mc "Oh, wow, there it is."

#        sis "Wonderful! Try it on! It should fit you perfectly." 

#        mc "Uh, okay then. I’ll do that. Any other secret packages I should be looking for?"

#        sis "Not right now! Don’t worry, though, the future holds great things."

#        mc "...Thanks." 

#        sis "No problem! Remember, have fun!"

#        mc "...Yeah, Thanks..."

#        sis "Bye Bye, now!"

#        mc "...Bye..."

#        #*jackie hangs up*

#        mc "Ugh. It’s like this was planned, or something..."

#        #*Knocking on door*

#        mw "Hey! MC! Are you ready yet?"

#        mc "...Marc? Hold on, I just got my tuxedo..."

#        mw "Tuxedo!? Wow, Mr. Fancy. Dressin’ in a tux."

#        mc "Please don’t. My sister got it for me."

#        mw "Oh, ok. Sounds like your sister expected you to have a date."

#        mc "Maybe she does. She’ll be awfully disappointed then."

#        mw "Haha I bet. Well, hurry up and get dressed, we need to leave soon."

#        mc "Don’t you need to go get Sarah or something?"

#        mw "OH! Yeah. I’ll be back in a few."

#        mc "...Bye."

#        mc "...."

#        mc "I can’t believe he forgot his date..."

#        #*Scene shift to outside the house*

#        mc "Where are they? I’d better just go."

#        mw "Hey! Wait Up!"

#        sg "Wait, Marc, not so fast..."

#        mw "Huh?" 

#        sg "..."

#        mw "Ookay. Well, the gang’s all here. Now lets go to homecoming!"

#        sg "You look very nice today, MC."

#        mc "Oh, uh, thanks Sarah."

#        sg "*Nods*"

#        mw "You DO look spiffy. Hopefully walking there won’t dirty it up any." 

#        mc "Haha, yeah, that would suck."

#        #*A limo pulls up beside them, and the chauffeur gets out and opens the door for the three to get in.*

#        ch "Sirs, Madam. I will take you to homecoming."

#        mc "I think you have the wrong address..."

#        ch "I assure you, I do not have the wrong address. I was hired by one Jackie (Whatever the mc’s last name is)."

#        mc "Oh. I see. Well, alright then... I guess we won’t have to walk after all." 

#        mw "Nice! Now your tux won’t get dirty."

#        mc "...Yeah. It won’t."

#        sg "Well, quit sitting around and get in the car. Homecoming won’t wait for your sarcasm."

#        mc "Sorry, sorry. After you two."

#        #*End Scene*

#        #*New Scene* 

#        #*At homecoming*

#        mw "... And that’s why a bow tie is more useful than a long tie."

#        sg "Mark, please. Not everyone thinks"

#        de "Welcome, everyone! Congratulations on surviving school so far. We haven’t done you in yet!" 

#        #*Nervous murmuring from the crowd*

#        de "Aww, don’t be like that! We are here to have fun! Before we begin, I have one important announcement to make..."

#        mw "Hey! Dude! Over here!"

#        mc "Wha...?"

#        mw "There you are! When we walked in here, you got lost in the crowd! It’s all good though, I found you."

#        mc "Um, yeah, thanks haha."

#        mw "Anyways, now that you are here, maybe you could find a date after all. I’ve seen a bunch of girls who don’t have dates!"

#        mc "How would you even know? Just looking doesn’t seem like enough to judge."

#        mw "Oh, trust me, I know about these sort of things."

#        sg "*HUff* Yeah, sure."

#        mw "What? What’s wrong?"

#        sg "Oh, nothing, don’t worry about it."

#        mw "Well, all right then. Anyways, go and have fun. That’s what we are here for."

#        mc "Sounds good. I’ll let you two get to dancing, then."

#        mw "Ha! I don’t dance. But I appreciate the gesture."

#        sg "You aren’t going to dance with me?"

#        mw "Oh, uh, sure I am..."













#        #First Encounter with Christina

#        mw "...and that’s what I heard happened at homecoming."

#        sg "Wow, that sounds pretty crazy, but I don’t want to cast stones before I know the hard facts."

#        mw "Me though, I wanna find out what’s going on. Though I don’t like getting involved in drama directly, I still like to be in the know, ya know?"

#        mc "Hey guys."

#        #Sarah/mw "Oh hey _____."

#        mw "What’s going on with you?"

#        mc "Oh, not much, I was just..."

#        cs "Excuse me?"

#        sg "Christina?"

#        mw "Oh hey, it’s the girl who’s getting cheated on by the star basketball player."

#        sg "Marc! *smacks him*"

#        cs "Hmph... you. *points at MC*"

#        mc "me?"

#        cs "Yes you. I want to speak to you, privately."

#        mw "Oh dang, the violinist wants a revenge relationship!"

#        sg "Marc! Stop! *smacks him*"

#        mw "Ouch..."

#        cs "Well freshie?"

#        mc "Uhhhh, ok..."

#        #*scene change to different room, only Christina and MC present*

#        mc "*thinking to himself* What could Christina possibly want with me"

#        cs "Tell me _____, what do you know about me and Kolby."

#        mc "Um, all I know is that you two are together-"

#        cs "And what do you know of what happened at homecoming?"

#        mc "Uh, I think I heard some rumors, but I didn’t really pay any attention to them-"

#        cs "Alright, here’s what’s going on. At homecoming, when I was up on stage performing for the school, I noticed that Kolby, who was supposed to be watching and supporting me, was sneaking off with somebody, I couldn’t see who."

#        mc "Well if you couldn’t see who the person was, how do you know he was sneaking off with somebody?"

#        cs "Because, I saw someone holding his hand leading him away."

#        mc "Oh..."

#        cs "What I want you to do is get to know Kolby and see if you can find out from him what he was doing at homecoming while I was performing.Can you do that for me?"

#        mc "Uh... um..."

#        cs "And I’m sure I don’t need to tell you this, but keep this to yourself. I don’t want it getting around that I recruited somebody to investigate my own boyfriend."

#        #Choice: Find out more details
#        #        Agree to Christina’s proposition

#        #Find out more details
        
#        mc "Wait wait, back up a second. Why do you want me of all people to help you? Can’t you get someone else?"

#        cs "I could, but you’re more likely to succeed because you’re new and we don’t know each other very well, which means Kolby won’t know I asked you to investigate him."

#        mc "And why should I investigate him for you? It sounds really backhanded..."

#        cs "Because I’m trying to clear him of doing anything outside our relationship that he shouldn’t, but at the same time I don’t want him to think that I’m doubting his loyalty in the case that he wasn’t doing anything he shouldn’t."

#        mc "Well… I mean I just don’t know if I want to get involved in this stuff..."

#        cs "What if I could give you some incentive on the side? I can get you and your friends passes to the Spring Festival later this year and front row seats for the stage."

#        mc "Really? I’m still not sure though..."

#        mw "____ you gotta do it!"

#        #MC, Christina "Huh?"

#        mw "C’mon ____, it’s not that hard! Just simply get to know Kolby, find out if he’s been cheating on Christina or not, and either way we’ll be getting passes to the Spring Festival!"

#        cs "Were you listening to our private conversation??"

#        mw "Well I mean it’s not like I can not eavesdrop when a girl pulls away my friend to talk privately, especially when it involves earning passes to the Spring Festival."

#        sg "I admit, I wanted to know what you were going to talk to _____ about Christina."

#        cs "Well what do you think Sarah?"

#        sg "I think it’s none of my business, so I’m going to stay out of it and not have an opinion. As for the Spring Festival, I don’t really care about getting free passes because I can pay for myself easily enough."

#        mw "I care though! _____, you gotta find out what Kolby may or may not be doing and get us those passes!"

#        mc "But… uh… well I mean..."

#        mw "Awesome! _______ will take the offer!"

#        mc "Wait what?"

#        cs "Great. Remember that it’s simple. Get to know Kolby, find out what he was doing at homecoming while I was performing, and report that back to me. Meanwhile, I’ll start working on securing those passes for you three."
        
#        mw "Yes! Thanks Christina, you won’t regret this!"

#        #*Christina walks away, exits scene*

#        mc "Oh man, what have you gotten me into Marc?"

#        mw "Psssh, don’t be a worry wart. In fact, you are welcome cause I basically just got you a free pass to the Spring Festival."

#        mc "But that’s only really because you wanted to get a free pass yourself..."

#        mw "Details, details. Now, tomorrow I know Kolby will be in the gym practicing shooting baskets cause that’s what he usually does. You can go introduce yourself to him then. *big grin*"

#        mc "Aw man..."

#        #*end scene*

#        #Agree to Christina’s proposition

#        mc "Well I guess I can do it..."

#        cs "*looks happy* Great! And I was about to say, no matter what happens your reward for helping me out is that I’ll get you and your friends passes to the Spring Festival later this year."

#        mw "All right!"

#        #MC, Christina: "Huh?"

#        cs "Were you listening to our private conversation??"

#        mw "Well I mean it’s not like I can not eavesdrop when a girl pulls away my friend to talk privately, especially when it involves earning passes to the Spring Festival."

#        sg "I admit, I wanted to know what you were going to talk to _____ about Christina."

#        cs "Well what do you think Sarah?"

#        sg "I think it’s none of my business, so I’m going to stay out of it and not have an opinion. As for the Spring Festival, I don’t really care about getting free passes because I can pay for myself easily enough."

#        mw "I care though! We’re gonna be getting free passes! Good going _____!"
                                                                                   
#        mc "You’re too fixated on the passes Marc..."

#        #*end scene*

#        #First Encounter with Kolby
        
#        mw "Alright, it’s time to get to work!"

#        mc "What do you mean Marc?"

#        mw "I know that Kolby is going to be in the gym practicing during lunch like he usually does. So, you should go meet him and introduce yourself, you know, start to get to know him."

#        mc "Oh... uh well I guess I can go do that..."

#        mw "Don’t worry, you’ll be just fine. And your hard work will be paid off very well, you’ll see!"

#        mc "There you go with being fixated on the passes again..."

#        #(later on looking for the gym)
        
#        mc "Finally I found it. And by the looks of it there’s only a one person in here using the court. He must be Kolby. (approach Kolby)"

#        #Choice: Poke Kolby
#        #Tap Kolby on the shoulder.

#        mc "Excuse me?"

#        kf "*turns around* Oh hi! Sorry I didn’t see you at first, I can really lose focus on everything around me when I get into practicing my three-pointers. I’m Kolby, what’s your name? ...Oh, well nice to meet you _____. So did you come here looking for me?"

#        #Choice: Actually I just wanted to shoot some hoops myself!                                   S
#        #        Yes I was; what happened between you and Christina at homecoming?   F
#        #        Well I just wanted to introduce myself because I’m new to the area.          S

#        #Success
#        #(shoot hoops)
#        kf "Hey awesome! Let’s see who can make the most shots in the time we have left."

#        #It’s very obvious that Kolby is a very good player. He easily beat me in our little competition. It’s also apparent that he is quite competitive.

#        kf "Aw man, we’ve just about run out of time. Well it’s been great shooting hoops with you, hope to see you around _____."

#        Choice: See you around!     End scene
#                Hey can I quickly ask you something?

#        kf "Sure, what do you want to know?"

#        Choice: I heard people talking about you and your girlfriend, is everything ok between you two?
#                What happened between you and your girlfriend at homecoming?

#        kf "Well I don’t know where we are right now, I mean I thought that nothing could get between Christina and me, but ever since homecoming things have become rocky."

#        mc "But what happened at homecoming?"

#        kf "Looks uncomfortable. It’s nothing I really want to talk about right now especially with someone I just met. I gotta get back to practic-"

#        #*bell rings*

#        kf "Aw man, I always forget the time. Well it’s time to go! See ya!"

#        #Success
#        #(introduce yourself)

#        kf "Oh, my name is Kolby Fredrickson, and I’m a member of the basketball team for the school."

#        mc "My name is _______, and my family recently moved into the area."

#        kf "Oh I see, well welcome to the school, I really hope you enjoy it here!"

#        #Choice: Thanks very much, I appreciate it.    End scene
#        #        Hey can I ask you a question?


#        #Failure
#        #(cut to the chase)

#        #Kolby’s face fell, and he looks like he might be a little bit angry.

#        kf "Oh, that’s the reason why you’re here. Well don’t worry about it, I’m pretty sure it doesn’t have anything to do with you. Anyway, I have to get back to practice."

#        #He turned away from me and resumed practicing. It looks like he’s just going to ignore me.


#        #Another Encounter with Kolby

#        #**NOTE: Player will be running a little late for school as part of the story**

#        mc "Oh man, I hope I’m not late today. It’s a good thing I woke up despite my alarm not going off. There’s the front gate..."

#        #Player enters into the school.

#        Hall Monitor: Hey! What are you doing coming into school late? Don’t you know better than that? Why back in my day, if students were late….

#        mc "(Kolby walks into scene behind the hall monitor who doesn’t notice.) Huh? It seems like Kolby is late to school too."

#        #Choice: Point out Kolby.
#        #        Let Kolby sneak by.

#        #Sell out Kolby
#        mc "Hey who’s that? (pointing behind the hall monitor)"

#        Hall Monitor: "Huh? Hey! What are you doing coming into school late? Don’t you know better than that? Why back in my day..."

#        #Player makes his/her escape while the hall monitor is distracted with Kolby.       -cut out of scene-

#        #*LATER THAT DAY*

#        mw "...and that’s why I don’t bother with combing my hair very often, there’s just little meaningful purpose behind it..."

#        kf "HEY YOU."

#        mw "Uh, I think Kolby is really angry, and it looks like he’s heading straight for..."

#        kf "Oi, (player), why did you sell me out to the hall monitor earlier this morning? All ya had to do was just let me sneak by, why’d you have to go and get me in trouble with you?"

#        #Choice: Tell Kolby the truth.
#        #        Lie to Kolby.

#        #Truth

#        mc "Sorry Kolby, I just didn’t want to get in trouble with the hall monitor."

#        kf "I nearly got detention because of you, and if that happens then my position on the basketball team could be thrown into jeopardy. That wasn’t cool at all. He walks away angrily."

#        mw "Dang, the dude needs to take a chill pill. Like seriously, no one can really blame you for wanting to avoid trouble, and he was late just like you. Anyway, don’t sweat it."

#        #End Scene

#        #Lie/Distract

#        mc "Sorry Kolby, it’s just that I had to meet up with Christina today and I didn’t want----"

#        kf "Oh, wait Christina? You were going to meet with Christina? Why, what were you two meeting for?"

#        mc "Oh, uh, I was going to ask her for help… on, uh, some homework."

#        kf "Alright then, well then forget about earlier. How’s Christina doing?"

#        mc "Um, well I last saw her yesterday in school and she seemed to be doing ok."

#        kf "Alright then, that’s good."

#        #Choice: Pursue asking about homecoming.
#        #        Run away from Kolby.

#        #Ask about homecoming
#        mc "Um, hey Kolby. I know you don’t really want to talk about it, but I do also know that whatever happened at homecoming has been troubling you, and want you to know that I’m here if you want to talk to somebody."

#        kf "Oh… well I really appreciate that ____. Well you see, the thing that’s really bothering me is that at homecoming, when I wasn’t with Christina, (someone) kissed me, and I guess Christina heard about it later. I’ve been trying to find the time to sit and talk with her, but we’ve both been busy with school and I’ve had basketball practice. That and all this stress has me even thinking second thoughts..."

#        mc "Wow that sounds terrible… Well I don’t think you and Christina should break up, you two are great people, and together you’re happy! You just have to work past the problem and it’ll make your relationship all the stronger."

#        kf "...wow, I didn’t think of things that way. Thanks _____, you’ve given me much to think about. But I’ll definitely try to make the time to speak with Christina soon."

#        #Run away
#        mc "Well Marc, we better get going, we need to get to class so we’re not late and all hahaha..."

#        mw "Huh? But we still have a couple more minutes to-----"

#        mc "C’mon let’s go!"

#        mw "Um, ok..."

#        #End Scene

#        #Help out Kolby
#        mc "I’m really sorry (hall monitor), I didn’t mean to be late today. My alarm didn’t go off on time."

#        Hall Monitor: Well you should have made sure the night before that your alarm was all set to go, there aren’t any excuses acceptable for being….

#        #Looks like Kolby slipped past (hall monitor).    -cut out of scene-


#        #*LATER THAT DAY*

#        mw "...and that’s why I don’t bother with combing my hair very often, there’s just little meaningful purpose behind it..."

#        kf "Hey (player), I just wanted to thank you for helping me out this morning. I felt a little guilty leaving you to take the heat by yourself, but I honestly didn’t want to get into trouble I could avoid."

#        mc "It’s ok Kolby, don’t worry about it."

#        #Choice: Ask about homecoming
#        #        Don’t ask   (end scene)

#        #Ask about homecoming
#        mc "Um, hey Kolby. I know you don’t really want to talk about it, but I do also know that whatever happened at homecoming has been troubling you, and want you to know that I’m here if you want to talk to somebody."

#        kf "Oh… well I really appreciate that ____. Well you see, the thing that’s really bothering me is that at homecoming, when I wasn’t with Christina, (someone) kissed me, and I guess Christina heard about it later. I’ve been trying to find the time to sit and talk with her, but we’ve both been busy with school and I’ve had basketball practice. That and all this stress has me even thinking second thoughts..."

#        mc "Wow that sounds terrible… Well I don’t think you and Christina should break up, you two are great people, and together you’re happy! You just have to work past the problem and it’ll make your relationship all the stronger."

#        kf "...wow, I didn’t think of things that way. Thanks _____, you’ve given me much to think about. But I’ll definitely try to make the time to speak with Christina soon."

#        #Encounter with Cynthia

#        mw "...and that’s why computers are better than consoles, ya see?"

#        mc "Well I mean if that’s your opinion..."

#        mw "It’s not just my opinion, it’s proven fact! Anyway, how have things been going with Kolby?"

#        mc "Oh, not very well actually. I don’t think I’m really close to finding out what he was doing from him."

#        mw "Hmmm... Well what if we try something different."

#        mc "What do you mean?"

#        mw "Well we can try finding out a different way. Let’s go talk to Cynthia."

#        sg "Oh, that’s a good idea Marc."

#        mw "Aw, thanks hahah (embarrassed)"

#        mc "Who’s Cynthia, and why talk to her?"

#        sg "She’s the rumor mill of the school, and she’s the one who got the rumors started in the first place."

#        mw "And she’s a sophomore so you can introduce us to her Sarah!"

#        mc "huh, well ok then."

#        sg "Alright then, sounds good."

#        #*later*
#        sg "Hey Cynthia!"

#        cl "Oh hi Sarah, what’s going on with you?"

#        sg "Actually I’m not the one that has to talk to you. Meet my friends Marc and _____."

#        cl "Hiyah guys! What can I do for you two?"

#        mc "We wanted to ask you about Kolby, more specifically what he was doing while Christina was performing."

#        cl "Oh, so you’ve heard about Kolby sneaking off with someone then."

#        mw "Yeah, I think just about the whole school has heard of it at least once."

#        cl "So let me guess, you all want to find out who that person was for whatever reason right?"

#        mc "uh, yeah, how did you know?"

#        cl "Why else would you come to me? Well I’m sorry to say I don’t know who it is, but if it was known, then the rumor wouldn’t have been as exciting as it is now."

#        mw "Riiiiiight..."

#        cl "So Sarah, while I have you here, I want to complain to you about Danny-"

#        sg "Oh brother..."

#        cl "At homecoming, I wanted to hang out with him and dance with him and all that great stuff but because of his silly interest in Agnes he didn’t pay much attention to me, even though I managed to get some alone time with him."

#        sg "I see..."

#        cl And Agnes is so obviously not into him, she apparently left him sometime in the evening.

#        mw "Wait a sec, Agnes disappeared during prom? Something about that seems a little fishy. I’d say it’s worth investigating. Wanna go talk to Danny, see what he has to say about it?"

#        mc "Sure, sounds like a plan since Cynthia didn’t have much information to offer."

#        mw "Hey Sarah, we’re going to the cafe to check something out, meet us there when you’re done?"

#        sg "Yeah go on ahead, I’ll stay and talk with Cynthia a bit."

#        #Encounter with Danny

#        #*at cafe
#        #*step through entrance*

#        mw "Look, there he is over there. Do you want to go talk to him alone or do you want me to come with you?"

#        #Choice: I’ll go alone.
#        #        Come with me.
#        #        Can’t you go alone?

#        #I’ll go alone
#        mc "I think I’ll go alone."

#        mw "Yeah, he might be more willing to open up with less people confronting him."

#        mc "huh?"

#        mw "Nothing, I’ll be sitting nearby listening in."

#        #*include Danny into scene*

#        dr "huh? Oh, it’s you, hey Derrick."

#        mc "Ummmm, no. My name is __________."

#        dr "Right, sure, whatever. What did you want to talk to me about?"

#        #Choice: Ask about homecoming
#        #        Ask about the rumors

#        #Ask about homecoming
#        mc "I was wondering how homecoming went for you."

#        dr "Oh, well I guess it was ok. I had a good time while my date was with me, but it fell flat after she left."

#        mc "Where did she go?"

#        dr "Oh I don’t know, she just upped and left in the middle of the evening, which really sucked for me cause she didn’t even bother to tell me and I’m really into her and just don’t know what to do-"

#        mc "Right right, that does suck, sorry to hear it."

#        dr "..."

#        mc "...soooooo, about Agnes-"

#        dr "Oh what about her? *irritated*"

#        mc "Do you know what she was doing after she left you, maybe she said something?"

#        dr "Nah, she wasn’t even kind enough to tell me that much. She just left saying she had to go do something or other. Man..."

#        mc "Huh, ok then. Sorry your night didn’t go so well man. But hey..."

#        #Choice: there’s someone in school who likes you.
#        #        You’ll find someone else.

#         #               There’s someone who likes you
#        mc "I’m pretty sure there’s someone in school who likes you a lot."

#        dr "You think so? I don’t know, I just can’t really see that being true. But thanks anyway Derrick."

#        mc "...My name is- nevermind"
#        #*leaves*

#         #               You’ll find someone else
#        mc "there are plenty of other cute girls here at school."

#        dr "Yeah but… I don’t know… Well I’ll see what happens, thanks anyway Derrick."

#        mc "...My name is- nevermind"
#        #*leaves*

#         #       Ask about rumors
#        mc "Just wondering, have you heard the rumors floating around school?"

#        dr "Which one? Oh wait, do you mean the one about Kolby sneaking off with some girl while his girlfriend was busy performing on stage? Yeah I’ve heard that one."

#        mc "Do you have some idea of who that mystery girl is?"

#        dr "Mmm not really, I don’t really concern myself with rumors generally."

#        mc "Oh ok then."

#        #Choice: ask about homecoming

#        mc "Well in any case, did you go to homecoming?"

#        dr "Oh, yeah i did."

#        mc "How was it for you?"

#        dr "Well I guess it was ok. I had a good time while my date was with me, but it fell flat after she left."

#        mc "Where did she go?"

#        dr "Oh I don’t know, she just upped and left in the middle of the evening, which really sucked for me cause she didn’t even bother to tell me and I’m really into her and just don’t know what to do-"

#        mc "Right right, that does suck, sorry to hear it."

#        dr "..."

#        mc "...soooooo, about Agnes-"

#        dr "Oh what about her? *irritated*"

#        mc "Do you know what she was doing after she left you, maybe she said something?"

#        dr "Nah, she wasn’t even kind enough to tell me that much. She just left saying she had to go so something or other. Man..."

#        mc "Huh, ok then. Sorry your night didn’t go so well man. But hey..."

#        #Choice: there’s someone in school who likes you.
#        #        You’ll find someone else.
#        #*player exits cafe and Marc follows*
#        mw "So how did it go with Danny?"

#        mc "Well he didn’t know anything directly about who it was Kolby sneaked off with, but he did confirm that Agnes ditched him earlier in the evening, and he didn’t know where she went or what she was doing."

#        mw "Hmmm… That seems pretty fishy to me. I think we should go talk to Agnes directly then, see if she’s hiding anything about homecoming."

#        mc "Alright then, sounds good to me."

#        mw "Oh man, those passes are so close I can almost feel them!"

#        mc "..."
#        #*end scene*

#        #Come with me
#        mc "I’d rather you come with me."

#        mw "Sounds good, since we usually stick together around school, it’ll appear more natural that we stay together."

#        mc "Huh?"

#        mw "Nothing, let’s get going."

#        #*include Danny into scene*

#        dr "huh? Oh, it’s you, hey Derrick, hey Marc."

#        mc "Ummmm, no. My name is __________."

#        dr "Right, sure, whatever. What did you two want to talk to me about?"

#        mw "ALRIGHT YOU MAGGOT, WHO WAS IT?!"

#        dr "Um, what?"

#        mc "Marc, I don’t think you should yell at him, remember we came to talk."

#        mw "Oh… Right. Sorry, I got carried away for a sec. Let me retry that. Danny, we want to ask you about homecoming and how your night went."

#        dr "...Riiiiight.... (disappointed/upset face) Well I guess it was ok. I had a good time while my date was with me, but it fell flat after she left."

#        mc "Where did she go?"

#        dr "Oh I don’t know, she just upped and left in the middle of the evening, which really sucked for me cause she didn’t even bother to tell me and I’m really into her and just don’t know what to do-"

#        mw "Yeah yeah, that’s enough of that. Focus kid."

#        dr "Kid? I’m older than you ya punk!"

#        mw "Who ya callin’ a punk you twerp?"

#        #Choice: Move the conversation along
#        #        Get Marc to focus

#        #        Move the conversation along
#        mc "Soooooo, about Agnes-"

#        dr "*irritated* Oh what about her?"

#        mc "Do you know what she was doing after she left you, maybe she said something?"

#        dr "Nah, she wasn’t even kind enough to tell me that much. She just left saying she had to go do something or other. Man..."

#        mc "Huh, ok then. Sorry your night didn’t go so well man."

#        mw "*under his breath* Scrub."

#        dr "What was that you little-"

#        bk "Hey you two! I’ve had about enough of you both disrupting the peace around here, and if you don’t stop then I’ll have you two kicked out, permanently."

#        mc "Sighhh..."

#        mw "Well we’re pretty much done here anyway, I don’t think Danny-boy has any more significant information to dish out. Let's get outta here _____."
                                                                                                                                         
#        #*leave*

#        #Get Marc to focus
                                                                                                                                         
#        mc "Marc, focus. Remember the passes."

#        mw "*takes a breath* Right right. Sorry, I promise I’ll stay calm."

#        mc "Soooooo, about Agnes-"

#        dr "*irritated* Oh what about her?"

#        mc "Do you know what she was doing after she left you, maybe she said something?"

#        dr "Nah, she wasn’t even kind enough to tell me that much. She just left saying she had to go do something or other. Man..."

#        mc "Huh, ok then. Sorry your night didn’t go so well man."

#        mw "Yeah, that sucks dude."

#        mc "But hey..."

#        #Choice: there’s someone in school who likes you.
#        #        You’ll find someone else.

#        #Can’t you go alone?
#        mc "Why can’t you go talk to him alone? You wanted to go meet him in the first place."

#        mw "Because Christina hired you, duh. Now c’mon, do you want to go alone or with me?"

#        #Encounter with Agnes

#        #*in chemistry class*

#        mg "And when we combine potassium chlorate with sulfur..."

#        #I wonder if I should talk to Agnes right now about homecoming. She looks like she isn’t paying much attention to the lesson anyway, on top of the fact that she looks really bored too."

#        ar "Hey, is it just me or is this class soooo dull?"

#        mc "Huh? Oh, yeah, I’d have to agree."

#        ar "Man, I wish my laptop hadn’t been confiscated last period..."

#        #Choice: Ask about homecoming
#        #        Ask about rumors

#        #Ask about homecoming
#        mc Hey I was wondering Agnes, how was homecoming for you?

#        ar What? Why do you ask?

#        mc Oh just wondering, like I said.

#        ar ...It was fine.

#        #Choice: Just fine?
#        #Did something go wrong?

        
#        mc "It was only fine?"

#        ar "Well I did have a good evening after I ditched my date. He was kinda lame."

#        mc "I think I heard that Danny’s date left him during homecoming. You were his date right?"

#        ar "...Yeah..."

#        mc "What did you do after you left him?"

#        ar "I went and had fun. Besides, I don’t think it’s really your business dude."

#        mc "Alright then, sorry, just curious."

#        ar "Oh it’s ok… If you really want to know I just snuck off to my locker to play games on my laptop."

#        mc "Oh… ok then, sorry to bother you."
#        #*end scene*

#        #Ask about rumors
#        mc "Hey have you been hearing any of the rumors going around the school lately?"

#        ar "What? Uh, no, I don’t really pay attention to gossip."

#        mc "Oh, well lately people have been talking about something that happened at homecoming. Apparently, Kolby the basketball player snuck off with someone while his girlfriend Christina was performing on stage for the school."

#        ar "Is that so?..."

#        mc "Yeah, it’s been a problem between Kolby and Christina since then."

#        ar "I guess that could happen..."

#        mc "By the way, where did you say you went after you left Danny at homecoming?"

#        ar "Uh, huh? What? Hey listen, it’s really none of your business, I went and had some fun ok? Besides, if you really want to know I went to my locker to play games on my laptop."

#        mc "Oh… ok then, sorry to bother you."
#        #*end scene*

#        #Encounter with Natalie

#        #(Natalie sees you texting with Marc about the situation, because of that she draws pictures leading up to revealing that Agnes did it.)

#        #*Texting Marc later on after encounter with Agnes*

#        mw "U able 2 get anything out of Agnes? Wut was she doin after dtching Danny-boy?"

#        mc "She told me that she snuck off to her locker to play games on her laptop, but she seemed really anxious to end the conversation and even seemed nervous."

#        mw "Prtty sure she lied bout goin 2 her lcker to play her laptop. She always has laptop with her, nvr leaves it at school. Super spicious of Agnes."

#        mc "Yeah, but how can we find out conclusively that she was the one Kolby snuck off with?"

#        mw "Dunno..."

#        mc "Huh? Who’s tapping my shoulder?..."

#        nm "Hi..."

#        mc "Oh, Natalie. Hi, what’s up?"

#        nm "Can I talk to you? About Agnes?"

#        mc "Uh sure, I’m not really paying attention to the class anyway."

#        nm "I know, I’ve been watching you text Marc."

#        mc "Really? Why? O.o"

#        nm "I didn’t mean to at first, I just simply glanced at your screen, but then I saw that you and Marc were talking about Agnes..."

#        mc "Oh, uhhh, we were just... that is..."

#        nm "You two are trying to figure out if she was the one who Kolby snuck off with during homecoming right?"

#        mc "Well..."

#        #Choice: Lie
#        #Tell the truth

#        #Lie
#        mc "Well actually we were.. Uh.. talking about a group project we were working on, it’s a game on Agnes’ laptop..."

#        nm "...I already said that I’ve been watching you text Marc. I know what you two are doing."

#        mc "Uh..."

#        #Tell the truth
#        mc "Yeah, that’s what we’re doing. I’m sorry if you don’t like that considering that Agnes is your friend-"

#        nm "No that isn’t a problem, but I need to tell you-"

#        mc "Really though I’m sorry-"

#        ----------------------------------------------------------------------------------------------------------------------------
#        nm "Listen, Agnes was the one."

#        mc "...What?!"

#        mk "Hey ______! Quiet down back there when I’m trying to teach!"

#        mc "*whisper* Agnes was the one?"

#        nm "Yes."

#        mc "Wait, why would you tell me this?"

#        nm "Because what Agnes did was wrong. She shouldn’t have done what she did with someone who already had a girlfriend. That and I want her to go back to being the quirky gamer girl I became friends with, without any guilt or anything tying her down."

#        mc "I see… Well thanks for letting me know, this helps a lot."

#        nm "Hey listen, please don’t tell anyone, especially Agnes that I gave up her secret. I want her to know from me that I did it."

#        mc "Alright then, I’ll keep it secret."

#        nm "Thanks, I appreciate it."

#        mk "Alright you two, I’ve had about enough of you two ignoring me when I teach. Both of you pay attention now or you two will have detention for a week."
#        #*end scene*

#        #Last Encounter with Kolby

#        #*passing in the hallway in the morning*
#        kf "Hey ________, can I talk to you after school today? Alone."

#        mc "Uh sure..."

#        #Choice: But why?
#        #        No problem

#        #Why?
#        mc "but why do you want to meet with me?"

#        kf "I want to talk to you about something you recently discovered, something Natalie told you."

#        mc "Huh? How do you know?"

#        kf "I’ll tell you after school. Let’s meet in the library."

#        mc "Ok then..."

#        #No problem
#        mc "No problem. Where do you want to meet?"

#        kf "Let’s meet in the library."

#        mc "Alright then, see ya."


#        #*after school in the library*
#        kf "So I want to talk to you about homecoming, about Agnes."

#        mc "Wait wait, how did you find out that I was looking into it?"

#        kf "Well first of all there was your questions about homecoming. Second, Natalie told Agnes who told me."

#        mc "Oh..."

#        kf "But what I really want to do is ask you to not tell Christina."

#        mc "What? Why would I not?"

#        kf "Because I promise you, myself, and to Christina even if she doesn’t know that I’ll drop Agnes completely and focus myself back on Christina and no one else. I made a mistake, and I’m going to fix it."

#        mc "How can I believe you?"

#        kf "I guess you really can’t, but all I have is my word. I won’t betray Christina again."

#        mc "..."

#        kf "Well it’s up to you, I deserve it if you do. But hopefully you’ll give me a second chance."
#        #*end scene*

#        #Last Encounter with Christina

#        mw "Well now that we’ve confirmed that Kolby went off with Agnes, it’s time that we told Christina to let her know, and earn us those passes!"

        mc "Sighhhhh..."

        sg "Is something wrong _______?"

        #Choice: Nothing
        #Tell them about what Kolby said.

        #Nothing
        mc "It’s fine, let’s go talk to Christina."

        #Tell them about Kolby.
        mc "Kolby talked to me earlier. He asked me not to tell Christina about Agnes."

#        Marc, sg "What?! Why would he do that?"

        mc "He said that he made a mistake, and that he wants to fix his relationship with Christina. He didn’t elaborate beyond that, but he left the choice to me."

        mw "Obviously you’ll tell Christina! Kolby screwed up for betraying Christina like that, she deserves to know, and most important of all, we’ll be getting passes to the Spring Festival for free."

        sg "Marc seriously, stop it with the passes. CONTINUE HERE"


        #*later*
        mc "Hey Christina, can we talk for a minute?"

        cs "Oh hey, did you guys find out who it was?"

        mw "Oh yeah we did! Did you bring us the passes you promised us?"

        sg "Marc! Calm down and let ______ talk first!"


