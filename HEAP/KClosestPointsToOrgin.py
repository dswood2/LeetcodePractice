"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane 
and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is 
the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be 
unique (except for the order that it is in).

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]

Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]

Explanation: The answer [[-2,4],[3,3]] would also be accepted.
 
Constraints:
1 <= k <= points.length <= 104
-104 < xi, yi < 104

"""

import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        answer=[]
        heapq.heapify(answer)
        for row in points:
            distance = -1*((row[0])**2 + (row[1])**2) #help create max heap
            if len(answer) < k: #create maxHeap of length k
                heapq.heappush(answer, (distance,row))
            else: #since numbers are negative it will bring the most negative number to the top and pop it.  Keeping the kth smallest number of points in heap
                heapq.heappushpop(answer, (distance,row))
        k-=1
        print(answer)
        while k >= 0:# trimming dictionary
            answer[k]=answer[k][1]
            k-=1
        return(answer)

#This can all be done in one line by the following:
    #return sorted(points,key = lambda p:p[0]*p[0]+p[1]*p[1])[:K]

testSet = [[1,3],[-2,2]]
k = 2
test = Solution()
print(test.kClosest(testSet,k))

