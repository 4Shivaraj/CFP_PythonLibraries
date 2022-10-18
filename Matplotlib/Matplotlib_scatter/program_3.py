'''
    @Author: Shivaraj
    @Date: 16-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 16-10-2022
    @Title: Write a Python program to draw a scatter plot using random distributions to generate balls of
            different sizes.
'''
import math
import matplotlib.pyplot as plt
import random
import sys

from data_log import get_logger

lg = get_logger(name="(program_3)", file_name="data_log.log")


class ScatterPlot:
    """
    class to perform ScatterPlot representation using matplotlib
    """

    def display_scatter_plot(self):
        """
        Description:
            This function is used to draw a scatter plot using random distributions to generate balls of
            different sizes.
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            no_of_balls = 25
            # Draw samples from the triangular distribution over the interval [left, right].
            x = [random.triangular() for _ in range(no_of_balls)]
            # draw samples from normal distribution/gaussian distribution
            y = [random.gauss(0.5, 0.25) for _ in range(no_of_balls)]
            colors = [random.randint(1, 4) for _ in range(no_of_balls)]
            areas = [
                math.pi * random.randint(5, 15) ** 2 for _ in range(no_of_balls)]
            # create a figure object
            plt.figure()
            plt.scatter(x, y, s=areas, c=colors, alpha=0.850)
            plt.axis([0.0, 1.0, 0.0, 1.0])
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.show()

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = ScatterPlot()
    np_obj.display_scatter_plot()
