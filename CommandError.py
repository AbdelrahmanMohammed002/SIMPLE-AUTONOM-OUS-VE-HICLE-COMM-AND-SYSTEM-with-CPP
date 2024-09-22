class CommandError(Exception):
    """Custom exception to handle invalid commands.

    This exception is raised when a command is not valid, 
    providing detailed information about the command that caused the error 
    and a message explaining the reason.
    """
    def __init__(self, command, message):
        """Initialize the exception with the command and error message.
        
        Args:
            command (dict): The invalid command that caused the error.
            message (str): A message explaining why the command is invalid.
        """
        self.command = command  # Command causing the error.
        self.message = message  # Explanation of the error.
        super().__init__(f"Error processing command {command}: {message}")

