def wave_print_2d_array(x, y):
    """Take x and y as width and height of 2D array, fill it with incrementing numbers and wave print it column-wise.
    # Source: Google Coding Interview Question (Coding Club - LinkedIn), Difficulty: Hard

    :param x: width of 2D array
    :param y: height of 2D array
    :return: list of elements wave printed column-wise
    """

    # Construct the 2D array
    array = []
    for i in range(1, x + 1):
        row = []
        for j in range(1, y + 1):
            row.append('{}{}'.format(str(i), str(j)))
        array.append(row)

    # Wave print the elements
    result = ''
    for col in range(y):
        if col % 2 == 0:
            vertical_position = col
            for row in range(x):
                result += '{} '.format(array[row][vertical_position])
        else:
            vertical_position = x - 1
            for row in range(x):
                result += '{} '.format(array[vertical_position][col])
                vertical_position -= 1

    return result
