def dfs(visited, computer, computers):
    visited[computer] = True
    
    for another, connected in enumerate(computers[computer]):
        if  connected == 1 and not visited[another]:
            dfs(visited, another, computers)
    
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for computer in range(n):
        if not visited[computer]:
            dfs(visited, computer, computers)
            answer += 1
            
    return answer