import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
from reuse_func import view_table


#display visualiztion options
def menu_visualize():
    print("Enter [1-2] for Different Plots: ")
    print("[1] Boxplot: ")
    print("[2] Histogram: ")
    print("[3] Density Histogram: ")
    print("[4] Scatter plots: ")
    print("[5] Hexagonal binning plot: ")
    print("[6] Contour Plot: ")
    print("[0] Exit: ")



# plot the visualization
def perform_visualize(df):
    #infinite loop untill user return the exit to main function [0] exit
    while True:
        #visualization option
        menu_visualize()
        choice_visualise=input("Enter [1-6] for visualize: ") #choice to select the visualization

        while True:
            try:
                if choice_visualise=="1":
                    view_table(df)   #diplay table which helps in selecting the colum
                    choice_column=input("Enter column you want to visualize Boxplot: ").strip() #give option to user for select the column
                    if choice_column in df.columns: #check if selected column exits
                        give_dividen=int(input("Enter the Number you want to divide data: ")) #takes dinominator value which helps user at what scale does they want to show plot
                        give_title=input("Enter the title of plot: ").strip() #takes title user want to set 
                        give_xlabel=input("Enter the xlabel of plot: ").strip() #takes xlabel user want to set
                        print("Here is your plot")
                        plt.figure(figsize=(10,4))  #set figuire size

                        plt.boxplot(df[choice_column]/give_dividen,vert=False) #plot histo gram

                        plt.title(give_title) # set title

                        plt.xlabel(give_xlabel) #set label on x axis

                        plt.yticks([]) #y is empty
                        plt.show() #display the whole plot
                        break
                    else:
                        print("Selected right column")
                        continue
                elif choice_visualise=="2":
                    view_table(df)
                    choice_column=input("Enter the column you what to histogram: ").strip()
                    if choice_column in df.columns:
                        num_bins=int(input("Enter no of bins/intervals you want to set: ")) #no of interals user want 
                        give_title=input("Enter the title you want to give for plot: ").strip()
                        give_xlabel=input("Enter the xlabel(population,age,dollar.. etc)").strip()
                        give_ylabel=input("Enter the ylabel(no of counts)").strip()
                    

                        plt.figure(figsize=(10,5))

                        n,bins,patches=plt.hist(df[choice_column],bins=num_bins,edgecolor="red",alpha=0.7) #plot histogram

                        plt.title(give_title)
                        plt.xlabel(give_xlabel)
                        plt.ylabel(give_ylabel)
                        plt.grid(axis='y',alpha=0.3)
                        plt.show()

                        print(f"no of counts: {n}")
                        print(f"no of bins: {bins}")
                        print(f"Patches: {patches}")
                        break
                    else:
                        print("Select Right column")
                        continue
                elif choice_visualise=="3":
                    view_table(df)
                    choice_column=input("Enter the column you want to plot density histogram: ").strip()
                    if choice_column in df.columns:
                        num_bins=int(input("Enter no of bins/intervals you want to set: "))
                        give_title=input("Enter the title of plot: ").strip()
                        give_xlabel=input("Enter the xlabel of plot: ").strip()

                        plt.figure(figsize=(10,5))
                    
                        sns.histplot(df[choice_column],stat='density',bins=num_bins,alpha=0.4) #plot histogram

                        sns.kdeplot(df[choice_column],linewidth=2,alpha=0.4) #plot smooth curve

                        plt.title(give_title)
                        plt.xlabel(give_xlabel)
                        plt.ylabel("Density") #mean while density histogram y label is dynamically plot value from 0 to 1 , thus Label "density" is given
                        plt.grid(axis='y',alpha=0.3)
                        plt.show()
                        break
                    else:
                        print("Enter Right Column")
                        continue

                elif choice_visualise=="4":
                    view_table(df)
                    print("To plot you need to enter two column/variable to perform scatter plot: ")
                    #to plot scatter two column because helps to visualize correlations of two variable/column
                    choice_column1=input("Enter the First column: ").strip()
                    choice_column2=input("Enter the Second column: ").strip()

                    if choice_column1 and choice_column2 in df.columns:
                        give_title=input("Enter the title of plot:  ").strip()
                        give_xlabel=input("Enter the xlabel of plot: ").strip()
                        give_ylabel=input("Enter the ylabel of plot: ").strip()

                   

                   
                        plt.figure(figsize=(9,7))
                        sns.scatterplot(x=df[choice_column1],y=df[choice_column2], color='red') #plot scatter plot

                        plt.title(give_title)
                        plt.xlabel(give_xlabel)
                        plt.ylabel(give_ylabel)
                    

                    
                        plt.grid(True)
                        plt.show()
                        break
                    else:
                        print("Choose right column")
                        continue

                elif choice_visualise=="5":
                    view_table(df)
                    print("To plot you need to enter two column/variable to perform Hexagonal binning: ")
                    choice_column1=input("Enter the First column: ").strip()
                    choice_column2=input("Enter the Second column: ").strip()
                    if choice_column1 and choice_column2 in df.columns:
                        give_title=input("Enter the title of plot:  ").strip()
                        give_xlabel=input("Enter the xlabel of plot: ").strip()
                        give_ylabel=input("Enter the ylabel of plot: ").strip()


                        plt.figure(figsize=(8, 5))

                    
                        plt.hexbin(df[choice_column1], df[choice_column2], gridsize=20, cmap='Blues', mincnt=1) #plot hexabin plot

                        plt.title(give_title)
                        plt.xlabel(give_xlabel)
                        plt.ylabel(give_ylabel)
                    
                        plt.show()
                        break
                    else:
                        print("Choose Right column: ")
                        continue

                elif choice_visualise=="6":
                    view_table(df)
                    print("To plot you need to enter two column/variable to perform Contour Plot: ")
                    choice_column1=input("Enter the First column: ").strip()
                    choice_column2=input("Enter the Second column: ").strip()
                    if choice_column1 and choice_column2 in df.columns:
                        give_title=input("Enter the title of plot:  ").strip()
                        give_xlabel=input("Enter the xlabel of plot: ").strip()
                        give_ylabel=input("Enter the ylabel of plot: ").strip()
                    
                        plt.figure(figsize=(8, 5))

                    
                        sns.kdeplot(x=df[choice_column1],y=df[choice_column2],cmap='coolwarm',fill=True,thresh=0.05) #plots contour plots

                        plt.title(give_title)
                        plt.xlabel(give_xlabel)
                        plt.ylabel(give_ylabel)
                    
                        plt.show()
                        break

                    
                              
                    else:
                        print("Choose Right column: ")
                        continue
                elif choice_visualise=="0":
                    print("Visualization is exiting....")
                    return "exit"
                    

                else:
                    print("Choose the visualise [1-6]")
                    break
            except ValueError:
                print("[Alert] Invalid value inputs, please enter correct value.")


'''
   Used for:
              boxplot: Find outlier.
             histogram and density: plot frequency table
             scatter plot: plot correlated data when dataset is small
             hexabin and contour: plot large correlated dataset. and contour is specially used for spatial dataset
     
'''

    
          




