"""Import sqrt(n) : used in isprime()."""
from math import sqrt

#### Fonction secondaire


def isprime(p: int) -> bool:
    """Check if the integer valer is prime.
    Args:
        p (int): Integer to check.
    Returns:
        bool: Truth value of the statement "Argument is prime" .
    """
    # votre code ici

    if p < 2:
        return False

    psup = int(sqrt(p)) + 1 # supremum of the test interval in range()

    for d in range(2, psup):
        if p % d == 0:
            return False
    return True

#### Fonction principale


def main():
    """Execution for the 100 first integers."""
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
