def solution(rows, columns, queries):
    answer = []
    
    grid = [[0] * columns for _ in range(rows)]
    num = 0
    for i in range(rows):
        for j in range(columns):
            num += 1
            grid[i][j] = num
    
    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        tmp = grid[x1][y1]
        minimum = tmp
        
        for x in range(x1, x2):
            value = grid[x + 1][y1]
            grid[x][y1] = value
            minimum = min(minimum, value)
        
        for y in range(y1, y2):
            value = grid[x2][y + 1]
            grid[x2][y] = value
            minimum = min(minimum, value)
        
        for x in range(x2, x1, -1):
            value = grid[x - 1][y2]
            grid[x][y2] = value
            minimum = min(minimum, value)
            
        for y in range(y2, y1, -1):
            value = grid[x1][y - 1]
            grid[x1][y] = value
            minimum = min(minimum, value)
            
        grid[x1][y1 + 1] = tmp
        answer.append(minimum)

    return answer