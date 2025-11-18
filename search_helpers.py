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
