import os
from time import sleep
# TODO: going to user's download folder
# TODO: make it possible for any folder actually
# TODO: getting info that how many folders and where should the folders be
# TODO: then search what type of files exist


class ChoseFolder:
    def __init__(self):
        self.folder_name = "Downloads"
        self.path = None
    def _input(self):
        print()
        process = True
        while (process == True):
            try:
                self.folder_name = input("Enter the name of the folder of your choice: (default: Downloads)")
                if self.folder_name == "" :
                    self.folder_name = 'Downloads' 
                
                # TODO: searche all accessible drives on any OS.
                # TODO: Search only specific drives
                # TODO: Add progress feedback
                # TODO: Make it faster with multithreading

                process = False

            except ValueError:
                print("It needs to be string don't enter anything else ;) ")
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

        for root, dirs, _ in os.walk(start_path):
            if self.folder_name in dirs:
                self.path =  os.path.join(root, self.folder_name)
    
        if self.path:
            print(f"Folder found at: {self.path}")

        else:
            print("Folder not found.")
            sleep(1)

    def main(self):
        try:
            self._input()
            self._search_for_folder()

        except Exception as e:
            print(f"the error is: {e}")
        else : 
            list = os.listdir(self.path)
            list_1 = self.path.split("\\")
            print("\n" , list_1[-1],":")
            for f in list:
                print(f"\t-{f}")
        finally:
            return self.path
        
if __name__ == '__main__':
    chooser = ChoseFolder()
    result = chooser.main()
    print("Selected folder:", result)