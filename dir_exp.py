
"""
    Experiments on macOS for doing image and directory stuff.
    Uses cv2 (Open CV) because that's how you do it on a mac
"""
import os 
from datetime import datetime
import cv2

# Some constants to make life easer
#-----------------------------------
WHERE_ARE_THE_FILES_AT = "/Users/stevenwinter/dev/python"
FILE_PREFIX = "cam_snap_"
DATE_FORMAT = "%Y-%m-%d_%H-%M-%S-%f"
FILE_EXTENSION = ".jpg"
#-----------------------------------

#--------------------------------------------------------
def getTimeDateFilename():
    """Get a filename in a specific date/time format

    Returns:
        _type_: A string that is a complete filename including extension
    """    
    # get the current time
    current_datetime = datetime.now().strftime(DATE_FORMAT)
        
    # convert datetime obj to string
    str_current_datetime = str(current_datetime)
    
    # create a file object along with extension
    file_name = FILE_PREFIX + str_current_datetime + FILE_EXTENSION

    # a full filename, with extension
    return file_name

#--------------------------------------------------------
def makeFile(): 
    """ generate an empty file using the system filenaming convention
    """    
    # get current date and time
    td_filename = getTimeDateFilename()
    file = open(td_filename, 'w')
    #print("File created : ", file.name)
    file.close()

#--------------------------------------------------------
def takeAPicture():
    """This is a macOS/OpenCV type of picture taking
    """ 
    # Initialize values, if you don't do this, they won't be know in a different scope
    cam = None
    image = None
    result = False

    try:
        # Get a camera device using open cv
        cam =  cv2.VideoCapture(0)
        # take a picture, or at least try to
        result, image = cam.read()
    except:
        print("Error trying to take picture, failure!")
        return

    if result:
        # get the filename
        dateTimeFilename = getTimeDateFilename()
        # make is complete with path
        fn = os.path.join(WHERE_ARE_THE_FILES_AT, dateTimeFilename)
        # write it
        try:
            cv2.imwrite(fn, image)
            # print("Wrote image to: " + fn)
        except:
            print('Error writing/saving picture')
            return
    else:
        print("Failed (FALSE) taking picture")

#--------------------------------------------------------
def ListFiles():

    try:
        dir_list = os.listdir(WHERE_ARE_THE_FILES_AT)
    except:
        print("ERROR finding files at " + WHERE_ARE_THE_FILES_AT)
        return
    
    print("Files and directories in '", WHERE_ARE_THE_FILES_AT, "' :")
    # prints all files
    for f in dir_list:
        if f.endswith("jpg") or f.endswith("jpeg"):
            print("File: " + f)

# The script itself
#=================================
#print(dir_list)
takeAPicture()

ListFiles()