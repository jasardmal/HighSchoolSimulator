    label firstSchoolDay:
        
        "*Bell Rings*"

        pa "Welcome to the first day of school at Ketsu High School! Here, we…."

        mc "That guy, there in the back? {w} That’s me. {w} I just moved here from Utah. {w} This is my first day at Ketsu High, and I don’t know anyone. {w} This day is gonna be such a drag."

        pa "....... And that is how the Cougars roar! Have a wonderful day, students!"

        mc "Ugh. {w} When I moved here, I thought that not really knowing anyone might be nice. {w} My parents are always gone on some trip or another, {w} so I don’t really have any actual 
            interactions. {w} This year, I thought that maybe, {w} just maybe, {w} I could find someone who would actually be my friend."

        "*Desk Slams Forward*"

        mw "Watch yourself! {w} Keep talking, {w} someday you'll say something intelligent!"

        s1 "If you weren’t so easy to make fun of, {w} I wouldn’t! {w} You’re just a little baby."

        mw "How many times do I have to flush before you go away? {w} *Punches other student*"

        "*Fight Ensues*"

        mw "*Wipes Chin* {w} I told you not to insult me. {w} Idiot."

        #Teacher comes in,#
        
        mh "Hey! {w} What’s going on? {w} How dare you engage in classroom violence! {w} Don’t you know that fights are against school rules? {w} Both of you, {w} to the dean’s office!"

        "*Marc and other student leave*"

        "You! New student! You were the closest and probably saw what happened the best. go to the deans office with them to fill out an incident report!"

        mc "But, wait, {w} no…."

        mh "Don’t argue, {w} just do it! {w} Don’t let your experiences be memories! {w} Go to the Dean’s office!"

        mc "*Sighs* {w} F-Fine..."
        
        mh "*Grumbling as you leave* {w} Back in my day, {w} when we had to fight over things, {w} we waited until after school...."

        #*CHANGE SCENES WOO DEAN'S OFFICE TIME*

        #*MC Standing outside door about to walk in*

        de "Now, {w} you both know better! {w} I can’t believe that it hasn’t even been a day into the school year and you have already begun fighting! {w} Shame on both of you! {w}
            Have you no dignity?!?!"

        co "Sorry, Mr Dean. It won’t happen again."

        mw "*Under his breath* {w} Fat lard."

        s1 "Excuse me? {w} What did you call me?"

        mw "Nothing, {w} I was talking about your mother."

        de "Both of you! {w} Behave! {w} Have you no decency? {w} You haven’t even left my office! {w} Marc, {w} stay here, and let him go."

        mw "Fine. {w} But he’s still a fat lard."

        de "One more word out of you and I will suspend you!"

        mw "..."

        mc "*walks in*"

        de "Who are you?"

        mc "I’m a new student. {w} I just moved here a few weeks ago. {w} Mr. Hart told me to come down here because I was closest to the fight, {w} so that I can fill out a report."

        de "Oh. Well, {w} in that case, {w} let me get one of those for you. *rummages in file cabinet*"
        
        label firstdayschoolchoice1:

            mc "What did I see?"

            #OPTIONS
            
            menu:

                "Marc Started it":
                    jump firstdayschoolchoice1outcome1
                
                "Marc didnt start it":
                    jump firstdayschoolchoice1outcome2
                    
            #-idk    -------> blame teacher
            #Marc started it:


        label firstdayschoolchoice1outcome1:
        #MC: It looked to me like that student was antagonizing the other student. I’m not sure what was said, but one minute I was waiting for class to start, and the next those two were duking it out by my desk. 

        #Dean: Well, are you sure you didn't see anything else?

        #MC: All I know is the two were fighting. I don’t know enough about either of them to tell.

        #Dean: Well, all right then. Get back to class.

        #MC: Yes, sir.

        #Dean: On your way back out, call Marc back in.

        #MC: Which one is Marc?

        #Dean: The one who probably started the fight.

        #MC: Oh, alright. 

        #*Walks out*

        #MC: Marc? The dean wants to see you.

        #Marc: Ugh, finally. I wish this would just be over… I can’t stand it when people insult me and get away with it. 

        #*Marc goes to office*

        #*Goes to class*

        #Mr. hart: Welcome back!

        #*End Scene*

        label firstdayschoolchoice1outcome2:
        #MARC DIDN'T START IT

        #MC: Well… To be honest, it seemed to me like the one who is still sitting outside was the victim. The other one had made some rude comments about him, and he didn’t like it. 
        #Dean: Is that right? Well, so far, that’s not what I’ve heard. Are you sure?

        #MC: Yes, Sir. I’m Sure.    

        #Dean: Hmm… Alright. Go back to class… Thank you for your help.

        #MC: Yes, sir.

        #Dean: On your way back out, call Marc back in.

        #MC: *to himself* Marc must be the one who is still in the foyer.* Ok.

        #*Walks out*

        #MC: Marc? The dean wants to see you.

        #Marc: Ugh, finally. I wish this would just be over… I can’t stand it when people insult me and get away with it. 

        #*Marc goes to office*

        #*Goes to class*

        #Mr. hart: Welcome back!

        #*End Scene*




        #AFTER BOTH VERSIONS:

        #*Bell Rings*

        #Mr Hart: Alright, Class Dismissed. *slams book closed dramatically.*

        #MC:*To Himself* I should probably get to my next class. It’s no good to dawdle. Looks like my next class is…*shift to picture of the schedule*... History.

        #*bell rings*

        #MC: Oh no! I’m late!

        #*enter Class*

        #MC: Sorry I’m late, Mrs. Ong.

        #Mrs. Ong: The Nerve! In my day, if we were late, we would be paddled! With a wooden spoon! Sit down, before I get any angrier. Now, class. What is the…

        #MC:*brain wandering off*


        #Mrs Ong: Mr MC can you tell me what the capital of Texas is?

        #MC: Er… Is it Houston.

        #Mrs. Ong: Actually, it’s Austin. Now, if you would stop dozing off in class, maybe you would learn something. In my day, we were whipped if we fell asleep in class! 

        #MC: Urgh… yes, Mrs Ong.

        #Mrs. Ong: Now, class. To start off the year, we will be researching how civilizations in the fertile crescent rose to power. By Friday, I want an essay no longer than 750 words on this subject. If you do not do this assignment, it will severely impact your grade at this, the beginning of the school year! *Bell rings* Dismissed!

        #MC:*In the hallway* *Groan* I can’t believe I got homework on the first day of school. What kind of sick place is this? 

        #Frederick Hobson: *shoulder bumps into MC* Hey, freshie, if you can’t take the heat get out of the oven. *Hurries off*

        #MC: What? Whatever… *end scene*












        #INSERT ELECTIVES HERE






















        #END ELECTIVE HERE



        #*Initiate end of day 1*
        #*Walking Home*

        #Marc: Hey, wait up!

        #MC: !?

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
        
        
        
        
#        ########################## August 31
        
        
        
