
from CommandError import CommandError

class CommandHandler:
    """A class to process and execute commands for the Vehicle class.
    
    This class handles validation of commands and calls the appropriate methods on the vehicle.
    """
    VALID_COMMANDS = {"speed", "move", "turn"}  # Set of valid command types.

    def __init__(self, vehicle):
        """Initialize the CommandHandler with a vehicle instance.

        Args:
            vehicle (Vehicle): The vehicle instance on which commands will be executed.
        """
        self.vehicle = vehicle
    
    def process_command(self, command):
        """Process an individual command.

        Validates the command type and executes the corresponding vehicle method.

        Args:
            command (dict): A dictionary with keys "type" and "value".
                - "type" is the type of command ("speed", "move", or "turn").
                - "value" is the value associated with the command (e.g., the speed or distance).

        Raises:
            CommandError: If the command type is invalid or cannot be processed.
        """
        cmd_type = command.get("type")
        value = command.get("value")
        
        if cmd_type not in self.VALID_COMMANDS:
            raise CommandError(command, f"Unknown command type: {cmd_type}")
        
        # Process each command type.
        if cmd_type == "speed":
            self.vehicle.set_speed(value)
        elif cmd_type == "move":
            self.vehicle.move(value)
        elif cmd_type == "turn":
            self.vehicle.turn(value)

    def execute_commands(self, commands):
        """Execute a list of commands on the vehicle.

        Iterates over the list of commands, processing each one.

        Args:
            commands (list): A list of command dictionaries to process.

        After processing all commands, prints the vehicle's final state and history.
        """
        for command in commands:
            try:
                self.process_command(command)
            except CommandError as e:
                print(e)  # Print error message but continue processing other commands.
        
        # After processing all commands, print final vehicle status.
        print(self.vehicle)
        print("History:", self.vehicle.history)
