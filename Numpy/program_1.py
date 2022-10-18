'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to convert a list of numeric value into a one-dimensional NumPy array.
            Expected Output:
            Original List: [12.23, 13.32, 100, 36.32]
            One-dimensional numpy array: [ 12.23 13.32 100. 36.32]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_1)", file_name="data_log.log")


class NumericalPython:

    def display_1D_array(self, my_list):
        """
        Description:
             This function is used to convert a list of numeric value into a one-dimensional NumPy array
        Parameter:
            my_list: The my_list to be checked
        Return:
            Returns None
        """
        try:
            np_array = np.array(my_list)
            lg.info(f" one-dimensional numpy array: \n{np_array}")
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    my_list = [12.23, 13.32, 100, 36.32]
    np_obj = NumericalPython()
    np_obj.display_1D_array(my_list)
