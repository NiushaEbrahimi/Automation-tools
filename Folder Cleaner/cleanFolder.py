from choseFolder import ChoseFolder

# TODO: every time after this runs, tell the user what are the type of the remaining 
#       files and what should be done to them

object = ChoseFolder()

class CleanFolder:
    _PATH = object.main()
    def __init__(self):
        # for example the number of the ones that went ot pictures and ...
        self.number_of_operations = {'image' : 0 , 'video' : 0 , 'audio' : 0 , 'doc' : 0}
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
        import os
        #TODO: get all the files names and formats
        files = os.listdir()
        try:
            # TODO: improve the algorithm to not have 3 for loops
            for k in files:
                for i in format:
                    for j in range(len(format[f"{i}"])):
                        if k==format[f"{i}"][j]:
                            # TODO: os.something ( move )
                            self.number_of_operations[f"{i}"]+=1
                            break
                # TODO: now move them to the target directory
                
        except PermissionError:
            print("couldn't move this file :")
        except Exception as e:
            print(f"error is: {e}")
        else:
            print("all the files have been moved and the folder is now clean")
        finally:
            print("Operation is done! \n" \
            f"{self.number_of_operations}")


    def final_step(self):
        process = True
        while (process == True):
            try: 
                continue_process = input(f"Are you sure you want to clean {self._PATH} the folder in this address(Y/n)")
                if (continue_process.lower) == "n" or (continue_process.lower) == "no":
                    print("breaking out ...")

                elif (continue_process.lower) == "yes" or (continue_process.lower) == "y" or (continue_process.lower) == "" :
                    self._move()
                    process = False
                    continue

                else: 
                    raise KeyboardInterrupt
            except KeyboardInterrupt :
                print("Invalid Input ... ")
                continue
