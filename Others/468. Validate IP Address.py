class Solution:
    def __init__(self):
        self.decimal = {str(x) for x in range(10)}

        self.hexal = {str(x) for x in range(10)}
        for x in range(ord("a"), ord("a") + 6):
            self.hexal.add(chr(x))
        for x in range(ord("A"), ord("A") + 6):
            self.hexal.add(chr(x))

    def check_4(self, IP):
        arr = IP.split(".")

        # check number of parts
        if len(arr) != 4:
            return False

        for num in arr:
            # check empty number, IP = "1.2..3", arr = ["1", "2", "", "3"]
            if not num:
                return False

            # check leading zero
            if num[0] == "0" and len(num) != 1:
                return False

            # check invalid character
            for ch in num:
                if ch not in self.decimal:
                    return False

            # check exceeding
            if int(num) > 255:
                return False

        return True

    def check_6(self, IP):
        arr = IP.split(":")

        # check number of parts
        if len(arr) != 8:
            return False

        for num in arr:
            # check number length
            if not 1 <= len(num) <= 4:
                return False

            # check invalid character
            for ch in num:
                if ch not in self.hexal:
                    return False

        return True

    def validIPAddress(self, IP: str) -> str:
        if self.check_4(IP):
            return "IPv4"
        if self.check_6(IP):
            return "IPv6"
        return "Neither"


if __name__ == "__main__":
    sol = Solution()
    IP = "172.16.254.10"
    print(sol.validIPAddress(IP))
