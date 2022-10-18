'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to find the number of elements of an array, length of one
            array element in bytes and total bytes consumed by the elements.
            Expected Output:
            Size of the array: 3
            Length of one array element in bytes: 8
            Total bytes consumed by the elements of the array: 24
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_11)", file_name="data_log.log")


class NumericalPython:

    def find_array_Details(self, arr_data):
        """
        Description:
             This function is used to find the size of array and total bytes consumed by the elements of the array
        Parameter:
            arr_data: The arr_data to be checked
        Return:
            Returns None
        """
        try:
            my_array = np.array(arr_data, dtype=np.float64)
            lg.info(
                f" \nsize of array: {my_array.size}, \nlength of one array element in list: {my_array.itemsize} and \ntotal bytes consumed by element of an array: {my_array.nbytes}")
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    arr_data = [1, 2, 3]
    np_obj = NumericalPython()
    np_obj.find_array_Details(arr_data)
