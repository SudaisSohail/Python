import secrets

print(secrets.choice(range(11)))   # Returns a random number from the given iterable

print(secrets.randbelow(5))        # Returns a random number which below the given number

print(secrets.randbits(8))         # Returns a random number which consists of the given number of bits

print(secrets.token_bytes(10))     # Used to generate a random token for security purposes

print(secrets.token_hex(16))       # Used to generate a hexadecimal token for security purposes

print(secrets.token_urlsafe(16))   # Used to generate a urlsafe token without symbols for security purposes

print(secrets.compare_digest("Hello", "Hello"))  # Always takes a random amount of time to determine whether 2 strings are same or not