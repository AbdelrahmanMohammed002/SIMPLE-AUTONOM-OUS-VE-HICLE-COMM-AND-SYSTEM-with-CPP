from Vehicle import Vehicle
from CommandHandler import CommandHandler


# Example usage:
commands = [
    {"type": "speed", "value": 5},  # Set speed to 5.
    {"type": "move", "value": 100},  # Move 100 units at speed 5.
    {"type": "turn", "value": 90},  # Turn 90 degrees (now facing south).
    {"type": "move", "value": 50},  # Move 50 units in the new direction.
    {"type": "speed", "value": -10},  # Invalid speed, should raise CommandError.
    {"type": "turn", "value": 360},  # Full turn, direction remains unchanged.
    {"type": "move", "value": 50},  # Move 50 units at speed 5.
    {"type": "fly", "value": 10},  # Invalid command type, should raise CommandError.
]

# Create a Vehicle instance.
vehicle = Vehicle()

# Create a CommandHandler instance to manage vehicle commands.
handler = CommandHandler(vehicle)

# Execute the list of commands.
handler.execute_commands(commands)
