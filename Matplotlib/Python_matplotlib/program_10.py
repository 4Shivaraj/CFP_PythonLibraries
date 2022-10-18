'''
    @Author: Shivaraj
    @Date: 16-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 16-10-2022
    @Title: Write a Python program to plot quantities which have an x and y position
'''
import matplotlib.pyplot as plt
import sys

from data_log import get_logger

lg = get_logger(name="(program_10)", file_name="data_log.log")


class DrawLine:
    """
    class to perform graphical representation of data using matplotlib
    """

    def plot_quantities(self):
        """
        Description:
             This function is used to plot quantities which have an x and y position
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            # Line 1
            x1 = [1, 2, 3, 4]
            y1 = [5, 4, 1, 6]
            lg.info(f'x1 range: {x1} and y1 range: {y1}')

            # Line 2
            x2 = [4, 2, 7, 3]
            y2 = [2, 4, 9, 5]
            lg.info(f'x2 range: {x2} and y2 range: {y2}')

            # set label for axes
            plt.xlabel('X axis')
            plt.ylabel('y axis')

            # title for plotting line
            plt.title(' Quantities which have an x and y position ')

            # set new axes limits
            plt.axis([0, 10, 0, 15])

            # plotted x and y as blue * and red circles
            plt.plot(x1, y1, 'b*', x2, y2, 'ro', )

            # show the figure
            plt.show()

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = DrawLine()
    np_obj.plot_quantities()
