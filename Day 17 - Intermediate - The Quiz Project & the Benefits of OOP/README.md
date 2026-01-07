# Day 17 - The Quiz Project & The Benefits of OOP
___
## Concepts Practised
___
- Classes and Objects
- Attributes and Methods
- Working with attributes, class constructors using the `__init__()` function.
- Adding Methods to a Class
- Modularity

When a function is attached to an `object`, it's called a `method`

```python
class User:
    def __init__(self, username, user_id): # parameters
        # print("new user being created...")
        self.username = username
        self.id = user_id
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("Motoko", "2501") # arguments
# user_1.id = "001"
# user_1.username = "Motoko"

user_2 = User("Bato", "0002")

user_1.follow(user_2)

print(user_1.username, user_1.id, user_1.followers, user_1.following)
print(user_2.username, user_2.id, user_2.followers, user_2.following)
```

## Quiz Project
___
