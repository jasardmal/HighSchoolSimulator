﻿# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:
    
    # This ensures that any other menu screen is replaced.
    tag menu

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0
    
    # If there's a time system, display it in upper right.
    if(clock):
        $ Calendar()
        $ Phase()
        $ Location()

    # Use the quick menu.
    use quick_menu
    
##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice
screen choice:
    
    # This ensures that any other menu screen is replaced.
    tag menu

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)

##############################################################################
# Input
#
# Screen that's used to display renpy.input().
# http://www.renpy.org/doc/html/screen_special.html#input
screen input:
    
    # This ensures that any other menu screen is replaced.
    tag menu

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu
screen main_menu:
    
    # This ensures that any other menu screen is replaced.
    tag menu
    
    # The background of the main menu.
    window:
        style "mm_root"

    # The main menu buttons.
    frame:
        style_group "mm"
        xalign 0.98
        yalign 0.98

        has vbox

        textbutton _("Start Game") action Start()
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit(confirm=False)

init -2:

    # Make all the main menu buttons be the same size.
    style mm_button:
        size_group "mm"

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:
    
    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign 0.98
        yalign 0.98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Story") action ShowMenu("storyhomecomeinvesthub")
        textbutton _("Inventory") action ShowMenu("inventoryhub")
        textbutton _("Stats") action ShowMenu("stats")
        textbutton _("Social") action ShowMenu("socialcontacts")
        textbutton _("System") action ShowMenu("system")

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl
screen nvl:
    
    # This ensures that any other menu screen is replaced.
    tag menu

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu
    

##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
screen preferences:

    # This ensures that any other menu screen is replaced.
    tag menu
    
    # The background of the game menu.
    window:
        style "gm_root"

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transitions")
                textbutton _("All") action Preference("transitions", "all")
                textbutton _("None") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Text Speed")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")
                
        # The middle column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Skip")
                textbutton _("Seen Messages") action Preference("skip", "seen")
                textbutton _("All Messages") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Begin Skipping") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("After Choices")
                textbutton _("Stop Skipping") action Preference("after choices", "stop")
                textbutton _("Keep Skipping") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Auto-Forward Time")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Wait for Voice") action Preference("wait for voice", "toggle")
                    
        #The right column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Music Volume")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Sound Volume")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Test"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Voice Volume")
                    bar value Preference("voice volume")

                    textbutton _("Voice Sustain") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Test"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"
                            
    # The return button.
    frame:
        xalign 0.98
        yalign 0.98
        
        has vbox

        textbutton _("Return") action Return()

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0
        
##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:
    
    # This ensures that any other menu screen is replaced.
    tag menu

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Menu") action ShowMenu('save')
        if thephase == 10 or thephase == 11:
            textbutton _("Map") action ShowMenu("mapSchool")
        else:
            textbutton _("Map") action NullAction()
        textbutton _("Q.Save") action QuickSave()
        textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"
        
##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.
screen file_picker:
    
    # This ensures that any other menu screen is replaced.
    tag menu

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save:

    # This ensures that any other menu screen is replaced.
    tag menu
    
    use navigation
    use file_picker
    
screen load:

    # This ensures that any other menu screen is replaced.
    tag menu
    
    use navigation
    use file_picker
    
init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text

##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:
    
    # This ensures that any other menu screen is replaced.
    tag menu

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin 0.05
        ypos 0.1
        yanchor 0
        ypadding 0.05

        has vbox:
            xalign 0.5
            yalign 0.5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"
        
##############################################################################
# Inventory
#
# Screens that allows the user to view inventory at appropriate times and read
# item descriptions.
screen inventoryhub:
    
    # This ensures that any other menu screen is replaced.
    tag menu
    
    # The background of the game menu.
    window:
        style "gm_root"
        
    # The various item tabs.
    frame:
        
        style "file_picker_frame"

        has vbox

        hbox:
            
            style_group "file_picker_nav"

            textbutton _("General") action FilePage(1) text_min_width 171
            textbutton _("Gifts") action FilePage(2) text_min_width 171
            textbutton _("Clothes") action FilePage(3) text_min_width 171
            textbutton _("Books") action FilePage(4) text_min_width 171

        # The selected item description.
        $ itemdescription = " "
        
        $ columns = 2
        $ rows = 5

        # Display a grid of item slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten item slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each item slot is a button.
                button:
                    
                    action NullAction()
                    xfill True

                    has hbox
                    $ file_name = FileSlotName(i, columns * rows)
                    
                    text "[file_name]."
        
    # The return button.
    frame:
        
        xalign 0.98
        yalign 0.98
        
        has hbox

        textbutton _("Return") action ShowMenu("save")
        
