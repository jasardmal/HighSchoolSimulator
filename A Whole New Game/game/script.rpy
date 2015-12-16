
image navi = "navi.png"
image arrow = "arrow.png"

define t = Character('Tutorial-Chan-San-Senpai', color="#c8ffc8")
define h = Character('Mr. Hart', color="#c8ffc8")
define k = Character('Mr. Kelly', color="#c8ffc8")
define g = Character('Mrs. Galvin', color="#c8ffc8")
define o = Character('Mrs. Ong', color="#c8ffc8")
define v = Character('Mr. V', color="#c8ffc8")
define pov = DynamicCharacter("povname", color ="#c8ffc8")

label start:
    
    $ povname = ""
    
    $ clock = False#make false to hide the calendar
    $ theweekday = 2#monday, the number of the weekday, this automatically changes but must be initially assigned
    $ themonth = 8#august, the number of the month, this automatically changes but must be initially assigned
    $ theday = 24#this automatically changes but must be initially assigned
    $ theyear = 2015#this automatically changes but must be initially assigned
    $ dayofyear = 236#you must calculate this properly, this automatically changes
    $ yearlim = 365#initially define it as 265 or 366, whichever is correct, this gets changed automatically later
    $ daylim = 31#initially define it as 28, 29, 30, or 31, whichever is correct, this gets changed automatically later
    $ stringweekday = "Monday"#2, the string of the weekday, this automatically changes but must be initially assigned
    $ stringmonth = "August"#8, the string of the month, this automatically changes but must be initially assigned
    $ thephase = 2#morning, the phase of the day, this automatically changes but must be initially assigned
    $ stringphase = "Morning"#2, the phase of the day, this automatically changes but must be initially assigned
    
    scene black

    t "Hey. Listen."

    t "......."
    
    t "WAKE UP!"
    
    scene img_1831
    show navi at Position(xpos = 0.5, xanchor = 0.5, ypos = 0.5, yanchor = 0.5)
    with Dissolve(1.0) 
    
    t "Jeez. Finally awake. You're late for school."
    
    t "We don't have much time before your first class starts, so listen up."
    
    $ clock = True
    show arrow at Position(xpos = 0.8, xanchor = 0.5, ypos = 0.25, yanchor = 0.5)
    
    t "See this thing?"

    t "This thing is your clock. If you look, you are late for school."
    
    t "That's not good. You slept in late."
    
    hide arrow
    
    t "So let's get going. You have to get to your first period..."
    
  

    t "Alright, let's go to English class!"
    
    $ thephase = 3
    
    #animation
    
    t "Here we are. English Class."
    
    t "Your teacher in this class is Mr. Hart."
    
    h "Another one? You're late. What is your name?"
    
    $ povname = renpy.input(_("Name?"))
    
    pov "My name is [povname!t]"
   




    t "Alright, let's go to Math class!"
    
    $ thephase = 4
    
    #animation
    
    t "Here we are. Math Class."
    
    t "Your teacher in this class is Mr. Kelly."
    
    k "Another one? You're late. What is your name?"

    pov "My name is [povname!t]"
    




    t "Alright, let's go to Science class!"
    
    $ thephase = 5
    
    #animation
    
    t "Here we are. Science Class."
    
    t "Your teacher in this class is Ms. Galvin."
    
    g "Another one? You're late. What is your name?"
    
    pov "My name is [povname!t]"
    
    
    
    
    t "Alright, let's go to History class!"
    
    $ thephase = 7
    
    #animation
    
    t "Here we are. History Class."
    
    t "Your teacher in this class is Mrs. Ong."
    
    o "Another one? You're late. What is your name?"
    
    pov "My name is [povname!t]"
    
    
    
    
    t "Alright, let's go to your first Elective class!"
    
    $ thephase = 8
    
    #animation
    
    t "Here we are. Your first Elective Class."
    
    t "Your teacher in this class is Mr. V. He has a real name, but people just call him V."
    
    v "Another one? You're late. What is your name?"

    pov "My name is [povname!t]"
    
    
    
    
    t "Alright, let's go to your second Elective class!"
    
    $ thephase = 9
    
    #animation
    
    t "Here we are. Your second Elective Class."
    
    t "Your teacher in this class is Mr. V. He has a real name, but people just call him V."
    
    v "Another one? You're late. What is your name?"

    pov "My name is [povname!t]"
        
 
    
    t "And that was your first day. You failed."
    
    t "Go home."

    return
