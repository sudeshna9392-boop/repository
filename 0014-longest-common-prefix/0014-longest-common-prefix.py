class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Start with the first string as the prefix
        prefix = strs[0]
        
        # Compare the prefix with each string
        for s in strs[1:]:
            # Reduce prefix until it matches the start of s
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix


# Example usage
words = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(words))  # Output: "fl"
        