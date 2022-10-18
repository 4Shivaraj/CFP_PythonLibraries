'''
    @Author: Shivaraj
    @Date: 14-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 14-10-2022
    @Title: Create a 3x3 matrix with values ranging from 2 to 10.
            Expected Output:
            [[ 2 3 4]
            [ 5 6 7]
            [ 8 9 10]]
'''
import sys

from data_log import get_logger

import numpy as np

lg = get_logger(name="(program_2)", file_name="data_log.log")


class NumericalPython:

    def create_matrix(self):
        """
        Description:
             This function is used to Create a 3x3 matrix with values ranging from 2 to 10.
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            matrix = np.random.randint(2, 10, (3, 3))
            lg.info(f" 3x3 matrix : \n{matrix}")
        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = NumericalPython()
    np_obj.create_matrix()
