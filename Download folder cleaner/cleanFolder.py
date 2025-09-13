
from choseFolder import ChoseFolder

class FormatFile:
    def __init__(self):
        self.format = []

    def _input_additional_fromat(self):
        print(f"the default formats are : \n\n{self.format}")
        # TODO: get the formats in a list
        try:
            users_formats = input("Enter the formats you want (seprate them with space)")
        # check if the user put them with "." in the first place
        except Exception as e:
            print(f"error is : {e}")
        else:
            self.format.append(lambda x: x in users_formats.split(" "))

    def main(self):
        self._input_additional_fromat()
        return self.format

class CleanFolder:
    _PATH = ChoseFolder.main()
    _FORMATS = FormatFile.main()
    def __init__(self):
        # for example the number of the ones that went ot pictures and ...
        self.number_of_operations = {}

    def _move(self):
        import os
        # get all the files names and formats
        files = os.listdrives()
        try:
            # now move them to the target directory
            pass
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
