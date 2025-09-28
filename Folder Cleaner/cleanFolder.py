from choseFolder import ChoseFolder
import os

chose_folder = ChoseFolder()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class CleanFolder:
    _PATH = chose_folder.main()

    def __init__(self):
        self.number_of_operations = {'Pictures': 0, 'Videos': 0, 'Music': 0, 'Documents': 0}
        self.unknown_files = []
        self.format = {
            'Pictures': [
                '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.svg', '.ico',
                '.raw', '.cr2', '.nef', '.arw', '.orf', '.sr2', '.dng', '.heic', '.heif'
            ],
            'Videos': [
                '.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.3gp', '.3g2',
                '.mpeg', '.mpg', '.vob', '.ts', '.mts', '.m2ts', '.ogv'
            ],
            'Music': [
                '.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma', '.m4a', '.aiff', '.au', '.mid', '.midi', '.opus'
            ],
            'Documents': [
                '.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.ppt', '.pptx', '.xls', '.xlsx', '.csv',
                '.md', '.zip', '.rar', '.7z', '.tar', '.gz', '.iso'
            ]
        }

    def _input_additional_format(self):
        clear_screen()
        print(f"Current formats:\n{self.format}\n")
        try:
            user_result = int(input(
                "Do you want to:\n"
                "1: Add formats to existing category\n"
                "2: Create a new category\n"
                "Choose (1 or 2): "
            ))
            
            if user_result == 1:
                category_user = input("Enter category name: ").strip()
                if category_user not in self.format:
                    print("Category does not exist.")
                    input("Press Enter...")
                    return

                format_input = input("Enter formats separated by comma (e.g., .webm,.mkv): ")
                formats = [f.strip() for f in format_input.split(",") if f.strip()]

                for fmt in formats:
                    if not fmt.startswith('.'):
                        fmt = '.' + fmt
                    if fmt not in self.format[category_user]:
                        self.number_of_operations[category_user] = 0
                        self.format[category_user].append(fmt)
                
                print(f"Updated {category_user}: {self.format[category_user]}")
                input("Press Enter to continue...")

            elif user_result == 2:
                name_of_category = input("Enter the name of the new category: ").strip()
                if not name_of_category:
                    print("Invalid name.")
                    return

                self.format[name_of_category] = [] 

                format_input = input("Enter formats separated by comma: ")
                formats = [f.strip() for f in format_input.split(",") if f.strip()]

                for fmt in formats:
                    if not fmt.startswith('.'):
                        fmt = '.' + fmt
                    self.format[name_of_category].append(fmt)

                print(f"Created '{name_of_category}' with formats: {self.format[name_of_category]}")
                input("Press Enter to continue...")

            else:
                print("Invalid choice.")
                input("Press Enter...")

        except ValueError:
            print("Please enter a number.")
            input("Press Enter...")
        except Exception as e:
            print(f"Error: {e}")
            input("Press Enter...")

    def _move(self):
        from pathlib import Path
        import shutil

        self.number_of_operations = {'Pictures': 0, 'Videos': 0, 'Music': 0, 'Documents': 0}
        path = Path(self._PATH)
        
        base_dest = Path.home()
        folders = {
            'Pictures': base_dest / "Pictures",
            'Videos':   base_dest / "Videos",
            'Music':    base_dest / "Music",
            'Documents':base_dest / "Documents"
        }

        for folder in folders.values():
            folder.mkdir(exist_ok=True)

        ext_to_category = {}
        for category, extensions in self.format.items():
            for ext in extensions:
                ext_to_category[ext.lower()] = category

        for item in path.iterdir():
            if item.is_file():
                ext = item.suffix.lower()
                if ext in ext_to_category:
                    category = ext_to_category[ext]
                    dest_folder = folders.get(category, path / category)
                    print(f"Debug: Moving '{item.name}' to category '{category}' -> folder: '{dest_folder}'")

                    if not dest_folder.exists():
                        dest_folder.mkdir(exist_ok=True)

                    dest_path = dest_folder / item.name
                    print(f"Debug: Full destination path: '{dest_path}'")

                    try:
                        shutil.move(str(item), str(dest_path))
                        self.number_of_operations[category] += 1
                        print(f"Moved '{item.name}' => {category}")
                    except PermissionError:
                        print(f"Permission denied: {item.name}")
                    except Exception as e:
                        print(f"Failed to move '{item.name}': [{type(e).__name__}] {e}")
                        print(f"Source: {item}")
                        print(f"Dest F: {dest_folder}")
                        print(f"Dest P: {dest_path}")
                else:
                    self.unknown_files.append(item.name)

        print("\nOperation completed!")
        for cat, count in self.number_of_operations.items():
            print(f"{count} file(s) moved to {cat}")


    def final_step(self):
        from pathlib import Path
        while True:
            try:
                clear_screen()
                response = input(f"Clean folder: {self._PATH}? (Y/n): ").strip().lower()
                if response in ('n', 'no'):
                    print("Cancelled.")
                    break

                elif response in ('y', 'yes', ''):
                    self._move()

                    remaining = [item.name for item in Path(self._PATH).iterdir() if item.is_file()]
                    if remaining:
                        print("\nUnknown files left:")
                        print(", ".join(remaining))
                        print()

                    again = input("Add custom formats and clean again? (Y/n): ").strip().lower()
                    if again in ('y', 'yes'):
                        self._input_additional_format()
                        continue
                    else:
                        print("Goodbye!")
                        break

                else:
                    print("Please enter 'y' or 'n'.")

            except KeyboardInterrupt:
                print("\n\nCancelled by user.")
                break

            except Exception as e:
                print(f"Unexpected error: {e}")
                break

if __name__ == '__main__':
    clean_folder = CleanFolder()
    clean_folder.final_step()