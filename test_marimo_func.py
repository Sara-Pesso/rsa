import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell
def _():
    # 1. Generate the encoding dictionary!
    import string

    # Lowercase alphabet (a-z) -> digits [11,36]
    int_to_letter = {}
    letter_to_int = {}

    encode = 11
    for letter in string.ascii_lowercase:
        int_to_letter[encode] = letter
        letter_to_int[letter] = encode
        encode += 1

    letter_to_int[' '] = encode
    int_to_letter[encode] = ' '


    return


@app.cell
def _():
    # 2. Successive Squaring
    def successive_squaring(a, k, m):
        exps = []
        while k > 0: 
            j = 0 
            while 2**(j+1) <= k:
                j += 1

            exps.append(j)
            k = k - 2**j

        # print(exps)
        mod_m = [a % m]
        for j in range(1, exps[0] + 1):
            mod_m.append(mod_m[j - 1]**2 % m)

        b = 1
        for i in range(0, len(exps)):
            b = b*mod_m[exps[i]] % m
        return b

    print(successive_squaring(758, 731, 1073))
    return


@app.cell
def _():
    # 3. Euclidean Alg. (Forward)
    def euclidean_alg(a, b):
        if b > a:
            a,b = b,a        
        remainders = [a, b]
        quotients = []
        r = a
        while r > 0:
            q, r = divmod(a, b)

            quotients.append(q)
            remainders.append(r)

            a = b
            b = r

        return quotients, remainders

    # 4. Extended Euclidean (Backward)

    def extended_euclidean_alg(a, b):
        quotients, remainders = euclidean_alg(a, b)

        # Iteratively calculate Bezout's coefficients
        # Bezout's Thm: Let a,b be ints with gcd = d
        # Then there exist ax + by = d
        # az + bt are multiples of d
        s = [1, 0]
        t = [0, 1]

        # Start: i = 2 b/c we initialize x0 = 1, x1 = 0, y0 = 0, and y1 = 1
        # Stop: num remainders - 1, b/c we are interested in the last **non 0** remainder from the EA
        for i in range(2, len(remainders) - 1):
            q = quotients[i-2]
            s.append(s[i-2] - q * s[i-1])
            t.append(t[i-2] - q * t[i-1])

        return s[-1], t[-1]

    # print(extended_euclidean_alg(240,46))


    def eea(a, b):
        # Goal: Solve ax + by = gcd
        # Start 1*x0 
        x0, x1, y0, y1 = 1, 0, 0, 1

        while b != 0: # r_i > 0
            q, r = divmod(a,b)

            a = b
            b = r

            new_x1 = x0 - q * x1
            x0 = x1
            x1 = new_x1

            new_y1 = y0 - q * y1
            y0 = y1
            y1 = new_y1
        

        gcd = a
        x = x0
        y = y0
        return gcd, x, y

    print(eea(131,1008))
    print(extended_euclidean_alg(131,1008))
    print(euclidean_alg(131, 1008))
    return


if __name__ == "__main__":
    app.run()