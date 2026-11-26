class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hashmap = {}
        for i in range(1, n + 1):
            hashmap[i] = [0,0] #[no of people trusting i, no of people i is trusting]

        for i in trust:
            ai,bi = i
            hashmap[ai][1] += 1
            hashmap[bi][0] += 1

        judge = -1
        for key, value in hashmap.items():
            if value[0] == n - 1:
                if value[1] == 0:
                    if judge == -1:
                        return key
        return judge
