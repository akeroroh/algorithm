from collections import deque

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        image_height = len(image)
        image_length = len(image[0])

        visited = [[0] * image_length for _ in range(image_height)]
        start_color = image[sr][sc]

        q = deque()
        q.extend([(sr, sc)])

        while q:
            temp = []
            while q:
                x, y = q.pop()
                print(x, y)
                for i, j in move:
                    dx = x+i
                    dy = y+j
                    # print("dx, dy")
                    # print(dx, dy)
                    if 0 <= dx < image_height and 0 <= dy < image_length:
                        if not visited[dx][dy] :
                            visited[dx][dy] = True
                            if image[dx][dy] == start_color:
                                image[dx][dy] = color
                                # print(image)
                                temp.append((dx, dy))
            q = temp
            # print(q)

        # print(image)

        return image


        