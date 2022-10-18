'''
    @Author: Shivaraj
    @Date: 16-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 16-10-2022
    @Title: Write a Python program to create bar plots with error bars on the same figure. 
            Sample Data
            Mean velocity: 54.74, 42.35, 67.37, 58.24, 30.25
            Standard deviation of velocity: 4, 3, 4, 1, 5
            '''
import matplotlib.pyplot as plt
import numpy as np
import sys

from data_log import get_logger

lg = get_logger(name="(program_12)", file_name="data_log.log")


class BarChart:
    """
    class to perform bar chart representation using matplotlib
    """

    def display_barchart(self):
        """
        Description:
             This function is used to display a bar chart of the popularity of programming Languages
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            n = 5
            men_means = (54.74, 42.35, 67.37, 58.24, 30.25)
            men_std = (4, 3, 4, 1, 5)

            # the x locations for the groups
            ind = np.arange(n)

            # the width of the bars
            width = 0.35

            # x(as ind), y(menMeans) define the data locations, yerr define the errorbar sizes.
            plt.bar(ind, men_means, width, yerr=men_std, color='blue')

            # put x and y axis label
            plt.ylabel('Scores')
            plt.xlabel('Velocity')

            # set graph title
            plt.title('Scores by Velocity, Error Bar')

            plt.show()

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = BarChart()
    np_obj.display_barchart()
