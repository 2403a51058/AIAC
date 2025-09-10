def safe_divide(dividend: float, divisor: float) -> float:
    # Combined validation - more efficient than separate checks
    if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
        raise TypeError("Both arguments must be numbers")
    
    if divisor == 0:
        raise ValueError("Cannot divide by zero")
    
    return dividend / divisor

def get_number(prompt: str) -> float:
    """Get a valid number from user input with error handling."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            raise

def main() -> None:
    """Main function to demonstrate safe division."""
    try:
        print("Safe Division Calculator")
        print("-" * 25)
        
        dividend = get_number("Enter dividend: ")
        divisor = get_number("Enter divisor: ")
        
        result = safe_divide(dividend, divisor)
        print(f"Result: {dividend} ÷ {divisor} = {result}")
        
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
if __name__ == "__main__":
    main()
