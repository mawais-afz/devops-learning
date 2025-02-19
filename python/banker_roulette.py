import random


friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# Options 1:
random_friend = friends[random.randint(0, len(friends) - 1)]
print(random_friend)

# Options 2:
random_friend1 = random.choice(friends)
print(random_friend1)
