class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []

        p_dict = Counter(p)

        window = None
        for i in range(0, len(s)-len(p)+1):
            if i == 0:
                window = Counter(s[:len(p)])
                # print(window)
            else:
                window[s[i-1]] -= 1
                window[s[i+len(p)-1]] += 1
                # print(window)

            if len(window - p_dict) == 0:
                result.append(i)

        return result