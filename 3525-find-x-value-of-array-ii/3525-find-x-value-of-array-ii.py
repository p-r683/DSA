class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        tree = [[1 % k, [0] * k] for _ in range(4 * n)]

        def merge(a, b):
            pa, ca = a
            pb, cb = b

            cnt = ca[:]

            for r in range(k):
                cnt[(pa * r) % k] += cb[r]

            return ((pa * pb) % k, cnt)

        def build(p, l, r):
            if l == r:
                v = nums[l] % k
                tree[p] = (v, [1 if i == v else 0 for i in range(k)])
                return

            m = (l + r) // 2
            build(p * 2, l, m)
            build(p * 2 + 1, m + 1, r)

            tree[p] = merge(tree[p * 2], tree[p * 2 + 1])

        def update(p, l, r, idx, val):
            if l == r:
                v = val % k
                tree[p] = (v, [1 if i == v else 0 for i in range(k)])
                return

            m = (l + r) // 2

            if idx <= m:
                update(p * 2, l, m, idx, val)
            else:
                update(p * 2 + 1, m + 1, r, idx, val)

            tree[p] = merge(tree[p * 2], tree[p * 2 + 1])

        def query(p, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[p]

            m = (l + r) // 2

            if qr <= m:
                return query(p * 2, l, m, ql, qr)

            if ql > m:
                return query(p * 2 + 1, m + 1, r, ql, qr)

            return merge(
                query(p * 2, l, m, ql, qr),
                query(p * 2 + 1, m + 1, r, ql, qr)
            )

        build(1, 0, n - 1)

        ans = []

        for idx, val, start, x in queries:
            update(1, 0, n - 1, idx, val)

            _, cnt = query(1, 0, n - 1, start, n - 1)

            ans.append(cnt[x])

        return ans