from choseFolder import ChoseFolder
import os

# TODO: every time after this runs, tell the user what are the types of the remaining 
#       files and ask what should be done to them

chose_foler = ChoseFolder()

class CleanFolder:
    _PATH = chose_foler.main()
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
            os.system("cls")
            print(f"the default formats are : \n\n{self.format}")
            while True:
                try:
                    user_result = int(input("Do you want to add formats to the categories that \nexist or you want to make a new one? (\n1:add to existing one\n2:make a new one\n)"))
                    if user_result ==1:
                        category_user=input("Enter the name of the category you want to add format to: ")

                        for category, extensions in self.format.items():
                            if category_user == category:
                                format_user = input("Enter the format you want to add to the category:use \",\" to seprate them" )
                                format_user = format_user.split(",")
                                for format in format_user:
                                    if format.strip()[0] is not ".":
                                        self.format[category_user].append("."+format)
                                    else:
                                        self.format[category_user].append(format.strip())
                                print(self.format)
                                return

                    elif user_result==2:
                        name_of_category = input("Enter the name of the new category: ")
                        format_user = input("Enter the format you want to add to the category:use \",\" to seprate them" )
                        format_user = format_user.split(",")
                        for format in format_user:
                            if format.strip()[0] is not ".":
                                self.format[name_of_category].append("."+format)
                            else:
                                self.format[name_of_category].append(format.strip())
                        print(self.format)
                        return
                    else:
                        raise Exception("Invalid Input")
                    
                except Exception as e:
                    print(f"{e}")

    def _move(self):
        from pathlib import Path

        self._PATH = Path(self._PATH)
        try:
            # Create destination folders inside user's home
            # TODO: Have to customize this
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
                    # this is the format
                    ext = item.suffix.lower()
                    if ext in ext_to_category:
                        category = ext_to_category[ext]
                        if category not in folders:
                            #TODO: you can add them here or ask the user to input the path
                            # for now add them into the existing folder
                            dest_folder = self._PATH / category
                            dest_folder.mkdir(exist_ok=True)
                        else:
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
                    print(f"{count} file(s) moved to {cat}")
                else: print(f"no files were moved to {cat}.")

    def final_step(self):
        process = True
        while (process == True):
            try: 
                os.system("cls")
                response = input(f"Are you sure you want to clean {self._PATH} the folder in this address(Y/n)")
                if response.strip().lower() in ('no' , 'n'):
                    print("breaking out ...")
                    break

                elif response.strip().lower() in ('y' , 'yes' , ''):
                    self._move()
                    if self._PATH.iterdir() is not None:
                        print("\nThe remaining files are: \n")
                        for item in self._PATH.iterdir():
                            print(item.name, end=", ")
                        print("\n")
                    clean_again= input("Do you want to clean the folder with your own formats? (Y/n)")
                    if clean_again.strip().lower() in ('y' , 'yes' , ''):
                        self._input_additional_fromat()
                        self.final_step()
                    elif clean_again.strip().lower() in ('no' , 'n'):
                        process = False
                        continue
                    else:
                        raise Exception("Invalid Input")
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
    # clean_folder._input_additional_fromat()