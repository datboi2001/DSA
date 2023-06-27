from typing import List

def permutations(letters: str) -> List[str]:
    # WRITE YOUR BRILLIANT CODE HERE
    def dfs(seen: List[bool], path: List[str], res: List[str]):
        if len(path) == len(letters):
            res.append(''.join(path))
            return
        
        for i, char in enumerate(letters):
            if seen[i]:
                continue
            path.append(char)
            seen[i] = True
            dfs(seen, path, res)
            path.pop()
            seen[i] = False

    res = []
    if len(letters) > 0:
        dfs([False] * len(letters), [], res)
    return res

if __name__ == '__main__':
    letters = input()
    res = permutations(letters)
    for line in res:
        print(line)
