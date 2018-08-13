threshold = 3

def normalize_conference(x):
    capital_count = 0
    first_i = 0
    last_i = 0

    for i in range(len(x)-1,-1,-1):
        c = x[i]

        # counting up
        if capital_count < threshold:

            if c.isupper():
                if capital_count == 0:
                    last_i = i
                    first_i = i
                    capital_count += 1
                else:
                    capital_count += 1
                    first_i = i
            else:
                capital_count = 0

        # reached threshold! now to find
        # next non-capital
        else:
            if c.isupper():
                first_i = i
            else:
                return x[first_i:last_i+1]

    if capital_count >= threshold:
        return x[first_i:last_i+1]
    else:

        last_i = 0
        # look for ending parentheses
        for i in range(len(x)-1,0,-1):
            c = x[i]
            if c == ")":
                last_i = i
            elif c == "(":
                return x[i+1:last_i]

    return x

print(normalize_conference( "SIGIR" ))