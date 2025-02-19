import argparse
import sys

def create_parser():
    """Create and return an argument parser"""
    parser = argparse.ArgumentParser(
        description="A command line utility demonstrating argparse functionality"
    )
    
    # Add arguments
    parser.add_argument('name', help='Name of the person to greet')
    parser.add_argument('-a', '--age', type=int, help='Age of the person')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    
    return parser

def process_args(args):
    """Process the parsed arguments"""
    output = f"Hello, {args.name}!"
    
    if args.age:
        output += f" You are {args.age} years old."
    
    if args.verbose:
        output += "\nVerbose mode is enabled."
        
    return output

def main():
    parser = create_parser()
    args = parser.parse_args()
    
    try:
        result = process_args(args)
        print(result)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
