from collections import defaultdict
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        adj = defaultdict(str)
        for src, dst in paths:
            adj[src]=dst
        for src, dst in paths:
            if dst not in adj:
                return dst

        pass
