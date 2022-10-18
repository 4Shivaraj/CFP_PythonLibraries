'''
    @Author: Shivaraj
    @Date: 16-10-2022
    @Last Modified by: Shivaraj
    @Last Modified date: 16-10-2022
    @Title: Write a Python programming to display a bar chart of the popularity of programming
            Languages. Attach a text label above each bar displaying its popularity (float value).
            Sample data:
            Programming languages: Java, Python, PHP, JavaScript, C#, C++
            Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7
'''
import matplotlib.pyplot as plt
import sys

from data_log import get_logger

lg = get_logger(name="(program_5)", file_name="data_log.log")


class BarChart:
    """
    class to perform bar chart representation using matplotlib
    """

    def display_barchart(self):
        """
        Description:
             This function is used to display a bar chart of the popularity of programming Languages
        Parameter:
            None
        Return:
            Returns None
        """
        try:
            prg_lang = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
            popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

            # iterate through no.of language
            x_pos = [i for i, _ in enumerate(prg_lang)]  # [0, 1, 2, 3, 4, 5]

            # using the variable ax for single a Axes
            fig, ax = plt.subplots()
            rects = ax.bar(x_pos, popularity, color=('Blue', 'Green', 'Red', 'Yellow', 'cyan', 'Violet'))

            # Set the x-axis label
            plt.xlabel("Languages")

            # Set the y-axis label
            plt.ylabel("Popularity")

            # Sets a title
            plt.title("Popularity of Programming Languages")
            plt.xticks(x_pos, prg_lang)

            # Attach a text label above each bar displaying its height
            for rect in rects:
                height = rect.get_height()
                lg.info(f"getx: {rect.get_x()}")
                ax.text(rect.get_x() + rect.get_width() / 2., 1.0 * height,
                        '%f' % float(height),
                        ha='center', va='bottom')

            # To display graph
            plt.show()

        except Exception:
            exception_type, _, exception_traceback = sys.exc_info()
            line_number = exception_traceback.tb_lineno
            lg.exception(
                f"Exception type : {exception_type} \nError on line number : {line_number}")


if __name__ == "__main__":
    np_obj = BarChart()
    np_obj.display_barchart()
