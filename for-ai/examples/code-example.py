# Example Code Reference
# This file demonstrates the coding style and patterns preferred for this project

class ExampleClass:
    """
    Example class demonstrating preferred code structure and documentation.
    
    This serves as a reference for the AI agent to understand the coding
    standards and patterns that should be followed in this project.
    """
    
    def __init__(self, name: str, config: dict = None):
        """Initialize the example class."""
        self.name = name
        self.config = config or {}
        self._private_var = None
    
    def public_method(self, param: str) -> str:
        """
        Example of a public method with proper type hints and docstring.
        
        Args:
            param: Description of the parameter
            
        Returns:
            Description of the return value
            
        Raises:
            ValueError: When param is invalid
        """
        if not param:
            raise ValueError("Parameter cannot be empty")
            
        return f"Processed: {param}"
    
    def _private_method(self) -> None:
        """Private method example."""
        pass

# Example of module-level constants
DEFAULT_CONFIG = {
    "timeout": 30,
    "retry_count": 3,
    "debug": False
}

# Example function
def utility_function(data: list) -> dict:
    """Example utility function with error handling."""
    try:
        result = {"count": len(data), "items": data}
        return result
    except Exception as e:
        print(f"Error processing data: {e}")
        return {"count": 0, "items": []}
