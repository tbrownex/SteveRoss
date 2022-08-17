''' Get the command line arguments:
    Mandatory
    - remOutliers: whether to remove outliers from Training
    - genFeature: whether to use a generated feature or not
    
    Optional arguments
    - log: the logging level (overrides "config")
    - normalize: the algorithm to use when normalizing the input'''

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('orgID',  type=int, 
                    help='Organization ID')
    return parser.parse_args()