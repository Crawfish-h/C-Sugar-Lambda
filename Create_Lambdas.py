import os
import shutil
import re



# Most of this code needs to be modified to use getline(), I think.
def Create(generated_File, lambda_Count):
    with open(generated_File, 'r') as file:
        braces_Count = 0
        lines = file.readlines()
        def Substrings_Count(string, substring): # returns the number of substrings in a string.
            return len([sub.start() for sub in re.finditer(substring, string)])
        
        lambda_Return_Type = []
        lambda_Argument_List = []
        
        for row in lines:
            braces_Count += Substrings_Count(row, "{")

            braces_Count -= Substrings_Count(row, "}")

            lambda_Index = row.find("Lambda")
            if lambda_Index != -1:
                def str_Index_Replace(index, source_Str, new_Str_At_Index): 
                    return source_Str[:index] + new_Str_At_Index + source_Str[index + 1:]
                
# ------------- Find the lambda's return type ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                search_For_Return_Type = False
                for i in range(lambda_Index + 5, len(row)):
                    if row[i] == "(":        
                        str_Index_Replace(i, row, "")            
                        if search_For_Return_Type == True:
                            search_For_Return_Type = False
                            lambda_Return_Type = "void"
                            break
                        
                        search_For_Return_Type = True
                    
                    if search_For_Return_Type == True and row[i].isspace == False:
                        lambda_Return_Type.append(row[i])
                        str_Index_Replace(i, row, "")
                    elif search_For_Return_Type == True:
                        lambda_Return_Type = "".join(lambda_Return_Type)
                        break
                
# ------------- Find the lambda's argument list ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                found_Arugment_List = False # Is true if the lambda's arugment list has been found.
                for i in range(lambda_Index + 5, len(row)):
                    if row[i] == "(":
                        found_Arugment_List = True

                    if row[i] == ")":
                        str_Index_Replace(i, row, "")
                        lambda_Argument_List = "".join(lambda_Argument_List)
                        break
                    
                    if found_Arugment_List == True:
                        lambda_Argument_List.append(row[i])
                        str_Index_Replace(i, row, "")

# --------------Find the lambda's function body ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                for i in range(lambda_Index + 5, len(row)):
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                Lambda_Signature = lambda_Return_Type + "Lambda_Function" + lambda_Count + "(" + lambda_Argument_List + ")"
                row = row.replace("Lambda", Lambda_Signature)
                lambda_Count += 1
                last_Two_Lines = 2 # Helps to move the creation of the C lambda function above a function definition.
                for rev_Row in reversed(lines):
                    if braces_Count == 0:
                        last_Two_Lines -= 1
                        if last_Two_Lines == 0:
                            if rev_Row == "":
                                
                        continue
                    braces_Count -= Substrings_Count(rev_Row, "{")

                    braces_Count += Substrings_Count(rev_Row, "}")

    
    return lambda_Count


        # file_Str = file.read()
        # braces_Count = 0
        # last_Five_Chars = []
        # index = 0
        # for char in file_Str:
        #     index += 1
        #     if char == "{":
        #         braces_Count += 1
        #     elif char == "}":
        #         braces_Count -= 1

        #     last_Five_Chars.append(char)
        #     if len(last_Five_Chars) > 5:
        #         last_Five_Chars.pop()
            
            
        #     if "".join(last_Five_Chars) == "Lambda":
        #         last_Five_Chars.clear()
        #         file_Str = file_Str[:index] + "_Function_" + lambda_Count + file_Str[index:]
        #         rev_Braces_Count = braces_Count
        #         rev_Index = index
        #         for rev_Char in reversed(file_Str):
        #             rev_Index -= 1
        #             if rev_Char == "{":
        #                 rev_Braces_Count -= 1
        #             elif rev_Char == "}":
        #                 rev_Braces_Count += 1

        #             if rev_Braces_Count == 0: 