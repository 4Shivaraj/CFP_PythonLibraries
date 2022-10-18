'''
    @Author: Shivaraj
    @Date: 16-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 16-10-2022
    @Title: Write a Python programming to create a pie chart of gold medal achievements of five most
            successful countries in 2016 Summer Olympics. Read the data from a csv file.
            Sample data:
            medal.csv
            country,gold_medal
            United States,46
            Great Britain,27
            China,26
            Russia,19
            Germany,17
'''
import matplotlib.pyplot as plt
import pandas as pd
import sys

from data_log import get_logger

lg = get_logger(name="(program_3)", file_name="data_log.log")


class PieChart:
    """
    class to perform pie chart representation using matplotlib
    """

    def display_piechart(self):
        """
        Description:
             This function is used to create a pie chart of gold medal achievements of five most successful countries
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            # read csv file medal.csv
            df = pd.read_csv("D:\MACHINE_LEARNING\CFP\PythonLibraries\Matplotlib\Matplotlib_pie\medal.csv")
            # get label and medal for each respective countries
            country = df["country"]
            medal = df["gold_medal"]
            # explode first country having large medal in olympics
            explode = (0.1, 0, 0, 0, 0)
            colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]
            # plotting of csv file data
            plt.pie(medal, explode=explode, labels=country, colors=colors,
                    autopct='%1.1f%%', shadow=True, startangle=140)
            plt.title("Gold medal achievements of five most successful\n" +
                      "countries in 2016 Summer Olympics")
            # show figure
            plt.show()

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = PieChart()
    np_obj.display_piechart()
