###############################################################################
## Inventory
##
## Screens that allows the user to view inventory at appropriate times and see
## items in inventory.
#screen inventoryhub:
    
#    # This ensures that any other menu screen is replaced.
#    tag menu
    
#    # The background of the game menu.
#    window:
#        style "gm_root"
        
#    # The various item tabs.
#    frame:
        
#        style "file_picker_frame"

#        has vbox

#        hbox:
            
#            style_group "file_picker_nav"

#            textbutton _("General") action ShowMenu("inventorygeneral") text_min_width 171
#            textbutton _("Gifts") action ShowMenu("inventorygifts") text_min_width 171
#            textbutton _("Clothes") action ShowMenu("inventoryclothes") text_min_width 171
#            textbutton _("Books") action ShowMenu("inventorybooks") text_min_width 171
            
#    # The return button.
#    frame:
        
#        xalign 0.98
#        yalign 0.98
        
#        has hbox

#        textbutton _("Return") action ShowMenu("save")

#screen inventorygeneral:
    
#    # This ensures that any other menu screen is replaced.
#    tag menu
    
#    # The background of the game menu.
#    window:
#        style "gm_root"
        
#    # The general item tab.
#    frame:
        
#        style "file_picker_frame"

#        has vbox

#        hbox:
            
#            style_group "file_picker_nav"

#            textbutton _("General") action NullAction() text_min_width 763
        
#    # The various item slots.
#    frame:

#        $ columns = 2
#        $ rows = 5
#        yalign 0.07

#        # Display a grid of item slots.
#        grid columns rows:
#            transpose True
#            xfill True
#            style_group "file_picker"

#            # Each item slot is a button.
#            button:
                
#                action ShowMenu("genitem1")
#                xfill True
                
#                text "[inventorygeneral[0]]"
                
#            button:
                
#                action ShowMenu("genitem2")
#                xfill True
                
#                text "[inventorygeneral[1]]"
                
#            button:
                
#                action ShowMenu("genitem3")
#                xfill True
                
#                text "[inventorygeneral[2]]"
            
#            button:
                
#                action ShowMenu("genitem4")
#                xfill True
                
#                text "[inventorygeneral[3]]"
            
#            button:
                
#                action ShowMenu("genitem5")
#                xfill True
                
#                text "[inventorygeneral[4]]"
            
#            button:
                
#                action ShowMenu("genitem6")
#                xfill True
                
#                text "[inventorygeneral[5]]"
            
#            button:
                
#                action ShowMenu("genitem7")
#                xfill True
                
#                text "[inventorygeneral[6]]"
            
#            button:
                
#                action ShowMenu("genitem8")
#                xfill True
                
#                text "[inventorygeneral[7]]"
            
#            button:
                
#                action ShowMenu("genitem9")
#                xfill True
                
#                text "[inventorygeneral[8]]"
                
#            button:
                
#                action ShowMenu("genitem10")
#                xfill True
                
#                text "[inventorygeneral[9]]"
                
#    # The return button.
#    frame:
        
#        xalign 0.98
#        yalign 0.98
        
#        has hbox

#        textbutton _("Return") action ShowMenu("inventoryhub")

#screen inventorygifts:
    
#    # This ensures that any other menu screen is replaced.
#    tag menu
    
#    # The background of the game menu.
#    window:
#        style "gm_root"
        
#    # The gifts item tab.
#    frame:
        
#        style "file_picker_frame"

#        has vbox

#        hbox:
            
#            style_group "file_picker_nav"

#            textbutton _("Gifts") action NullAction() text_min_width 763
        
#    # The various item slots.
#    frame:

#        $ columns = 2
#        $ rows = 5
#        yalign 0.07

#        # Display a grid of item slots.
#        grid columns rows:
#            transpose True
#            xfill True
#            style_group "file_picker"

#            # Each item slot is a button.
#            button:
                
#                action ShowMenu("giftitem1")
#                xfill True
                
#                text "[inventorygifts[0]]"
                
#            button:
                
#                action ShowMenu("giftitem2")
#                xfill True
                
#                text "[inventorygifts[1]]"
                
#            button:
                
#                action ShowMenu("giftitem3")
#                xfill True
                
#                text "[inventorygifts[2]]"
            
#            button:
                
#                action ShowMenu("giftitem4")
#                xfill True
                
#                text "[inventorygifts[3]]"
            
#            button:
                
#                action ShowMenu("giftitem5")
#                xfill True
                
#                text "[inventorygifts[4]]"
            
#            button:
                
#                action ShowMenu("giftitem6")
#                xfill True
                
#                text "[inventorygifts[5]]"
            
#            button:
                
#                action ShowMenu("giftitem7")
#                xfill True
                
#                text "[inventorygifts[6]]"
            
#            button:
                
#                action ShowMenu("giftitem8")
#                xfill True
                
#                text "[inventorygifts[7]]"
            
