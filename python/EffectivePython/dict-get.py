# dict用get处理值不存在的情况是最佳的
votes = {
    'bread': ['kitty', 'Vikky'],
    'ramen': ['suzuki', 'watanabe'],
}

key = 'curry'
who = 'ryouhei'

# 一般的处理in
if key in votes:
    names = votes[key]
else:
    votes[key] = names = []
names.append(who)
print(votes)


# KeyError处理
try:
    names = votes[key]
except KeyError:
    votes[key] = names = []
names.append(who)


# get!
names = votes.get(key)
if names is None:
    votes[key] = names = []
names.append(who)

# better!
if names := votes.get(key) is None:
    votes[key] = names = []
names.append(who)
