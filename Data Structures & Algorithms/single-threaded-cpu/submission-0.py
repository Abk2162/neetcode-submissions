class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)], reverse=True)
        
        pending = []  # Min-heap storing (processingTime, index)
        res = []
        timer = 0
        
        while indexed_tasks or pending:
            # If CPU is idle and nothing is ready, jump directly to next arrival
            if not pending and timer < indexed_tasks[-1][0]:
                timer = indexed_tasks[-1][0]
                
            while indexed_tasks and indexed_tasks[-1][0] <= timer:
                enq, proc, idx = indexed_tasks.pop()
                heapq.heappush(pending, (proc, idx))
             
            proc, idx = heapq.heappop(pending)
            timer += proc
            res.append(idx)
            
        return res