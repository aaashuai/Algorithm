#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class ChainLRU:
    def __init__(self, length: int = 5):
        self.length = length
        self.start = Node(0)

    def put(self, val):
        if self.start.next is None:
            self.start.next = Node(val)
            return
        # 判断是否在链表中
        prev = self.start
        cur = self.start.next
        length = 0
        while cur is not None:
            length += 1
            # 如果相等,则拿到链表首部
            if cur.val == val:
                prev.next = cur.next
                cur.next = self.start.next
                self.start.next = cur
                return
            prev = cur
            cur = cur.next

        # 如果满了, 就把最后一个扔掉
        if length == self.length:
            pass

        # 如果没满就放在链表首部
        else:
            pass


    def throughout(self):
        ret = []
        cur = self.start.next
        while cur is not None:
            ret.append(cur.val)
            cur = cur.next
        return ret

    def clear():
        pass


class ChainLRUTest:
    def __init__(self):
        self.lru_cache = ChainLRU(length=5)

    def test_put(self):
        for i in range(5):
            self.lru_cache.put(i)

        self.lru_cache.put(0)
        assert self.lru_cache.get() == [0, 4, 3, 2, 1]


if __name__ == '__main__':
    c = ChainLRU()
    c.put("3")
    print(c.throughout())
