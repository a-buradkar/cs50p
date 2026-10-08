import helper as h
import analysis as a


def caesar(txt, key, capitals=False) -> str: #unoptimised, unfinished
    # todo check key format - must be builtinto this caesar function - accept both chr and int input as the key
    return a.shift(txt, key, capitals)


x = "Intro: B (Keyword Substitution Cipher, Key: Prism)"
print(h.clean(x))
print(h.reformat(caesar(h.clean(x), 1), x))