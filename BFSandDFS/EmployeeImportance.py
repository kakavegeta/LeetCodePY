"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        this is a DFS method
        """
        emap = {e.id: e for e in employees}
        dfs = lambda eid: emap[eid].importance + sum([dfs(e) for e in emap[eid].subordinates]) # e: employee_id
        return dfs(id)

class Solution2:
    def getImportance(self, employees, id):
        """
        BFS method
        since there is no backward edge, we do not need to check whether an employee has been visited
        """
        emap = {e.id: e for e in employees}
        score = 0
        frontier = []
        frontier.append(emap[id])
        while frontier:
            employee = frontier.pop()
            score += employee.importance
            frontier.extend([emap[eid] for eid in employee.subordinates])
        return score
