"""
This is called by cron to post picture to dropbox and clean up dropbox folder
"""

import sys
import dropbox
from datetime import datetime
import time
from datetime import timedelta
import os

from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

# Add OAuth2 access token here. 
TOKEN = ''   #secret token

DROPBOX_PATH   = '/Apps/rpi_workcam'

#----------------------------------------
# MANAGE DROPBOX FOLDER (DELETE OLD FILES)
def manageDboxFolder(dbx):
    """List a folder.
           Return a dict mapping unicode filenames to
           FileMetadata|FolderMetadata entries.
    """
    #print('Folder listing for', DROPBOX_PATH)
    try:
        res = dbx.files_list_folder(DROPBOX_PATH)
    except dropbox.exceptions.ApiError as err:
        print('Folder listing failed for', DROPBOX_PATH, '-- assumped empty:', err)
        return {}
    else:
        rv = {}

        delTime = datetime.now() - timedelta(hours=24)   # one day
        now_timestamp = time.time()
        offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)

        #print('delTime:' + str(delTime))

        # FOR EACH FILE
        for entry in res.entries:
            srvTime = entry.server_modified
            localTime =  srvTime + offset   # The last mod (local) time of the file

            #print(str(entry.name))
            #print('  srvTime:' + str(srvTime))
            #print('  locTime:' + str(localTime))

            if (localTime < delTime):
                fn = DROPBOX_PATH + '/' + entry.name
                print('Attempting to delete old file: ' + fn)
                try:
                    dbx.files_delete(fn)
                except ApiError as err:
                    print('Error deleting file: ' + str(err))
                    #sys.exit()
                print('successfully deleted file!')

                
def cronEvent(upFile, fullUpFile):
    #--------------------
    # CONNECT TO DROPBOX
    # Create an instance of a Dropbox class, which can make requests to the API.
    print("Creating a Dropbox object...")
    dbx = dropbox.Dropbox(TOKEN)

    # Check that the access token is valid
    try:
        dbx.users_get_current_account()
    except AuthError as err:
        print("Error creating dropbox object");
        sys.exit("ERROR: Invalid access token; try re-generating an access token from the app console on the web.")

    #--------------------
    #DELETE THE OLD FILES
    manageDboxFolder(dbx)


    #---------------------------------------------
    # UPLOAD NEW IMAGE TO DROPBOX
    mypath = DROPBOX_PATH + '/' + upFile

    
    with open(fullUpFile, 'rb') as f:
        # We use WriteMode=overwrite to make sure that the settings in the file
        # are changed on upload
        print("Uploading " + upFile + " to Dropbox as " + mypath + "...")
        try:
            dbx.files_upload(f, mypath, mode=WriteMode('overwrite'))
        except ApiError as err:
            # This checks for the specific error where a user doesn't have
            # enough Dropbox space quota to upload this file
            if (err.error.is_path() and
                    err.error.get_path().error.is_insufficient_space()):
                print("ERROR: Cannot back up; insufficient space.")
                sys.exit("ERROR: Cannot upload; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                #sys.exit()  # Don't exit, just log and continue
                return
            else:
                print(err)
                #sys.exit()  # Don't exit, log and continue
                return
    # Delete local file (cleanup)
    print("Done with cron event at " + str(datetime.now()))

#----------------------- MAIN APP ---------------------------

if __name__ == '__main__':
    # Check for an access token
    if (len(TOKEN) == 0):
        sys.exit("ERROR: Looks like you didn't add your access token.")

#  Filename, Full Path Filename
        
cronEvent(sys.argv[1], sys.argv[2])

#-------------------------------------------------------------
