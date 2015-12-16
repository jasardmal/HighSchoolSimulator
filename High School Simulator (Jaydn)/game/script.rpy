define t = Character('Generic Activity', color="#c8ffc8")
define l = Character('Location Change', color = "#c8ffc8")

label start:
    
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
    $ thephase = 2#morning, the phase of the day, this automatically changes but must be initially assigned
    $ stringphase = "Morning"#2, the phase of the day, this automatically changes but must be initially assigned
    $ location = 2
    $ stringlocation = "School"
    
    #Stats to code intelligence, charisma, stamina, mental
    $ intellegence = 0
    $ charisma = 0
    $ stress = 0
    $ stamina = 0

    scene img_1831
    
    while True: #loops the choice system forever
        
        if theweekday >= 2 and theweekday <= 6:
        
            menu: #displays buttons for choices of location
                
                l "Choose a Location"
                
                "Home":
                    jump choiceHome
                    
                "School":
                    jump choiceSchool
                    
            
            label choiceHome:
                l "Going Home"
                $location = 1
                scene img_1802
                jump locationDone
                
            label choiceSchool:
                l "Going to School"
                $location = 2
                scene img_1831
                jump locationDone
                
            label locationDone:
                
        else:
                
            menu: #displays buttons for choices of location
                    
                    l "Choose a Location"
                    
                    "Home":
                        jump choiceHome
                        
                    "School":
                        jump choiceSchool
                        
                    "Town":
                        jump choiceTown
                        
                    "Park":
                        jump choicePark
                        
                        
            label choiceHome:
                    l "Going Home"
                    $location = 1
                    scene img_1802
                    jump locationDone
                    
            label choiceSchool:
                    l "Going to School"
                    $location = 2
                    scene img_1831
                    jump locationDone
                    
            label choiceTown:
                    l "Going into Town"
                    $location = 3
                    scene img_1720
                    jump locationDone
                    
            label choicePark:
                    l "Going to the Park"
                    $location = 4
                    scene img_1822
                    jump locationDone
                    
            label locationDone:
                
            
            #HOME *********************************************************************************************
            
            
            if location == 1:
            
                menu:
                    
                    t "Choose an activity"
                    
                    "Study":
                        jump choiceIntellegence
                    
                    "Apply Makeup":
                        jump choiceCharisma
                    
                    "Work out":
                        jump choiceStamina
                    
                    "Sleep":
                        jump choiceStress
                    
                #i need you to make a loop for the above.
            
                label choiceIntellegence:
                    t "Intellegence increased"
                    $ intellegence = intellegence + 1
                    $ thephase = thephase + 1
                    jump done


                label choiceCharisma:
                    t "Charisma increased"
                    $ charisma = charisma + 1
                    $ thephase = thephase + 1
                    jump done
                
                
                label choiceStamina:
                    t "Stamina increased"
                    $ stamina = stamina + 1
                    $ thephase = thephase + 1
                    jump done
                
                
                label choiceStress:
                    t "Stress increased"
                    $ stress = stress + 1
                    $ thephase = thephase + 1
                    jump done
                    
                    
                label done:
                    
                    
                    #SCHOOL ******************************************************************************************
                    
                    
            if location == 2:
            
                menu:
                    
                    t "Choose an activity"
                    
                    "Do homework":
                        jump choiceIntellegence
                    
                    "Flirt":
                        jump choiceCharisma
                    
                    "Run laps":
                        jump choiceStamina
                    
                    "Go to class":
                        jump choiceStress
                    
                #i need you to make a loop for the above.
            
                label choiceIntellegence:
                    t "Intellegence increased"
                    $ intellegence = intellegence + 1
                    $ thephase = thephase + 1
                    jump done


                label choiceCharisma:
                    t "Charisma increased"
                    $ charisma = charisma + 1
                    $ thephase = thephase + 1
                    jump done
                
                
                label choiceStamina:
                    t "Stamina increased"
                    $ stamina = stamina + 1
                    $ thephase = thephase + 1
                    jump done
                
                
                label choiceStress:
                    t "Stress increased"
                    $ stress = stress + 1
                    $ thephase = thephase + 1
                    jump done
                    
                    
                label done:
                    
                    
                    #STORE **************************************************************************************************
                    
                
            if location == 3:
            
                menu:
                    
                    t "What do you want to do?"
                    
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
                        t "Intellegence increased."
                        $ intellegence = intellegence + 1
                        $ thephase = thephase + 1
                        jump done
                        
                    label choiceClothes:
                        t "Charisma increased."
                        $ charisma = charisma + 1
                        $ thephase = thephase + 1
                        jump done
                        
                    label choiceSouvenier:
                        t "Charisma increased."
                        $ charisma = charisma + 1
                        $ thephase = thephase + 1
                        jump done
                        
                    label choiceElectronics:
                        t "Intellegence increased."
                        $ intellegence = intellegence + 1
                        $ thephase = thephase + 1
                        jump done
                            
                    label choiceOffice:
                        t "Intellegence increased."
                        $ intellegence = intellegence + 1
                        $ thephase = thephase + 1
                        jump done
                        
                    label choiceRestaurant:
                        t "Stamina increased."
                        $ stamina = stamina + 1
                        $ thephase = thephase + 1
                        jump done
                        
                    label done:

                    jump done


                label choiceKareoke:
                    t "Charisma increased"
                    $ charisma = charisma + 1
                    $ thephase = thephase + 1
                    jump done
                
                
                label choiceArcade:
                    t "Stress decreased"
                    $ stress = stress - 1
                    $ thephase = thephase + 1
                    jump done
                
                
                label choiceWalk:
                    t "Stamina increased"
                    $ stamina = stamina + 1
                    $ thephase = thephase + 1
                    jump done
                    
                    
                label done:
                    
                    
                    #PARK *********************************************************************************************************
                    
                    
            if location == 4:
            
                menu:
                    
                    t "Choose an activity"
                    
                    "Study":
                        jump choiceStudy
                    
                    "Go jogging":
                        jump choiceJogging
                        
                    "Relax":
                        jump choiceRelax
                    
                    "Socialize":
                        jump choiceSocialize
                    
                #i need you to make a loop for the above.
            
                label choiceStudy:
                    t "Intellegence increased"
                    $ intellegence = intellegence + 1
                    $ thephase = thephase + 1
                    jump done


                label choiceJogging:
                    t "Stamina increased"
                    $ stamina = stamina + 1
                    $ thephase = thephase + 1
                    jump done
                
                
                label choiceRelax:
                    t "Stress decreased"
                    $ stress = stress - 1
                    $ thephase = thephase + 1
                    jump done
                
                
                label choiceSocialize:
                    t "Charisma increased"
                    $ charisma = charisma + 1
                    $ thephase = thephase + 1
                    jump done
                    
                    
                label done:
            
        