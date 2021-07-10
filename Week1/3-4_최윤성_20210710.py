case = int(input())
door = (input() == "1")
print("Love is open door" if case > 5 else "\n".join(["101010"[int(door) + i] for i in range(case - 1)]))