import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        sorted_c = sorted(courses,key = lambda x: x[1])
        max_d = []
        heapq.heapify(max_d)
        current = 0
        ans = 0
        for dur, dead in sorted_c:
            current += dur
            heapq.heappush(max_d, -dur)
            ans += 1
            if current > dead:
                p = -heapq.heappop(max_d)
                current -= p
                ans -= 1
                
        return ans


        
