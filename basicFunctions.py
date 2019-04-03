"""This File presents some basic Functions needed to run the script."""

def cleanup(d):
    z = d.replace(",","")
    x = z.replace("[", "")
    y = x.replace("]","")
    g = y.replace("'", "")
    d = g.replace("\"", "")
    return d

def reverseWords(phrase):
    inpWords = phrase.split(" ")
    first = ", ".join((inpWords[-1],inpWords[0]))
    second = "".join(cleanup(str(inpWords[1:-1])))
    outWords = " ".join((first, second))
    return outWords