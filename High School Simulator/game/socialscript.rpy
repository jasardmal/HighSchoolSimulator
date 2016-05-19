    label librarySocialize:
        $ randSocialize = renpy.random.choice([1, 2, 3, 4])
        if randSocialize == 1:
            if hasmetagnes == True:
                show agnesr with moveinbottom
                $ charismasub = charismasub + 1
                $ agnesprogression = agnesprogression + 1
                mc "I socialized with Agnes. >Charisma increased."
                hide agnesr
                jump timePass
            else:
                jump failtoSocialize
        elif randSocialize == 2:
            if hasmetbecka == True:
                show beckak with moveinbottom
                $ charismasub = charismasub + 1
                $ beckaprogression = beckaprogression + 1
                mc "I socialized with Becka. >Charisma increased."
                hide beckak
                jump timePass
            else:
                jump failtoSocialize
        elif randSocialize == 3:
            if hasmetdanny == True:
                show dannyr with moveinbottom
                $ charismasub = charismasub + 1
                $ dannyprogression = dannyprogression + 1
                mc "I socialized with Danny. >Charisma increased."
                hide dannyr
                jump timePass
            else:
                jump failtoSocialize
        else:
            jump failtoSocialize
        
    label teacherloungeSocialize:
        $ randSocialize = renpy.random.choice([1, 2, 3])
        if randSocialize == 1:
            if hasmetfrederick == True:
                show frederickh with moveinbottom
                $ charismasub = charismasub + 1
                $ frederickprogression = frederickprogression + 1
                mc "I socialized with Frederick. >Charisma increased."
                hide frederickh
                jump timePass
            else:
                jump failtoSocialize
        elif randSocialize == 2:
            if hasmetbecka == True:
                show beckak with moveinbottom
                $ charismasub = charismasub + 1
                $ beckaprogression = beckaprogression + 1
                mc "I socialized with Becka. >Charisma increased."
                hide beckak
                jump timePass
            else:
                jump failtoSocialize
        else:
            jump failtoSocialize
        
    label lunchroomSocialize:
        $ randSocialize = renpy.random.choice([1, 2, 3, 4, 5])
        if randSocialize == 1:
            if hasmetivor == True:
                #show ivork with moveinbottom
                $ charismasub = charismasub + 1
                $ ivorprogression = ivorprogression + 1
                mc "I socialized with Ivor. >Charisma increased."
                #hide ivork
                jump timePass
            else:
                jump failtoSocialize
        elif randSocialize == 2:
            if hasmetagnes == True:
                show agnesr with moveinbottom
                $ charismasub = charismasub + 1
                $ agnesprogression = agnesprogression + 1
                mc "I socialized with Agnes. >Charisma increased."
                hide agnesr
                jump timePass
            else:
                jump failtoSocialize
        elif randSocialize == 3:
            if hasmetsarah == True:
                show sarahg with moveinbottom
                $ charismasub = charismasub + 1
                $ sarahprogression = sarahprogression + 1
                mc "I socialized with Sarah. >Charisma increased."
                hide sarahg
                jump timePass
            else:
                jump failtoSocialize
        elif randSocialize == 4:
            if hasmetmarc == True:
                show marcw with moveinbottom
                $ charismasub = charismasub + 1
                $ marcprogression = marcprogression + 1
                mc "I socialized with Marc. >Charisma increased."
                hide marcw
                jump timePass
            else:
                jump failtoSocialize
        else:
            jump failtoSocialize
        
    label gymSocialize:
        $ randSocialize = renpy.random.choice([1, 2, 3, 4, 5])
        if randSocialize == 1:
            if hasmetkolby == True:
                #show kolbyf with moveinbottom
                $ charismasub = charismasub + 1
                $ kolbyprogression = kolbyprogression + 1
                mc "I socialized with Kolby. >Charisma increased."
                #hide kolbyf
                jump timePass
            else:
                jump failtoSocialize
        elif randSocialize == 2:
            if hasmetcynthia == True:
                #show cynthial with moveinbottom
                $ charismasub = charismasub + 1
                $ cynthiaprogression = cynthiaprogression + 1
                mc "I socialized with Cynthia. >Charisma increased."
                #hide cynthial
                jump timePass
            else:
                jump failtoSocialize
        elif randSocialize == 3:
            if hasmetsarah == True:
                show sarahg with moveinbottom
                $ charismasub = charismasub + 1
                $ sarahprogression = sarahprogression + 1
                mc "I socialized with Sarah. >Charisma increased."
                hide sarahg
                jump timePass
            else:
                jump failtoSocialize
        elif randSocialize == 4:
            if hasmetmarc == True:
                show marcw with moveinbottom
                $ charismasub = charismasub + 1
                $ marcprogression = marcprogression + 1
                mc "I socialized with Marc. >Charisma increased."
                hide marcw
                jump timePass
            else:
                jump failtoSocialize
        else:
            jump failtoSocialize
        
    label electivehallSocialize:
        $ randSocialize = renpy.random.choice([1, 2, 3, 4])
        if randSocialize == 1:
            if hasmetnatalie == True:
                #show nataliem with moveinbottom
                $ charismasub = charismasub + 1
                $ natalieprogression = natalieprogression + 1
                mc "I socialized with Natalie. >Charisma increased."
                #hide nataliem
                jump timePass
            else:
                jump failtoSocialize
        elif randSocialize == 2:
            if hasmetchristina == True:
                #show christinal with moveinbottom
                $ charismasub = charismasub + 1
                $ christinaprogression = christinaprogression + 1
                mc "I socialized with Christina. >Charisma increased."
                #hide christinal
                jump timePass
            else:
                jump failtoSocialize
        elif randSocialize == 3:
            if hasmetivor == True:
                #show ivork with moveinbottom
                $ charismasub = charismasub + 1
                $ ivorprogression = ivorprogression + 1
                mc "I socialized with Ivor. >Charisma increased."
                #hide ivork
                jump timePass
            else:
                jump failtoSocialize
        else:
            jump failtoSocialize
        
    label failtoSocialize:
        mc "Nobody showed up."
        jump timePass
    
    label timePass:
        if thephase == 2:
            $ thephase = 3
            jump period
        if thephase == 6:
            $ thephase = 7
            jump period
        if thephase == 10:
            $ isafterschool = False
            jump 