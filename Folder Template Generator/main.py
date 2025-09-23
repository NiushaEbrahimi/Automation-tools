# what kind of templates : web(what kind) , "make your own template"
# first see if it's going on github
# check if you can generate README for them
import json
import os

class Template:

    def __init__(self):
        _BASE_URL = os.getcwd()
        with open(os.path.join(_BASE_URL, "Folder Template Generator", "templates.json"), "r") as f:
                self.content = f.read()
        self.destination = ""

    def _get_address(self):
        while True:
            try:
                print("Current directory:", os.getcwd())
                print("Contents:", os.listdir(os.getcwd()))
                print(" **Enter .. to go back to the previous directory\n")
                user_input = input("Enter the path of the folder (absolute or relative): ").strip()

                if user_input == "":
                    # stay in current directory
                    self.destination = os.getcwd()
                    break

                # If user gave an absolute path → use it directly
                if os.path.isabs(user_input):
                    target_path = user_input
                else:
                    target_path = os.path.join(os.getcwd(), user_input)

                os.chdir(target_path)
                self.destination = os.getcwd()
                break

            except FileNotFoundError:
                print("That folder does not exist, try again.")
            except PermissionError:
                print("You don't have permission to access this folder.")
            
    def chose_template(self) -> int:
        print("Current directory:", os.getcwd())
        content = json.loads(self.content)
        self.options = content.keys()

        print("Available templates:")
        for index , option in enumerate(list(self.options)):
            print(f"{index+1}.{option}" , end="\t")
        
        while True:
            try:
                template_num = int(input("\nchoose one to import : "))
            except ValueError:
                print("Invalid input")
                continue
            else:
                return template_num
    
    # TODO: chech if template_num should be in __init__
    def _add_github_files(self, template_num : int):
        while True:
            try:
                github_answer = input("Is your project going on github (meaning that do you need a README.md and ... files?)(y/n)")
                if github_answer.lower() in ["yes", "y" , ""]:
                    #TODO: this part has been used twice make it a def
                    template_name = list(self.options)[template_num-1]
                    template_content = json.loads(self.content)[template_name]

                    files = list(template_content["git_files"].keys())
                    file_content=list(template_content["git_files"].values())

                    for i in range(len(template_content["git_files"])):
                        with open(f"{self.destination}/{files[i]}", "w") as f:
                            f.write(file_content[i])

                    print("Files were imported successfully.")
                    break             

                elif github_answer.lower() in ["no", "n"]:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Rresponse")
                continue
            except Exception as e:
                print(e)
                continue

    def import_template(self, template_num: int):

        template_name = list(self.options)[template_num-1]
        template_content = json.loads(self.content)[template_name]

        # making the folders
        for folder in template_content['folders']:
            # this should be self.destination when i debug
            os.mkdir(os.path.join(self.destination, folder))

        # making the essential files with content
        files = list(template_content["files_with_content"].keys())
        file_content=list(template_content["files_with_content"].values())

        for i in range(len(template_content["files_with_content"])):
            with open(f"{self.destination}/{files[i]}", "w") as f:
                f.write(file_content[i])

        input("Template imported successfully!\nPress Enter to continue")

    def main(self):
        os.system("cls")
        print()
        self._get_address()
        template_num = self.chose_template()
        self.import_template(template_num)
        os.system("cls")
        self._add_github_files(template_num)

temp = Template()
if __name__ == "__main__":
    temp.main()
