import os
import pandas as pd
import json
 
#function save calculated values
def save_analysis(collected_stats):
    # check if collected list is empty
    if not collected_stats:
        print("No statistics to save. Run 'Perform statistics' first")
        return
    



    #save to csv with a fixed filename
    file_path="results/amalysis_results.csv"


    #save to json 
    with open(file_path,"w") as f:
        json.dump(collected_stats,f,indent=4)

    print(f"Saved {len(collected_stats)} statistics to {file_path}")




        

