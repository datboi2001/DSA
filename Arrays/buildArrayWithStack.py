class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        index = 0
        result = []

        for i in range(1, n + 1):
            if index == len(target):
                break
            else:
                if target[index] == i:
                    result.append("Push")
                    index += 1
                else:
                    result.append("Push")
                    result.append("Pop")
        return result


print(Solution().buildArray([1, 3], 3))