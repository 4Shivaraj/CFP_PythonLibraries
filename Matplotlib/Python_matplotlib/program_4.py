'''
    @Author: Shivaraj
    @Date: 16-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 16-10-2022
    @Title: Write a Python program to draw line charts of the financial data of Alphabet Inc. between
            October 3, 2016 to October 7, 2016.
            Sample Financial data (fdata.csv):
            Date,Open,High,Low,Close
            03-10-16,774.25,776.065002,769.5,772.559998
            04-10-16,776.030029,778.710022,772.890015,776.429993
            05-10-16,779.309998,782.070007,775.650024,776.469971
            06-10-16,779,780.47998,775.539978,776.859985
            07-10-16,779.659973,779.659973,770.75,775.080017
'''
import matplotlib.pyplot as plt
import pandas as pd
import sys

from data_log import get_logger

lg = get_logger(name="(program_4)", file_name="data_log.log")


class DrawLine:
    """
    class to perform graphical representation of data using matplotlib
    """

    def line_charts_plotting(self):
        """
        Description:
             This function is used to draw line charts of the financial data
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            # reading .csv file
            df = pd.read_csv('fdata.csv', sep=',',
                             parse_dates=True, index_col=0)
            print(df)

            # plotting of fdata.csv file's financial data
            df.plot()

            # show the figure
            plt.show()

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = DrawLine()
    np_obj.line_charts_plotting()
