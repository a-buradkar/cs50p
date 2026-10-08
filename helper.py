alp = "abcdefghijklmnopqrstuvqxyz"

def clean(txt, capitals=False) -> str: # unoptimised
    msg = ""
    for c in txt:
        if c.isalpha():
            if capitals:
                msg += c
            else:
                msg += c.lower()
    
    return msg

def reformat(new, src, capitals=True) -> str: # unoptimised
    msg = ""
    i=0
    for c in new:
        while not src[i].isalpha():
            msg += src[i]
            i+=1

        if capitals and src[i].isupper():
            msg += c.upper()
        else:
            msg += c.lower()
        i+=1

    return msg