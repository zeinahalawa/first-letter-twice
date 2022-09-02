def repeatedCharacter(self, s):
        array = []
        for counter in range(len(s)):
            array.append(s[counter])
            if array.count(s[counter]) == 2:
                return s[counter]
