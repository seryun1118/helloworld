# 다양한 문제 상황
# 1. 한 지점에서 다른 한 지점까지의 최단 경로
# 2. 한 지점에서 다른 모든 지점까지의 최단 경로
# 3. 모든 지점에서 다른 모든 지점까지의 최단 경로

# 시작점을 기준으로 인접한 방문하지 않은 노드중에서 최단거리가 가장 짧은 노드를 선택한 뒤
# 그 노드를 거쳐가는 거리와 비교하며 최단거리를 갱신하는 방법이다.
# 우선순위큐를 이용하여 구현할 수 있다.

import heapq

V, E, P = map(int, input().split())
# V : 정점의 개수 (2<=V<=5000)
# E : 간선의 개수 (1<=E<=10000)
# P : 건우 위치 (1<=P<=V)
# 방향그래프 초기화
INF = int(1e9)
graph = { i:[] for i in range(V+1)}
# 방향그래프 값 넣어주기
for _ in range(E):
    start, end, value = map(int, input().split())
    graph[start].append([end, value])
    graph[end].append([start, value])

# print(graph)

def dijkstra(start, end):
# 시작지점으로부터 모든 노드까지의 거리를 무한대로 초기화한다.
    distances = [ INF for _ in range(V+1) ]
# 시작지점 -> 시작지점까지 거리 (항상 0)
    distances[start] = 0
# 모든 정점이 저장될 큐 생성
    queue = []
    heapq.heappush(queue, [0,start]) # 시작 노드부터 탐색시작하기 위함.

# queue에 남아있는 노드가 없을때까지 반복
    while queue:
        # 탐색할 거리, 현재 방문 노드
        dist, now = heapq.heappop(queue)
        #기존 값보다 크면 아래 탈 필요 없음
        if distances[now] < dist: continue
        # 현재 방문 노드 기준으로 인접 노드 탐색
        for nNode, weight in graph[now]:
            # 인접 노드까지 거리
            newDist = dist + weight
            # 만약 시작 정점에서 인접 정점으로 바로 가는 것보다, 현재 정점을 통해 가는 것이 가까우면
            if newDist < distances[nNode]:
                distances[nNode] = newDist # 업데이트 해주기
                heapq.heappush(queue, [newDist, nNode])


    return distances[end]

if dijkstra(1,V) == dijkstra(1,P) + dijkstra(P,V):
    print('SAVE HIM')
else:
    print('GOOD BYE')
