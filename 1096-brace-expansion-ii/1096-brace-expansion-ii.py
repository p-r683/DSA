class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:

        def parse(i):
            res = set()
            cur = {""}

            while i < len(expression) and expression[i] != '}':
                
                if expression[i] == '{':
                    part, i = parse(i + 1)

                elif expression[i] == ',':
                    res |= cur
                    cur = {""}
                    i += 1
                    continue

                else:
                    part = {expression[i]}
                    i += 1

                cur = {a + b for a in cur for b in part}

            res |= cur

            if i < len(expression) and expression[i] == '}':
                i += 1

            return res, i

        ans, _ = parse(0)
        return sorted(ans)