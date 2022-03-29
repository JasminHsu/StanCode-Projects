"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_result = GRAPH_MARGIN_SIZE + year_index*((width - GRAPH_MARGIN_SIZE) / len(YEARS))
    return x_result


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')  # delete all existing lines from the canvas
    # Draw the upper line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    # Draw the lower line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    # Draw vertical line and label according to the list of years
    for i in range(len(YEARS)):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_coordinate, GRAPH_MARGIN_SIZE, x_coordinate, CANVAS_HEIGHT)
        canvas.create_text(x_coordinate+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid
    scale = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / MAX_RANK
    for i in range(len(lookup_names)):  # Number of names
        color_num = i % len(COLORS)
        color = COLORS[color_num]

        for j in range(len(YEARS)-1):  # Number of curves
            name = lookup_names[i]

            if j <= len(YEARS)-2:
                year_1 = YEARS[j]
                year_2 = YEARS[j+1]
                x1 = get_x_coordinate(CANVAS_WIDTH, j)
                x2 = get_x_coordinate(CANVAS_WIDTH, j+1)
                # Determine if the ranking of names is higher or lower than 1000
                if str(year_1) in name_data[name]:
                    rank_1 = name_data[name][str(year_1)]
                    y1 = GRAPH_MARGIN_SIZE + int(rank_1) * scale
                else:
                    y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    rank_1 = '*'
                if str(year_2) in name_data[name]:
                    rank_2 = name_data[name][str(year_2)]
                    y2 = GRAPH_MARGIN_SIZE + int(rank_2) * scale
                else:
                    y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    rank_2 = '*'

                # Draw curves and year label by concatenating every year
                canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)
                canvas.create_text(x1+TEXT_DX, y1, text=(name, rank_1), anchor=tkinter.SW, fill=color)
                if j == len(YEARS)-2:  # Last year label
                    canvas.create_text(x2 + TEXT_DX, y2, text=(name, rank_2), anchor=tkinter.SW, fill=color)


# Don't understand why below can't work
#             if j <= len(YEARS)-2:
#                 year_1 = YEARS[j]
#                 year_2 = YEARS[j+1]
#                 x1 = get_x_coordinate(CANVAS_WIDTH, j)
#                 x2 = get_x_coordinate(CANVAS_WIDTH, j+1)
#                 rank_1 = name_data[name][str(year_1)]
#                 rank_2 = name_data[name][str(year_2)]
#                 # Determine (x,y) coordinate based on rank
#                 if rank_1 is not None or int(rank_1) <= MAX_RANK:  # Rank <= 1000
#                     y1 = GRAPH_MARGIN_SIZE + int(rank_1) * scale
#                 else:  # Rank > 1000
#                     y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
#                     rank_1 = '*'
#                 if rank_2 is not None and int(rank_2) <= MAX_RANK:  # Rank <= 1000
#                     y2 = GRAPH_MARGIN_SIZE + int(rank_2) * scale
#                 else:  # Rank > 1000
#                     y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
#                     rank_2 = '*'
#                 canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[i])
#                 canvas.create_text(x1+TEXT_DX, y1, text=(name, rank_1), anchor=tkinter.SW)
#                 if j == len(YEARS)-2:
#                     canvas.create_text(x2 + TEXT_DX, y2, text=(name, rank_2), anchor=tkinter.SW)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
