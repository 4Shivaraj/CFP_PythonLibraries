'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to convert a NumPy array into Python list structure.
            Expected Output:
            Original array elements:
            [[0 1]
            [2 3]
            [4 5]]
            Array to list:
            [[0, 1], [2, 3], [4, 5]]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_23)", file_name="data_log.log")


class NumericalPython:

    def convert_array_list(self):
        """
        Description:
             This function is used to convert a NumPy array into Python list structure
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            my_array = np.arange(6).reshape(3, 2)
            lg.info(f"original array elements: \n{my_array}")
            lg.info(f'array to list: \n{my_array.tolist()}')

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = NumericalPython()
    np_obj.convert_array_list()
