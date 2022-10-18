'''
    @Author: Shivaraj
    @Date: 16-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 16-10-2022
    @Title: Write a Python program to draw a scatter graph taking a random distribution in X and Y and
            plotted against each other.
'''
import matplotlib.pyplot as plt
import random
import sys

from data_log import get_logger

lg = get_logger(name="(program_1)", file_name="data_log.log")


class ScatterPlot:
    """
    class to perform ScatterPlot representation using matplotlib
    """

    def display_scatter_plot(self):
        """
        Description:
             This function is used to draw a scatter graph taking a random distribution in X and Y
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            x, y = [], []
            for i in range(0, 10):
                x_value = random.randint(0, 10)
                x.append(x_value)
                y_value = random.randint(0, 100)
                y.append(y_value)
            lg.info(f"x data: {x}")
            lg.info(f"y data: {y}")
            plt.scatter(x, y)
            plt.show()

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = ScatterPlot()
    np_obj.display_scatter_plot()
