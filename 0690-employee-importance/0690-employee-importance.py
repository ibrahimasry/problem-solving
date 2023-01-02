"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp = {e.id:e for e in employees}
        
        def dfs(curr):
            employee = emp[curr]
            return (employee.importance + sum(dfs(eid) for eid in employee.subordinates))
        return dfs(id)
            