###############################################################################
## Inventory
##
## Screens that allows the user to read/view item descriptions of respective 
## categories.
#screen genitem1:
    
#    # This ensures that any other menu screen is replaced.
#    tag menu
    
#    # The background of the game menu.
#    window:
#        style "gm_root"
        
#    # The item description
#    frame:
        
#        xalign 0.5
#        yalign 0
        
#        has hbox
        
#        text "Test General Item Description1"
        
#    # The return button.
#    frame:
        
#        xalign 0.98
#        yalign 0.98
        
#        has hbox

#        textbutton _("Return") action ShowMenu("inventorygeneral")

#screen giftitem1:
    
#    # This ensures that any other menu screen is replaced.
#    tag menu
    
#    # The background of the game menu.
#    window:
#        style "gm_root"
        
#    # The item description
#    frame:
        
#        xalign 0.5
#        yalign 0
        
#        has hbox
        
#        text "Test Gift Item Description1"
        
#    # The return button.
#    frame:
        
#        xalign 0.98
#        yalign 0.98
        
#        has hbox

#        textbutton _("Return") action ShowMenu("inventorygifts")

#screen clothesitem1:
    
#    # This ensures that any other menu screen is replaced.
#    tag menu
    
#    # The background of the game menu.
#    window:
#        style "gm_root"
        
#    # The item description
#    frame:
        
#        xalign 0.5
#        yalign 0
        
#        has hbox
        
#        text "Test Clothes Item Description1"
        
#    # The return button.
#    frame:
        
#        xalign 0.98
#        yalign 0.98
        
#        has hbox

#        textbutton _("Return") action ShowMenu("inventorygeneral")
        
#screen bookitem1:
    
#    # This ensures that any other menu screen is replaced.
#    tag menu
    
#    # The background of the game menu.
#    window:
#        style "gm_root"
        
#    # The item description
#    frame:
        
#        xalign 0.5
#        yalign 0
        
#        has hbox
        
#        text "Test Book Item Description1"
        
#    # The return button.
#    frame:
        
#        xalign 0.98
#        yalign 0.98
        
#        has hbox

#        textbutton _("Return") action ShowMenu("inventorygeneral")