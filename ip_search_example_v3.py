# looking for strings in Shodan output (or other text files)
# this version is an example of "version 0.3" of the class project assignment

import os

output_file = "count_results.txt"

# starting up, help orient the user
print(f"You are currently in: {os.getcwd()}")
print("The following are in this location:")
print(os.listdir())

# get the info for the search
# - what file/directory to search inside
# - what string to search/count
# - whether the search/count should be case sensitive
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
        for thing in os.listdir(thing_to_search):
            if os.path.isfile(thing):
                files_to_search.append(thing)
        if len(files_to_search) > 0:
            valid_files_found= True
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

# perform the search/count
# save results in a dictionary
count_results = {"file searched" : [],
                 "string counted" : [],
                 "case sensitive" : [],
                 "count" : []}
for target_file in files_to_search:
    try:
        with open(folder_path + "/" + target_file, mode = "r", encoding = "utf-8") as fc:
            file_contents = fc.read()
    except Exception as e:
        print(f"Something went wrong with opening {target_file}: {e}")
        file_contents = "" # to allow code to continue with empty results

    if not case_sensitive:
        file_contents = file_contents.casefold()
        string_to_count = string_to_count.casefold()
    
    count_of_string = file_contents.count(string_to_count)

    count_results["file searched"].append(target_file)
    count_results["string counted"].append(string_to_count)
    count_results["case sensitive"].append(case_sensitive)
    count_results["count"].append(count_of_string)
    

# save output in a file, CSV-style
# set the header depending on if the file exists already or not
if os.path.exists(output_file):
    header = ""
else:
    header = "file,string,case_sensitive,count\n"
with open(output_file, mode = "a", encoding = "utf-8") as out_connection:
    out_connection.write(header)
    for index in range(len(count_results["count"])):
        out_connection.write(f"{count_results['file searched'][index]},{count_results['string counted'][index]},{count_results['case sensitive'][index]},{count_results['count'][index]}\n")
