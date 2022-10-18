'''
    @Author: Shivaraj
    @Date: 16-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 16-10-2022
    @Title: Write a Python program to plot two or more lines with different styles
'''
import sys

import matplotlib.pyplot as plt

from data_log import get_logger

lg = get_logger(name="(program_7)", file_name="data_log.log")


class DrawLine:
    """
    class to perform graphical representation of data using matplotlib
    """

    def plot_two_or_more_lines(self):
        """
        Description:
             This function is used to plot two or more lines with different styles
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            # Line 1
            x1 = [1, 2, 3]
            y1 = [10, 20, 5]
            lg.info(f'x1 range: {x1} and y1 range: {y1}')
            # plotting the line 1 points with dash line style
            plt.plot(x1, y1, color='blue', label='dashed', linestyle='dashed')
            # Line 2
            x2 = [1, 2, 3]
            y2 = [40, 10, 5]
            lg.info(f'x2 range: {x2} and y2 range: {y2}')
            # plotting the line 2 points with dot line style
            plt.plot(x2, y2, color='green', label='dotted', linestyle='dotted')
            # set label for axes
            plt.xlabel('X axis')
            plt.ylabel('y axis')

            # title for plotting line
            plt.title('Two or more lines on same plot with suitable legends ')

            # show a legend on the plot
            plt.legend()
            # show the figure
            plt.show()

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = DrawLine()
    np_obj.plot_two_or_more_lines()
