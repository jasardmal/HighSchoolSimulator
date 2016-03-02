init python:
    def time_callback():#constantly calculate the stats
        
        if (hasattr(store, 'charismasub')):#manages charisma
            if store.charismasub == 10 or store.charismasub > 10:
                store.charismasub = 0
                store.charismasubmax = 20
                store.charisma = store.charisma + 1
            elif store.charismasub == 20 or store.charismasub > 20:
                store.charismasub = 0
                store.charismasubmax = 40
                store.charisma = store.charisma + 1
            elif store.charismasub == 40 or store.charismasub > 40:
                store.charismasub = 0
                store.charismasubmax = 80
                store.charisma = store.charisma + 1
            elif store.charismasub == 80 or store.charismasub > 80:
                store.charismasub = 0
                store.charismasubmax = 160
                store.charisma = store.charisma + 1
            elif store.charismasub == 160 or store.charismasub > 160:
                store.charismasub = 0
                store.charisma = store.charisma + 1
                
        if (hasattr(store, 'couragesub')):#manages courage
            if store.couragesub == 10 or store.couragesub > 10:
                store.couragesub = 0
                store.couragesubmax = 20
                store.courage = store.courage + 1
            elif store.couragesub == 20 or store.couragesub > 20:
                store.couragesub = 0
                store.couragesubmax = 40
                store.courage = store.courage + 1
            elif store.couragesub == 40 or store.couragesub > 40:
                store.couragesub = 0
                store.couragesubmax = 80
                store.courage = store.courage + 1
            elif store.couragesub == 80 or store.couragesub > 80:
                store.couragesub = 0
                store.couragesubmax = 160
                store.courage = store.courage + 1
            elif store.couragesub == 160 or store.couragesub > 160:
                store.couragesub = 0
                store.courage = store.courage + 1
                
        if (hasattr(store, 'intelligencesub')):#manages intelligence
            if store.intelligencesub == 10 or store.intelligencesub > 10:
                store.intelligencesub = 0
                store.intelligencesubmax = 20
                store.intelligence = store.intelligence + 1
            elif store.intelligencesub == 20 or store.intelligencesub > 20:
                store.intelligencesub = 0
                store.intelligencesubmax = 40
                store.intelligence = store.intelligence + 1
            elif store.intelligencesub == 40 or store.intelligencesub > 40:
                store.intelligencesub = 0
                store.intelligencesubmax = 80
                store.intelligence = store.intelligence + 1
            elif store.intelligencesub == 80 or store.intelligencesub > 80:
                store.intelligencesub = 0
                store.intelligencesubmax = 160
                store.intelligence = store.intelligence + 1
            elif store.intelligencesub == 160 or store.intelligencesub > 160:
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
            elif store.staminasub == store.staminasubcurrentlim or store.staminasub > store.staminasubcurrentlim:
                store.staminasub = 0
                store.stamina = store.stamina + 1
                
        if (hasattr(store, 'stress')):#manages stress.
            if store.stress > 5:
                store.stress = 5
            elif store.stress < 1:
                store.stress = 1
                
        if (hasattr(store, 'stresssub')):#manages stress sublevels.
            if store.stresssub == 5 or store.stresssub > 5:
                store.stresssub = 0
                store.stress = store.stress + 1
            elif store.stresssub == 0 or store.stresssub < 0:
                store.stressub = 5
                store.stress = store.stress - 1
                
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