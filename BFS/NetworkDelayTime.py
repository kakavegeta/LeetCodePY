class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        def find_lowest_dist_node(dist, processed):
            lowest_dist = float('inf')
            lowest_dist_node = None
            for node in dist:
                d = dist[node]
                if d < lowest_dist and node not in processed:
                    lowest_dist = d
                    lowest_dist_node = node
            return lowest_dist_node
        graph, dist, parent = {}, {}, {}
        processed = []
        for u, v, w in times:
            if u in graph.keys():
                graph[u].update({v:w})
            else:
                graph[u] = {v:w}
        for i in range(1, N+1):
            dist.update({i: float('inf')})
            parent.update({i: None})
        dist[K] = 0
        node = find_lowest_dist_node(dist, processed)
        print(node)
        while node is not None:
            d = dist[node]
            if node not in graph.keys():
                processed.append(node)
                node = find_lowest_dist_node(dist, processed)
                continue
            neighbors = graph[node]
            for n in neighbors.keys():
                new_d = d + neighbors[n]
                if dist[n] > new_d:
                    dist[n] = new_d
                    parent[n] = node
            processed.append(node)
            node = find_lowest_dist_node(dist, processed)
            print(dist)
        ans = max(dist.values())
        return ans if ans<float('inf') else -1

if __name__ == "__main__":
    sol = Solution()
    Input = [[2,1,1],[2,3,1],[3,4,1]]
    print(sol.networkDelayTime(Input, 4, 2))

