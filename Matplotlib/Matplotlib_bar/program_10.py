'''
    @Author: Shivaraj
    @Date: 16-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 16-10-2022
    @Title: Write a Python program to create bar plot of scores by group and gender. Use multiple X
            values on the same chart for men and women.
            Sample Data:
            Means (men) = (22, 30, 35, 35, 26)
            Means (women) = (25, 32, 30, 35, 29)
'''
import matplotlib.pyplot as plt
import numpy as np
import sys

from data_log import get_logger

lg = get_logger(name="(program_10)", file_name="data_log.log")


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
            men = (22, 30, 35, 35, 26)
            women = (25, 32, 30, 35, 29)
            n_groups = 5

            # create plot or creates object of subplot
            fig, ax = plt.subplots()

            index = np.arange(n_groups)
            bar_width = 0.35

            # plotting men means values to create bar chart
            plt.bar(index, men, bar_width, color='g', label='Men')

            # plotting women means values to create bar chart before men
            plt.bar(index + bar_width, women, bar_width, color='r', label='Women')

            # Set the x-axis label
            plt.xlabel('Person')

            # Set the y-axis label
            plt.ylabel('Scores')

            # Sets a title
            plt.title('scores by group and gender')

            # group label
            plt.xticks(index + bar_width / 2, ('G1', 'G2', 'G3', 'G4', 'G5'))

            # show a legend on the plot
            plt.legend()

            # Display a figure.
            plt.show()

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = BarChart()
    np_obj.display_barchart()
