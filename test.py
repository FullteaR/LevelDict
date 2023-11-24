from leveldict import LevelDict

db = LevelDict("out")

db.clear()
assert len(db) == 0


db[1] = "a"
db[set(["abc", 5.5])] = "xyz"
assert len(db) == 2

assert db[1] == "a"
assert db[set(["abc", 5.5])] == "xyz"

db[1] = "b"
assert len(db) == 2
assert db[1] == "b"