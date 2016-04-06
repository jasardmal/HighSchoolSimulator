init python:
    def time_callback():#constantly calculate the stats
        
        if(hasattr(store, 'marcprogression')):#manages marc's social progression
            if store.marcprogression < 0:
                store.marcprogression = 0
            elif store.marcprogression == 10:
                store.marcprogression = 0
                store.marcrank = store.marcrank + 1
        
    config.python_callbacks.append(time_callback)