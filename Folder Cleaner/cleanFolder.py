from choseFolder import ChoseFolder
import os

# TODO: every time after this runs, tell the user what are the types of the remaining 
#       files and ask what should be done to them

object = ChoseFolder()

class CleanFolder:
    _PATH = object.main()
    def __init__(self):
        self.number_of_operations = {'Pictures' : 0 , 'Videos' : 0 , 'Music' : 0 , 'Documents' : 0}
        self.unknown_files = []
        self.format = {
            'Pictures' : [
                '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.svg', '.ico',
                '.raw', '.cr2', '.nef', '.arw', '.orf', '.sr2', '.dng', '.heic', '.heif'
            ],
            'Videos' : [
                '.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.3gp', '.3g2',
                '.mpeg', '.mpg', '.vob', '.ts', '.mts', '.m2ts', '.ogv'
            ],
            'Music' : [
                '.mp3', '.wav', '.aac', '.flac', '.ogg', '.wma', '.m4a', '.aiff', '.au', '.mid', '.midi', '.opus'
            ],
            'Documents' : [
                '.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.ppt', '.pptx', '.xls', '.xlsx', '.csv', 
                '.md', '.zip', '.rar', '.7z', '.tar', '.gz', '.iso'
            ]
        }

    # TODO: implement this 
    def _input_additional_fromat(self):
            print(f"the default formats are : \n\n{self.format}")
            # TODO: get the formats in a list
            try:
                users_formats = input("Enter the formats you want (seprate them with space)")
            # TODO: check if the user put them with "." in the first place
            except Exception as e:
                print(f"error is : {e}")
            else:
                self.format.append(lambda x: x in users_formats.split(" "))

    def _move(self):
        from pathlib import Path

        self._PATH = Path(self._PATH)
        files = os.listdir()
        try:
            # Create destination folders inside user's home
            # TODO: HAve to customize this
            base_dest = Path.home()
            folders = {
                'Pictures': base_dest / "Pictures",
                'Videos':   base_dest / "Videos",
                'Music':    base_dest / "Music",
                'Documents':base_dest / "Documents"
            }

            
            self.unknown_files = []

            ext_to_category = {}
            for category, extensions in self.format.items():
                for ext in extensions:
                    ext_to_category[ext.lower()] = category

            for item in self._PATH.iterdir():
                if item.is_file():
                    ext = item.suffix.lower()

                    if ext in ext_to_category:
                        category = ext_to_category[ext]
                        dest_folder = folders[category]
                        dest_path = dest_folder / item.name

                        try:
                            # shutil.move for robust cross-device support
                            import shutil
                            shutil.move(str(item), str(dest_path))
                            self.number_of_operations[category] += 1
                            print(f"Moved '{item.name}' => {category}")

                        except PermissionError:
                            print("Don't have the permission to move this file.")

                        except Exception as error:
                            print(f"Failed to move {item.name}: because of {error}")

                    else:
                        self.unknown_files.append(item.name)

        except Exception as e:
            print(f"error is: {e}")

        finally:
            print("\nOperation is done!\n")
            for cat, count in self.number_of_operations.items():
                if count > 0:
                    print(f"{count} file(s) moved to {cat}\n")
                else: print("no files were moved.")
            # TODO:show the unknown_files to the user
            


    def final_step(self):
        process = True
        while (process == True):
            try: 
                os.system("cls")
                response = input(f"Are you sure you want to clean {self._PATH} the folder in this address(Y/n)")
                if response.strip().lower() in ('no' , 'n'):
                    print("breaking out ...")

                elif response.strip().lower() in ('y' , 'yes' , ''):
                    self._move()
                    process = False
                    continue

                else: 
                    raise KeyboardInterrupt
                
            except KeyboardInterrupt :
                print("Invalid Input ... ")
                continue

clean_folder = CleanFolder()
if __name__ == '__main__':
    clean_folder.final_step()