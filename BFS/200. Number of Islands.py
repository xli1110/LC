from collections import deque


class Solution:
    def is_exceed(self, i, M):
        return i < 0 or i >= M

    def BFS(self, start_i, start_j, grid, searched):
        M = len(grid)
        N = len(grid[0])
        q = deque()
        q.append([start_i, start_j])
        searched[start_i][start_j] = True

        while q:
            point = q.popleft()
            i = point[0]
            j = point[1]

            # top
            if not self.is_exceed(i - 1, M) and grid[i - 1][j] == "1" and not searched[i - 1][j]:
                searched[i - 1][j] = True
                q.append([i - 1, j])
            # bottom
            if not self.is_exceed(i + 1, M) and grid[i + 1][j] == "1" and not searched[i + 1][j]:
                searched[i + 1][j] = True
                q.append([i + 1, j])
            # left
            if not self.is_exceed(j - 1, N) and grid[i][j - 1] == "1" and not searched[i][j - 1]:
                searched[i][j - 1] = True
                q.append([i, j - 1])
            # right
            if not self.is_exceed(j + 1, N) and grid[i][j + 1] == "1" and not searched[i][j + 1]:
                searched[i][j + 1] = True
                q.append([i, j + 1])

    def numIslands(self, grid: [[str]]) -> int:
        if not grid or not grid[0]:
            raise Exception("Empty Matrix")

        num = 0
        searched = [[False] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and not searched[i][j]:
                    self.BFS(i, j, grid, searched)
                    num += 1
        return num


if __name__ == "__main__":
    grid = [["1", "0", "1", "1", "0", "1", "1"]]

    sol = Solution()
    print(sol.numIslands(grid))
