# While loop example
print("=== While Loop ===")
count = 0
while count < 3:
    print(f"While loop iteration: {count}")
    count += 1

# For loop example
print("\n=== For Loop ===")
for i in range(3):
    print(f"For loop iteration: {i}")

# Do-While loop simulation (Python doesn't have native do-while)
print("\n=== Do-While Loop (Simulated) ===")
num = 0
while True:
    print(f"Do-While loop iteration: {num}")
    num += 1
    if num >= 3:
        break