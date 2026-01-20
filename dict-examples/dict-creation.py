score = {"tamil": 56, "english": 65, "math": 64}

print(score)
print(type(score))
# print(dir(score))

# get ("tamil") -> 56
# update ({ "tamil": 60, "science": 45 })
# get ("tamil") -> 60

ta = score.get("tamil")
print(ta)

score.update({"tamil": 60})
score.update({"science": 60})
print(score)

# items = score.items()
# print(items)

# values = score.values()
# print(values)

# keys = score.keys()
# print(keys)

# NO-SQL
# Key-Value Pairs
# Redis
# Mongo-DB
