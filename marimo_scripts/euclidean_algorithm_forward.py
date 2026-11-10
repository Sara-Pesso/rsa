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

    print(euclidean_alg(131, 1008))
    return