﻿#Main Character
define mc = DynamicCharacter("mcname", color="#ffffff")

#Generic Students
define s1 = Character('Other Student', color="#c8ffc8")

#Students
define mw = DynamicCharacter("mwname", color="#c8ffc8")
define kf = Character('Kolby Frederickson', color="#c8ffc8")
define fh = DynamicCharacter("fhname", color="#c8ffc8")
define ik = Character('Ivor Kovosad', color="#c8ffc8")
define dr = Character('Danny Reuter', color="#c8ffc8")
define sg = DynamicCharacter("sgname", color="#c8ffc8")
define cs = Character('Christina Shulz', color="#c8ffc8")
define ar = DynamicCharacter("arname", color="#c8ffc8")
define cl = Character('Cynthia Lucas', color="#c8ffc8")
define nm = DynamicCharacter("nmname", color="#c8ffc8")
define bk = Character('Becka Krakowski', color="#c8ffc8")
define mom = Character('Mom', color="#c8ffc8")
define sis = Character('Jackie', color="#c8ffc8")

#School Staff
define de = Character('Dean', color="#c8ffc8")
define pa = Character('PA', color="#c8ffc8")
define hm = Character('Hall Monitor', color="#c8ffc8")

#Teachers
define mk = Character('Mr. Kelly', color="#c8ffc8")
define mh = Character('Mr. Hart', color="#c8ffc8")
define mg = Character('Ms. Galvin', color="#c8ffc8")
define mo = Character('Mrs. Ong', color="#c8ffc8")
define te = Character('Teacher', color="#c8ffc8")

#Combo Character
define co = DynamicCharacter("coname", color="#c8ffc8")

label start:
    
    #Start placeholder music
    play music "SweetSuccess.mp3"
    
    #Initialize Default Character Names
    $ mcname = "???"
    $ mwname = "Delinquet Student"
    $ fhname = "Refined Student"
    $ nmname = "Silent Student"
    $ arname = "Smart Student"
    $ sgname = "Plain Student"
    $ coname = "Delinquet Student and Other Student"
    
    
    #Initialize Main Character's Birthday
    $ mcbirthday = " "
    
    #Initialize Calendar/Time/Location
    $ clock = False#make false to hide the calendar
    $ stats = False#make false to hide the stats
    $ theweekday = 2#monday, the number of the weekday, this automatically changes but must be initially assigned
    $ themonth = 8#august, the number of the month, this automatically changes but must be initially assigned
    $ theday = 31#this automatically changes but must be initially assigned
    $ theyear = 2015#this automatically changes but must be initially assigned
    $ dayofyear = 243#you must calculate this properly, this automatically changes
    $ yearlim = 365#initially define it as 365 or 366, whichever is correct, this gets changed automatically later
    $ daylim = 31#initially define it as 28, 29, 30, or 31, whichever is correct, this gets changed automatically later
    $ stringweekday = "Monday"#2, the string of the weekday, this automatically changes but must be initially assigned
    $ stringmonth = "August"#8, the string of the month, this automatically changes but must be initially assigned
    $ thephase = 2#morning, the phase of the day, this automatically changes but must be initially assigned
    $ stringphase = "Morning"#2, the phase of the day, this automatically changes but must be initially assigned
    $ location = 1#school, the current location, this automatically changes but must be initially assigned
    $ stringlocation = "School"#1, the current location, this automatically changes but must be initially assigned
    
    #Initialize Special Day/Event Flags.
    $ ischaractercreation = True
    $ isfirstday = False
    $ issecondday = False
    $ isafterschool = True
    $ isendofweekend = False
    
    #Initialize Stats
    $ charismasubmax = 10
    $ charismasub = 0
    $ charisma = 0
    
    $ couragesubmax = 10
    $ couragesub = 0
    $ courage = 0
    
    $ intelligencesubmax = 10
    $ intelligencesub = 0
    $ intelligence = 0
    
    $ stresssub = 0
    $ stress = 3
    
    $ staminasubcurrentlim = 5
    $ staminasubfuturelim = 5
    $ staminasub = 0
    $ stamina = 3
    
    $ money = 10
    
    #Initialize Skills.
    $ spanishskillsub = 0
    $ spanishskill = 1
    $ hasdiscoveredspanish = True
    
    $ frenchskillsub = 0
    $ frenchskill = 0
    $ hasdiscoveredfrench = False
    
    $ latinskillsub = 0
    $ latinskill = 0
    $ hasdiscoveredlatin = False
    
    $ artskillsub = 0
    $ artskill = 0
    $ hasdiscoveredart = False
    
    $ musicskillsub = 0
    $ musicskill = 0
    $ hasdiscoveredmusic = False
    
    $ peskillsub = 0
    $ peskill = 0
    $ hasdiscoveredpe = False
    
    $ financeskillsub = 0
    $ financeskill = 0
    $ hasdiscoveredfinance = False
    
    $ programmingskillsub = 0
    $ programmingskill = 0
    $ hasdiscoveredprogramming = False
    
    $ homeecskillsub = 0
    $ homeecskill = 0
    $ hasdiscoveredhomeec = False
    
    #Initialize Inventory
    $ inventorygeneral = ["testgen1", "testgen2", "testgen3", "testgen4", "testgen5", "testgen6", "testgen7", "testgen8", "testgen9", "testgen10"]
    $ inventorygifts = ["testgif1", "testgif2", "testgif3", "testgif4", "testgif5", "testgif6", "testgif7", "testgif8", "testgif9", "testgif10"]
    $ inventoryclothes = ["testclo1", "testclo2", "testclo3", "testclo4", "testclo5", "testclo6", "testclo7", "testclo8", "testclo9", "testclo10"]
    $ inventorybooks = ["testboo1", "testboo2", "testboo3", "testboo4", "testboo5", "testboo6", "testboo7", "testboo8", "testboo9", "testboo10"]
    
    #Initialize Social Contacts
    $ hasmetmarc = True
    $ marcrank = 1
    $ marcprogression = 5
    
    $ hasmetkolby = True
    $ kolbyrank = 1
    $ kolbyprogression = 5
    
    $ hasmetfrederick = True
    $ frederickrank = 1
    $ frederickprogression = 5
    
    $ hasmetivor = True
    $ ivorrank = 1
    $ ivorprogression = 5
    
    $ hasmetdanny = True
    $ dannyrank = 1
    $ dannyprogression = 5
    
    $ hasmetsarah = True
    $ sarahrank = 1
    $ sarahprogression = 5
    
    $ hasmetchristina = True
    $ christinarank = 1
    $ christinaprogression = 5
    
    $ hasmetagnes = True
    $ agnesrank = 1
    $ agnesprogression = 5
    
    $ hasmetcynthia = True
    $ cynthiarank = 1
    $ cynthiaprogression = 5
    
    $ hasmetnatalie = True
    $ natalierank = 1
    $ natalieprogression = 5
    
    $ hasmetbecka = True
    $ beckarank = 1
    $ beckaprogression = 5
            
    #CHARACTER CREATION ******************************************************************************************
    label nameCreation:
        scene img_home
        mc "Who am I?"
        call screen input_charactersoftkeyboard
    
        label nameCheck:
            mc "Is this correct?"
        
            menu:
                
                "Yes":
                    $ mcname = input_value
                    $ ischaractercreation = False
                    #jump birthdayCreation
                    jump startDecider
                
                "No":
                    jump nameCreation
                    
