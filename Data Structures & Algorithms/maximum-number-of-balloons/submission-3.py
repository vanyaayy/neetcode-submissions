class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        have = Counter(text)
        need = Counter("balloon")
        return min(have[c]//need[c] for c in "balloon")
        