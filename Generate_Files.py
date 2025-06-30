import os
import shutil
import Create_Lambdas

def Generate():
    lambda_Count = 0 # The total amount of lambdas that have been generated.

    if not os.path.exists("Lambda_Generated"):
        os.makedirs("Lambda_Generated")

    invalid_Directories = ["build", "Lambda_Generated"]
    for root, dirs, files in os.walk("."):
        for file in files:
            is_Invalid_Dir = False
            for i in range(len(invalid_Directories)): 
                if invalid_Directories[i] in root:
                    is_Invalid_Dir = True
            if (file.endswith(".h") or file.endswith(".c")) and is_Invalid_Dir == False and file != "Lambda.h":
                file_Extention = ".h"
                copied_File = ""
                if ".h" in file:
                    copied_File = file.replace(".h", "")
                else:
                    copied_File = file.replace(".c", "")
                    file_Extention = ".c"
                    
                path_Of_Copy = os.path.join("Lambda_Generated", root)
                if not os.path.exists(path_Of_Copy):
                    os.makedirs(path_Of_Copy)

                generated_File = shutil.copyfile(os.path.join(root, file), os.path.join(path_Of_Copy, file))
                lambda_Count = Create_Lambdas.Create(generated_File, lambda_Count)
