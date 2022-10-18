'''
    @Author: Shivaraj
    @Date: 16-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 16-10-2022
    @Title: Write a Python program to draw a line with suitable label in the x axis, y axis and a title
'''

import matplotlib.pyplot as plt
import sys

from data_log import get_logger

lg = get_logger(name="(program_1)", file_name="data_log.log")


class DrawLine:
    """
    class to perform graphical representation of data using matplotlib
    """

    def line_plotting(self):
        """
        Description:
             This function is used to draw a line with suitable label in the x axis, y axis and a title
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            x = [0, 1, 2, 3, 4, 5, 6]
            y = [value * 3 for value in x]
            lg.info(f'x range: {x} and y range: {y}')
            # plot lines to the axes
            plt.plot(x, y)
            # set label for axes
            plt.xlabel('X axis')
            plt.ylabel('y axis')
            # title for plotting line
            plt.title('Line')
            # show the figure
            plt.show()

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = DrawLine()
    np_obj.line_plotting()
