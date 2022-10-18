'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to find the real and imaginary parts of an array of complex numbers.
            Expected Output:
            Original array [ 1.00000000+0.j 0.70710678+0.70710678j]
            Real part of the array:
            [ 1. 0.70710678]
            Imaginary part of the array:
            [ 0. 0.70710678]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_10)", file_name="data_log.log")


class NumericalPython:

    def append_values(self, complex_array):
        """
        Description:
             This function is used to find the real and imaginary parts of an array of complex numbers.
        Parameter:
            complex_array: The complex_array to be checked
        Return:
            Returns None
        """
        try:
            lg.info(f"original complex number arrays are: \n{complex_array}")
            real_num = np.real(complex_array)
            imaginary_num = np.imag(complex_array)
            lg.info(
                f"\nreal number: {real_num} and \ncomplex number: {imaginary_num}")
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    complex_array = [1.00000000 + 0.j, 0.70710678 + 0.70710678j]
    np_obj = NumericalPython()
    np_obj.append_values(complex_array)
