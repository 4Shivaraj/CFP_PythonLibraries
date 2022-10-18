'''@Author: Shivaraj @Date: 14-10-2022 @Last Modified by: Shivaraj @Last Modified date: 14-10-2022 @Title: Write a
Python program to create an array of (3, 4) shape, multiply every element value by 3 and display the new array.
Expected Output: Original array elements: [[ 0 1 2 3] [ 4 5 6 7] [ 8 9 10 11]] New array elements: [[ 0 3 6 9] [12 15
18 21] [24 27 30 33]] '''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_22)", file_name="data_log.log")


class NumericalPython:

    def multiply_array(self):
        """
        Description:
             This function is used to multiply every element value by 3 and display the new array
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            arr = np.arange(12).reshape((3, 4))
            my_array = arr.astype(int)
            lg.info(f"original array elements: \n{my_array}")
            new_array = my_array * 3
            lg.info(f'new array elemts: \n{new_array}')

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = NumericalPython()
    np_obj.multiply_array()
