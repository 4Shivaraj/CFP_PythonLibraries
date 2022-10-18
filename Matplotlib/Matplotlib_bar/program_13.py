'''
    @Author: Shivaraj
    @Date: 16-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 16-10-2022
    @Title: Write a Python program to create bar plots with errorbars on the same figure. Attach a text
            label above each bar displaying men means (integer value).
            Sample Data
            Mean velocity: 0.2474, 0.1235, 0.1737, 0.1824
            Standard deviation of velocity: 0.3314, 0.2278, 0.2836, 0.2645
'''
import matplotlib.pyplot as plt
import numpy as np
import sys

from data_log import get_logger

lg = get_logger(name="(program_13)", file_name="data_log.log")


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

            ind = np.arange(n)  # the x locations for the groups
            width = 0.35  # the width of the bars

            fig, ax = plt.subplots()
            rects = ax.bar(ind, men_means, width, color='r', yerr=men_std)

            # add some text for labels, title and axes ticks
            plt.ylabel('Scores')
            plt.xlabel('Velocity')
            plt.title('Scores by Velocity')

            # Attach a text label above each bar displaying its height
            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                        '%d' % int(height),
                        ha='center', va='bottom')
            plt.show()

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = BarChart()
    np_obj.display_barchart()
