class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sources = {src for src,_ in paths}
        for _,dst in paths:
            if dst not in sources:
                return dst