##############################################################################
# Maps
# 
# Screens that allow the user to view the town map and change their location
# at appropriate times.
screen mapSchool:
    
    # This ensures that any other menu screen is replaced.
    tag menu
    
    imagemap:
        
        ground "map"
        hover "mappng"
        
        hotspot (0, 0, 100, 100) clicked Jump("eveningSchool")
        hotspot (700, 0, 100, 100) clicked Jump("homeSchool")
        hotspot (0, 500, 100, 100) clicked Jump("choiceTown")
        hotspot (700, 500, 100, 100) clicked Jump("choicePark")
        
##############################################################################
# Social Contacts
#
# Screen that allows the user to view their character's social contacts
screen socialcontacts:
    
    # This ensures that any other menu screen is replaced.
    tag menu
    
    # The background of the game menu.
    window:
        style "gm_root"

    # The character database.
    frame:
        style_group "gm_nav"
        xalign 0
        yalign 0

        has vbox
        
        if hasmetmarc == False:
            textbutton _("???") action NullAction()
        else:
            textbutton _("Marc Waller") action ShowMenu("marc")
        
        if hasmetkolby == False:
            textbutton _("???") action NullAction()
        else:
            textbutton _("Kolby Frederickson") action ShowMenu("kolby")
        
        if hasmetfrederick == False:
            textbutton _("???") action NullAction()
        else:
            textbutton _("Frederick Hobson") action ShowMenu("frederick")
        
        if hasmetivor == False:
            textbutton _("???") action NullAction()
        else:
            textbutton _("Ivor Kovosad") action ShowMenu("ivor")
        
        if hasmetdanny == False:
            textbutton _("???") action NullAction()
        else:
            textbutton _("Danny Reuter") action ShowMenu("danny")
        
        if hasmetsarah == False:
            textbutton _("???") action NullAction()
        else:
            textbutton _("Sarah Granger") action ShowMenu("sarah")
        
        if hasmetchristina == False:
            textbutton _("???") action NullAction()
        else:
            textbutton _("Christina Schulz") action ShowMenu("christina")
        
        if hasmetagnes == False:
            textbutton _("???") action NullAction()
        else:
            textbutton _("Agnes Rocco") action ShowMenu("agnes")
        
        if hasmetcynthia == False:
            textbutton _("???") action NullAction()
        else:
            textbutton _("Cynthia Lucas") action ShowMenu("cynthia")
        
        if hasmetnatalie == False:
            textbutton _("???") action NullAction()
        else:
            textbutton _("Natalie Mcneil") action ShowMenu("natalie")
        
        if hasmetbecka == False:
            textbutton _("???") action NullAction()
        else:
            textbutton _("Becka Krakowski") action ShowMenu("becka")
    
    # The return button.
    frame:
        xalign 0.98
        yalign 0.98
        
        has hbox

        textbutton _("Return") action ShowMenu("save")
        
##############################################################################
# Social Progression
#
# Screens that allows the user to view their character's social progression
# with each of their contacts.
screen marc:
    
    # This ensures that any other menu screen is replaced.
    tag menu
    
    # The background of the game menu.
    window:
        style "gm_root"

    # Marc's social progression level displayed as a bar.
    frame:
        
        has hbox
        
        hbox:
            bar range 10 value 1 xmaximum 400
            
    # Marc's social progression level displayed as a number.
    frame:
        xalign 0.55
        yalign 0
        
        has hbox
            
        text "1/10"
    
    # The return button.
    frame:
        xalign 0.98
        yalign 0.98
        
        has hbox

        textbutton _("Return") action ShowMenu("socialcontacts")
    
screen kolby:
    
    # This ensures that any other menu screen is replaced.
    tag menu
    
    # The background of the game menu.
    window:
        style "gm_root"

    # Kolby's social progression level displayed as a bar.
    frame:
        
        has hbox
        
        hbox:
            bar range 10 value 1 xmaximum 400
            
    # Kolby's social progression level displayed as a number.
    frame:
        xalign 0.55
        yalign 0
        
        has hbox
            
        text "1/10"
    
    # The return button.
    frame:
        xalign 0.98
        yalign 0.98
        
        has hbox

        textbutton _("Return") action ShowMenu("socialcontacts")
    
screen frederick:
    
    # This ensures that any other menu screen is replaced.
    tag menu
    
    # The background of the game menu.
    window:
        style "gm_root"

    # Frederick's social progression level displayed as a bar.
    frame:
        
        has hbox
        
        hbox:
            bar range 10 value 1 xmaximum 400
            
    # Frederick's social progression level displayed as a number.
    frame:
        xalign 0.55
        yalign 0
        
        has hbox
            
        text "1/10"
        
    # The return button.
    frame:
        xalign 0.98
        yalign 0.98
        
        has hbox

        textbutton _("Return") action ShowMenu("socialcontacts")
    
