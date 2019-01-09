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
        """
        emap = {e.id: e for e in employees}
        dfs = lambda eid: emap[eid].importance + sum([dfs(e) for e in emap[eid].subordinates]) # e: employee_id
        return dfs(id)