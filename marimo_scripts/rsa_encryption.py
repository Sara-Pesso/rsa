import marimo


__generated_with = "0.25.2"
app = marimo.App(width="medium", auto_download=["html"])

@app.cell
def _():
    # Python dependencies
    from math import ceil, log10
    
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

    # 2. Successive Squaring
    def successive_squaring(a, k, m):
        exps = []
        while k > 0: 
            j = 0 
            while 2**(j+1) <= k:
                j += 1

            exps.append(j)
            k = k - 2**j

        mod_m = [a % m]
        for j in range(1, exps[0] + 1):
            mod_m.append(mod_m[j - 1]**2 % m)

        b = 1
        for i in range(0, len(exps)):
            b = b*mod_m[exps[i]] % m
        return b

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
        s = [1, 0]
        t = [0, 1]

        for i in range(2, len(remainders) - 1):
            q = quotients[i-2]
            s.append(s[i-2] - q * s[i-1])
            t.append(t[i-2] - q * t[i-1])

        return s[-1], t[-1]

    def encrypt_rsa(msg, k, m):
        msg = msg.lower() #TODO: add upper/lower case, punctuation, etc.!

        msg_ints = []
        for char in msg:
            msg_ints.append(letter_to_int[char])

        num_digits = ceil(log10(m))-1

        num_a = ceil(2*len(msg_ints) / num_digits)

        msg_int_str = "".join(map(str,msg_ints))
        a = []
        for i in range(0, num_a):
            if i < num_a - 1:
                a_i = msg_int_str[num_digits*i:num_digits*(i+1)]
            else: # num_a - 1 (remainder digits)
                a_i = msg_int_str[num_digits*i:]

            a.append(int(a_i))

        b = []
        for ai in a:
            bi = successive_squaring(ai, k, m)
            b.append(bi)

        return b

    ## EXAMPLE:
    m = 163276871
    p = 12553
    q = 13007
    k = 79921
    m_totient = m - p - q + 1

    M = "To be or not to be"
    B = encrypt_rsa(M, k, m)
    print(B)
    return