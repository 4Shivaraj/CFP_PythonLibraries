'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to make an array immutable (read-only).
            Expected Output:
            Test the array is read-only or not:
            Try to change the value of the first element:
            Traceback (most recent call last):
            File "19236bd0-0bd9-11e7-a232-c706d0968eb6.py", line 6, in
            x[0] = 1
            ValueError: assignment destination is read-only
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_21)", file_name="data_log.log")


class NumericalPython:

    def make_immutable(self):
        """
        Description:
             This function is used to make an array immutable.
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            my_array1 = np.zeros(10)
            my_array1.flags.writeable = False
            lg.info('Test the array is read-only or not: ')
            lg.info('Try to change the value of the first element: ')
            my_array1[0] = 5
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = NumericalPython()
    np_obj.make_immutable()
