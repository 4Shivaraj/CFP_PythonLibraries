'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to change the data type of an array.
            Expected Output:
            [[ 2 4 6]
            [ 6 8 10]]
            Data type of the array x is: int32
            New Type: float64
            [[ 2. 4. 6.]
            [ 6. 8. 10.]]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_17)", file_name="data_log.log")


class NumericalPython:

    def change_data_type(self, arr1):
        """
        Description:
             This function is used to change the data type of an array.
        Parameter:
            arr1: The arr1 to be checked
        Return:
            Returns None
        """
        try:
            array1 = np.array(arr1, np.int32)
            lg.info(f'Array-1: \n{array1} and data type: {array1.dtype}')
            float_array = array1.astype(float)
            lg.info(f'new data type array : \n{float_array}')
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    my_array = [[2, 4, 6], [6, 8, 10]]
    np_obj = NumericalPython()
    np_obj.change_data_type(my_array)
