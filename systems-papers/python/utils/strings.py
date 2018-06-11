bad_tokens = "\""

def clean(s):
    for tok in bad_tokens:
        s = s.replace(tok,'')
    return s