##*Alarm Rings*

#mc "Urgh… My head…"

#mc "*Alarm rings again*"

#mc "Fine, I’ll get up. Where’s my toothbrush?"

##*Screen shakes cause hes looking for stuff*

#mc "*OBTAINED TOOTHBRUSH* Aha! Here we go."

##*KNOCK KNOCK KNOCK*

#mc "What? Who’s here? Who even knows I live here?"

#m "OI! YOU READY FOR SCHOOL?"

#mc "Marc?!?!?!?!?!?! Wha-"

#m "YOU’RE GUNNA BE LATE BRO"

#mc "Ok, ok! I just got out of bed! Let me put on some clothes first, jeez!" *puts on clothes*

##*runs out of door*

#mc "*out of breath* Alright, Marc, I’m here. How did you figure out where I live?"

#m "You dropped your wallet. Your address was inside."

#mc "......Oh........."

#m " You probably want this back." 

#m "*hands over wallet*  *OBTAINED WALLET*" 

#m "Now we’re even."

#mc "Even?"

#m "Yeah, for when you had my back at the dean’s."

#mc "Oh, Right."

##(Or, if you didn’t, Oh, Uh, Right, Sure.)

#m "Sooo… Shall we? {w}If we stand here any longer, we’ll be late for school."

#mc "Oh! let’s go."

##*go to school ya chump*

##*Arrives at school*

#m "Hey, MC. Can I talk to you for a sec?"

#mc "Uh, sure Marc. What’s up?"

#m "Since you’re new in town, you probably don’t know nothin ‘bout anything. If you want to get through the year, you’ll need someone to show you around. I can do that for you."

