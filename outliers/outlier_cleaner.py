#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    error = []
    for i in range(len(predictions)):
        error.append([abs(net_worths[i] - predictions[i]), net_worths[i], ages[i]])
    error = sorted(error)
    error = error[:-9]
    for iterator in error:
        cleaned_data.append((iterator[2], iterator[1], iterator[0]))
    return cleaned_data

