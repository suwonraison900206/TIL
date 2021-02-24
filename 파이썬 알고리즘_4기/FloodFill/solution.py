# 방문처리 해서 풀었습니다.

def solution(n, m, image):
    visit = [[0] * m for __ in range(n)]
    cnt = 0
    dir = [(-1,0), (0,1), (1,0), (0,-1)]

    for i in range(n):
        for j in range(m):
            if visit[i][j] == 0:
                target_number = image[i][j]
                visit[i][j] = 1
                stack = [(i,j)]

                while stack:
                    dx,dy = stack.pop()

                    for q in range(4):
                        di = dx + dir[q][0]
                        dj = dy + dir[q][1]

                        if 0 <= di < n and 0 <= dj < m and image[di][dj] == target_number and visit[di][dj] == 0:
                            stack.append((di,dj))
                            visit[di][dj] = 1

                cnt += 1

    return cnt

n = 2
m = 3
images = [[1,2,3] , [3,2,1]]

solution(n,m,images)