def combinationSum(candidates, target):
    candidates.sort()
    path = []
    result = []

    def backtracking(candidates, target, total, startidx):

        if total == target:
            result.append(path[:])
            return
        for i in range(startidx, len(candidates)):
            if total + candidates[i] > target:
                return
            total += candidates[i]
            path.append(candidates[i])
            backtracking(candidates, target, total, i)
            total -= candidates[i]
            path.pop()

    backtracking(candidates, target, 0, 0)
    return result


candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))
