__author__ = "ResearchInMotion"


candidates = [2,3,6,7]
target = 7


def combinationSum(candidates, target):
    dp = [[] for i in range(target + 1)]

    for c in candidates:
        for i in range(target + 1):
            if i < c: continue
            if i == c:
                dp[i].append([c])
            else:
                for blist in dp[i - c]:
                    dp[i].append(blist + [c])
    return dp[target]


print(combinationSum(candidates,target))


