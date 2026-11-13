class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        def h(i):
            if i ==len(words):
                return ""

            return h(i +1) + " " + words[i]

        return h(0).strip()