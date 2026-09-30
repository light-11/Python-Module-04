import sys
import typing


def ft_archive_creation() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{sys.argv[1]}'")
        try:
            open_text: typing.IO[str] = open(sys.argv[1])
            print("---")
            read_text = open_text.read()
            print(read_text)
            print("---")
            open_text.close()
            print(f"File '{sys.argv[1]}' closed.")
            print()
            print("Transform data:")
            print("---")
            text_list = read_text.split("\n")
            new_text_list = [text + "#" for text in text_list]
            for new_text in new_text_list:
                print(new_text)
            print("---")
            name = input("Enter archive filename (or press Enter to skip): ")
            if name != "":
                print(f"Saving data to '{name}'...")
                open_new_file: typing.IO[str] = open(name, mode='w')
                for new_text in new_text_list:
                    open_new_file.write(new_text + '\n')
                open_new_file.close()
                print("Data saved successfully.")
            else:
                print("Not saving data.")
        except Exception as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")


ft_archive_creation()
