'''
    @Author: Shivaraj
    @Date: 16-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 16-10-2022
    @Title: Write a Python programming to display a horizontal bar chart of the popularity of
            programming Languages.
            Sample data:
            Programming languages: Java, Python, PHP, JavaScript, C#, C++
            Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
'''
import matplotlib.pyplot as plt
import sys

from data_log import get_logger

lg = get_logger(name="(program_2)", file_name="data_log.log")


class BarChart:
    """
    class to perform bar chart representation using matplotlib
    """

    def display_horizontal_barchart(self):
        """
        Description:
             This function is used to display a horizontal bar chart of the popularity of programming Languages
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            prg_lang = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
            popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

            # plotting x and y-axis values to create horizontal bar chart
            plt.barh(prg_lang, popularity)

            # Set the x-axis label
            plt.xlabel("Languages")

            # Set the y-axis label
            plt.ylabel("Popularity")

            # Sets a title
            plt.title("Popularity of Programming Languages")

            # To display graph
            plt.show()

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = BarChart()
    np_obj.display_horizontal_barchart()
