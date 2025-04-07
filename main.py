from perform_statistics import perform_statistics
from perform_visualize import perform_visualize
from browse import browse_file
from save_analysis import save_analysis
import sys 
import pandas as pd

#display the menu options
def menu_main():
    print("\n CLI  Exploratory Data Analysis Tool")
    print("[1] Browse Csv File: ")
    print("[2] Perform Statistics: ")
    print("[3] Perform Visualiztions: ")
    print("[4] Save Analysis: ")
    print("[0] Exit: ")
   
   
# mani function which helps in executing and linking sub functions
def main(data):
     #empty list that collect calculated value from perform statistics and saved to result/analysis_result.csv
    collected_stats=[]
    
    #start the infimit loop unless user exit the system
    while True:
        #handling value error
        try:
            #main option is shown
            menu_main()
            choice=input("Choose the options you want to perform: ") #take choice from user
        
            if choice=="1":
                #catch the return value from browse filr
                new_data=browse_file()
                if new_data is not None: #check if there is user selected  file 
                    data=new_data # if True , file is assigned to data variable
                    
                    print("File is loaded succussfully...")
                else:
                    print("No selected file found.....")
            
            elif choice=="2":
                # call the funtions and stats_resukt catch the return value from perform_statistics while exiting in sub functon
                stats_result=perform_statistics(data)
                if stats_result:
                    collected_stats.extend(stats_result) #add new stats to the list 
                    print(f"{len(stats_result)} result added")
                    continue

            elif choice=="3":
                result=perform_visualize(data) #call and result catch the value which is return while exiting in sub function
                if result == "exit":
                    continue

            elif choice=="4":
                save_analysis(collected_stats) #call and pass collected_stats to sub functions
            elif choice=="5":
                print("Exiting....")
                sys.exit() #exit the system
            else:
                print("Choose option 1-4 again, input value unmatched")

        except ValueError:
            print("[Alert}, Invalid inputs, please enter the correct inputs")



if __name__ =="__main__":
    data=None  #intially data is kept non
    while data is None: #this imsist user to  select  a file  forcefully if list is empyty
        print("Please Load a CSV file First.")
        data= browse_file() #call the sub function


main(data) #main function is call here






