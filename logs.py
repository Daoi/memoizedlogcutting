def memoize(f):
    omemo = []
    memo = {}

    def helper(p, n):
        if p not in omemo:
            memo.clear()
            omemo.clear()
            omemo.append(p)
        if n not in memo:
            memo[n] = f(p, n)
        return memo[n]

    return helper


@memoize
def cut_log(p, n):
   if (n == 0):
      return 0
   q = -1
   for i in range(1, n+1):
      q = max(q, p[i] + cut_log(p, n-i))
   return q


'''
def cut_log(p, n):
    log = [0]
    for _ in range(n):
        log.append(max(pi + li for pi, li in zip(p[1:], log[::-1])))
    return log[n]
'''