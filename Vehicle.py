
from CommandError import CommandError

class Vehicle:
    """A class to simulate a vehicle's movement, direction, and speed control.
    
    This class provides methods to set the vehicle's speed, move it in the current
    direction, and turn by adjusting its direction.
    """
    
    def __init__(self):
        """Initialize the vehicle with a default position, speed, and direction.
        
        Attributes:
            x (float): The x-coordinate of the vehicle.
            y (float): The y-coordinate of the vehicle.
            speed (int): The vehicle's speed (initially 0).
            direction (int): The vehicle's direction in degrees (initially 90, facing east).
            history (list): A log of all commands executed on the vehicle.
        """
        self.x = 0.0  # x-coordinate
        self.y = 0.0  # y-coordinate
        self.speed = 0  # Speed of the vehicle
        self.direction = 0  # Initial direction facing 'North' (0 degrees)
        self.history = []  # History of executed commands
    
    def set_speed(self, speed):
        """Set the speed of the vehicle.

        Args:
            speed (int): The speed to set (must be non-negative).

        Raises:
            CommandError: If the speed is negative.

        Records the action in the history.
        """
        if speed < 0:
            raise CommandError({"type": "speed", "value": speed}, "Speed cannot be negative")
        self.speed = speed
        self.history.append(f"Speed set to {speed}")
    
    def move(self, distance):
        """Move the vehicle a certain distance in the current direction.

        The movement is based on the current speed and direction of the vehicle.

        Args:
            distance (float): The distance to move.

        Raises:
            CommandError: If the speed is 0, as the vehicle cannot move.

        Records the action in the history.
        """
        if self.speed == 0:
            raise CommandError({"type": "move", "value": distance}, "Speed is 0, cannot move")
        
        import math
        # Convert the direction to radians for calculation.
        radians = math.radians(self.direction)
        self.x += distance * math.cos(radians)
        self.y += distance * math.sin(radians)
        self.history.append(f"Moved {distance} units")
    
    def turn(self, degrees):
        """Turn the vehicle by adjusting its direction.

        Args:
            degrees (int): The degrees to turn (can be positive or negative).
        
        Records the action in the history.
        """
        self.direction = (self.direction + degrees) % 360
        self.history.append(f"Turned {degrees} degrees")
    
    def __str__(self):
        """Return a human-readable string describing the vehicle's current state.

        Example output:
            "Position: (x, y), Speed: speed, Direction: direction°"
        """
        return f"Position: ({self.x:.1f}, {self.y:.1f}), Speed: {self.speed}, Direction: {self.direction}°"

    def __repr__(self):
        """Return a formal string representation of the vehicle's state.

        This is mainly used for debugging purposes.
        """
        return f"Vehicle(Position=({self.x:.1f}, {self.y:.1f}), Speed={self.speed}, Direction={self.direction})"
