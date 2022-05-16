#!/usr/bin/python3

__doc__ = """并查集可以压缩路径

"""
class UnionFind:
    def __init__(self, n: int):
        """初始化一个1-n的集合

        1、初始时各人都是各人的父节点
        2、当前连通分量
        """
        self.parent = list(range(n))
        self.size = [1] * n
        self.n = n
        # 当前连通分量数目
        self.setCount = n

    def findset(self, x: int) -> int:
        if self.parent[x] == x:
            return x
        # 不断递归查找x的根节点
        self.parent[x] = self.findset(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> bool:
        """合并两个节点x,y所在的集合

        1、首先找到x和y的根节点
        2、然后将小集合归并到大集合上，并更新小集合根节点的parent为x
        3、更新集合大小与集合数目
        """
        x, y = self.findset(x), self.findset(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        self.setCount -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        x, y = self.findset(x), self.findset(y)
        return x == y