screen ivor:
    
    # This ensures that any other menu screen is replaced.
    tag menu
    
    # The background of the game menu.
    window:
        style "gm_root"

    # Ivor's social progression level displayed as a bar.
    frame:
        
        has hbox
        
        hbox:
            bar range 10 value 1 xmaximum 400
            
    # Ivor's's social progression level displayed as a number.
    frame:
        xalign 0.55
        yalign 0
        
        has hbox
            
        text "1/10"
    
    # The return button.
    frame:
        xalign 0.98
        yalign 0.98
        
        has hbox

        textbutton _("Return") action ShowMenu("socialcontacts")
    
screen danny:
    
    # This ensures that any other menu screen is replaced.
    tag menu
    
    # The background of the game menu.
    window:
        style "gm_root"

    # Danny's social progression level displayed as a bar.
    frame:
        
        has hbox
        
        hbox:
            bar range 10 value 1 xmaximum 400
            
    # Danny's social progression level displayed as a number.
    frame:
        xalign 0.55
        yalign 0
        
        has hbox
            
        text "1/10"
    
    # The return button.
    frame:
        xalign 0.98
        yalign 0.98
        
        has hbox

        textbutton _("Return") action ShowMenu("socialcontacts")
    
screen sarah:
    
    # This ensures that any other menu screen is replaced.
    tag menu
    
    # The background of the game menu.
    window:
        style "gm_root"

    # Sarah's social progression level displayed as a bar.
    frame:
        
        has hbox
        
        hbox:
            bar range 10 value 1 xmaximum 400
            
    # Sarah's social progression level displayed as a number.
    frame:
        xalign 0.55
        yalign 0
        
        has hbox
            
        text "1/10"
    
    # The return button.
    frame:
        xalign 0.98
        yalign 0.98
        
        has hbox

        textbutton _("Return") action ShowMenu("socialcontacts")
    
screen christina:
    
    # This ensures that any other menu screen is replaced.
    tag menu
    
    # The background of the game menu.
    window:
        style "gm_root"

    # Christina's social progression level displayed as a bar.
    frame:
        
        has hbox
        
        hbox:
            bar range 10 value 1 xmaximum 400
            
    # Christina's social progression level displayed as a number.
    frame:
        xalign 0.55
        yalign 0
        
        has hbox
            
        text "1/10"
        
    # The return button.
    frame:
        xalign 0.98
        yalign 0.98
        
        has hbox

        textbutton _("Return") action ShowMenu("socialcontacts")
    
screen agens:
    
    # This ensures that any other menu screen is replaced.
    tag menu
    
    # The background of the game menu.
    window:
        style "gm_root"

    # Agnes's social progression level displayed as a bar.
    frame:
        
        has hbox
        
        hbox:
            bar range 10 value 1 xmaximum 400
            
    # Agnes's social progression level displayed as a number.
    frame:
        xalign 0.55
        yalign 0
        
        has hbox
            
        text "1/10"
        
    # The return button.
    frame:
        xalign 0.98
        yalign 0.98
        
        has hbox

        textbutton _("Return") action ShowMenu("socialcontacts")
    
screen cynthia:
    
    # This ensures that any other menu screen is replaced.
    tag menu
    
    # The background of the game menu.
    window:
        style "gm_root"

    # Cynthia's social progression level displayed as a bar.
    frame:
        
        has hbox
        
        hbox:
            bar range 10 value 1 xmaximum 400
            
    # Cynthia's social progression level displayed as a number.
    frame:
        xalign 0.55
        yalign 0
        
        has hbox
            
        text "1/10"
        
    # The return button.
    frame:
        xalign 0.98
        yalign 0.98
        
        has hbox

        textbutton _("Return") action ShowMenu("socialcontacts")
    
screen natalie:
    
    # This ensures that any other menu screen is replaced.
    tag menu
    
    # The background of the game menu.
    window:
        style "gm_root"

    # Natalie's social progression level displayed as a bar.
    frame:
        
        has hbox
        
        hbox:
            bar range 10 value 1 xmaximum 400
            
    # Natalie's social progression level displayed as a number.
    frame:
        xalign 0.55
        yalign 0
        
        has hbox
            
        text "1/10"
        
    # The return button.
    frame:
        xalign 0.98
        yalign 0.98
        
        has hbox

        textbutton _("Return") action ShowMenu("socialcontacts")
    
screen becka:
    
    # This ensures that any other menu screen is replaced.
    tag menu
    
    # The background of the game menu.
    window:
        style "gm_root"

    # Becka's social progression level displayed as a bar.
    frame:
        
        has hbox
        
        hbox:
            bar range 10 value 1 xmaximum 400
            
    # Becka's social progression level displayed as a number.
    frame:
        xalign 0.55
        yalign 0
        
        has hbox
            
        text "1/10"
        
    # The return button.
    frame:
        xalign 0.98
        yalign 0.98
        
        has hbox

        textbutton _("Return") action ShowMenu("socialcontacts")
    
