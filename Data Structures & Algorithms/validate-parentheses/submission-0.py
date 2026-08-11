class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []
        i = 0
        while i < n:
            # if closing came and the stack is nullnot allwoed
            currBracket = s[i]
            if not stack:
                if (
                    currBracket == ")" or currBracket == "]" or currBracket == "}"
                ):  # closing bracket aaya toh ye kro
                    return False
                else:  # opening brakce t aaya toh add krdo
                    stack.append(currBracket)

            else:  # else ki stackhas some values in it

                if (
                    currBracket == "(" or currBracket == "[" or currBracket == "{"
                ):  # opening brakcet hai and kuch kro
                    stack.append(currBracket)

                else:  # stack has some brackets might be open or closed lets stack has-> (([ curr = ]
                    if not (
                        (stack[-1] == "(" and currBracket == ")")
                        or (stack[-1] == "[" and currBracket == "]")
                        or (stack[-1] == "{" and currBracket == "}")
                    ):  # top of stack should be the closing of the bracket
                        return False
                    stack.pop()  # pop that closing brackert as it amtched back
                    # contnue return True
            i += 1
        return len(stack) == 0