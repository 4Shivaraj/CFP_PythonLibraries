'''@Author: Shivaraj
    @Date: 16-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 16-10-2022
    @Title: Write a Python program to draw a scatter plot comparing two subject marks of Mathematics and Science. Use
            marks of 10 students. Test Data: math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34] science_marks =
            [35, 79, 79, 48, 100, 88, 32, 45, 20, 30] marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
            Write a Python program to draw a scatter graph taking a random distribution in X and Y and plotted against
            each other.
'''
import matplotlib.pyplot as plt
import sys

from data_log import get_logger

lg = get_logger(name="(program_4)", file_name="data_log.log")


class ScatterPlot:
    """
    class to perform ScatterPlot representation using matplotlib
    """

    def display_scatter_plot(self):
        """
        Description:
             This function is used draw a scatter plot comparing two subject marks
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
            science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
            mark_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

            plt.scatter(mark_range, math_marks, label='Math Marks', color='b')
            plt.scatter(mark_range, science_marks,
                        label='Science Marks', color='g')
            plt.title('Scatter Plot')
            plt.xlabel("Marks Range")
            plt.ylabel('Marks Scored')
            # linked to the data being graphically displayed in the plot area of the chart.
            plt.legend()
            plt.show()

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = ScatterPlot()
    np_obj.display_scatter_plot()
