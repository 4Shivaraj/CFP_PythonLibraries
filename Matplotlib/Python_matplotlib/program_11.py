'''
    @Author: Shivaraj
    @Date: 16-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 16-10-2022
    @Title: Write a Python program to plot several lines with different format styles in one command using arrays.
'''
import matplotlib.pyplot as plt
import numpy as np
import sys

from data_log import get_logger

lg = get_logger(name="(program_11)", file_name="data_log.log")


class DrawLine:
    """
    class to perform graphical representation of data using matplotlib
    """

    def line_plotting(self):
        """
        Description:
             This function is used to plot several lines with different format styles in one command using arrays.
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            t = np.arange(0., 5., 0.2)
            # array([0. , 0.2, 0.4, 0.6, 0.8, 1. , 1.2, 1.4, 1.6, 1.8, 2. , 2.2, 2.4, 2.6, 2.8, 3. , 3.2, 3.4, 3.6,
            # 3.8, 4. , 4.2, 4.4, 4.6, 4.8])

            # green dashes, blue squares and red triangles
            plt.plot(t, t, 'g--', t, t ** 2, 'bs', t, t ** 3, 'r^')
            plt.show()

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = DrawLine()
    np_obj.line_plotting()
