import os
from time import sleep
from pathlib import Path


class ChoseFolder:
    def __init__(self):
        self.folder_name = "Downloads"
        self.path = None
        os.system("cls")

    def _input(self):
        print()
        process = True
        while (process == True):
            try:
                self.folder_name = input("Enter the name of the folder of your choice:(We'll show all the possible options, also default is: Downloads)")
                if self.folder_name == "" :
                    self.folder_name = 'Downloads' 
                
                # TODO: check if => accessible drives on any OS.
                # TODO: Add progress feedback
                # TODO: Make it faster with multithreading

                process = False

            except ValueError:
                print("Invalid input, please try again ")
                continue

            except Exception as e:
                print(f"error is: {e}")
                continue

    def _search_for_folder(self):
        start_path = os.path.expanduser("~")

        if os.name == "nt": 
            start_path = "C:\\"
        else:
            start_path = "/"
        paths =[]
        for root, dirs, _ in os.walk(start_path):
            if self.folder_name in dirs:
                paths.append(os.path.join(root, self.folder_name))
        return paths
    
    def _chose_path(self, paths):
        for index , value in enumerate(paths):
            print(f"{index+1}. {value}")
        num = int(input("which one of these you want to chose?  "))
        self.path = paths[num-1]
    
    def main(self):
        while True:
            try:
                self._input()
                print("\n this may take a few seconds")
                all_paths = self._search_for_folder()
                if all_paths:
                    os.system("cls")
                    self._chose_path(all_paths)                
                else:
                    print("no folders were found")
                    continue
                
            except Exception as e:
                print(f"the error is: {e}")
            else : 
                try:
                    items = os.listdir(self.path)
                    # also => name = os.path.basename(self.path)
                    print(f"\n{self.path.split("\\")[-1]}:")
                    counter = 0
                    for item in items:
                        print(f"\t -{item}")
                        #only show the first 5 
                        if counter ==5:
                            break
                        counter+=1
                    print("\t...")
                except PermissionError:
                    print(f"Cannot read contents of '{self.path.split("\\")[-1]}'")
            finally:
                user_action = input("\nDo you want to try again and chose another folder? (Y/n)")
                if user_action.lower == "y" or user_action.lower == "yes" or user_action.lower == "":
                    continue
                else:
                    return self.path
                
if __name__ == '__main__':
    cl = ChoseFolder()
    result = cl.main()
    print(f"the chosen path is: {result}")
