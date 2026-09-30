import sys
import typing


def ft_ancient_text() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            read_text: typing.IO[str] = open(sys.argv[1])
            print("---")
            print(read_text.read())
            print("---")
            read_text.close()
            print(f"File '{sys.argv[1]}' closed.")
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")


ft_ancient_text()
