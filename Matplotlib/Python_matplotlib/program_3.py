'''
    @Author: Shivaraj
    @Date: 16-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 16-10-2022
    @Title: Write a Python program to draw a line using given axis values taken from a text file, with
            suitable label in the x axis, y axis and a title.
            Test Data:
            test.txt
            1 2
            2 4
            3 1
'''

import matplotlib.pyplot as plt
import sys

from data_log import get_logger

lg = get_logger(name="(program_3)", file_name="data_log.log")


class DrawLine:
    """
    class to perform graphical representation of data using matplotlib
    """

    def line_plotting(self):
        """
        Description:
             This function is used to draw a line using given axis values taken from a text file
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            # opening file
            with open("test.txt") as f:
                # read content from file
                data = f.read()

            data = data.split('\n')  # ['1 2', '2 4', '3 1']

            # get row 0 value in x axis
            # [['1', '2'], ['2', '4'], ['3', '1']] before accessing 0 index
            x = [row.split(' ')[0] for row in data]
            lg.info(f'X axis: {x}')

            # get row 1 value in y axis
            y = [row.split(' ')[1] for row in data]
            lg.info(f'Y axis: {y}')

            # plot lines to the axes
            plt.plot(x, y)

            # set label for axes
            plt.xlabel('X axis')
            plt.ylabel('Y axis')

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
