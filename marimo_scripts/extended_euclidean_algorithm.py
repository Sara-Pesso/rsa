import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium", auto_download=["html"])

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
        s = [1, 0]
        t = [0, 1]

        for i in range(2, len(remainders) - 1):
            q = quotients[i-2]
            s.append(s[i-2] - q * s[i-1])
            t.append(t[i-2] - q * t[i-1])

        return s[-1], t[-1]

    print(extended_euclidean_alg(131,1008))
    return