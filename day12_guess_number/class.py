################### Scope ####################

# enemies = 1


# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")


# increase_enemies()
# print(f"enemies outside function: {enemies}")


""" enemies = "xy"


def increase_enemies():
    enemies = "ab"
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}") """


enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
