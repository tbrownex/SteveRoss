import os

from getOrganization import getOrg
from getCampaign import getCampaign

def main():
    orgID = input("Enter the Organization ID: ")
    orgName = getOrg(orgID)
    campaignID = input("Enter the Campaign ID: ")
    confirm = confirmCampaign(orgID, campaignID)
    if confirm:
        confirm = confirmImages(orgName)

def confirmCampaign(orgID, campaignID):
    print('\n')
    print("confirm this is the right campaign:")
    print('\n')
    
    _ =getCampaign(orgID, campaignID)
    
    confirm = input("Confirm? (yes)")
    
    if confirm == 'yes':
        return True
    else:
        return False

def confirmImages(orgName):
    print('\n')
    print("confirm these are the right image files:")
    for img in sorted(os.listdir(f'{orgName}/images')):
        print(img)
    
    confirm = input("Confirm? (yes)")
    if confirm == 'yes':
        return True
    else:
        return False

if __name__ == "__main__":
    main()