#            button:
                
#                action ShowMenu("giftitem9")
#                xfill True
                
#                text "[inventorygifts[8]]"
                
#            button:
                
#                action ShowMenu("giftitem10")
#                xfill True
                
#                text "[inventorygifts[9]]"
                
#    # The return button.
#    frame:
        
#        xalign 0.98
#        yalign 0.98
        
#        has hbox

#        textbutton _("Return") action ShowMenu("inventoryhub")
        
#screen inventoryclothes:
    
#    # This ensures that any other menu screen is replaced.
#    tag menu
    
#    # The background of the game menu.
#    window:
#        style "gm_root"
        
#    # The clothes item tab.
#    frame:
        
#        style "file_picker_frame"

#        has vbox

#        hbox:
            
#            style_group "file_picker_nav"

#            textbutton _("Clothes") action NullAction() text_min_width 763
        
#    # The various item slots.
#    frame:

#        $ columns = 2
#        $ rows = 5
#        yalign 0.07

#        # Display a grid of item slots.
#        grid columns rows:
#            transpose True
#            xfill True
#            style_group "file_picker"

#            # Each item slot is a button.
#            button:
                
#                action ShowMenu("clothesitem1")
#                xfill True
                
#                text "[inventoryclothes[0]]"
                
#            button:
                
#                action ShowMenu("clothesitem2")
#                xfill True
                
#                text "[inventoryclothes[1]]"
                
#            button:
                
#                action ShowMenu("clothesitem3")
#                xfill True
                
#                text "[inventoryclothes[2]]"
            
#            button:
                
#                action ShowMenu("clothesitem4")
#                xfill True
                
#                text "[inventoryclothes[3]]"
            
#            button:
                
#                action ShowMenu("clothesitem5")
#                xfill True
                
#                text "[inventoryclothes[4]]"
            
#            button:
                
#                action ShowMenu("clothesitem6")
#                xfill True
                
#                text "[inventoryclothes[5]]"
            
#            button:
                
#                action ShowMenu("clothesitem7")
#                xfill True
                
#                text "[inventoryclothes[6]]"
            
#            button:
                
#                action ShowMenu("clothesitem8")
#                xfill True
                
#                text "[inventoryclothes[7]]"
            
#            button:
                
#                action ShowMenu("clothesitem9")
#                xfill True
                
#                text "[inventoryclothes[8]]"
                
#            button:
                
#                action ShowMenu("clothesitem10")
#                xfill True
                
#                text "[inventoryclothes[9]]"
                
#    # The return button.
#    frame:
        
#        xalign 0.98
#        yalign 0.98
        
#        has hbox

#        textbutton _("Return") action ShowMenu("inventoryhub")
        
#screen inventorybooks:
    
#    # This ensures that any other menu screen is replaced.
#    tag menu
    
#    # The background of the game menu.
#    window:
#        style "gm_root"
        
#    # The books item tab.
#    frame:
        
#        style "file_picker_frame"

#        has vbox

#        hbox:
            
#            style_group "file_picker_nav"

#            textbutton _("Books") action NullAction() text_min_width 763
        
#    # The various item slots.
#    frame:

#        $ columns = 2
#        $ rows = 5
#        yalign 0.07

#        # Display a grid of item slots.
#        grid columns rows:
#            transpose True
#            xfill True
#            style_group "file_picker"

#            # Each item slot is a button.
#            button:
                
#                action ShowMenu("bookitem1")
#                xfill True
                
#                text "[inventorybooks[0]]"
                
#            button:
                
#                action ShowMenu("bookitem2")
#                xfill True
                
#                text "[inventorybooks[1]]"
                
#            button:
                
#                action ShowMenu("bookitem3")
#                xfill True
                
#                text "[inventorybooks[2]]"
            
#            button:
                
#                action ShowMenu("bookitem4")
#                xfill True
                
#                text "[inventorybooks[3]]"
            
#            button:
                
#                action ShowMenu("bookitem5")
#                xfill True
                
#                text "[inventorybooks[4]]"
            
#            button:
                
#                action ShowMenu("bookitem6")
#                xfill True
                
#                text "[inventorybooks[5]]"
            
#            button:
                
#                action ShowMenu("bookitem7")
#                xfill True
                
#                text "[inventorybooks[6]]"
            
#            button:
                
#                action ShowMenu("bookitem8")
#                xfill True
                
#                text "[inventorybooks[7]]"
            
#            button:
                
#                action ShowMenu("bookitem9")
#                xfill True
                
#                text "[inventorybooks[8]]"
                
#            button:
                
#                action ShowMenu("bookitem10")
#                xfill True
                
#                text "[inventorybooks[9]]"
                
#    # The return button.
#    frame:
        
#        xalign 0.98
#        yalign 0.98
        
#        has hbox

#        textbutton _("Return") action ShowMenu("inventoryhub")