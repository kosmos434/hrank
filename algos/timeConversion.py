# time conversion time ⌚⌛⏳⏲


s = "12:45:54PM"


def timeConversion(s):
    # take in 12 hour time, return 24 hour time
    if s[-2:] == "AM":
        if s[:2] == "12":
            s = "00" + s[2:]
        return(s[:-2])
    if s[-2:] == "PM":
        if s[:2] == "12":
            return(s[:-2])
        # like, convert to int to add 12, then back to str
        newhour24style = str(int(s[:2]) + 12)
        restoftime = s[2:-2]
        return(newhour24style+restoftime)


timeConversion(s)
