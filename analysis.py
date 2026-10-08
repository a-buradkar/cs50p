def shift(txt, key, capitals=False) -> str: #unoptimised
    msg=""
    for c in txt:
        if capitals and c.isupper():
            msg += chr((ord(c) - 65 + key)%26+65)
        else:
            msg += chr((ord(c) - 97 + key)%26 +97)

    return msg

# todo freq function