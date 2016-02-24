init python:
    def time_callback():#constantly calculate the stats
        
        if (hasattr(store, 'charismasub')):#manages charisma
            if store.charismasub == 5 or store.charismasub > 5:
                store.charismasub = 0
                store.charisma = store.charisma + 1
            elif store.charismasub == 15 or store.charismasub > 15:
                store.charismasub = 0
                store.charisma = store.charisma + 1
            elif store.charismasub == 25 or store.charismasub > 25:
                store.charismasub = 0
                store.charisma = store.charisma + 1
            elif store.charismasub == 35 or store.charismasub > 35:
                store.charismasub = 0
                store.charisma = store.charisma + 1
                
        if (hasattr(store, 'couragesub')):#manages courage
            if store.couragesub == 5 or store.couragesub > 5:
                store.couragesub = 0
                store.courage = store.courage + 1
            elif store.couragesub == 15 or store.couragesub > 15:
                store.couragesub = 0
                store.courage = store.courage + 1
            elif store.couragesub == 25 or store.couragesub > 25:
                store.couragesub = 0
                store.courage = store.courage + 1
            elif store.couragesub == 35 or store.couragesub > 35:
                store.couragesub = 0
                store.courage = store.courage + 1
                
        if (hasattr(store, 'intelligencesub')):#manages intelligence
            if store.intelligencesub == 5 or store.intelligencesub > 5:
                store.intelligencesub = 0
                store.intelligence = store.intelligence + 1
            elif store.intelligencesub == 15 or store.intelligencesub > 15:
                store.intelligencesub = 0
                store.intelligence = store.intelligence + 1
            elif store.intelligencesub == 25 or store.intelligencesub > 25:
                store.intelligencesub = 0
                store.intelligence = store.intelligence + 1
            elif store.intelligencesub == 35 or store.intelligencesub > 35:
                store.intelligencesub = 0
                store.intelligence = store.intelligence + 1
                
        if (hasattr(store, 'stamina')):#manages stamina.
            if store.stamina > 5:
                store.stamina = 5
            elif store.stamina < 1:
                store.stamina = 1
                
        if (hasattr(store, 'staminasub')):#manages stamina sublevels.
            if store.staminasub == 0 or store.staminasub < 0:
                store.staminasub = store.staminasubcurrentlim
                store.stamina = store.stamina - 1
                
        if (hasattr(store, 'stress')):#manages stress.
            if store.stress > 5:
                store.stress = 5
            elif store.stress < 1:
                store.stress = 1
                
        if (hasattr(store, 'stresssub')):#manages stress sublevels.
            if store.stresssub == 5 or store.stresssub > 5:
                store.stresssub = 0
                store.stress = store.stress + 1
                
    config.python_callbacks.append(time_callback)
    
    def statsWindow():#manages display of stats
        ui.frame(xfill=False, xminimum = None, yminimum=None, xalign=0.0, yalign = 0.0)
        ui.vbox()
        ui.text("Charisma")
        ui.bar(range=5, value=charisma, xmaximum=150)
        ui.text("Courage")
        ui.bar(range=5, value=courage, xmaximum=150)
        ui.text("Intelligence")
        ui.bar(range=5, value=intelligence, xmaximum=150)
        ui.text("Stamina")
        ui.bar(range=5, value=stamina, xmaximum=150)
        ui.text("Stress")
        ui.bar(range=5, value=stress, xmaximum=150)
        ui.close()