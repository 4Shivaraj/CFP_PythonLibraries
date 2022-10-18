'''
    @Author: Shivaraj
    @Date: 16-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 16-10-2022
    @Title: Write a Python program to display the current axis limits values and set new axis values.
'''
import matplotlib.pyplot as plt
import sys

from data_log import get_logger

lg = get_logger(name="(program_9)", file_name="data_log.log")


class DrawLine:
    """
    class to perform graphical representation of data using matplotlib
    """

    def display_set_axis(self):
        """
        Description:
             This function is used to display the current axis limits values and set new axis values
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            x = [1, 4, 5, 6, 8]
            y = [10, 50, 100, 150, 200]
            lg.info(f'x range: {x} and y range: {y}')

            # plot lines to the axes
            plt.plot(x, y, label='line 1')

            # set label for axes
            plt.xlabel('X axis')
            plt.ylabel('y axis')

            # title for plotting line
            plt.title('Two or more lines on same plot with suitable legends ')

            # returns current axis values
            lg.info(plt.axis())  # (0.85, 4.15, 0.75, 6.25)

            # xmin,xmax,ymin,ymax=plt.axis()
            plt.axis([0, 10, 0, 200])

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
    np_obj.display_set_axis()
