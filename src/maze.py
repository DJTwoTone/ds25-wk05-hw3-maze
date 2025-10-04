def find_path(grid, start, end):
    R = len(grid)
    C = len(grid[0]) if R else 0
    sr, sc = start
    er, ec = end
    if not (0 <= sr < R and 0 <= sc < C and 0 <= er < R and 0 <= ec < C):
        return None
    if grid[sr][sc] == 1 or grid[er][ec] == 1:
        return None

    visited = [[False]*C for _ in range(R)]

    def dfs(r, c):
        if (r, c) == (er, ec):
            return [(r, c)]
        visited[r][c] = True
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and grid[nr][nc] == 0:
                p = dfs(nr, nc)
                if p is not None:
                    return [(r, c)] + p
        return None

    return dfs(sr, sc)
