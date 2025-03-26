class Solution(object):
    def floodFill(self, image, sr, sc, color):
        initial_colour = image[sr][sc]
        if initial_colour == color:
            return image
            
        image[sr][sc] = color

        q = collections.deque()
        q.append((sr, sc))

        dirs = [[0,1], [1,0], [0,-1], [-1,0]]

        while q:
            for i in range(len(q)):
                cur = q.popleft()
                for dire in dirs:
                    nr = cur[0] + dire[0]
                    nc = cur[1] + dire[1]
                    if 0<= nr <len(image) and 0<= nc <len(image[0]):
                        if image[nr][nc] == initial_colour:
                            image[nr][nc] = color
                            q.append((nr, nc))


        return image


        