##mc 1. "You Could? That’d be great!" (+affection)
##       2. "I think I would rather do it on my own." (- affection)
##        3. "Uh, sure...."
        
##marc (1) "Alright, meet me after school in the courtyard, ok? See you in class!"
# #         (2) "Oh, ok. Well, let me know if you need anything then. See you in class."
# #         (3) "‘Kay. Cya Round."

##*Scene Change MATH CLASS*

#mk "Ok Class! Take your seats! One… One… Two… Three… Five… Eight… Thirteen… Twenty one…" *continues mumbling* (LEAVE RESOLUTION OF JOKE UNTIL THE END OF THE YEAR, TELLS STUDENTS THAT IT’S THE FIBONACCI SEQUENCE)

#n "……………" *scribble scribble*

#mk  "Now, class. I know that you hate homework on the first day, but I want to get you all learned up by the end of the year."

##*collective groans*

#mk "I will hand out your assignments on the way out. For now, there is a text book under everyone’s desk. Pull it out and turn to page 394. That is where we will start."

##*MORE GROANS*

#mk "Today’s topic will be geometry. You know, I really like angles, to a certain degree."

#mc "............ was that a pun"

#mc "What was that pun"

#n "*doodles smiley faces*"

#mk "Ms. McNeil, I don’t see you opening up your textbook. Please don’t try to measure my patience."

#n "*quickly sketches frowny face and shows it to Mr. Kelly*"

#mk "….. Okaaaaaay Ms. McNeil, I think you should put away your sketchbook now."

#n "*opens eyes really wide, vigorously shakes her head*"

#mk "I insist."

#n "*eyes tear up a bit, puts sketch book away and begins to sulk.*"

#mk "That’s better."

##*later in class*

#mk ".... and that’s how these laws of geometry work. You, know, it’s a shame parallel lines will never meet. They have so much in common."

##*class groans*

#mk "*bell rings* Alright class, you are dismissed."

##mc 1. (Ask how she’s feeling) *walks up to Natalie before they leave* "hey, are you ok? I couldn’t help but notice that you seemed upset. "  (+affection)
##        2. (Question her behavior) "Why didn’t you pay any attention in class? Are you mute?" (-Affection)
##        3. (Ignore her) 

##n 
##*blushes*
##*makes an angry face*
#     # 3.          ………………………………..



#mc "Huh. That was strange…."

#mc "My next class is science, it looks like. I’d better get there fast."


##*scene change = ENTER SCIENCE*

#mg "Before you sit down, line up at the back of the room. I have some important questions."

#mg "Since this is a science class, we must observe the scientific method. That means collecting questions. Now, my first question is this:…"

##*Fade out*

#mc "....Now, pick your partners. We will begin our lectures tomorrow, and collect data. Tonight, I want you to take notes on the first chapter of the textbook. Before you leave, let me know who you are sitting with. If you don’t, you will be randomly assigned with a partner. Go!"

#mc "Uh… Hey… Anyone want to be my partner?"

#mc "Anyone? Hey, you… No? Alright…"

#mc "Urgh… Seems like no one is available…"

#mg "Now, does anyone not have a partner yet?"

#mc "*looks around*  Uh, I guess I don’t have a partner yet…"

#mg "Interesting. Now, could you take a look around the room? Can you tell me what you see?"

#mc "Uhm… Oh." 

#mc "*looks at agnes*" 

#mc "Uh, alright. Hi…"

#a "Hi."

#Mrs. Galvin: " Wonderful. Now, tomorrow’s lecture will be about the chapter in which you are currently engaged in notetaking. Remember, the chapter notes will be due at the end of every week. The first chapter is rather short, so if you do not have them completed, there will be no excuse."

#a "*staring at her phone, headphones in*"

#mc "Um, hi. Er, since we are working together and everything, I was wondering…"

#a "Hmmm?"

#mc " Oh, I was just wondering…"

#a "Agnes. But don’t call me that. I prefer..."

#a ".... Novahawk."

#mc " Uh… Right… Novahawk… ok…"

#a " Mhm. Now get outta here."

#mc "*agnes leaves* .........Huh."

#mc "I guess it’s time for the electives now. Let’s see what Marc is up to."

#*Insert Elective here*

#m "...And that’s how you disguise your phone number."

#mc "Oh, cool… What would I use that for?"

#m "Probably nothing, but hey, the more you know."

