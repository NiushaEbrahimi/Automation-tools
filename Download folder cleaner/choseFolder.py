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
                if type(self.folder_name) != 'String':
                    raise ValueError
                process = False
            except Exception as e:
                print(f"error is: {e}")
                self._input()
                continue
            except ValueError:
                print("It needs to be string don't enter nums or symbols ;) ")
                continue

    def _search_for_folder(self):
        import os
        pass

    def main(self):
        try:
            self._input()
            self.path = self._search_for_folder()
            
        except Exception as e:
            print(f"the error is: {e}")
        else : 
            # TODO show the folder structure to user so that they can check if it's right
            pass
        finally:
            return self.path
        