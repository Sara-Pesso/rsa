import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium", auto_download=["html"])

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

        mod_m = [a % m]
        for j in range(1, exps[0] + 1):
            mod_m.append(mod_m[j - 1]**2 % m)

        b = 1
        for i in range(0, len(exps)):
            b = b*mod_m[exps[i]] % m
        return b

    print(successive_squaring(758, 731, 1073))
    return