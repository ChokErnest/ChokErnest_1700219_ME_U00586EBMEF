from itertools import groupby

try:
    xrange
except:
    xrange = range

maxwt = 600 * 100

groupeditems = (
            ("rice", 3190, 250, 6),
            ("papaya", 680, 8, 20),
            ("kangkung", 190, 3, 50),
            ("chicken", 510, 1, 20),
            ("eggs", 1099, 15, 10),
            ("baked beans", 330, 4, 20),
            ("milk powder", 1887, 20, 30),
           )
items = sum( ([(item, wt, val)]*n for item, wt, val,n in groupeditems), [])

def knapsack01_dp(items, limit):
    table = [[0 for w in range(limit + 1)] for j in xrange(len(items) + 1)]

    for j in xrange(1, len(items) + 1):
        item, wt, val = items[j-1]
        for w in xrange(1, limit + 1):
            if wt > w:
                table[j][w] = table[j-1][w]
            else:
                table[j][w] = max(table[j-1][w],
                                  table[j-1][w-wt] + val)

    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j-1][w]

        if was_added:
            item, wt, val = items[j-1]
            result.append(items[j-1])
            w -= wt

    return result


bagged = knapsack01_dp(items, maxwt)
print("Bagged the following %i items\n  " % len(bagged) +
      '\n  '.join('%i of: %s' % (len(list(grp)), item[0])
                  for item,grp in groupby(sorted(bagged))))
print("for a total value of %i and a total weight of %i" % (
    sum(item[2] for item in bagged), sum(item[1] for item in bagged)))
