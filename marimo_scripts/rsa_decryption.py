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
    
    def decrypt_rsa(encrypted_b, m, p, q, k, m_tot):
        msg_ints = []
        for bi in encrypted_b:
            
            if k > m_tot:
                v, u = extended_euclidean_alg(k, m_tot)
            else:
                v, u = extended_euclidean_alg(m_tot, k)

            u, v = m_tot + u, k - v

            ai = successive_squaring(bi, u, m)

            ai_str = str(ai)

            ai_ints = [ai_str[i:i+2] for i in range(0, len(ai_str), 2)]
            msg_ints += ai_ints
            
        # Map back to letters
        chars = [int_to_letter[int(i)] for i in msg_ints]
        decrypted_msg = "".join(chars)

        return decrypted_msg

    ## EXAMPLE:
    m = 163276871
    p = 12553
    q = 13007
    k = 79921
    m_totient = m - p - q + 1
    B = [124051554, 123619784, 123420070, 44442925, 132143181] #From previous script!
    original_msg = decrypt_rsa(B, m, p, q, k, m_totient)
    print(original_msg)
    return