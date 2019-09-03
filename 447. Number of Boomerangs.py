'''
平面上n个点，多少个三元组(i,j,k), distace(i,j) = distance(i,k)


Given n points in the plane that are all pairwise distinct, 
a "boomerang" is a tuple of points (i, j, k) 
such that the distance between i and j equals the distance between i and k 
(the order of the tuple matters).

Find the number of boomerangs. 
You may assume that n will be at most 500 
and coordinates of points are all in the range [-10000, 10000] 
(inclusive).

Example:
```
Input: [[0,0],[1,0],[2,0]]
Output: 2
Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
```
'''

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        n = len(points)
        if n<3:
            return 0

        total=0
        for i in range(0,n):
            i_map={}
            for j in range(0,n):
                if i==j:
                    continue
                dist = (points[j][0]-points[i][0])**2 + (points[j][1]-points[i][1])**2
                # print(points[i],points[j],dist)
                i_map[dist]=i_map.get(dist,0)+1

            # print(points[i],i_map)
            i_total=0
            for cnt in i_map.values():
                i_total+=cnt*(cnt-1) 
            total+=i_total
        return total
        

if __name__ == '__main__':

    points=[[0,0],[1,0],[2,0]]

    # points=[[0,0],[1,0],[2,0],[1,1]]

    # points=[[0,0],[1,0],[-1,0],[0,1],[0,-1]]

    solution = Solution()
    result = solution.numberOfBoomerangs(points)
    print(result)



