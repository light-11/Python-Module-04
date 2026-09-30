import sys
import typing


def ft_stream_management() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
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
            sys.stdout.write("Enter archive filename "
                             "(or press Enter to skip): ")
            sys.stdout.flush()
            name = sys.stdin.readline().rstrip("\n")
            if name != "":
                print(f"Saving data to '{name}'...")
                try:
                    open_new_file: typing.IO[str] = open(name, mode='w')
                    for new_text in new_text_list:
                        open_new_file.write(new_text + '\n')
                    open_new_file.close()
                    print("Data saved successfully.")
                except Exception as e:
                    sys.stderr.write(f"[STDERR] "
                                     f"Error opening file '{name}': {e}\n")
                    print("Data not saved.")
            else:
                print("Not saving data.")
        except Exception as e:
            sys.stderr.write(f"[STDERR] "
                             f"Error opening file '{sys.argv[1]}': {e}\n")


ft_stream_management()
