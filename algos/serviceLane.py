# 🚗🚗

# basially find the minumum in a slice

def serviceLane(width, cases):
    wifs = []
    for i in width:
        wifs.append(min(cases[i[0]:i[1]]))
        return wifs
