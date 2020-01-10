class Solution:
    pre_time = None
    post_time = None

    adjacent_list = None

    pre_time_cnt = 0
    post_time_cnt = 0

    def set_collections(self, n):
        self.pre_time = [None for _ in range(n)]
        self.post_time = [None for _ in range(n)]
        self.adjacent_list = [list() for _ in range(n)]

    # 위상정렬 물어보는 문제
    # 위상정렬은 pre_time, post_time, DFS로 구현
    def findOrder(self, numCourses, prerequisites):
        self.set_collections(numCourses)

        for v1, v2 in prerequisites:
            self.adjacent_list[v2].append(v1)

        for v in range(numCourses):
            if not self.pre_time[v]:
                is_cyclic = self.is_cyclic(v)
                # 그래프에 사이클이 존재하면 위상정렬이 불가하므로 빈 리스트를 리턴한다.
                if is_cyclic:
                    return []

        ordered_result = []
        for vertex, p_time in enumerate(self.post_time):
            ordered_result.append((vertex, p_time))

        # post_time이 큰 정점일수록 source에 가깝고, 작은 정점일수록 sink에 가깝다.
        # 각 정점의 post_time 을 내림차순 정렬한 결과를 리턴한다.
        ordered_result = sorted(ordered_result, key=lambda x: x[1], reverse=True)
        return [x[0] for x in ordered_result]

    def is_cyclic(self, v):
        self.pre_time_cnt += 1
        self.pre_time[v] = self.pre_time_cnt

        for adj_v in self.adjacent_list[v]:
            if self.pre_time[adj_v]:
                if not self.post_time[adj_v]:
                    return True
            else:
                result = self.is_cyclic(adj_v)
                if result:
                    return True

        self.post_time_cnt += 1
        self.post_time[v] = self.post_time_cnt

        return False
