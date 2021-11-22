from ai4c19.core import main
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise Exception('No input file detected.')
    elif len(sys.argv) > 2:
        raise Exception('More than one input detected.')
    else:
        print(f'Input file is: {str(sys.argv)}')

    main(sys.argv[1])