# file for functions, classes, etc to help with the search code
import os

def get_search_info():
    """
    This function asks the user for the search information.
    The user can provide either a single file or a directory.
    This returns a tuple with all of the search term values.
    """
    # print(os.getcwd())
    valid_files_found = False
    while not valid_files_found:
        thing_to_search = input("Provide a path to a file or directory that you want searched:\n")
        if not os.path.exists(thing_to_search):
            print("That does not appear to be a valid path, please try again.")
        elif os.path.isfile(thing_to_search):
            valid_files_found = True
            # make a singleton list, so that follow-on code can always expect a list
            files_to_search = [thing_to_search]
            folder_path = os.getcwd()
        elif os.path.isdir(thing_to_search):
            files_to_search = []
            print(os.listdir(thing_to_search))
            for thing in os.listdir(thing_to_search):
                # print(thing)
                if os.path.isfile(thing_to_search + "/" + thing):
                    files_to_search.append(thing)
                # print(files_to_search)
            if len(files_to_search) > 0:
                valid_files_found = True
                folder_path = thing_to_search
            else:
                print("There do not appear to be any files in the specified directory, please try again.")
        else:
            raise ValueError(f"Somehow {thing_to_search} exists but is neither a file nor a directory. Not sure what to do with that.")
        
    string_to_count = input("Please enter a string to be counted in the target file(s):\n")

    case_sensitive = input("Do you want the search to be case sensitive? [y]/n\n")
    if case_sensitive.lower() == "n":
        case_sensitive = False
    else:
        case_sensitive = True

    return files_to_search, folder_path, string_to_count, case_sensitive

## tests
# get_search_info() # test with a directory
# get_search_info() # test with a single file

class IPSearch:
    """
    """

    def __init__(self, files_to_search, string_to_count, case_sensitive, folder_path = "."):
        self.files = files_to_search
        self.path = folder_path
        self.string_to_count = string_to_count
        self.case_sensitive = case_sensitive

    def __str__(self):
        return f"""
        String to count: {self.string_to_count}
        Case sensitive: {self.case_sensitive}
        Files to search: {self.files}
        """

    def __repr__(self):
        return f"IPSearch({self.files}, {self.string_to_count}, {self.case_sensitive}, {self.path})"
    
    def check_for_files(self):
        bad_files = []
        for target_file in self.files:
            try:
                with open(self.path + "/" + target_file, mode = "r", encoding = "utf-8") as fc:
                    pass
            except Exception as e:
                # print(f"Something went wrong with opening {target_file}: {e}")
                bad_files.append(target_file)
        return bad_files

    def remove_file_list(self, bad_files: list):
        for bad_file in bad_files:
            self.files.pop(self.files.index(bad_file))

    def find_counts(self) -> dict:
        count_results = {"file searched" : [],
                        "string counted" : [],
                        "case sensitive" : [],
                        "count" : []}
        for target_file in self.files:
            try:
                with open(self.path + "/" + target_file, mode = "r", encoding = "utf-8") as fc:
                    file_contents = fc.read()
            except Exception as e:
                print(f"Something went wrong with opening {target_file}: {e}")
                file_contents = "" # to allow code to continue with empty results

            if not self.case_sensitive:
                file_contents = file_contents.casefold()
                string_to_count = self.string_to_count.casefold()
            else:
                string_to_count = self.string_to_count
            
            count_of_string = file_contents.count(string_to_count)

            count_results["file searched"].append(target_file)
            count_results["string counted"].append(self.string_to_count)
            count_results["case sensitive"].append(self.case_sensitive)
            count_results["count"].append(count_of_string)
        return count_results


## tests
some_files = ['shodan_search1.txt', 'shodan_search_p2.txt', 'shodan_search_p3.txt']
target_string = "404"
case_sensitive = True
sample_path = "sample_texts"
new_search = IPSearch(some_files, target_string, case_sensitive, sample_path)
new_search.files
new_search.path
print(new_search)
new_search

new_search.find_counts()

new_search.string_to_count

new_search.string_to_count = "200"
new_search.find_counts()

files_to_remove = new_search.check_for_files()
new_search.remove_file_list(files_to_remove)
print(new_search)

new_search.find_counts()
