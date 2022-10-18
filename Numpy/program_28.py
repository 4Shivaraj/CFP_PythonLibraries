'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to save a NumPy array to a text file.
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_28)", file_name="data_log.log")


class NumericalPython:

    def save_to_text(self):
        """
        Description:
             This function is used to to save a NumPy array to a text file
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            array1 = np.arange(12).reshape(3, 4)
            lg.info(f'original array : \n{array1}')
            header = 'col1 col2 col3'
            np.savetxt('demo.txt', array1, fmt='%d', header=header)
            result = np.loadtxt('demo.txt')
            lg.info(f"After loading, content of the text file: {result}")
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = NumericalPython()
    np_obj.save_to_text()
