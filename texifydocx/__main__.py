# texifydocx/__main__.py

import sys
from .converter import convert_docx

def main():
    if len(sys.argv) != 3:
        print("Usage: python -m texifydocx <input.docx> <output.docx>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    convert_docx(input_path, output_path)
    print(f"Conversion complete: {output_path}")

if __name__ == "__main__":
    main()