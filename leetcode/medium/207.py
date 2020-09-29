class Solution:
    # 그래프에 사이클 유무를 물어보는 것.
    # 사이클이 있으면 False를 리턴하고 없으면, 즉 DAG(Directed Acyclic Graph)이면 True를 리턴함.
    def canFinish(self, numCourses, prerequisites) -> bool:
        adjacent_list = [list() for _ in range(numCourses)]
        for v1, v2 in prerequisites:
            adjacent_list[v2].append(v1)

        pre_time = [None for _ in range(numCourses)]
        post_time = [None for _ in range(numCourses)]

        for i in range(numCourses):
            if not pre_time[i]:
                result = self.is_cyclic(i, adjacent_list, pre_time, post_time)
                if result:
                    return False
        return True

    # DFS와 pre_time, post_time을 이용하여 그래프에 사이클을 찾아낸다.
    def is_cyclic(self, init_v, adjacent_list, pre_time, post_time):
        stack = list()
        stack.append(init_v)

        pre_time_cnt = 1
        pre_time[init_v] = pre_time_cnt

        post_time_cnt = 0

        while stack:
            v = stack[-1]
            is_pushed = False

            for adj_v in adjacent_list[v]:
                if pre_time[adj_v]:
                    if not post_time[adj_v]:
                        return True
                else:
                    pre_time_cnt += 1
                    pre_time[adj_v] = pre_time_cnt
                    stack.append(adj_v)
                    is_pushed = True
                    break

            if not is_pushed:
                complete_v = stack.pop(-1)
                post_time_cnt += 1
                post_time[complete_v] = post_time_cnt

        return False
