'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to reverse an array (first element becomes last).
            Original array:
            [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
            Reverse array:
            [37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_4)", file_name="data_log.log")


class NumericalPython:

    def reverse_array(self):
        """
        Description:
             This function is used to reverse an array.
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            my_array = np.arange(12, 38)
            lg.info(f"original array: \n{my_array}")
            reversed_array = my_array[::-1]
            lg.info(f"array after reversing: \n{reversed_array}")
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = NumericalPython()
    np_obj.reverse_array()