##############################################################################
# Stats
#
# Screen that allows the user to view their character's stats.
screen stats:
    
    # This ensures that any other menu screen is replaced.
    tag menu
    
    # The background of the game menu.
    window:
        style "gm_root"
        
    # Charisma Label.
    frame:
        xalign 0
        yalign 0
        
        text "Charisma"
        
    # Charisma Bar.
    frame:
        xalign 0
        yalign 0.05
        
        has hbox
    
        hbox:
            bar range 5 value charisma xmaximum 400
            
    # Charisma displayed as a number.
    frame:
        xalign 0.54
        yalign 0.05
        
        has hbox
            
        text "[charisma]/5"
            
    # Courage Label.
    frame:
        xalign 0
        yalign 0.1
        
        text "Courage"
            
    # Courage Bar.
    frame:
        xalign 0
        yalign 0.15
        
        has hbox
    
        hbox:
            bar range 5 value courage xmaximum 400
            
    # Courage displayed as a number.
    frame:
        xalign 0.54
        yalign 0.15
        
        has hbox
            
        text "[courage]/5"
            
    # Intelligence Label.
    frame:
        xalign 0
        yalign 0.2
        
        text "Intelligence"
    
    # Intelligence Bar.
    frame:
        xalign 0
        yalign 0.25
        
        has hbox
    
        hbox:
            bar range 5 value intelligence xmaximum 400
            
    # Intelligence displayed as a number.
    frame:
        xalign 0.54
        yalign 0.25
        
        has hbox
            
        text "[intelligence]/5"
            
    # Stamina Label.
    frame:
        xalign 0
        yalign 0.3
        
        text "Stamina"
            
    # Stamina Bar.
    frame:
        xalign 0
        yalign 0.35
        
        has hbox
    
        hbox:
            bar range 5 value stamina xmaximum 400
            
    # Stamina displayed as a number.
    frame:
        xalign 0.54
        yalign 0.35
        
        has hbox
            
        text "[stamina]/5"
            
    # Stress Label.
    frame:
        xalign 0
        yalign 0.4
        
        text "Stress"
        
    # Stress Bar.
    frame:
        xalign 0
        yalign 0.45
        
        has hbox
    
        hbox:
            bar range 5 value stress xmaximum 400
            
    # Stress displayed as a number.
    frame:
        xalign 0.54
        yalign 0.45
        
        has hbox
            
        text "[stress]/5"
    
    # The return button.
    frame:
        xalign .98
        yalign .98
        
        has hbox

        textbutton _("Return") action ShowMenu("save")
        
    # Money Label.
    frame:
        xalign 0
        yalign 0.5
        
        text "Money"
    
    # Money.
    frame:
        xalign 0
        yalign 0.55
        
        has hbox
        
        text "$[money]"
        

##############################################################################
# Story (Homecoming Investigative Arc)
#
# Screen that shows the user info related to the homecoming Investigative Arc
# on a day-by-day basis.
screen storyhomecomeinvesthub:

    # This ensures that any other menu screen is replaced.
    tag menu
    
    # The background of the game menu.
    window:
        style "gm_root"
        
    # The story arc header.
    frame:
        xalign 0.5
        yalign 0
        
        has hbox
        
        text "Homecoming Investigative Arc"
        
    # The 1st day.
    frame:
        style_group "gm_nav"
        xalign 0.5
        yalign 0.05
        
        has hbox

        textbutton _("Day 1") action NullAction() text_min_width 300
        
    # The 2nd day.
    frame:
        style_group "gm_nav"
        xalign 0.5
        yalign 0.1
        
        has hbox

        textbutton _("Day 2") action ShowMenu("save") text_min_width 300
        
    # The 3rd day.
    frame:
        style_group "gm_nav"
        xalign 0.5
        yalign 0.15
        
        has hbox

        textbutton _("Day 3") action ShowMenu("save") text_min_width 300
        
    # The 4th day.
    frame:
        style_group "gm_nav"
        xalign 0.5
        yalign 0.2
        
        has hbox

        textbutton _("Day 4") action ShowMenu("save") text_min_width 300
    
    
    # The return button.
    frame:
        xalign 0.98
        yalign 0.98
        
        has hbox

        textbutton _("Return") action ShowMenu("save")
        
    
        
##############################################################################
# System
#
# Screen that allows the user to do/change system things.
screen system:
    
    # This ensures that any other menu screen is replaced.
    tag menu
    
    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign 0.98
        yalign 0.98
        
        has vbox
        
        textbutton _("Return") action ShowMenu("save")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()