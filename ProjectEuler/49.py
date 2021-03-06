from em import primes

def isperm(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))

def solve():
    lprimes = [p for p in primes(10000) if p > 1000]
    for idx, p1 in enumerate(lprimes):
        for p2 in lprimes[:idx]:
            if not isperm(p1, p2):
                continue

            p3 = 2 * p2 - p1
            if p3 in lprimes and isperm(p2, p3):
                if p3 != 1487: # given by problem
                    return str(p3) + str(p2) + str(p1)

if __name__ == "__main__":
	print(solve())
