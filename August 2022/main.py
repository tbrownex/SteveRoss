import time
import pandas as pd

from copyCampaign import copyCampaign

CAMPAIGN_TO_COPY = 2945588
ORGANIZATION_ID = 351975
NUM_COPIES = 5000

def main():
    start_time = time.time()
    df = pd.read_csv('newIDs.csv')
    newIDs = df['campaignID']
    copyCampaign(ORGANIZATION_ID, CAMPAIGN_TO_COPY, NUM_COPIES, newIDs)
    #newIDs = copyCampaign(ORGANIZATION_ID, CAMPAIGN_TO_COPY, NUM_COPIES)
    #pd.DataFrame(newIDs, columns=['newID']).to_csv('newIDs.csv', index=False)
    print("\ncomplete after {:,.0f} minutes".format((time.time() -start_time)/60))

if __name__ == "__main__":
    main()