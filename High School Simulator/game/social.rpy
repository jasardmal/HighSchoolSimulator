init python:
    def time_callback():#constantly calculate the stats
        
        if(hasattr(store, 'marcprogression')):#manages marc's social progression
            if store.marcprogression < 0:
                store.marcprogression = 0
            elif store.marcprogression == 10:
                store.marcprogression = 0
                store.marcrank = store.marcrank + 1
        
        if(hasattr(store, 'frederickprogression')):#manages marc's social progression
            if store.frederickprogression < 0:
                store.frederickprogression = 0
            elif store.frederickprogression == 10:
                store.frederickprogression = 0
                store.frederickrank = store.frederickrank + 1
                
        if(hasattr(store, 'sarahprogression')):#manages sarah's social progression
            if store.sarahprogression < 0:
                store.sarahprogression = 0
            elif store.sarahprogression == 10:
                store.sarahprogression = 0
                store.sarahrank = store.sarahrank + 1
                
        if(hasattr(store, 'agnesprogression')):#manages agnes's social progression
            if store.agnesprogression < 0:
                store.agnesprogression = 0
            elif store.agnesprogression == 10:
                store.agnesprogression = 0
                store.agnesrank = store.agnesrank + 1
                
        if(hasattr(store, 'natalieprogression')):#manages natalie's social progression
            if store.natalieprogression < 0:
                store.natalieprogression = 0
            elif store.natalieprogression == 10:
                store.natalieprogression = 0
                store.natalierank = store.natalierank + 1
                
        if(hasattr(store, 'beckaprogression')):#manages becka's social progression
            if store.beckaprogression < 0:
                store.beckaprogression = 0
            elif store.beckaprogression == 10:
                store.beckaprogression = 0
                store.beckarank = store.beckarank + 1
        
    config.python_callbacks.append(time_callback)