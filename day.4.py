#!/usr/bin/env python3

def valid_password(password):
    if len(password) != 6:
        return False

    digits = [int(c) for c in password]

    if sorted(digits) != digits:
        return False

    if len(set(digits)) > 5: # No duplicates
        return False

    counts = [0] * 10
    for d in digits:
        counts[d] += 1
    if 2 not in counts:
        return False

    return True

def execute():
    password_range = range(284639,748760)
    return len([p for p in password_range if valid_password(str(p))])

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def test_cases():
    verify(False, valid_password("1"))
    # verify(True, valid_password("111111")) # Not valid in part 2
    verify(False, valid_password("223450"))
    verify(False, valid_password("123789"))
    verify(True, valid_password("112233"))
    verify(False, valid_password("123444"))
    verify(True, valid_password("111122"))

if __name__ == "__main__":
    test_cases()
    print(execute())