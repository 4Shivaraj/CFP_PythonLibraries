'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Write a Python program to convert a list and tuple into arrays.
            List to array:
            [1 2 3 4 5 6 7 8]
            Tuple to array:
            [[8 4 6]
            [1 2 3]]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_8)", file_name="data_log.log")


class NumericalPython:

    def convert_to_array(self, my_list, my_tuple):
        """
        Description:
             This function is used to convert a list and tuple into arrays
        Parameter:
            my_list, my_tuple: The my_list and my_tuple to be checked
        Return:
            Returns None
        """
        try:
            list_data = np.asarray(my_list)
            lg.info(f"after converting list to array: \n{list_data}")
            tuple_data = np.asarray(my_tuple)
            lg.info(f"after converting tuple to array: \n{tuple_data}")
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]
    my_tuple = ([8, 4, 6], [1, 2, 3])
    np_obj = NumericalPython()
    np_obj.convert_to_array(my_list, my_tuple)
