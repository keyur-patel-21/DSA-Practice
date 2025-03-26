class Solution(object):
    def floodFill(self, image, sr, sc, color):
        initialColor = image[sr][sc]

        if initialColor == color:
            return image
        dirs = [[0,1], [0,-1], [-1,0], [1,0]]
        def dfs(image, sr, sc, color, initialColor, dirs):
            # base
            image[sr][sc] = color

            # logic
            for dire in dirs:
                nr = sr + dire[0]
                nc = sc + dire[1]
                if 0<=nr<len(image) and 0<=nc<len(image[0]):
                    if image[nr][nc] == initialColor:
                        dfs(image, nr, nc, color, initialColor, dirs)

            

        dfs(image, sr, sc, color, initialColor, dirs)
        return image

        