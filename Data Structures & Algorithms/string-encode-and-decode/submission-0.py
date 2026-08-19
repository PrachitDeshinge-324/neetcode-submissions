class Solution:

    def encode(self, strs: List[str]) -> str:
        f=""
        for t in strs:
            f+=t
            f+='\n'
        return f

    def decode(self, s: str) -> List[str]:
        return s.split('\n')[:-1]