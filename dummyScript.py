import cv2
import os

def dummyScript(interiorStyle, roomStyle, prompt, budgetControl, fileName):
    # print ("inside dummyScript")
    # print(str(interiorStyle) + "::" + str(roomStyle) + "::" + str(prompt) + "::" + str(budgetControl) + "::" + str(fileName))
    
    ## note: ##
    ## the script should return the file name as: ##
    # "Output_" + filename that will be used during the API call ##
    
    input_path = "E:/polydesign/test/API Flask/static/Images/Input/"
    output_path = "E:/polydesign/test/API Flask/static/Images/Output/"

    img = cv2.imread(input_path+fileName)
    # print(img)

    output_filename = fileName.replace("InputForScriptProcessing_Polydesign_", "OutputFromScript_")

    cv2.imwrite(os.path.join(output_path , output_filename), img)

    ## this should be saved to the Output Folder ##
    ## in current case, ".../static/Images/Output/" folder ##

    return (output_filename)

#c = dummyScript(1, 2, 3, 4, 5)