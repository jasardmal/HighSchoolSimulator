init python:
    def time_callback():#constantly calculate the stats
        
        if (hasattr(store, 'charismasub')):#manages charisma
            if store.charismasub == 5:
                store.charismasub = 0
                store.charisma = store.charisma + 1
            elif store.charismasub == 15:
                store.charismasub = 0
                store.charisma = store.charisma + 1
            elif store.charismasub == 25:
                store.charismasub = 0
                store.charisma = store.charisma + 1
            elif store.charismasub == 35:
                store.charismasub = 0
                store.charisma = store.charisma + 1
            elif store.charismasub == 45:
                store.charismasub = 0
                store.charisma = store.charisma + 1
                
        if (hasattr(store, 'couragesub')):#manages courage
            if store.couragesub == 5:
                store.couragesub = 0
                store.courage = store.courage + 1
            elif store.couragesub == 15:
                store.couragesub = 0
                store.courage = store.courage + 1
            elif store.couragesub == 25:
                store.couragesub = 0
                store.courage = store.courage + 1
            elif store.couragesub == 35:
                store.couragesub = 0
                store.courage = store.courage + 1
            elif store.couragesub == 45:
                store.couragesub = 0
                store.courage = store.courage + 1
                
        if (hasattr(store, 'intelligencesub')):#manages intelligence
            if store.intelligencesub == 5:
                store.intelligencesub = 0
                store.intelligence = store.intelligence + 1
            elif store.intelligencesub == 15:
                store.intelligencesub = 0
                store.intelligence = store.intelligence + 1
            elif store.intelligencesub == 25:
                store.intelligencesub = 0
                store.intelligence = store.intelligence + 1
            elif store.intelligencesub == 35:
                store.intelligencesub = 0
                store.intelligence = store.intelligence + 1
            elif store.intelligencesub == 45:
                store.intelligencesub = 0
                store.intelligence = store.intelligence + 1
                
        if (hasattr(store, 'staminasub')):#manages stamina
            if store.staminasub == 0 or store.staminasub < 0:
                store.staminasub = store.staminasubcurrentlim
                store.stamina = store.stamina - 1
                
        if (hasattr(store, 'stresssub')):#manages stress
            if store.stresssub == 5:
                store.stresssub = 0
                store.stress = store.stress + 1
                
    config.python_callbacks.append(time_callback)