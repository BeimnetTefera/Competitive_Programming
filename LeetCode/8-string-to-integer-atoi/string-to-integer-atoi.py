class Solution:
    def myAtoi(self, s: str) -> int:
        res = []
        ptr = 0
        sign = 1
        sign_seen = False

        while ptr < len(s):
            # if the char is digit
            if s[ptr].isdigit():
                # if it is not zero add it to res directly
                if s[ptr] != "0":
                    res.append(s[ptr])

                # if it is zero we check 2 things
                else:
                    # if res is empty
                    if not res:
                        # if the next value is digit we move our pointer
                        if ptr + 1 < len(s) and s[ptr + 1].isdigit():
                            ptr += 1
                            continue
                        # if not we add zero into res
                        else:
                            res.append(s[ptr])
                            break
                    else:
                        res.append(s[ptr])

            # if the char is not digit
            else:
                # if it is space we move our pointer only if parsing hasn't started
                if s[ptr] == " ":
                    if res or sign_seen:
                        break
                    ptr += 1
                    continue

                # if it is alphabet we stop there
                elif s[ptr].isalpha():
                    break

                # if it is "-" or "+"
                elif s[ptr] == "-" or s[ptr] == "+":
                    if not res and not sign_seen:
                        if s[ptr] == "-":
                            sign *= -1
                        sign_seen = True
                    else:
                        break

                # invalid symbols
                else:
                    break

            # move the ptr forward
            ptr += 1

        # if res is empty we return 0
        if not res:
            return 0

        # if it has value change it integer and multiply it with sign then return
        val = int("".join(res)) * sign

        if val > (2**31 - 1):
            return 2**31 - 1
        elif val < (-2**31):
            return -2**31

        return val