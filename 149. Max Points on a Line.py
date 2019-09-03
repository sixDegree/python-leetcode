'''

2D平面上，最多有多少个点在一条直线上

Given n points on a 2D plane, 
find the maximum number of points that lie on the same straight line.

Example 1:

```
Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
```

Example 2:

```
Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
```

NOTE: 
input types have been changed on April 15, 2019. 
Please reset to default code definition to get new method signature.
'''

import math

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        n = len(points)
        if n<=2:
            return n

        max_cnt = 0
        for i in range(0,n):
            i_map = {}
            dup = 0
            cnt = 0
            for j in range(0,n):
                if i == j:
                    continue
                if points[i]==points[j]:
                    dup+=1
                    continue
                # print(points[i],points[j])
                dx = points[i][0]-points[j][0]
                dy = points[i][1]-points[j][1]

                a,b,c = 0,0,None
                if dx == 0:
                    c = 'x='+str(points[i][0])
                elif dy == 0:
                    c = 'y='+str(points[i][1])
                else:
                    # a = dy/dx
                    # b = points[i][1]-a*points[i][0]
                    t = math.gcd(dy,dx)
                    dy=dy//t
                    dx=dx//t
                    a = "%d/%d" % (dy,dx)
                    b = "%d/%d" % ((points[i][1]*dx-dy*points[i][0]),dx) 

                g = (a,b,c)
                i_map[g] = i_map.get(g,0)+1

            print(points[i],i_map)
            if len(i_map)>0:
                cnt = max(i_map.values())
            cnt += dup
            if max_cnt<cnt:
                max_cnt=cnt

        return max_cnt+1

    def maxPoints2(self,points):
        n = len(points)
        if n<=2:
            return n

        max_cnt = 0
        for i in range(0,n-1):
            dup = 0
            for j in range(i+1,n):
                cnt=0
                if points[j]==points[i]:    # i & j can't determine a line
                    dup+=1
                else:
                    # search [j+1,n-1], find points in line i & j
                    cnt=1+self.getLinePoints(i,j,n,points)
                cnt+=dup
                if max_cnt < cnt:
                    max_cnt = cnt
        return max_cnt+1


    def getLinePoints(self,i,j,n,points):
        dup = 0
        cnt = 0
        j_dx = points[j][0]-points[i][0]
        j_dy = points[j][1]-points[i][1]
        for k in range(j+1,n):
            if points[k]==points[j]:
                dup+=1
                continue
            k_dx = points[k][0]-points[i][0]
            k_dy = points[k][1]-points[i][1]
            if j_dy*k_dx == j_dx*k_dy:
                cnt+=1
        return cnt+dup
  

if __name__ == '__main__':

    points_cases=[
        [[0,0],[1,0],[-1,0],[0,1],[0,-1]],
        [[1,1],[2,2],[3,3]],
        [[1,1],[1,1],[2,2],[2,2]],
        [[1,1],[1,1],[1,1]],
        [[1,1],[1,1],[1,1],[1,1]],
        [[0,0],[94911151,94911150],[94911152,94911151]],
        [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]],
        [[0,0],[1,1],[0,0]]
    ]

    expect_results=[3,3,4,3,4,2,4,3]

    solution = Solution()
    for i in range(0,len(points_cases)):
        result = solution.maxPoints2(points_cases[i])
        print(i,":",points_cases[i],"result:",result,"expect:"
            ,expect_results[i],result==expect_results[i])
    print('done')

    # points=[[0,0],[1,0],[-1,0],[0,1],[0,-1]]
    # points=[[1,1],[2,2],[3,3]]
    # points=[[1,1],[1,1],[2,2],[2,2]]
    # points=[[1,1],[1,1],[1,1],[1,1]]
    # points=[[0,0],[94911151,94911150],[94911152,94911151]]
    # points=[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    # points = [[0,0],[1,1],[0,0]]

    # solution = Solution()
    # result = solution.maxPoints2(points)
    # print(points,"result:",result)

    # import matplotlib.pyplot as plt
    # import numpy as np 

    # n = len(points_cases)
    # col = 3
    # row = n//3+1

    # plt.figure(1)
    # for i in range(0,n):
    #     plt.subplot(row,col,i+1)
    #     a = np.array(points_cases[i])
    #     plt.scatter(a[:,0],a[:,1],)
    # plt.show()



