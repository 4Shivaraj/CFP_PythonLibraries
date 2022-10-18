'''
    @Author: Shivaraj
    @Date: 16-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 16-10-2022
    @Title: Write a Python program to create bar plot from a DataFrame.
            Sample Data Frame:
            a b c d e
            2 4,8,5,7,6
            4 2,3,4,2,6
            6 4,7,4,7,8
            8 2,6,4,8,6
            10 2,4,3,3,2
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys

from data_log import get_logger

lg = get_logger(name="(program_11)", file_name="data_log.log")


class BarChart:
    """
    class to perform bar chart representation using matplotlib
    """

    def display_barchart(self):
        """
        Description:
             This function is used to create bar plot from a DataFrame
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            data = np.array([[2, 4, 6, 8, 10], [4, 2, 4, 2, 2], [8, 3, 7, 6, 4], [5, 4, 4, 4, 3], [6, 6, 8, 6, 2]])

            # arrange all data in a Data Frame, here
            data_frame = pd.DataFrame(data, columns=['a', 'b', 'c', 'd', 'e'], index=[
                "Delhi", 'Mumbai', 'Hyderabad', 'Pune', 'Bengaluru'])

            # kind check , which type of graph, kind='bar'-> specify vertical bar (by default)
            data_frame.plot(kind='bar')

            # To display graph
            plt.show()

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = BarChart()
    np_obj.display_barchart()
