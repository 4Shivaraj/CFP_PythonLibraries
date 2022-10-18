'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to remove specific elements in a numpy array.
            Expected Output:
            Original array:
            [ 10 20 30 40 50 60 70 80 90 100]
            Delete first, fourth and fifth elements:
            [ 20 30 60 70 80 90 100]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_27)", file_name="data_log.log")


class NumericalPython:

    def remove_element(self, arr1):
        """
        Description:
             This function is used to remove specific elements in a numpy array.
        Parameter:
            arr1: The arr1 to be checked
        Return:
            Returns None
        """
        try:
            my_array = np.array(arr1)
            lg.info(f'original array: \n{my_array}')
            index = [0, 3, 4]
            result_array = np.delete(my_array, index)
            lg.info(f'final array: \n{result_array}')
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    np_obj = NumericalPython()
    np_obj.remove_element(arr)
