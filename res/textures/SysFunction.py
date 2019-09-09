def printTimeSec(seconds):
    seconds = 3667
    secs = seconds % 60
    minutes = seconds // 60
    mins = minutes % 60
    hours = minutes // 60
    hrs = hours % 24
    days = hours // 24
    print(secs, "seconds,", mins, "minutes", hrs, "hours", days, "days")
