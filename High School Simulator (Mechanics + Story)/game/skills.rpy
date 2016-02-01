init python:
def time_callback():#constantly calculate the stats
        
        if (hasattr(store, 'spanishskillsub')):#manages spanish
            if store.spanishskillsub == 5 or store.spanishskillsub > 5:
                store.spanishskillsub = 0
                store.spanishskill = store.spanishskill + 1
            elif store.spanishskillsub == 15 or store.spanishskillsub > 15:
                store.spanishskillsub = 0
                store.spanishskill = store.spanishskill + 1
            elif store.spanishskillsub == 25 or store.spanishskillsub > 25:
                store.spanishskillsub = 0
                store.spanishskill = store.spanishskill + 1
            elif store.spanishskillsub == 35 or store.spanishskillsub > 35:
                store.spanishskillsub = 0
                store.spanishskill = store.spanishskill + 1
                
        if (hasattr(store, 'frenchskillsub')):#manages french
            if store.frenchskillsub == 5 or frenchskillsub > 5:
                store.frenchskillsub = 0
                store.frenchskill = store.frenchskill + 1
            elif store.frenchskillsub == 15 or store.frenchskillsub > 15:
                store.frenchskillsub = 0
                store.frenchskill = store.frenchskill + 1
            elif store.frenchskillsub == 25 or store.frenchskillsub > 25:
                store.frenchskillsub = 0
                store.frenchskill = store.frenchskill + 1
            elif store.frenchskillsub == 35 or store.frenchskillsub > 35:
                store.frenchskillsub = 0
                store.frenchskill = store.frenchskill + 1
                
        if (hasattr(store, 'latinskillsub')):#manages latin
            if store.latinskillsub == 5 or store.latinskillsub > 5:
                store.latinskillsub = 0
                store.latinskill = store.latinskill + 1
            elif store.latinskillsub == 15 or store.latinskillsub > 15:
                store.latinskillsub = 0
                store.latinskill = store.latinskill + 1
            elif store.latinskillsub == 25 or store.latinskillsub > 25:
                store.latinskillsub = 0
                store.latinskill = store.latinskill + 1
            elif store.latinskillsub == 35 or store.latinskillsub > 35:
                store.latinskillsub = 0
                store.latinskill = store.latinskill + 1
                
        if (hasattr(store, 'artskillsub')):#manages art
            if store.artskillsub == 5 or store.artskillsub > 5:
                store.artskillsub = 0
                store.artskill = store.artskill + 1
            elif store.artskillsub == 15 or store.artskillsub > 15:
                store.artskillsub = 0
                store.artskill = store.artskill + 1
            elif store.artskillsub == 25 or store.artskillsub > 25:
                store.artskillsub = 0
                store.artskill = store.artskill + 1
            elif store.artskillsub == 35 or store.artskillsub > 35:
                store.artskillsub = 0
                store.artskill = store.artskill + 1
                
        if (hasattr(store, 'musicskillsub')):#manages music
            if store.musicskillsub == 5 or store.musicskillsub > 5:
                store.musicskillsub = 0
                store.musicskill = store.musicskill + 1
            elif store.musicskillsub == 15 or store.musicskillsub > 15:
                store.musicskillsub = 0
                store.musicskill = store.musicskill + 1
            elif store.musicskillsub == 25 or store.musicskillsub > 25:
                store.musicskillsub = 0
                store.musicskill = store.musicskill + 1
            elif store.musicskillsub == 35 or store.musicskillsub > 35:
                store.musicskillsub = 0
                store.musicskill = store.musicskill + 1
                
        if (hasattr(store, 'peskillsub')):#manages pe
            if store.peskillsub == 5 or store.peskillsub > 5:
                store.peskillsub = 0
                store.peskill = store.peskill + 1
            elif store.peskillsub == 15 or store.peskillsub > 15:
                store.peskillsub = 0
                store.peskill = store.peskill + 1
            elif store.peskillsub == 25 or store.peskillsub > 25:
                store.peskillsub = 0
                store.peskill = store.peskill + 1
            elif store.peskillsub == 35 or store.peskillsub > 35:
                store.peskillsub = 0
                store.peskill = store.peskill + 1
                
        if (hasattr(store, 'financeskillsub')):#manages finance
            if store.financeskillsub == 5 or store.financeskillsub > 5:
                store.financeskillsub = 0
                store.financeskill = store.financeskill + 1
            elif store.financeskillsub == 15 or store.financeskillsub > 15:
                store.financeskillsub = 0
                store.financeskill = store.financeskill + 1
            elif store.financeskillsub == 25 or store.financeskillsub > 25:
                store.financeskillsub = 0
                store.financeskill = store.financeskill + 1
            elif store.financeskillsub == 35 or store.financeskillsub > 35:
                store.financeskillsub = 0
                store.financeskill = store.financeskill + 1
                
        if (hasattr(store, 'programmingskillsub')):#manages programming
            if store.programmingskillsub == 5 or store.programmingskillsub > 5:
                store.programmingskillsub = 0
                store.programmingskill = store.programmingskill + 1
            elif store.programmingskillsub == 15 or store.programmingskillsub > 15:
                store.programmingskillsub = 0
                store.programmingskill = store.programmingskill + 1
            elif store.programmingskillsub == 25 or store.programmingskillsub > 25:
                store.programmingskillsub = 0
                store.programmingskill = store.programmingskill + 1
            elif store.programmingskillsub == 35 or store.programmingskillsub > 35:
                store.programmingskillsub = 0
                store.programmingskill = store.programmingskill + 1
                
        if (hasattr(store, 'homeecskillsub')):#manages home ec
            if store.homeecskillsub == 5 or store.homeecskillsub > 5:
                store.homeecskillsub = 0
                store.homeecskill = store.homeecskill + 1
            elif store.homeecskillsub == 15 or store.homeecskillsub > 15:
                store.homeecskillsub = 0
                store.homeecskill = store.homeecskill + 1
            elif store.homeecskillsub == 25 or store.homeecskillsub > 25:
                store.homeecskillsub = 0
                store.homeecskill = store.homeecskill + 1
            elif store.homeecskillsub == 35 or store.homeecskillsub > 35:
                store.homeecskillsub = 0
                store.homeecskill = store.homeecskill + 1
        
    #Refer to stats.rpy in making the skill progression formula.
        
config.python_callbacks.append(time_callback)