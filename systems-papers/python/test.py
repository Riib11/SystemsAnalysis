# import authors.author_stats as a_stats

# hindecies = a_stats.getAllAuthorHIndecies()
# print(hindecies)

def f(k,d={}):
    d[k] = 1
    return d

print(f("A"))
print(f("B"))
print(f("C"))