'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to append values to the end of an array.
            Expected Output:
            Original array:
            [10, 20, 30]

            After append values to the end of the array:
            [10 20 30 40 50 60 70 80 90]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_9)", file_name="data_log.log")


class NumericalPython:

    def append_values(self, my_array):
        """
        Description:
             This function is used to append values to the end of an array.
        Parameter:
            my_array: The my_array to be checked
        Return:
            Returns None
        """
        try:
            lg.info(f"original array: {my_array}")
            array_data = np.append(my_array, values=[[40, 50, 60, 70, 80, 90]])
            lg.info(f"after appending array: {array_data}")
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    my_array = [10, 20, 30]
    np_obj = NumericalPython()
    np_obj.append_values(my_array)
