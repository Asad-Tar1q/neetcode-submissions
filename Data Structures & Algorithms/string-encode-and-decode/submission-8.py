class Solution:

    def encode(self, strs: List[str]) -> str:
        parts = []
        for word in strs:
            parts.append("#")
            parts.append(str(len(word)))
            parts.append("#")
            parts.append(word)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(s):
            i += 1                              # skip first '#'

            j = i
            while s[j] != "#":                  # read digits until next '#'
                j += 1
            length = int(s[i:j])

            word = s[j + 1 : j + 1 + length]    # skip second '#', take length chars
            decoded_str.append(word)

            i = j + 1 + length                  # now at next '#'

        return decoded_str