import myhash

h = myhash.HashTable()
h[54] = "cat"
h[26] = "dog"
h[93] = "lion"
print(h.slots)
print(h.data)
print(h[54])
