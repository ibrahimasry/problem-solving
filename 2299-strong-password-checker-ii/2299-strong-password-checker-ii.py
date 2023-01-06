class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        sp = "!@#$%^&*()-+"
        seen = set()
        if len(password) < 8:
            return False
        
        for c1,c2 in zip(password, password[1:]):
            if c1 == c2:
                return False
        for c in password:
            if c in sp:
                seen.add('-')
            elif c.isupper():
                seen.add("A")
            elif c.islower():
                seen.add('a')
            elif c.isdigit():
                seen.add(1)
            else:
                return False
        return len(seen) == 4
                