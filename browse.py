import tkinter as tk
from tkinter import filedialog
import pandas as pd
#helps to display browse window 
def browse_file():
    #create root
    root=tk.Tk() 
    root.withdraw()
    file_path= filedialog.askopenfilename(title="Select CSV File",filetypes=[("CSV Files","*.csv")]) #diplay browse window
    root.destroy()

    if file_path: #check if file is selected 
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            print(f"Error:{e}")
            return None
        return None



