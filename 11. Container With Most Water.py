'''
非负整数数组，X轴上有不同高度的墙，选2堵墙，使得它们与X轴形成的容器可容纳最多的水
eg:
    [1,8,6,2,5,4,8,3,7] => choose [1]=8 & [8]=7 => (8-1)*7 = 49

Given n non-negative integers a1, a2, ..., an , 
where each represents a point at coordinate (i, ai). 

n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, 
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

![pic](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.


Example:

```
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```

'''


class Solution(object):
    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)

        i=0
        j=n-1
        max_area=0

        while i<j:
            area=min(height[i],height[j])*(j-i)
            max_area=max(max_area,area)
            # 矩形区域的面积受限于较短的线段，将指向较短线段的指针移动一步
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_area
        

if __name__ == '__main__':

    height = [1,8,6,2,5,4,8,3,7]

    solution = Solution()
    result = solution.maxArea(height)
    print(result)