#        label birthdayCreation:
#            mc "When is my birthday?"
#            call screen input_birthdaysoftkeyboard
            
#        label birthdayCheck:
#            mc "Is this correct?"
            
#            menu:
                    
#                    "Yes":
#                        $ mcbirthday = input_value
#                        jump startDecider
                    
#                    "No":
#                        jump birthdayCreation
    #START DECIDER *********************************************************************************************
    label startDecider:
        $ clock = True
        if isfirstday == True:
            jump firstSchoolDay
        if issecondday == True:
            jump secondSchoolDay
        if theweekday == 1:
            jump regularWeekend
        elif theweekday == 2:
            jump regularSchool
        elif theweekday == 3:
            jump regularSchool
        elif theweekday == 4:
            jump regularSchool
        elif theweekday == 5:
            jump regularSchool
        elif theweekday == 6:
            jump regularSchool
        elif theweekday == 7:
            jump regularWeekend
    
    #REGULAR SCHOOL START *********************************************************************************************
    label regularSchool:
        $ location = 2
        if isendofweekend == True:
            if stamina < 3:
                $ stamina = 3
            if stress > 3:
                $ stress = 3
            $ money = 10
            $ isendofweekend = False
        scene img_home with Dissolve(1.0)
        mc "It's time for school."
        scene img_nearschool with Dissolve(1.0)
        jump beforeSchool
    
        #BEFORESCHOOL ******************************************************************************************
        label beforeSchool:
            mc ">Going to school."
            $ location = 1
            $ thephase = 2
            scene img_hall with Dissolve(1.0)
            jump beforeSchoolChoice
                
        label beforeSchoolChoice:
            
            menu:
                
                mc "I have a bit of time before class starts. What should I do?"
                
                "Socialize":
                    jump beforeSchoolSocialize
                
                "Study":
                    jump beforeSchoolStudy
                
                "Exercise":
                    jump beforeSchoolExercise
                    
            label beforeSchoolSocialize:
                
                menu:
                    
                    mc "Where should I socialize?"
                    
                    "Library":
                        jump librarySocialize
                        
                    "Teacher's Lounge":
                        jump teacherloungeSocialize
                        
                    "Lunch Room":
                        jump lunchroomSocialize
                        
                    "Gym":
                        jump gymSocialize
                        
                    "Elective Hallway":
                        jump electivehallSocialize
        
            label beforeSchoolStudy:
                if stress == 0 or stress == 1:
                    mc "I studied and understood a lot! >Intelligence greatly increased. >Stress greatly increased. >Stamina decreased."
                    $ intelligencesub = intelligencesub + 2
                    $ stresssub = stresssub + 2
                    $ staminasub = staminasub - 1
                    $ thephase = 3
                    jump period
                elif stress == 2 or stress == 3:
                    $ randStudy = renpy.random.choice([1, 2])
                    if randStudy == 1:
                        mc "I studied and understood a lot! >Intelligence greatly increased. >Stress greatly increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 2
                        $ stresssub = stresssub + 2
                        $ staminasub = staminasub - 1
                        $ thephase = 3
                        jump period
                    else:
                        mc "I studied. >Intelligence increased. >Stress increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 1
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        $ thephase = 3
                        jump period
                elif stress == 4 or stress == 5:
                    mc "I tried to study but couldn't focus... >Stress increased. >Stamina decreased."
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    $ thephase = 3
                    jump period


            label beforeSchoolExercise:
                if stress == 0 or stress == 1 or stress == 2:
                    mc "I feel stronger. >Endurance increased. >Stress increased. Stamina decreased."
                    $ staminasubfuturelim = staminasubfuturelim + 0.1
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    $ thephase = 3
                    jump period
                elif stress == 3 or stress == 4:
                    $ randExercise = renpy.random.choice([1, 2])
                    if randExercise == 1:
                        mc "I feel stronger. >Endurance increased. >Stress increased. Stamina decreased."
                        $ staminasubfuturelim = staminasubfuturelim + 0.1
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        $ thephase = 3
                        jump period
                    else:
                        mc "I'm not feeling too motivated to exercise... >Stress increased. Stamina decreased."
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        $ thephase = 3
                        jump period
                elif stress == 5:
                    mc "I'm not feeling too motivated to exercise... >Stress increased. Stamina decreased."
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    $ thephase = 3
                    jump period
                
        #PERIOD *********************************************************************************************
        label period:
            if thephase == 5:
                if issecondday:
                    "*Bell rings*"
                    jump secondDayPath1
            if thephase == 6:
                jump lunchSchool
            if thephase == 10:
                if issecondday:
                    jump secondDayPath3
                else:
                    jump afterSchool
            else:
                "*Bell rings*"
                scene img_class with Dissolve(1.0)
                jump periodChoice
            
        label periodChoice:
            
                menu:
            
                    mc "What should I do in class today?"
                    
                    "Listen to lecture":
                        jump periodLecture
                            
                    "Sleep":
                        jump periodSleep
                
                label periodLecture:
                    if stress == 0 or stress == 1:
                        mc "I listened to the lecture and learned a lot! >Intelligence vastly increased. >Stress vastly increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 3
                        $ stresssub = stresssub + 3
                        $ staminasub = staminasub - 1
                        $ thephase = thephase + 1
                        scene img_hall with Dissolve(1.0)
                        jump period
                    elif stress == 2 or stress == 3:
                        $ randLecture = renpy.random.choice([1, 2])
                        if randLecture == 1:
                            mc "I listened to the lecture and learned a lot! >Intelligence vastly increased. >Stress vastly increased. >Stamina decreased."
                            $ intelligencesub = intelligencesub + 3
                            $ stresssub = stresssub + 3
                            $ staminasub = staminasub - 1
                            $ thephase = thephase + 1
                            scene img_hall with Dissolve(1.0)
                            jump period
                        else:
                            mc "I listened to the lecture. >Intelligence increased. >Stress increased. >Stamina decreased."
                            $ intelligencesub = intelligencesub + 1
                            $ stresssub = stresssub + 1
                            $ staminasub = staminasub - 1
                            $ thephase = thephase + 1
                            scene img_hall with Dissolve(1.0)
                            jump period
                    elif stress == 4 or stress == 5:
                        mc "I tried to listen to the lecture but couldn't focus... >Stress increased. >Stamina decreased."
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        $ thephase = thephase + 1
                        scene img_hall with Dissolve(1.0)
                        jump period
                    
                label periodSleep:
                    $ randSleep = renpy.random.choice([1, 2, 3, 4, 5])
                    if randSleep == 1 or randSleep == 2 or randSleep == 3 or randSleep == 4:
                        mc "Zzz..."
                        mc "I feel somewhat rested."
                        $ thephase = thephase + 1
                        scene img_hall with Dissolve(1.0)
                        jump period
                    else:
                        mc "Zzz..."
                        te "Hey! Wake up and pay attention!"
                        mc "...!"
                        mc "Ugh. How embarassing... >Stress increased."
                        $ stresssub = stresssub + 1
                        $ thephase = thephase + 1
                        scene img_hall with Dissolve(1.0)
                        jump period
                    
                    
        #LUNCHSCHOOL *********************************************************************************************
        label lunchSchool:
            mc ">Going to lunch room."
            scene img_hall with Dissolve(1.0)
            jump lunchSchoolMealChoice
            
        label lunchSchoolMealChoice:
                
            menu:
                
                mc "I wonder what I should eat for lunch today."
                
                "Skip Lunch":
                    jump lunchSchoolSkip
                
                "$1 Bag of Chips":
                    if money <= 0:
                        mc "I don't have enough money. I guess I'll starve."
                        jump lunchSchoolSkip
                    else:
                        $ money = money - 1
                        jump lunchSchoolMin
                
                "$2 Sandwich":
                    if money <= 1:
                        mc "I don't have enough money. I guess I'll starve."
                        jump lunchSchoolSkip
                    else:
                        $ money = money - 2
                        jump lunchSchoolAvg
                    
                "$3 Combo Meal":
                    if money <= 2:
                        mc "I don't have enough money. I guess I'll starve."
                        jump lunchSchoolSkip
                    else:
                        $ money = money - 3
                        jump lunchSchoolMax
                    
            label lunchSchoolSkip:
                mc "... >stomach growls. >Stress greatly increased. >Stamina greatly decreased."
                $ stresssub = stresssub + 2
                $ staminasub = staminasub - 2
                jump lunchSchoolActionChoice
                
            label lunchSchoolMin:
                mc "That was okay."
                jump lunchSchoolActionChoice
                
            label lunchSchoolAvg:
                mc "That was good. >Stress decreased. >Stamina increased."
                $ stresssub = stresssub - 1
                $ staminasub = staminasub + 1
                jump lunchSchoolActionChoice
                
            label lunchSchoolMax:
                mc "That was delicious! >Stress greatly decreased. >Stamina greatly increased."
                $ stresssub = stresssub - 2
                $ staminasub = staminasub + 2
                jump lunchSchoolActionChoice
                
            label lunchSchoolActionChoice:
                    
                menu:
                    
                    mc "I have a bit of time before class starts again. What should I do?"
                    
                    "Socialize":
                        jump lunchSchoolSocialize
                    
                    "Study":
                        jump lunchSchoolStudy
                    
                    "Exercise":
                        jump lunchSchoolExercise
                        
                label lunchSchoolSocialize:
                
                menu:
                    
                    mc "Where should I socialize?"
                    
                    "Library":
                        jump librarySocialize
                        
                    "Teacher's Lounge":
                        jump teacherloungeSocialize
                        
                    "Lunch Room":
                        jump lunchroomSocialize
                        
                    "Gym":
                        jump gymSocialize
                        
                    "Elective Hallway":
                        jump electivehallSocialize
                    
            
                label lunchSchoolStudy:
                    if stress == 0 or stress == 1:
                        mc "I studied and understood a lot! >Intelligence greatly increased. >Stress greatly increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 2
                        $ stresssub = stresssub + 2
                        $ staminasub = staminasub - 1
                        if issecondday:
                            jump secondDayPath2
                        else:
                            $ thephase = 7
                            jump period
                    elif stress == 2 or stress == 3:
                        $ randStudy = renpy.random.choice([1, 2, 3, 4])
                        if randStudy == 1 or randStudy == 2:
                            mc "I studied and understood a lot! >Intelligence greatly increased. >Stress greatly increased. >Stamina decreased."
                            $ intelligencesub = intelligencesub + 2
                            $ stresssub = stresssub + 2
                            $ staminasub = staminasub - 1
                            if issecondday:
                                jump secondDayPath2
                            else:
                                $ thephase = 7
                                jump period
                        else:
                            mc "I studied. >Intelligence increased. >Stress increased. >Stamina decreased."
                            $ intelligencesub = intelligencesub + 1
                            $ stresssub = stresssub + 1
                            $ staminasub = staminasub - 1
                            if issecondday:
                                jump secondDayPath2
                            else:
                                $ thephase = 7
                                jump period
                    elif stress == 4 or stress == 5:
                        mc "I tried to study but couldn't focus... >Stress increased. >Stamina decreased."
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        if issecondday:
                            jump secondDayPath2
                        else:
                            $ thephase = 7
                            jump period

                    
                label lunchSchoolExercise:
                    if stress == 0 or stress == 1 or stress == 2:
                        mc "I feel stronger. >Endurance increased. >Stress increased. Stamina decreased."
                        $ staminasubfuturelim = staminasubfuturelim + 0.1
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        if issecondday:
                            jump secondDayPath2
                        else:
                            $ thephase = 7
                            jump period
                    elif stress == 3 or stress == 4:
                        $ randExercise = renpy.random.choice([1, 2])
                        if randExercise == 1:
                            mc "I feel stronger. >Endurance increased. >Stress increased. Stamina decreased."
                            $ staminasubfuturelim = staminasubfuturelim + 0.1
                            $ stresssub = stresssub + 1
                            $ staminasub = staminasub - 1
                            if issecondday:
                                jump secondDayPath2
                            else:
                                $ thephase = 7
                                jump period
                        else:
                            mc "I'm not feeling too motivated to exercise... >Stress increased. Stamina decreased."
                            $ stresssub = stresssub + 1
                            $ staminasub = staminasub - 1
                            if issecondday:
                                jump secondDayPath2
                            else:
                                $ thephase = 7
                                jump period
                    elif stress == 5:
                        mc "I'm not feeling too motivated to exercise... >Stress increased. Stamina decreased."
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        if issecondday:
                            jump secondDayPath2
                        else:
                            $ thephase = 7
                            jump period
                
        #AFTERSCHOOL ******************************************************************************************
        label afterSchool:
            mc ">After School"
            scene img_hall with Dissolve(1.0)
            if isfirstday == True:
                jump firstSchoolDayEnd
            elif stamina == 0 or stamina == 1:
                mc "I'm REALLY tired. I should head home and sleep."
                $ thephase = 11
                $ location = 2
                scene img_home with Dissolve(1.0)
                jump homeSchoolLongSleep
            elif stamina == 2 or stamina == 3:
                jump afterSchoolChoice
            elif stamina == 4 and isafterschool == True:
                jump afterSchoolChoice
            elif stamina == 4 and isafterschool == False:
                mc "Looks like the school's closing. Better get out."
                jump eveningSchool
            elif stamina == 5 and isafterschool == True:
                jump afterSchoolChoice
            elif stamina == 5 and isafterschool == False:
                mc "Looks like the school's closing. Better get out."
                jump eveningSchool
           
        label afterSchoolChoice:
                
            menu:
                
                mc "I have a bit of time before school closes. What should I do?"
                
                "Socialize":
                    jump afterSchoolSocialize
                    
                "Study":
                    jump afterSchoolStudy
                
                "Exercise":
                    jump afterSchoolExercise
                    
            label afterSchoolSocialize:
                
                menu:
                    
                    mc "Where should I socialize?"
                    
                    "Library":
                        jump librarySocialize
                        
                    "Teacher's Lounge":
                        jump teacherloungeSocialize
                        
                    "Lunch Room":
                        jump lunchroomSocialize
                        
                    "Gym":
                        jump gymSocialize
                        
                    "Elective Hallway":
                        jump electivehallSocialize
        
            label afterSchoolStudy:
                if stress == 0 or stress == 1:
                    mc "I easily studied! >Intelligence greatly increased. >Stress greatly increased. >Stamina decreased."
                    $ intelligencesub = intelligencesub + 2
                    $ stresssub = stresssub + 2
                    $ staminasub = staminasub - 1
                    if stamina == 2 or stamina == 3:
                        mc "I'm really tired. I should head home and sleep."
                        $ thephase = 11
                        $ location = 2
                        scene img_home with Dissolve(1.0)
                        jump homeSchoolRegularSleep
                    $ isafterschool = False
                    jump afterSchool
                elif stress == 2 or stress == 3:
                    $ randHomework = renpy.random.choice([1, 2])
                    if randHomework == 1:
                        mc "I easily studied! >Intelligence greatly increased. >Stress greatly increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 2
                        $ stresssub = stresssub + 2
                        $ staminasub = staminasub - 1
                        if stamina == 2 or stamina == 3:
                            mc "I'm really tired. I should head home and sleep."
                            $ thephase = 11
                            $ location = 2
                            scene img_home with Dissolve(1.0)
                            jump homeSchoolRegularSleep
                        $ isafterschool = False
                        jump afterSchool
                    else:
                        mc "I studied. >Intelligence increased. >Stress increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 1
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        if stamina == 2 or stamina == 3:
                            mc "I'm really tired. I should head home and sleep."
                            $ thephase = 11
                            $ location = 2
                            scene img_home with Dissolve(1.0)
                            jump homeSchoolRegularSleep
                        $ isafterschool = False
                        jump afterSchool
                elif stress == 4 or stress == 5:
                    mc "I tried to study but couldn't focus... >Intelligence increased. >Stress increased. >Stamina decreased."
                    $ intelligencesub = intelligencesub + 1
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    if stamina == 2:
                        mc "I'm really tired. I should head home and sleep."
                        $ thephase = 11
                        $ location = 2
                        scene img_home with Dissolve(1.0)
                        jump homeSchoolRegularSleep
                    $ isafterschool = False
                    jump afterSchool

            label afterSchoolExercise:
                if stress == 0 or stress == 1 or stress == 2:
                    mc "I feel stronger. >Endurance increased. >Stress increased. Stamina decreased."
                    $ staminasubfuturelim = staminasubfuturelim + 0.1
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    if stamina == 2:
                        mc "I'm really tired. I should head home and sleep."
                        $ thephase = 11
                        $ location = 2
                        scene img_home with Dissolve(1.0)
                        jump homeSchoolRegularSleep
                    $ isafterschool = False
                    jump afterSchool
                elif stress == 3 or stress == 4:
                    $ randExercise = renpy.random.choice([1, 2])
                    if randExercise == 1:
                        mc "I feel stronger. >Endurance increased. >Stress increased. Stamina decreased."
                        $ staminasubfuturelim = staminasubfuturelim + 0.1
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        if stamina == 2:
                            mc "I'm really tired. I should head home and sleep."
                            $ thephase = 11
                            $ location = 2
                            scene img_home with Dissolve(1.0)
                            jump homeSchoolRegularSleep
                        $ isafterschool = False
                        jump afterSchool
                    else:
                        mc "I'm not feeling too motivated to exercise... >Stress increased. Stamina decreased."
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        if stamina == 2:
                            mc "I'm really tired. I should head home and sleep."
                            $ thephase = 11
                            $ location = 2
                            scene img_home with Dissolve(1.0)
                            jump homeSchoolRegularSleep
                        $ isafterschool = False
                        jump afterSchool
                elif stress == 5:
                    mc "I'm not feeling too motivated to exercise... >Stress increased. Stamina decreased."
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    if stamina == 2:
                        mc "I'm really tired. I should head home and sleep."
                        $ thephase = 11
                        $ location = 2
                        scene img_home with Dissolve(1.0)
                        jump homeSchoolRegularSleep
                    $ isafterschool = False
                    jump afterSchool
                
        #EVENINGSCHOOL ******************************************************************************************
        label eveningSchool:
        
            scene img_nearschool with Dissolve(1.0)
            
            menu:
                
                mc "Looks like it's the evening. I wonder where I should go now."
                
                "Home":
                    jump homeSchool
                    
                "Park":
                    mc "The park's still under construction. I guess I'll head home."
                    jump homeSchool
                    
                "Town":
                    mc "The town's still under construction. I guess I'll head home."
                    jump homeSchool
                
        #HOMESCHOOL *********************************************************************************************
        label homeSchool:
            mc ">Going home."
            scene img_nearschool with Dissolve(1.0)
            $location = 2
            scene img_home with Dissolve(1.0)
            jump homeSchoolChoice
            
        label homeSchoolChoice:
        
            menu:
                
                mc "What should I do tonight?"
                
                "Study":
                    jump homeSchoolStudy
                
                "Exercise":
                    jump homeSchoolExercise
                
                "Sleep":
                    jump homeSchoolLongSleep
        
            label homeSchoolStudy:
                if stress == 0 or stress == 1:
                    mc "I easily studied! >Intelligence greatly increased. >Stress greatly increased. >Stamina decreased."
                    $ intelligencesub = intelligencesub + 2
                    $ stresssub = stresssub + 2
                    $ staminasub = staminasub - 1
                    mc "I'm really tired. I should sleep now."
                    jump homeSchoolRegularSleep
                elif stress == 2 or stress == 3:
                    $ randHomework = renpy.random.choice([1, 2])
                    if randHomework == 1:
                        mc "I easily studied! >Intelligence greatly increased. >Stress greatly increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 2
                        $ stresssub = stresssub + 2
                        $ staminasub = staminasub - 1
                        mc "I'm really tired. I should sleep now."
                        jump homeSchoolRegularSleep
                    else:
                        mc "I studied. >Intelligence increased. >Stress increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 1
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        mc "I'm really tired. I should sleep now."
                        jump homeSchoolRegularSleep
                elif stress == 4 or stress == 5:
                    mc "I tried to study but couldn't focus... >Intelligence increased. >Stress increased. >Stamina decreased."
                    $ intelligencesub = intelligencesub + 1
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    mc "I'm really tired. I should sleep now."
                    jump homeSchoolRegularSleep
            
            label homeSchoolExercise:
                label afterSchoolExercise:
                if stress == 0 or stress == 1 or stress == 2:
                    mc "I feel stronger. >Endurance increased. >Stress increased. Stamina decreased."
                    $ staminasubfuturelim = staminasubfuturelim + 0.1
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    mc "I'm really tired. I should sleep now."
                    jump homeSchoolRegularSleep
                elif stress == 3 or stress == 4:
                    $ randExercise = renpy.random.choice([1, 2])
                    if randExercise == 1:
                        mc "I feel stronger. >Endurance increased. >Stress increased. Stamina decreased."
                        $ staminasubfuturelim = staminasubfuturelim + 0.1
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        mc "I'm really tired. I should sleep now."
                        jump homeSchoolRegularSleep
                    else:
                        mc "I'm not feeling too motivated to exercise... >Stress increased. Stamina decreased."
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        mc "I'm really tired. I should sleep now."
                        jump homeSchoolRegularSleep
                elif stress == 5:
                    mc "I'm not feeling too motivated to exercise... >Stress increased. Stamina decreased."
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    mc "I'm really tired. I should sleep now."
                    jump homeSchoolRegularSleep
            
            label homeSchoolLongSleep:
                mc "ZZZ... Stamina level increased/Stress level decreased"
                $ stamina = stamina + 1
                $ stress = stress - 1
                if staminasubfuturelim % 1 > 0:
                    $ staminasub = staminasubcurrentlim
                elif staminasubfuturelim % 1 == 0:
                    $ staminasub = staminasubfuturelim
                $ thephase = 11 + 1
                scene img_home with Dissolve(1.0)
                jump startDecider
            
            label homeSchoolRegularSleep:
                mc "Zzz..."
                if staminasubfuturelim % 1 > 0:
                    $ staminasub = staminasubcurrentlim
                elif staminasubfuturelim % 1 == 0:
                    $ staminasub = staminasubfuturelim
                $ thephase = 11 + 1
                scene img_home with Dissolve(1.0)
                jump startDecider
                
        #TOWNSCHOOL **************************************************************************************************
        label choiceTown:
            mc ">Town"
            $location = 3
            scene img_1720 with Dissolve(1.0)
            jump storeChoice
                
        label storeChoice:
        
            menu:
                
                mc "What do you want to do?"
                
                "Go Shopping":
                    jump choiceShopping
                
                "Do Kareoke":
                    jump choiceKareoke
                
                "Go to an Arcade":
                    jump choiceArcade
                
                "Walk around":
                    jump choiceWalk
        
            label choiceShopping:
                
                menu:
                    
                    t "What do you want to buy?"
                    
                    "Books":
                        jump choiceBooks
                    
                    "Clothes":
                        jump choiceClothes
                    
                    "Souvenir":
                        jump choiceSouvenier
                    
                    "Electronics":
                        jump choiceElectronics
                    
                    "Office Store":
                        jump choiceOffice
                    
                    "Restaurant":
                        jump choiceRestaurant
                        
                label choiceBooks:
                    mc "Intelligence increased."
                    $ intelligence = intelligence + 1
                    $ thephase = 1
                    
                label choiceClothes:
                    mc "Charisma increased."
                    $ charisma = charisma + 1
                    $ thephase = 1
                    
                label choiceSouvenier:
                    mc "Charisma increased."
                    $ charisma = charisma + 1
                    $ thephase = 1
                    
                label choiceElectronics:
                    mc "Intelligence increased."
                    $ intelligence = intelligence + 1
                    $ thephase = 1
                        
                label choiceOffice:
                    mc "Intelligence increased."
                    $ intelligence = intelligence + 1
                    $ thephase = 1
                    
                label choiceRestaurant:
                    mc "Stamina increased."
                    $ stamina = stamina + 1
                    $ thephase = 1

                label choiceKareoke:
                    mc "Charisma increased"
                    $ charisma = charisma + 1
                    $ thephase = 1
                
                label choiceArcade:
                    mc "Stress decreased"
                    $ stress = stress - 1
                    $ thephase = 1
                
                label choiceWalk:
                    mc "Stamina increased"
                    $ stamina = stamina + 1
                    $ thephase = 1
                
        #PARKSCHOOL *********************************************************************************************************
        label choicePark:
            mc "Going to Park"
            $location = 4
            scene img_2428 with Dissolve(1.0)
            jump parkChoice
                
        label parkChoice:
        
            menu:
                
                mc "Choose an activity"
                
                "Study":
                    jump choiceStudy
                
                "Go jogging":
                    jump choiceJogging
                    
                "Relax":
                    jump choiceRelax
                
                "Socialize":
                    jump choiceSocialize
        
            label choiceStudy:
                mc "Intelligence increased"
                $ intelligence = intelligence + 1
                $ thephase = 1

            label choiceJogging:
                mc "Stamina increased"
                $ stamina = stamina + 1
                $ thephase = 1
            
            label choiceRelax:
                mc "Stress decreased"
                $ stress = stress - 1
                $ thephase = 1
            
            label choiceSocialize:
                mc "Charisma increased"
                $ charisma = charisma + 1
                $ thephase = 1
                    
    #REGULAR WEEKEND START (VARIANTS)*********************************************************************************************
    label regularWeekend:
        $ location = 2
        scene img_home with Dissolve(1.0)
        if stamina == 0 or stamina == 1:
            $ thephase = 5
            mc "...! {w} Oh no! I slept the entire day away. It's almost evening."
            $ thephase = 5 + 1
            jump regularWeekendAfternoonHome
        elif stamina == 2:
            $ thephase = 4
            mc "...! {w} Look likes I slept in. It's well into the afternoon."
            $ thephase = 4 + 1
            jump regularWeekendAfternoonHome
        elif stamina == 3:
            $ thephase = 3
            mc "...! {w} Looks like the morning is ending soon. It's almost the afternoon."
            $ thephase = 3 + 1
            jump regularWeekendMorning
        elif stamina == 4:
            $ thephase = 2
            mc "...! {w} Looks like the morning is just starting."
            $ thephase = 2 + 1
            jump regularWeekendMorning
        elif stamina == 5:
            $ thephase = 1
            mc "...! {w} I feel well rested. Looks like the sun's just rising."
            $ thephase = 1 + 1
            jump regularWeekendMorning
            
    
    #REGULAR WEEKEND MORNING *********************************************************************************************
    label regularWeekendMorning:
        
        if thephase == 4:
            
            menu:
                
                mc "Looks like it's the afternoon. I wonder if I should head out or stay home."
                
                "Home":
                    jump regularWeekendAfternoonHome
                    
                "Park":
                    mc "The park's still under construction. I guess I'll stay home."
                    jump regularWeekendAfternoonHome
                    
                "Town":
                    mc "The town's still under construction. I guess I'll stay home."
                    jump regularWeekendAfternoonHome
            
        label homeWeekendMorningChoice:
        
            menu:
                
                mc "What should I do this morning?"
                
                "Study":
                    jump regularWeekendMorningStudy
                
                "Exercise":
                    jump regularWeekendMorningExercise
                
                "Eat":
                    jump regularWeekendMorningEat
        
            label regularWeekendMorningStudy:
                if stress == 0 or stress == 1:
                    mc "I easily studied! >Intelligence greatly increased. >Stress greatly increased. >Stamina decreased."
                    $ intelligencesub = intelligencesub + 2
                    $ stresssub = stresssub + 2
                    $ staminasub = staminasub - 1
                    $ thephase = thephase + 1
                    jump regularWeekendMorning
                elif stress == 2 or stress == 3:
                    $ randHomework = renpy.random.choice([1, 2])
                    if randHomework == 1:
                        mc "I easily studied! >Intelligence greatly increased. >Stress greatly increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 2
                        $ stresssub = stresssub + 2
                        $ staminasub = staminasub - 1
                        $ thephase = thephase + 1
                        jump regularWeekendMorning
                    else:
                        mc "I studied. >Intelligence increased. >Stress increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 1
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        $ thephase = thephase + 1
                        jump regularWeekendMorning
                elif stress == 4 or stress == 5:
                    mc "I tried to study but couldn't focus... >Intelligence increased. >Stress increased. >Stamina decreased."
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    $ thephase = thephase + 1
                    jump regularWeekendMorning
            
            label regularWeekendMorningExercise:
                if stress == 0 or stress == 1 or stress == 2:
                    mc "I feel stronger. >Endurance increased. >Stress increased. Stamina decreased."
                    $ staminasubfuturelim = staminasubfuturelim + 0.1
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    $ thephase = thephase + 1
                    jump regularWeekendMorning
                elif stress == 3 or stress == 4:
                    $ randExercise = renpy.random.choice([1, 2])
                    if randExercise == 1:
                        mc "I feel stronger. >Endurance increased. >Stress increased. Stamina decreased."
                        $ staminasubfuturelim = staminasubfuturelim + 0.1
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        $ thephase = thephase + 1
                        jump regularWeekendMorning
                    else:
                        mc "I'm not feeling too motivated to exercise... >Stress increased. Stamina decreased."
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        $ thephase = thephase + 1
                        jump regularWeekendMorning
                elif stress == 5:
                    mc "I'm not feeling too motivated to exercise... >Stress increased. Stamina decreased."
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    $ thephase = thephase + 1
                    jump regularWeekendMorning
                    
            label regularWeekendMorningEat:
                mc "That was good. >Stress decreased. >Stamina increased."
                $ stresssub = stresssub - 1
                $ staminasub = staminasub + 1
                $ thephase = thephase + 1
                jump regularWeekendMorning
                
        
    #REGULAR WEEKEND AFTERNOON HOME *********************************************************************************************
    label regularWeekendAfternoonHome:
        
        if thephase == 6:
            
            menu:
                
                mc "Looks like it's the evening. I wonder if I should head out or stay home."
                
                "Home":
                    jump regularWeekendEveningHome
                    
                "Park":
                    mc "The park's still under construction. I guess I'll stay home."
                    jump regularWeekendEveningHome
                    
                "Town":
                    mc "The town's still under construction. I guess I'll stay home."
                    jump regularWeekendEveningHome
            
        label homeWeekendAfternoonChoice:
        
            menu:
                
                mc "What should I do this afternoon?"
                
                "Study":
                    jump regularWeekendAfternoonStudy
                
                "Exercise":
                    jump regularWeekendAfternoonExercise
                
                "Eat":
                    jump regularWeekendAfternoonEat
        
            label regularWeekendAfternoonStudy:
                if stress == 0 or stress == 1:
                    mc "I easily studied! >Intelligence greatly increased. >Stress greatly increased. >Stamina decreased."
                    $ intelligencesub = intelligencesub + 2
                    $ stresssub = stresssub + 2
                    $ staminasub = staminasub - 1
                    $ thephase = thephase + 1
                    jump regularWeekendAfternoonHome
                elif stress == 2 or stress == 3:
                    $ randHomework = renpy.random.choice([1, 2])
                    if randHomework == 1:
                        mc "I easily studied! >Intelligence greatly increased. >Stress greatly increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 2
                        $ stresssub = stresssub + 2
                        $ staminasub = staminasub - 1
                        $ thephase = thephase + 1
                        jump regularWeekendAfternoonHome
                    else:
                        mc "I studied. >Intelligence increased. >Stress increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 1
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        $ thephase = thephase + 1
                        jump regularWeekendAfternoonHome
                elif stress == 4 or stress == 5:
                    mc "I tried to study but couldn't focus... >Intelligence increased. >Stress increased. >Stamina decreased."
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    $ thephase = thephase + 1
                    jump regularWeekendAfternoonHome
            
            label regularWeekendAfternoonExercise:
                if stress == 1 or stress == 2 or stress == 3:
                    mc "I feel stronger. >Endurance increased. >Stress increased. Stamina decreased."
                    $ staminasubfuturelim = staminasubfuturelim + 0.1
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    $ thephase = thephase + 1
                    jump regularWeekendAfternoonHome
                elif stress == 4:
                    $ randExercise = renpy.random.choice([1, 2])
                    if randExercise == 1:
                        mc "I feel stronger. >Endurance increased. >Stress increased. Stamina decreased."
                        $ staminasubfuturelim = staminasubfuturelim + 0.1
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        $ thephase = thephase + 1
                        jump regularWeekendAfternoonHome
                    else:
                        mc "I'm not feeling too motivated to exercise... >Stress increased. Stamina decreased."
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        $ thephase = thephase + 1
                        jump regularWeekendAfternoonHome
                elif stress == 5:
                    mc "I'm not feeling too motivated to exercise... >Stress increased. Stamina decreased."
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    $ thephase = thephase + 1
                    jump regularWeekendAfternoonHome
                    
            label regularWeekendAfternoonEat:
                mc "That was good. >Stress decreased. >Stamina increased."
                $ stresssub = stresssub - 1
                $ staminasub = staminasub + 1
                $ thephase = thephase + 1
                jump regularWeekendAfternoonHome
    
    #REGULAR WEEKEND EVENING HOME *********************************************************************************************
    label regularWeekendEveningHome:
        
        if thephase == 8:
            mc "Wow! Look at the time. I should get some sleep."
            jump regularWeekendSleep
        
        label homeWeekendEveningChoice:
        
            menu:
                
                mc "What should I do this evening?"
                
                "Study":
                    jump regularWeekendEveningStudy
                
                "Exercise":
                    jump regularWeekendEveningExercise
                
                "Eat":
                    jump regularWeekendEveningEat
        
        label regularWeekendEveningStudy:
            if stress == 0 or stress == 1:
                    mc "I easily studied! >Intelligence greatly increased. >Stress greatly increased. >Stamina decreased."
                    $ intelligencesub = intelligencesub + 2
                    $ stresssub = stresssub + 2
                    $ staminasub = staminasub - 1
                    $ thephase = thephase + 1
                    jump regularWeekendEveningHome
            elif stress == 2 or stress == 3:
                $ randHomework = renpy.random.choice([1, 2])
                if randHomework == 1:
                    mc "I easily studied! >Intelligence greatly increased. >Stress greatly increased. >Stamina decreased."
                    $ intelligencesub = intelligencesub + 2
                    $ stresssub = stresssub + 2
                    $ staminasub = staminasub - 1
                    $ thephase = thephase + 1
                    jump regularWeekendEveningHome
                else:
                    mc "I studied. >Intelligence increased. >Stress increased. >Stamina decreased."
                    $ intelligencesub = intelligencesub + 1
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    $ thephase = thephase + 1
                    jump regularWeekendEveningHome
            elif stress == 4 or stress == 5:
                mc "I tried to study but couldn't focus... >Intelligence increased. >Stress increased. >Stamina decreased."
                $ stresssub = stresssub + 1
                $ staminasub = staminasub - 1
                $ thephase = thephase + 1
                jump regularWeekendEveningHome
        
        label regularWeekendEveningExercise:
            if stress == 1 or stress == 2 or stress == 3:
                mc "I feel stronger. >Endurance increased. >Stress increased. Stamina decreased."
                $ staminasubfuturelim = staminasubfuturelim + 0.1
                $ stresssub = stresssub + 1
                $ staminasub = staminasub - 1
                $ thephase = thephase + 1
                jump regularWeekendEveningHome
            elif stress == 4:
                $ randExercise = renpy.random.choice([1, 2])
                if randExercise == 1:
                    mc "I feel stronger. >Endurance increased. >Stress increased. Stamina decreased."
                    $ staminasubfuturelim = staminasubfuturelim + 0.1
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    $ thephase = thephase + 1
                    jump regularWeekendEveningHome
                else:
                    mc "I'm not feeling too motivated to exercise... >Stress increased. Stamina decreased."
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    $ thephase = thephase + 1
                    jump regularWeekendEveningHome
            elif stress == 5:
                mc "I'm not feeling too motivated to exercise... >Stress increased. Stamina decreased."
                $ stresssub = stresssub + 1
                $ staminasub = staminasub - 1
                $ thephase = thephase + 1
                jump regularWeekendEveningHome
                
        label regularWeekendEveningEat:
            mc "That was good. >Stress decreased. >Stamina increased."
            $ stresssub = stresssub - 1
            $ staminasub = staminasub + 1
            $ thephase = thephase + 1
            jump regularWeekendEveningHome
            
        label regularWeekendSleep:
            mc "Zzz..."
            if staminasubfuturelim % 1 > 0:
                $ staminasub = staminasubcurrentlim
            elif staminasubfuturelim % 1 == 0:
                $ staminasub = staminasubfuturelim
            $ thephase = 8 + 1
            if theweekday == 2:
                $ isendofweekend = True
            scene img_home
            jump startDecider