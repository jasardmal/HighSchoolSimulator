#Main Character
define mc = Character('You', color="#ffffff")

#Students
define mw = Character('Marc Waller', color="#c8ffc8")
define kf = Character('Kolby Frederickson', color="#c8ffc8")
define fh = Character('Frederick Hobson', color="#c8ffc8")
define ik = Character('Ivor Kovosad', color="#c8ffc8")
define dr = Character('Danny Reuter', color="#c8ffc8")
define sg = Character('Sarah Granger', color="#c8ffc8")
define cs = Character('Christina Shulz', color="#c8ffc8")
define ar = Character('Agnes Rocco', color="#c8ffc8")
define cl = Character('Cynthia Lucas', color="#c8ffc8")
define nm = Character('Natalie Mcneil', color="#c8ffc8")
define bk = Character('Becka Krakowski', color="#c8ffc8")

#Teachers
define mk = Character('Mr. Kelly', color="#c8ffc8")
define mh = Character('Mr. Hart', color="#c8ffc8")
define mg = Character('Ms. Galvin', color="#c8ffc8")
define mo = Character('Mrs. Ong', color="#c8ffc8")

define t = Character('Teacher', color="#c8ffc8")

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
    
    #Initialize Inventory
    $ inventorygeneral = ["testgen1", "testgen2", "testgen3", "testgen4", "testgen5", "testgen6", "testgen7", "testgen8", "testgen9", "testgen10"]
    $ inventorygifts = ["testgif1", "testgif2", "testgif3", "testgif4", "testgif5", "testgif6", "testgif7", "testgif8", "testgif9", "testgif10"]
    $ inventoryclothes = ["testclo1", "testclo2", "testclo3", "testclo4", "testclo5", "testclo6", "testclo7", "testclo8", "testclo9", "testclo10"]
    $ inventorybooks = ["testboo1", "testboo2", "testboo3", "testboo4", "testboo5", "testboo6", "testboo7", "testboo8", "testboo9", "testboo10"]
    
    #Initialize Stats
    $ charismasub = 0
    $ charisma = 1
    
    $ couragesub = 0
    $ courage = 1
    
    $ intelligencesub = 0
    $ intelligence = 1
    
    $ staminasub = 3
    $ staminasubcurrentlim = 5
    $ staminasubfuturelim = 5
    $ stamina = 3
    
    $ stresssub = 3
    $ stress = 3
    
    $ money = 10
    
    #Initialize Social Contacts
    $ hasmetmarc = False
    $ hasmetkolby = False
    $ hasmetfrederick = False
    $ hasmetivor = False
    $ hasmetdanny = False
    $ hasmetsarah = False
    $ hasmetchristina = False
    $ hasmetagnes = False
    $ hasmetcynthia = False
    $ hasmetnatalie = False
    $ hasmetbecka = False
    
    #Initialize Extra Actions
    $ afterSchoolExtraAction = True
    
    #START DECIDER
    label startDecider:
        if theweekday == 1:
            jump regularWeekendDay
        if theweekday == 2:
            jump regularSchoolDay
        if theweekday == 3:
            jump regularSchoolDay
        if theweekday == 4:
            jump regularSchoolDay
        if theweekday == 5:
            jump regularSchoolDay
        if theweekday == 6:
            jump regularSchoolDay
        if theweekday == 7:
            jump regularWeekendDay
    
    #REGULAR SCHOOL DAY*********************************************************************************************
    label regularSchoolDay:
        call screen input_softkeyboard
        $ location = 2
        scene img_black
        mc "It's time for school."
        scene img_1806
        jump beforeSchool
    
        #BEFORESCHOOL ******************************************************************************************
        label beforeSchool:
            mc ">Going to school."
            $ location = 1
            $ thephase = 2
            scene img_1831
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
                mc "Charisma increased"
                $ charismasub = charismasub + 1
                $ thephase = 3
                jump period
        
            label beforeSchoolStudy:
                if stress == 1 or stress == 2:
                    mc "I studied and understood a lot! >Intelligence greatly increased. >Stress greatly increased. >Stamina decreased."
                    $ intelligencesub = intelligencesub + 2
                    $ stresssub = stresssub + 2
                    $ staminasub = staminasub - 1
                    $ thephase = 3
                    jump period
                elif stress == 3:
                    $ randStudy = renpy.random.choice([1, 2, 3, 4])
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
                elif stress == 4:
                    mc "I studied. >Intelligence increased. >Stress increased. >Stamina decreased."
                    $ intelligencesub = intelligencesub + 1
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    $ thephase = 3
                    jump period
                elif stress == 5:
                    mc "I tried to study but couldn't focus... >Stress increased. >Stamina decreased."
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    $ thephase = 3
                    jump period

            label beforeSchoolExercise:
                if stress == 1 or stress == 2 or stress == 3:
                    mc "I feel stronger. >Endurance increased. >Stress increased. Stamina decreased."
                    $ staminasubfuturelim = staminasubfuturelim + 0.1
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    $ thephase = 3
                    jump period
                elif stress == 4:
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
            if thephase == 6:
                jump lunchSchool
            if thephase == 10:
                jump afterSchool
            else:
                mc ">Going to [stringphase]"
                scene img_1832
                jump periodChoice
            
        label periodChoice:
            
                menu:
            
                    mc "What should I do in class today?"
                    
                    "Listen to lecture":
                        jump periodLecture
                            
                    "Sleep":
                        jump periodSleep
                
                label periodLecture:
                    if stress == 1:
                        mc "I listened to the lecture and learned a lot! >Intelligence vastly increased. >Stress vastly increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 3
                        $ stresssub = stresssub + 3
                        $ staminasub = staminasub - 1
                        $ thephase = thephase + 1
                        scene img_1831
                        jump period
                    elif stress == 2:
                        $ randLecture = renpy.random.choice([1, 2])
                        if randLecture == 1:
                            mc "I listened to the lecture and learned a lot! >Intelligence vastly increased. >Stress vastly increased. >Stamina decreased."
                            $ intelligencesub = intelligencesub + 3
                            $ stresssub = stresssub + 3
                            $ staminasub = staminasub - 1
                            $ thephase = thephase + 1
                            scene img_1831
                            jump period
                        else:
                            mc "I listened to the lecture. >Intelligence increased. >Stress increased. >Stamina decreased."
                            $ intelligencesub = intelligencesub + 1
                            $ stresssub = stresssub + 1
                            $ staminasub = staminasub - 1
                            $ thephase = thephase + 1
                            scene img_1831
                            jump period
                    elif stress == 3:
                        mc "I listened to the lecture. >Intelligence increased. >Stress increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 1
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        $ thephase = thephase + 1
                        scene img_1831
                        jump period
                    elif stress == 4:
                        $ randLecture = renpy.random.choice([1, 2])
                        if randLecture == 1:
                            mc "I listened to the lecture. >Intelligence increased. >Stress increased. >Stamina decreased."
                            $ intelligencesub = intelligencesub + 1
                            $ stresssub = stresssub + 1
                            $ staminasub = staminasub - 1
                            $ thephase = thephase + 1
                            scene img_1831
                            jump period
                        else:
                            mc "I tried to listen to the lecture but couldn't focus... >Stress increased. >Stamina decreased."
                            $ stresssub = stresssub + 1
                            $ staminasub = staminasub - 1
                            $ thephase = thephase + 1
                            scene img_1831
                            jump period
                    elif stress == 5:
                        mc "I tried to listen to the lecture but couldn't focus... >Stress increased. >Stamina decreased."
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        $ thephase = thephase + 1
                        scene img_1831
                        jump period
                    
                label periodSleep:
                    $ randSleep = renpy.random.choice([1, 2, 3, 4, 5])
                    if randSleep == 1 or randSleep == 2 or randSleep == 3 or randSleep == 4:
                        mc "Zzz..."
                        mc "I feel somewhat rested."
                        $ thephase = thephase + 1
                        scene img_1831
                        jump period
                    else:
                        mc "Zzz..."
                        t "Hey! Wake up and pay attention!"
                        mc "...!"
                        mc "Ugh. How embarassing... >Stress increased."
                        $ stresssub = stresssub + 1
                        $ thephase = thephase + 1
                        scene img_1831
                        jump period
                    
                    
        #LUNCHSCHOOL *********************************************************************************************
        label lunchSchool:
            mc ">Going to lunch room."
            scene img_1831
            jump lunchSchoolMealChoice
            
        label lunchSchoolMealChoice:
                
            menu:
                
                mc "I wonder what I should eat for lunch today."
                
                "Skip Lunch":
                    jump lunchSchoolSkip
                
                "$1 Bag of Chips":
                    jump lunchSchoolMin
                
                "$2 Sandwich":
                    jump lunchSchoolAvg
                    
                "$3 Combo Meal":
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
                    mc "Charisma increased"
                    $ charismasub = charismasub + 1
                    $ thephase = 7
                    jump period
            
                label lunchSchoolStudy:
                    if stress == 1 or stress == 2:
                        mc "I studied and understood a lot! >Intelligence greatly increased. >Stress greatly increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 2
                        $ stresssub = stresssub + 2
                        $ staminasub = staminasub - 1
                        $ thephase = 7
                        jump period
                    elif stress == 3:
                        $ randStudy = renpy.random.choice([1, 2, 3, 4])
                        if randStudy == 1:
                            mc "I studied and understood a lot! >Intelligence greatly increased. >Stress greatly increased. >Stamina decreased."
                            $ intelligencesub = intelligencesub + 2
                            $ stresssub = stresssub + 2
                            $ staminasub = staminasub - 1
                            $ thephase = 7
                            jump period
                        else:
                            mc "I studied. >Intelligence increased. >Stress increased. >Stamina decreased."
                            $ intelligencesub = intelligencesub + 1
                            $ stresssub = stresssub + 1
                            $ staminasub = staminasub - 1
                            $ thephase = 7
                            jump period
                    elif stress == 4:
                        mc "I studied. >Intelligence increased. >Stress increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 1
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        $ thephase = 7
                        jump period
                    elif stress == 5:
                        mc "I tried to study but couldn't focus... >Stress increased. >Stamina decreased."
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        $ thephase = 7
                        jump period
                    
                label lunchSchoolExercise:
                    if stress == 1 or stress == 2 or stress == 3:
                        mc "I feel stronger. >Endurance increased. >Stress increased. Stamina decreased."
                        $ staminasubfuturelim = staminasubfuturelim + 0.1
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        $ thephase = 7
                        jump period
                    elif stress == 4:
                        $ randExercise = renpy.random.choice([1, 2])
                        if randExercise == 1:
                            mc "I feel stronger. >Endurance increased. >Stress increased. Stamina decreased."
                            $ staminasubfuturelim = staminasubfuturelim + 0.1
                            $ stresssub = stresssub + 1
                            $ staminasub = staminasub - 1
                            $ thephase = 7
                            jump period
                        else:
                            mc "I'm not feeling too motivated to exercise... >Stress increased. Stamina decreased."
                            $ stresssub = stresssub + 1
                            $ staminasub = staminasub - 1
                            $ thephase = 7
                            jump period
                    elif stress == 5:
                        mc "I'm not feeling too motivated to exercise... >Stress increased. Stamina decreased."
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        $ thephase = 7
                        jump period
                
        #AFTERSCHOOL ******************************************************************************************
        label afterSchool:
            mc ">After School"
            scene img_1831
            if stamina == 1:
                mc "I'm REALLY tired. I should head home and sleep."
                $ thephase = 11
                $ location = 2
                scene img_black
                jump homeSchoolLongSleep
            elif stamina == 2:
                mc "I have a bit of time before school closes. What should I do?"
                jump afterSchoolChoice
            elif stamina == 3 and afterSchoolExtraAction == True:
                mc "I have a bit of time before school closes. What should I do?"
                jump afterSchoolChoice
            elif stamina == 3 and afterSchoolExtraAction == False:
                mc "Looks like the school's closing. Better get out."
                jump eveningSchool
            elif stamina == 4 and afterSchoolExtraAction == True:
                mc "I have a bit of time before school closes. What should I do?"
                jump afterSchoolChoice
            elif stamina == 4 and afterSchoolExtraAction == False:
                mc "Looks like the school's closing. Better get out."
                jump eveningSchool
            elif stamina == 5 and afterSchoolExtraAction == True:
                mc "I have a bit of time before school closes. What should I do?"
                jump afterSchoolChoice
            elif stamina == 5 and afterSchoolExtraAction == False:
                mc "Looks like the school's closing. Better get out."
                jump eveningSchool
           
        label afterSchoolChoice:
                
            menu:
                
                mc "I have a bit of time before school closes. What should I do?"
                
                "Socialize":
                    jump afterSchoolSocialize
                    
                "Do homework":
                    jump afterSchoolHomework
                
                "Exercise":
                    jump afterSchoolExercise
                    
            label afterSchoolSocialize:
                mc "Charisma increased"
                $ charismasub = charismasub + 1
                $ thephase = 11
                scene img_1822
                jump afterSchool
        
            label afterSchoolHomework:
                if stress == 1 or stress == 2:
                    mc "I easily did my homework! >Intelligence greatly increased. >Stress greatly increased. >Stamina decreased."
                    $ intelligencesub = intelligencesub + 2
                    $ stresssub = stresssub + 2
                    $ staminasub = staminasub - 1
                    if stamina == 2:
                        mc "I'm really tired. I should head home and sleep."
                        $ thephase = 11
                        $ location = 2
                        scene img_black
                        jump homeSchoolRegularSleep
                    $ afterSchoolExtraAction = False
                    jump afterSchool
                elif stress == 3:
                    $ randHomework = renpy.random.choice([1, 2])
                    if randHomework == 1:
                        mc "I easily did my homework! >Intelligence greatly increased. >Stress greatly increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 2
                        $ stresssub = stresssub + 2
                        $ staminasub = staminasub - 1
                        if stamina == 2:
                            mc "I'm really tired. I should head home and sleep."
                            $ thephase = 11
                            $ location = 2
                            scene img_black
                            jump homeSchoolRegularSleep
                        $ afterSchoolExtraAction = False
                        jump afterSchool
                    else:
                        mc "I did my homework. >Intelligence increased. >Stress increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 1
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        if stamina == 2:
                            mc "I'm really tired. I should head home and sleep."
                            $ thephase = 11
                            $ location = 2
                            scene img_black
                            jump homeSchoolRegularSleep
                        $ afterSchoolExtraAction = False
                        jump afterSchool
                elif stress == 4:
                    $ randHomework = renpy.random.choice([1, 2, 3, 4])
                    if randHomework == 1 or randHomework == 2 or randHomework == 3:
                        mc "I did my homework. >Intelligence increased. >Stress increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 1
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        if stamina == 2:
                            mc "I'm really tired. I should head home and sleep."
                            $ thephase = 11
                            $ location = 2
                            scene img_black
                            jump homeSchoolRegularSleep
                        $ afterSchoolExtraAction = False
                        jump afterSchool
                    else:
                        mc "I tried to do my homework but couldn't figure it out... >Intelligence increased. >Stress increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 1
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        if stamina == 2:
                            mc "I'm really tired. I should head home and sleep."
                            $ thephase = 11
                            $ location = 2
                            scene img_black
                            jump homeSchoolRegularSleep
                        $ afterSchoolExtraAction = False
                        jump afterSchool
                elif stress == 5:
                    mc "I tried to do my homework but couldn't figure it out... >Stress increased. >Stamina decreased."
                    $ intelligencesub = intelligencesub + 1
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    if stamina == 2:
                        mc "I'm really tired. I should head home and sleep."
                        $ thephase = 11
                        $ location = 2
                        scene img_black
                        jump homeSchoolRegularSleep
                    $ afterSchoolExtraAction = False
                    jump afterSchool

            label afterSchoolExercise:
                if stress == 1 or stress == 2 or stress == 3:
                    mc "I feel stronger. >Endurance increased. >Stress increased. Stamina decreased."
                    $ staminasubfuturelim = staminasubfuturelim + 0.1
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    if stamina == 2:
                        mc "I'm really tired. I should head home and sleep."
                        $ thephase = 11
                        $ location = 2
                        scene img_black
                        jump homeSchoolRegularSleep
                    $ afterSchoolExtraAction = False
                    jump afterSchool
                    
                elif stress == 4:
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
                            scene img_black
                            jump homeSchoolRegularSleep
                        $ afterSchoolExtraAction = False
                        jump afterSchool
                        
                    else:
                        mc "I'm not feeling too motivated to exercise... >Stress increased. Stamina decreased."
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        if stamina == 2:
                            mc "I'm really tired. I should head home and sleep."
                            $ thephase = 11
                            $ location = 2
                            scene img_black
                            jump homeSchoolRegularSleep
                        $ afterSchoolExtraAction = False
                        jump afterSchool
                        
                elif stress == 5:
                    mc "I'm not feeling too motivated to exercise... >Stress increased. Stamina decreased."
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    if stamina == 2:
                        mc "I'm really tired. I should head home and sleep."
                        $ thephase = 11
                        $ location = 2
                        scene img_black
                        jump homeSchoolRegularSleep
                    $ afterSchoolExtraAction = False
                    jump afterSchool
                
        #EVENINGSCHOOL ******************************************************************************************
        while True:
            label eveningSchool:
                $ thephase = 11
                scene img_1822
                mc "It's getting pretty late. I wonder where I should go now? (Check Map)"
                
        #HOMESCHOOL *********************************************************************************************
        label homeSchool:
            mc ">Going home."
            scene img_1806
            $location = 2
            scene img_black
            jump homeSchoolChoice
            
        label homeSchoolChoice:
        
            menu:
                
                mc "What should I do tonight?"
                
                "Do homework":
                    jump homeSchoolHomework
                
                "Exercise":
                    jump homeSchoolExercise
                
                "Sleep":
                    jump homeSchoolLongSleep
        
            label homeSchoolHomework:
                if stress == 1 or stress == 2:
                    mc "I easily did my homework! >Intelligence greatly increased. >Stress greatly increased. >Stamina decreased."
                    $ intelligencesub = intelligencesub + 2
                    $ stresssub = stresssub + 2
                    $ staminasub = staminasub - 1
                    mc "I'm really tired. I should sleep now."
                    jump homeSchoolRegularSleep
                elif stress == 3:
                    $ randHomework = renpy.random.choice([1, 2])
                    if randHomework == 1:
                        mc "I easily did my homework! >Intelligence greatly increased. >Stress greatly increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 2
                        $ stresssub = stresssub + 2
                        $ staminasub = staminasub - 1
                        mc "I'm really tired. I should sleep now."
                        jump homeSchoolRegularSleep
                    else:
                        mc "I did my homework. >Intelligence increased. >Stress increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 1
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        mc "I'm really tired. I should sleep now."
                        jump homeSchoolRegularSleep
                elif stress == 4:
                    $ randHomework = renpy.random.choice([1, 2, 3, 4])
                    if randHomework == 1 or randHomework == 2 or randHomework == 3:
                        mc "I did my homework. >Intelligence increased. >Stress increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 1
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        mc "I'm really tired. I should sleep now."
                        jump homeSchoolRegularSleep
                    else:
                        mc "I tried to do my homework but couldn't figure it out... >Intelligence increased. >Stress increased. >Stamina decreased."
                        $ intelligencesub = intelligencesub + 1
                        $ stresssub = stresssub + 1
                        $ staminasub = staminasub - 1
                        mc "I'm really tired. I should sleep now."
                        jump homeSchoolRegularSleep
                elif stress == 5:
                    mc "I tried to do my homework but couldn't figure it out... >Stress increased. >Stamina decreased."
                    $ intelligencesub = intelligencesub + 1
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    mc "I'm really tired. I should sleep now."
                    jump homeSchoolRegularSleep
            
            label homeSchoolExercise:
                label afterSchoolExercise:
                if stress == 1 or stress == 2 or stress == 3:
                    mc "I feel stronger. >Endurance increased. >Stress increased. Stamina decreased."
                    $ staminasubfuturelim = staminasubfuturelim + 0.1
                    $ stresssub = stresssub + 1
                    $ staminasub = staminasub - 1
                    mc "I'm really tired. I should sleep now."
                    jump homeSchoolRegularSleep
                elif stress == 4:
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
                $ staminasubcurrentlim = staminasubfuturelim
                $ thephase = 11 + 1
                scene img_black
                jump startDecider
            
            label homeSchoolRegularSleep:
                mc "Zzz..."
                $ staminasubcurrentlim = staminasubfuturelim
                $ thephase = 11 + 1
                scene img_black
                jump startDecider
                
        #TOWNSCHOOL **************************************************************************************************
        label choiceTown:
            mc ">Town"
            $location = 3
            scene img_1720
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
            scene img_2428
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
                    
    #REGULAR WEEKEND DAY*********************************************************************************************
    label regularWeekendDay:
        $ location = 2
        scene img_black
        mc "It's the weekend."
        scene img_1806
        $ thephase = thephase + 1
        jump startDecider