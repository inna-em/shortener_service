base = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def encode(base10):
    base62 = []

    while base10 > 0:
        val = base10 % 62
        base62.append(base[val])
        base10 //= 62

    return "".join(base62[::-1])


def get_url_idx(code):
    idx = []

    for i in range(len(code)):
        idx.append(base.index(code[i]))

    for i in range(len(idx)):
        idx[i] *= (62 ** (len(idx) - i - 1))

    return sum(idx)
