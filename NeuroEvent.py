    """ Module containing several functions used to import neural data and 
    convert them to DataFrame for further analysis
    
    King-Lun Li(Allen) 2025"""


import numpy as np
import pandas as pd
import scipy as sy
from scipy import stats
import statistics as st
from more_itertools import numeric_range
from sklearn.decomposition import PCA
import matplotlib as mpl
import matplotlib.pyplot as plt

class Neve:
    def __init__(self, data):
        """
        Initialize the Neve (Neural EVEnt analyzer) with a dataset.
        :param data: imported data containing the dataset.
        """
        self.data = data

    def NeuroEvent(self):
        """
        Parses the file content to extract event data.
        This method outputs a DataFrame containing the event data in the following format:
        Event Type	Onset(s)
        Image	    0.5
        Sound	    1.2
        Image	    2.8

        """
        # Create an empty list 
        events = []

        #
        for lines in self.data.splitlines():
            # Parsing the lines to separate "Event" and "Onset"
            parts = lines.strip().split(", ")
            # Getting the Event Type
            event_type = parts[0].split(": ")[1]
            # Getting the Onset time and removing 's' from the value
            onset = float(parts[1].split(": ")[1][:-1])
            
            # appending the Event Type and Onset(s) to the empty list
            events.append({"Event Type": event_type, "Onset(s)": onset})
        return pd.DataFrame(events) # Return a DataFrame for all Evernt Types and Onset Times


    def describe_data(self):
        """
        Return basic statistics of the dataset.
        :return: A pandas DataFrame with descriptive statistics.
        """
        df = self.NeuroEvent()
        return df["Onset(s)"].describe()