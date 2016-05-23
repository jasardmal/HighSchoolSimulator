Table of Contents:
1.) Overview
2.) Github / Ren'py Set-up
3.) Ren'py Learning Resources
4.) File Explanation

1.) High School Simulator is a visual novel-esque (https://en.wikipedia.org/wiki/Visual_novel) game with some RPG elements incoporated
intended to simulate high school life from freshman to senior year.

2.) After cloning the repository, find the Ren'py engine (renpy.exe) and launch it. Navigate to preferences and ensure the project
directory is set to where the respository was cloned (Note: While working on the project, it helps to make sure Github is up-to-date
which can be checked by clicking the gear in the upper-right hand corner of the Github app and navigating to "About Github Desktop.").

3.) 
Ren'py Documentation:
https://www.renpy.org/doc/html/#
Ren'py Forums:
https://lemmasoft.renai.us/forums/viewforum.php?f=8

4.)
inventory.rpy - is a menu with four item categories that contains info on the items currently held
inventorysub.rpy - is the backend to handling individual items within the inventory
options.rpy - is a menu which controls the settings of the game
screens.rpy - is the frontend to a majority of the game's menus/interfaces
script.rpy - handle the general gameplay of generic (main character development) days
skills.rpy - is the backend to handling calculations with skill (elective) points
social.rpy - is the backend to handling calculations with social (character relationship) points
socialscript.rpy - handles the results of the "Socialize" action
stats.rpy - is the backend to handling calculations with stat (charisma, courage, intelligence, stamina, stress) points
storyscript.rpy - handles the main story gameplay
time.rpy - handles the backend of the time system
