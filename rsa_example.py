from math import ceil, log10

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

from rsa import *
from math import ceil

m = 163276871
p = 12553
q = 13007
k = 79921
m_totient = m - p - q + 1

message = "To be or not to be"
encrypted_b = encrypt_rsa(message, k, m)

def decrypt_rsa(encrypted_b, m, p, q, k, m_tot):
    msg_ints = []
    for bi in encrypted_b:

        # solve for ai in 
        # ai^k = bi (mod m)

        # Euler's Totient Thm.: gcd(bi, m) = 1 (m is prime, so this is always true!)
        # Implies --> bi^m_tot = 1 (mod m)
        

        # Extended Euclidean algorithm
        # Solve (u,v): u*k - v*m_tot = 1
        
        if k > m_tot:
            v, u = extended_euclidean_alg(k, m_tot)
        else:
            v, u = extended_euclidean_alg(m_tot, k)

        # Bezout's solution:
        u, v = m_tot + u, k - v

        # Reduces to: x^k*u = x^(1 + m_tot*v) = (x^1)*(x^m_tot*v) = x * 1^v = x (mod m)
        ai = successive_squaring(bi, u, m)

        ai_str = str(ai)

        ai_ints = [ai_str[i:i+2] for i in range(0, len(ai_str), 2)]
        msg_ints += ai_ints
        
    # Map back to letters
    chars = [int_to_letter[int(i)] for i in msg_ints]
    decrypted_msg = "".join(chars)
        


    return decrypted_msg


print(decrypt_rsa(encrypted_b, m, p, q, k, m_totient))