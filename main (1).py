Certainly! Here's a Python implementation of the `Player`, `Batsman`, and `Bowler` classes, along with a program to create objects of each class and call their `play()` methods:

```python
# Define the Player class
class Player:
    def play(self):
        print("The player is playing cricket")

# Define the Batsman class, derived from Player
class Batsman(Player):
    def play(self):
        print("The batsman is batting")

# Define the Bowler class, derived from Player
class Bowler(Player):
    def play(self):
        print("The bowler is bowling")

# Create objects of the Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()
```

When you run this program, it will create objects of the `Batsman` and `Bowler` classes and call their `play()` methods, producing the following output:

```
The batsman is batting
The bowler is bowling
```

This demonstrates the concept of inheritance and method overriding in object-oriented programming, where the derived classes (`Batsman` and `Bowler`) override the `play()` method from the base class (`Player`) to provide their specific behavior.