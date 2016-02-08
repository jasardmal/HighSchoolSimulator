    label firstSchoolDay:
        
        scene img_1832
        "*Bell Rings*"
        $ thephase = 3;

        pa "Welcome to the first day of school at Ketsu High School! Here, we…."

        mc "That guy, there in the back? {w} That’s me. {w} I just moved here from Utah. {w} This is my first day at Ketsu High, and I don’t know anyone. {w} This day is gonna be such a drag."

        pa "....... And that is how the Cougars roar! Have a wonderful day, students!"

        mc "Ugh. {w} When I moved here, I thought that not really knowing anyone might be nice. {w} My parents are always gone on some trip or another, {w} so I don’t really have any actual 
            interactions. {w} This year, I thought that maybe, {w} just maybe, {w} I could find someone who would actually be my friend."

        #Desk Slams Forward

        mw "Watch yourself! {w} Keep talking, {w} someday you'll say something intelligent!"

        s1 "If you weren’t so easy to make fun of, {w} I wouldn’t! {w} You’re just a little baby."

        mw "How many times do I have to flush before you go away?"

        #Punches other student
        
        #Fight Ensues
        
        #Wipes Chin

        mw "I told you not to insult me. {w} Idiot."

        #Teacher comes in
        
        mh "Hey! {w} What’s going on? {w} How dare you engage in classroom violence! {w} Don’t you know that fights are against school rules? {w} Both of you, {w} to the dean’s office!"

        #Marc and other student leave

        "You! New student! You were the closest and probably saw what happened the best. go to the deans office with them to fill out an incident report!"

        mc "But, wait, {w} no…."

        mh "Don’t argue, {w} just do it! {w} Don’t let your experiences be memories! {w} Go to the Dean’s office!"
        
        #Sighs

        mc "F-Fine..."
        
        #Grumbling as you leave
        
        mh "Back in my day, {w} when we had to fight over things, {w} we waited until after school...."

        #CHANGE SCENES WOO DEAN'S OFFICE TIME

        #MC Standing outside door about to walk in
        scene img_1831

        de "Now, {w} you both know better! {w} I can’t believe that it hasn’t even been a day into the school year and you have already begun fighting! {w} Shame on both of you! {w}
            Have you no dignity?!?!"

        co "Sorry, Mr Dean. It won’t happen again."
        
        #Under his breath

        mw "Fat lard."

        s1 "Excuse me? {w} What did you call me?"

        mw "Nothing, {w} I was talking about your mother."

        de "Both of you! {w} Behave! {w} Have you no decency? {w} You haven’t even left my office! {w} Marc, {w} stay here, and let him go."
        
        $mwname = "Marc"

        mw "Fine. {w} But he’s still a fat lard."

        de "One more word out of you and I will suspend you!"

        mw "..."

        #Walks in

        de "Who are you?"

        mc "I’m a new student. {w} I just moved here a few weeks ago. {w} Mr. Hart told me to come down here because I was closest to the fight, {w} so that I can fill out a report."

        de "Oh. Well, {w} in that case, {w} let me get one of those for you."
        
        #Rummages through cabinet file
        
        label firstdayschoolchoice1:

            mc "What did I see?"

            #OPTIONS
            
            menu:

                "Marc started it":
                    jump firstSchoolC1O1
                
                "Marc didn't start it":
                    jump firstSchoolC1O2


        label firstSchoolC1O1:
            #MARC STARTED IT
            mc "It looked to me like that student was antagonizing the other student. {w} I’m not sure what was said, {w} but one minute I was waiting for class to start, {w} 
                and the next those two were duking it out by my desk."

            de "Well, {w} are you sure you didn't see anything else?"

            mc "All I know is the two were fighting. {w} I don’t know enough about either of them to tell."

            de "Well, {w} all right then. {w} Get back to class."

            mc "Yes, sir."

            de "On your way back out, {w} call Marc back in."

            mc "Which one is Marc?"

            de "The one who probably started the fight."

            mc "Oh, alright."

            #Walks out

            mc "Marc? {w} The dean wants to see you."

            mw "Ugh, {w} finally. {w} I wish this would just be over… {w} I can’t stand it when people insult me and get away with it."

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
            
            #To himself

            mc "Marc must be the one who is still in the foyer. {w} Ok."

            #Walks out

            mc "Marc? {w} The dean wants to see you."

            mw "Ugh, {w} finally. {w} I wish this would just be over… {w} I can’t stand it when people insult me and get away with it."

            #Marc goes to office

            #Goes to class
            jump firstSchoolPath

        label firstSchoolPath:
        #AFTER BOTH VERSIONS:
        scene img_1832
        
        mh "Welcome back!"

        #Bell Rings

        #Slams book closed dramatically
        
        mh "Alright, {w} Class Dismissed."
        
        #To Himself
        scene img_1831

        mc "I should probably get to my next class. {w} It’s no good to dawdle. Looks like my next class is… {w}"
            
        #Shift to picture of the schedule
            
        mc "... History."

        "Bell rings*"
        $ thephase = 4

        mc "Oh no! {w} I’m late!"

        #Enter Class
        scene img_1832

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
        scene img_1831
        
        #Groan

        mc "I can’t believe I got homework on the first day of school. {w} What kind of sick place is this?"
        
        #Shoulder bumps into MC

        fh "Hey, freshie, {w} if you can’t take the heat get out of the oven."
        
        #Hurries off"

        mc "What? {w} Whatever…"
        $ thephase = 5
        jump period
        
        #Initiate end of day 1
        label firstSchoolDayEnd:
            
            scene img_1801
        
            mc ">Walking Home"

            mw "Hey, wait up!"

            mc "!?"

            #Marc: I wanted to thank you for helping me out. I’ve never seen you before. What’s your name?

            #MC: Uh… No problem… my name is *tells him name*... hey…

            #Marc: If you ever need anything, let me know. I’ll return the favor. 

            #MC: Oh, uh, ok… Thanks… 

            #Marc: Cya round.
            #MC: Um, Ok. Cya. 


            #*At home*

            #*Phone is ringing*

            #Pick up the Phone

            #MC: Hello?

            #Mom: Hey honey! How was the first day of school?

            #MC: Oh, it was alright I guess.

            #Mom: Make any new friends?

            #MC: Erm, Maybe.

            #Mom: *sigh* Well, that's something. You should try to be friends with more people, like your sister.

            #MC: Ok, Mom. I’ll try.

            #Mom: Don’t try, do! *sigh* Love you, hun.

            #MC: Love you too, mom. *click*

    #        #*Sigh* It’d be nice if mom or dad was home for once...

    #        #*end scene*



    ##        #Dont Pick Up the Phone


    ##        MC: *groan* Ugh! I wonder who it is. Well, they can wait. I need to sleep… Today was busy…

            # *end scene*
        
        
        
        
    ########################### August 31
            
    label secondSchoolDay:        
            
        #Alarm Rings

        mc "Urgh… My head…"

        #Alarm rings again

        mc "Fine, I’ll get up. Where’s my toothbrush?"

        #Screen shakes cause hes looking for stuff

        #OBTAINED TOOTHBRUSH

        mc "Aha! Here we go."

        #KNOCK KNOCK KNOCK

        mc "What? Who’s here? Who even knows I live here?"

        mw "OI! YOU READY FOR SCHOOL?"

        mc "Marc?!?!?!?!?!?! Wha-"

        mw "YOU’RE GUNNA BE LATE BRO"

        mc "Ok, ok! I just got out of bed! Let me put on some clothes first, jeez!" #*puts on clothes*

        #Runs out of door

        #Out of breath 

        mc "Alright, Marc, I’m here. How did you figure out where I live?"

        mw "You dropped your wallet. Your address was inside."

        mc "......Oh........."

        mw "You probably want this back." 

        #Hands over wallet

        #OBTAINED WALLET

        mw "Now we’re even."

        mc "Even?"

        mw "Yeah, for when you had my back at the dean’s."

        mc "Oh, Right."

        #(Or, if you didn’t, Oh, Uh, Right, Sure.)

        mw "Sooo… Shall we? {w}If we stand here any longer, we’ll be late for school."

        mc "Oh! let’s go."

        #Go to school ya chump

        #Arrives at school

        mw "Hey, MC. Can I talk to you for a sec?"

        mc "Uh, sure Marc. What’s up?"

        mw "Since you’re new in town, you probably don’t know nothin ‘bout anything. If you want to get through the year, you’ll need someone to show you around. I can do that for you."


        label seconddayschoolchoice1:
        
            menu:
                
                "You Could? That’d be great!": #(+affection)
                    jump seconddayschoolC1O1
                "I think I would rather do it on my own.": #(- affection)
                    jump seconddayschoolC1O2
                "Uh, sure....":
                    jump seconddayschoolC1O3
                    
                    
        label seconddayschoolC1O1:
            mw "Alright, meet me after school in the courtyard, ok? See you in class!"
            jump secondSchoolDay
        label seconddayschoolC1O2:
            mw "Oh, ok. Well, let me know if you need anything then. See you in class."
            jump secondSchoolDay
        label seconddayschoolC1O3:
            mw "‘Kay. Cya Round."
            jump secondSchoolDayPath2
            
    label secondSchoolDayPath1:        
                
        #Scene Change MATH CLASS

        mk "Ok Class! Take your seats! One… One… Two… Three… Five… Eight… Thirteen… Twenty one…"

        #Continues mumbling (LEAVE RESOLUTION OF JOKE UNTIL THE END OF THE YEAR, TELLS STUDENTS THAT IT’S THE FIBONACCI SEQUENCE)

        n "........" 

        n "*Scribble scribble*"

        mk  "Now, class. I know that you hate homework on the first day, but I want to get you all learned up by the end of the year."

        #Collective groans

        mk "I will hand out your assignments on the way out. For now, there is a text book under everyone’s desk. Pull it out and turn to page 394. That is where we will start."

        #MORE GROANS

        mk "Today’s topic will be geometry. You know, I really like angles, to a certain degree."

        mc "............ was that a pun"

        mc "What was that pun"

        n "*Doodles smiley faces*"

        mk "Ms. McNeil, I don’t see you opening up your textbook. Please don’t try to measure my patience."

        n "*Quickly sketches frowny face and shows it to Mr. Kelly*"

        mk "... Okaaaaaay Ms. McNeil, I think you should put away your sketchbook now."

        n "*Opens eyes really wide, vigorously shakes her head*"

        mk "I insist."

        n "*Eyes tear up a bit, puts sketch book away and begins to sulk*"

        mk "That’s better."

        #Later in class

        mk ".... and that’s how these laws of geometry work. You, know, it’s a shame parallel lines will never meet. They have so much in common."

        #Class groans

        #Bell rings 

        mk "Alright class, you are dismissed."

        #mc 1. (Ask how she’s feeling) *walks up to Natalie before they leave* "hey, are you ok? I couldn’t help but notice that you seemed upset. "  (+affection)
        #        2. (Question her behavior) "Why didn’t you pay any attention in class? Are you mute?" (-Affection)
        #        3. (Ignore her) 

        #n 
        #*blushes*
        #*makes an angry face*
             # 3.          ………………………………..

        label seconddayschoolchoice2:
        
            menu:
                
                "Ask how she's feeling":  #(+affection)
                    jump seconddayschoolC2O1
                "Question her behavior": #(-Affection)
                    jump seconddayschoolC2O2
                "Ignore her":
                    jump seconddayschoolC2O3
                    
                    
        label seconddayschoolC2O1:
            mc "Hey, are you ok? I couldn’t help but notice that you seemed upset."
            n "*Blushes"
            jump secondSchoolDayPath2
        label seconddayschoolC2O2:
            mc "Why didn’t you pay any attention in class? Are you mute?"
            n "*Makes an angry face*"
            jump secondSchoolDayPath2
        label seconddayschoolC2O3:
            jump secondSchoolDayPath2
            
    label secondSchoolDayPath2:
        
        mc "Huh. That was strange…."

        mc "My next class is science, it looks like. I’d better get there fast."


        #Scene change = ENTER SCIENCE

        mg "Before you sit down, line up at the back of the room. I have some important questions."

        mg "Since this is a science class, we must observe the scientific method. That means collecting questions. Now, my first question is this:…"

        #Fade out

        mc "....Now, pick your partners. We will begin our lectures tomorrow, and collect data. Tonight, I want you to take notes on the first chapter of the textbook. Before you leave, let me know who you are sitting with. If you don’t, you will be randomly assigned with a partner. Go!"

        mc "Uh… Hey… Anyone want to be my partner?"

        mc "Anyone? Hey, you… No? Alright…"

        mc "Urgh… Seems like no one is available…"

        mg "Now, does anyone not have a partner yet?"

        #Looks around  

        mc "Uh, I guess I don’t have a partner yet…"

        mg "Interesting. Now, could you take a look around the room? Can you tell me what you see?"

        mc "Uhm… Oh." 

        #Looks at agnes 

        mc "Uh, alright. Hi…"

        ar "Hi."

        mg " Wonderful. Now, tomorrow’s lecture will be about the chapter in which you are currently engaged in notetaking. Remember, the chapter notes will be due at the end of every week. The first chapter is rather short, so if you do not have them completed, there will be no excuse."

        #Staring at her phone, headphones in

        mc "Um, hi. Er, since we are working together and everything, I was wondering…"

        ar "Hmmm?"

        mc " Oh, I was just wondering…"

        ar "Agnes. But don’t call me that. I prefer..."

        ar ".... Novahawk."

        mc " Uh… Right… Novahawk… ok…"

        ar " Mhm. Now get outta here."

        #Agnes leaves 

        mc ".........Huh."

        mc "I guess it’s time for the electives now. Let’s see what Marc is up to."

        #Insert Elective here*

        mw "...And that’s how you disguise your phone number."

        mc "Oh, cool… What would I use that for?"

        mw "Probably nothing, but hey, the more you know."

