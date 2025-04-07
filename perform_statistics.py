import pandas as pd
import numpy as np
import sys
from scipy.stats import trim_mean, iqr, median_abs_deviation,pearsonr,spearmanr,kendalltau
from reuse_func import view_table

#display menu display options statistics
def menu_statistics():
    print("This section Calculate Statistics")
    print("[1] Mean: ")
    print("[2] Median: ")
    print("[3] Trimmed Mean: ")
    print("[4] Weghted Mean: ")
    print("[5] Variance: ")
    print("[6] Standart Deviation: ")
    print("[7] Mean Abs Dev: ")
    print("[8] Median Abs Dev: ")
    print("[9] IQR: ")
    print("[10] Percentiles: ")
    print("[11] Frequency Table: ")
    print("[12] Correlation: ")
    print("[0] Exits")


#clean the missing dataset of column
def data_clean(data):
    numeric_col = pd.to_numeric(data, errors='coerce')
    cleaned_col = numeric_col.fillna(0) 
    return cleaned_col



#sub function perform the statistics
def perform_statistics(df):

    computed_stats=[] #store all calculated stats
    #infinite the loop that runs until exit value is return to main function
    while True:
        #display the menu options
        menu_statistics()
        choice_statistics=input("Enter the statistics you want to perform: ")#take user choice
        while True:
            try:
                if choice_statistics=="1":
                    #diplay table which helps in selecting the column
                    view_table(df)
                    choice_column = input("Choose a column: ").strip() #take user choice column

                    if choice_column in df.columns: #check if user selected column is in table
                        cleaned_col=data_clean(df[choice_column]) #if exist data is cleaned or missing value like nan is handled
                        mean= np.mean(cleaned_col) #calculate mean
                        print(f"mean: {mean:.2f}")

                        #store the result
                        computed_stats.append({
                            "statistic": "mean",
                            "column":choice_column,
                            "value":float(mean)

                        })
                        break
                    
                        
                    else:
                        print("Unavailable columns,please select right column")
                        continue
      

                elif choice_statistics=="2":
                    view_table(df)
                    choice_column=input("choose a column: ").strip()

                    if choice_column in df.columns:
                        cleaned_col=data_clean(df[choice_column])
                        median= np.median(cleaned_col) #calculate median of selected column
                        print(f"median: {median:.2f}")
                        
                        computed_stats.append({
                            "statistic": "median",
                            "column":choice_column,
                            "value":float(median)
                        })
                        break
                    else:
                        print("Unavailable column,please select right column")
                        continue

                elif choice_statistics=="3":
                    view_table(df)
                    choice_column=input("choose a column: ").strip()

                    if choice_column in df.columns:
                        cleaned_col=data_clean(df[choice_column])
                        trimmed_mean= trim_mean(cleaned_col,proportiontocut=0.1) #calculate trim mean of selected column
                        print(f"Trimmed mean: {trimmed_mean:.2f}")
                        
                        computed_stats.append({
                            "statistic": "Trimed_mean",
                            "column":choice_column,
                            "value":float(trimmed_mean)
                        })
                        break 
                    else:
                        print("Unavailable column,please select right column")
                        continue

                elif choice_statistics=="4":
                    view_table(df)
                    print("Weighted need two column for calculation ")
                    # to calculate weight mean, we need two numeric column so user are insisted to select two column
                    choice_column1 =input ("choose a 1st Column: ").strip()
                    choice_column2=input (" Choose a 2nd column: ").strip()

                    if choice_column1 and choice_column2 in df.columns: # check if two column exist in table
                        cleaned_col1=data_clean(df[choice_column1])
                        cleaned_col2=data_clean(df[choice_column2])
                        weighted_mean=np.average(cleaned_col1,weights=cleaned_col2) #calculate weighted mean
                        print(f"weighted mean: {weighted_mean:.2f}")
                        computed_stats.append({
                            "statistic": "weight_mean",
                            "column1":choice_column1,
                            "column2": choice_column2,
                            "value":float(weighted_mean)
                        })
                        break 

                    else:
                        print("Unavailable column,Please select right column")
                        continue

                elif choice_statistics=="5":
                    view_table(df)
                    choice_column=input("choose a column: ").strip()

                    if choice_column in df.columns:
                        cleaned_col=data_clean(df[choice_column])
                        variance=np.var(cleaned_col,ddof=1) #calculate variance
                        print(f"variance: {variance:.2f}")
                        computed_stats.append({
                            "statistic": "variance",
                            "column":choice_column,
                            "value":float(variance)
                        })
                        break

                    else:
                        print("Unvailable column, Please select right column")
                        continue
        
                elif choice_statistics=="6":
                    view_table(df)
                    choice_column=input("choose a column: ").strip()

                    if choice_column in df.columns:
                        cleaned_col=data_clean(df[choice_column])
                        stand_dev=np.std(cleaned_col,ddof=1)
                        print(f"Standard Deviation: {stand_dev:.2f}") #calculate standard deviation
                        computed_stats.append({
                            "statistic": "Standard_Deviations",
                            "column":choice_column,
                            "value":float(stand_dev)
                        })
                        break 
                    else:
                        print("Unvailable column,Please Select right column")
                        continue

                elif choice_statistics=="7":
                    view_table(df)
                    choice_column=input("choose a column: ").strip()

                    if choice_column in df.columns:
                        cleaned_col=data_clean(df[choice_column])
                        mean=np.mean(cleaned_col)
                        mean_abs_dev=np.mean(np.abs(cleaned_col-mean)) #calculate mean absolute deviation
                        print(f"Mean Absolute Deviation: {mean_abs_dev:.2f}")
                        computed_stats.append({
                            "statistic": "Mean Abs Deviation",
                            "column":choice_column,
                            "value":float(mean_abs_dev)
                        })
                        break

                    else:
                        print("Unavailable Column,Please Select right column")
                        continue

                elif choice_statistics=="8":
                    view_table(df)
                    choice_column=input("choose a column: ").strip()

                    if choice_column in df.columns:
                        cleaned_col=data_clean(df[choice_column])
                        median_abs_dev=median_abs_deviation(cleaned_col) #calculate median absolute deviation
                        print(f"Median Absolute Deviation: {median_abs_dev:.2f}")
                        computed_stats.append({
                            "statistic": "Median abs deviation",
                            "column":choice_column,
                            "value":float(median_abs_dev)
                        })
                        break

                    else:
                        print("Unvailable Column,Please Select right column")
                        continue


      
                elif choice_statistics=="9":
                    view_table(df)
                    choice_column=input("choose a column: ").strip()

                    if choice_column in df.columns:
                        cleaned_col=data_clean(df[choice_column])
                        IQR=iqr(cleaned_col) #calculate Inter quartile range
                        computed_stats.append({
                            "statistic": "Inter Quartile Range",
                            "column":choice_column,
                            "value":float(IQR)
                        })

                        print(f"Inter Quartile Range: {IQR:.2f}")
                        break

                    else:
                         print("Unavailable column,Please select right column")


                elif choice_statistics=="10":
                    view_table(df)
                    choice_column=input("choose a column: ").strip()

                    if choice_column in df.columns:
                        cleaned_col=data_clean(df[choice_column])
                        percentiles=cleaned_col.quantile([.05,.25,.5,.75,.95]) #assign value of selected with respect to percentiles. if list is [1,2,3,4,5,6,7,8,9,10] percentile[.05] match with 2

                        print(f"5th percentiles: {percentiles[.05]:.2f}")
                        print(f"25th percentiles: {percentiles[.25]:.2f}")
                        print(f"50th(median) percentiles: {percentiles[.5]:.2f}")
                        print(f"75th percentiles: {percentiles[.75]:.2f}")
                        print(f"95th percentiles: {percentiles[.95]:.2f}")
                        computed_stats.append({
                            "statistic": "Percentiles",
                            "column":choice_column,
                            "5th percentiles":float(percentiles[.05]),
                            "25th percentiles":float(percentiles[.25]),
                            "50th percentiles":float(percentiles[.5]),
                            "75th percentiles":float(percentiles[.75]),
                            "75th percentiles":float(percentiles[.95])
                        })
                        break 

                    else:
                        print("Unavailable column,Please select right column")
                        continue

                elif choice_statistics=="11":
                    view_table(df)
                    choice_column=input("choose a column: ").strip()

                    if choice_column in df.columns:

                        cleaned_col=data_clean(df[choice_column])

                    

                        num_bins=int(input("Enter the bins/interval you want: ")) #take num of bins or interval user want to set

                        min_data,max_data=cleaned_col.min(),cleaned_col.max() #minimum/starting value and maximum/ending value is find and set using tuple unpacking

                        bins=np.linspace(min_data,max_data,num_bins+1) #create equale bins from starting value to last value

                        freq_table=pd.cut(cleaned_col,bins=bins,include_lowest=True).value_counts().sort_index() #equal bins , frequency of data and sorting helps in creating frequency table

                        print(f"Frequency of selected column is:{freq_table}")
                        computed_stats.append({
                            "statistic": "frequency_table",
                            "column": choice_column,
                            "num_bins": num_bins,
                            "bins": [str(interval) for interval in freq_table.index],  # Interval as string
                            "counts": freq_table.tolist()
                            })
                        break


                    else:
                        print("Unvailable column,Please Select right column")


                
                elif choice_statistics=="12":
                    view_table(df)
                    print("To perform Correlation We need Two variable/ Two columns")
                    choice_column1=input("choose a column1: ").strip()
                    choice_column2=input("choice a column2: ").strip()



                    if choice_column1 and choice_column2 in df.columns:
                        cleaned_col1=data_clean(df[choice_column1])
                        cleaned_col2=data_clean(df[choice_column2])
                        print("Choose [1] for Pearsons Correlations: ")
                        print("Choose [2] for spearsons correlations: ")
                        print("choose [3] for kendall's Tau correlarions: ")

                        corr_choice=input("enter the correlation[1-3]: ")

                        if corr_choice=="1":

                            r,p_value=pearsonr(cleaned_col1,cleaned_col2) #calculate pearsons

                            print(f"Pearson Correlation: {r:.2f}")

                            print(f"P_value: {p_value:.2f}") #p value is threshold or significant of r value, which determine how much sigmificant is r
                            computed_stats.append({
                            "statistic": "Pearson Correlation",
                            "column1":choice_column1,
                            "column2": choice_column2,
                            "value":float(r)
                            })
                            break
                            

                        elif corr_choice=="2":

                            spearmanr_corr,p_value=spearmanr(cleaned_col1,cleaned_col2) #calculate spearson

                            print(f"Spearman Correlation: {spearmanr_corr:.2f}")

                            print(f"p_value: {p_value:.2f}")
                            computed_stats.append({
                            "statistic": "Spearman Correlation",
                            "column1":choice_column1,
                            "column2": choice_column2,
                            "value":float(spearmanr_corr)
                            })
                            
                            break

                        elif corr_choice=="3":

                            tau, p_value=kendalltau(cleaned_col1,cleaned_col2) #calculate kandal tau

                            print(f"Kendall tau: {tau:.2f}")
                            computed_stats.append({
                            "statistic": "Kendalltau Correlation",
                            "column1":choice_column1,
                            "column2": choice_column2,
                            "value":float(tau)
                            })
                            break    

                

                        else:
                            print("Unvailable column,Please Select right column")
                            continue

                elif choice_statistics=="0":
                    print("Satistics Calculations is exiting..")
                    return computed_stats #retutn all the collected value and helps exiting system back to main function
                    
                else:
                    print("Please Enter [1-12]") #if user input is not in 1-12
                    break
            except ValueError: #throws value error lets in choice 11 of frequncy table , if user inputs str in'num_bns' which is design to take int value , in this case value error is handled and alert user to input right data types
                print("[Alert] Invalid Input, Please Enter Correct Value")









         



