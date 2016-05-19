init python:
    def time_callback():#constantly calculate the time
        
        if (hasattr(store, 'thephase')):#manages phases
            if store.theweekday == 7:
                if store.thephase > 8:
                    store.theweekday = store.theweekday + 1
                    store.theday = store.theday + 1
                    store.dayofyear = store.dayofyear + 1
                    store.thephase = store.thephase - 8
                if store.thephase == 1:
                    store.stringphase = "Early Morning"
                elif store.thephase == 2:
                    store.stringphase = "Morning"
                elif store.thephase == 3:
                    store.stringphase = "Morning"
                elif store.thephase == 4:
                    store.stringphase = "Afternoon"
                elif store.thephase == 5:
                    store.stringphase = "Afternoon"
                elif store.thephase == 6:
                    store.stringphase = "Evening"
                elif store.thephase == 7:
                    store.stringphase = "Evening"
                elif store.thephase == 8:
                    store.stringphase = "Night"
                else:
                    store.stringweekday = "Error"
            
            elif store.theweekday == 1:
                if store.thephase > 8:
                    store.theweekday = store.theweekday + 1
                    store.theday = store.theday + 1
                    store.dayofyear = store.dayofyear + 1
                    store.thephase = store.thephase - 8
                if store.thephase == 1:
                    store.stringphase = "Early Morning"
                elif store.thephase == 2:
                    store.stringphase = "Morning"
                elif store.thephase == 3:
                    store.stringphase = "Morning"
                elif store.thephase == 4:
                    store.stringphase = "Afternoon"
                elif store.thephase == 5:
                    store.stringphase = "Afternoon"
                elif store.thephase == 6:
                    store.stringphase = "Evening"
                elif store.thephase == 7:
                    store.stringphase = "Evening"
                elif store.thephase == 8:
                    store.stringphase = "Night"
                else:
                    store.stringweekday = "Error"
                    
            else:
                if store.thephase > 11:
                    store.theweekday = store.theweekday + 1
                    store.theday = store.theday + 1
                    store.dayofyear = store.dayofyear + 1
                    store.thephase = store.thephase - 11
                if store.thephase == 1:
                    store.stringphase = "Early Morning"
                elif store.thephase == 2:
                    store.stringphase = "Morning"
                elif store.thephase == 3:
                    store.stringphase = "1st Period"
                elif store.thephase == 4:
                    store.stringphase = "2nd Period"
                elif store.thephase == 5:
                    store.stringphase = "3rd Period"
                elif store.thephase == 6:
                    store.stringphase = "Lunchtime"
                elif store.thephase == 7:
                    store.stringphase = "4th Period"
                elif store.thephase == 8:
                    store.stringphase = "5th Period"
                elif store.thephase == 9:
                    store.stringphase = "6th Period"
                elif store.thephase == 10:
                    store.stringphase = "After School"
                elif store.thephase == 11:
                    store.stringphase = "Evening"
                else:
                    store.stringweekday = "Error"
        
        if(hasattr(store, 'location')):#manages locations
            if store.location == 1:
                store.stringlocation = "School"
            elif store.location == 2:
                store.stringlocation = "Home"
            elif store.location == 3:
                store.stringlocation = "Town"
            elif store.location == 4:
                store.stringlocation = "Park"
            elif store.location == 5:
                store.stringlocation = "???"
            else:
                store.stringlocation = "Error"
                
        if (hasattr(store, 'theday')):#manages days of the month
            if store.theday > store.daylim:
                store.theday = store.theday - store.daylim
                store.themonth = store.themonth + 1
                
        if (hasattr(store, 'themonth')):#manages months and their day limits
            if store.themonth > 12:
                store.themonth = store.themonth - 12
            if store.themonth == 1:
                store.stringmonth = "January"
                store.daylim = 31
            if store.themonth == 2:
                store.stringmonth = "February"
                if ((((int(store.theyear) / 4)*4) - store.theyear) == 0):
                    store.daylim = 29
                else:
                    store.daylim = 28
            if store.themonth == 3:
                store.stringmonth = "March"
                store.daylim = 31
            if store.themonth == 4:
                store.stringmonth = "April"
                store.daylim = 30
            if store.themonth == 5:
                store.stringmonth = "May"
                store.daylim = 31
            if store.themonth == 6:
                store.stringmonth = "June"
                store.daylim = 30
            if store.themonth == 7:
                store.stringmonth = "July"
                store.daylim = 31
            if store.themonth == 8:
                store.stringmonth = "August"
                store.daylim = 31
            if store.themonth == 9:
               store.stringmonth = "September"
               store.daylim = 30
            if store.themonth == 10:
               store.stringmonth = "October"
               store.daylim = 31
            if store.themonth == 11:
               store.stringmonth = "November"
               store.daylim = 30
            if store.themonth == 12:
               store.stringmonth = "December"
               store.daylim = 31
            
            if (hasattr(store, 'dayofyear') and hasattr(store, 'yearlim')):#manages years
                if store.dayofyear > store.yearlim:
                   store.dayofyear = store.dayofyear - store.yearlim
                   store.theyear = store.theyear + 1
                if ((((int(store.theyear) / 4)*4) - store.theyear) == 0):
                   store.yearlim = 366
                else:
                   store.yearlim = 365
            
            if (hasattr(store, 'theweekday')):#manages weekdays
                if store.theweekday > 7:
                    store.theweekday = store.theweekday - 7
                if store.theweekday == 1:
                    store.stringweekday = "Sunday"
                elif store.theweekday == 2:
                    store.stringweekday = "Monday"
                elif store.theweekday == 3:
                    store.stringweekday = "Tuesday"
                elif store.theweekday == 4:
                    store.stringweekday = "Wednesday"
                elif store.theweekday == 5:
                    store.stringweekday = "Thursday"
                elif store.theweekday == 6:
                    store.stringweekday = "Friday"
                elif store.theweekday == 7:
                    store.stringweekday = "Saturday"
                else:
                    store.stringweekday = "Error"
                    
    config.python_callbacks.append(time_callback)
    
    def Calendar():#manages display of calendar
        ui.frame(xfill=False, xminimum = 200, yminimum=None, xalign=1.0, yalign = 0.0)
        ui.vbox()
        ui.text("(%s) - %s %d %d" % (stringweekday, stringmonth, theday, theyear), xalign=1.0, size=20)
        ui.close()
        
    def Phase():#manages display of phases
        ui.frame(xfill=False, xminimum = None, yminimum=None, xalign=1.0, yalign = 0.05)
        ui.vbox()
        ui.text("%s" % (stringphase), xalign=0, size=20)
        ui.close()
        
    def Location():#manages display of phases
        ui.frame(xfill=False, xminimum = None, yminimum=None, xalign=1.0, yalign = 0.1)
        ui.vbox()
        ui.text("%s" % (stringlocation), xalign=0, size=20)
        ui.close()