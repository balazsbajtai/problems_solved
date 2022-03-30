def positive_sum(nums):
    """ Return the smallest positive start value which when added to the elements of the provided list
    (from left to right) always yields a number not less than 1.
    # Source: Google Coding Interview Question (Coding Club - LinkedIn), Difficulty: Hard

    :param nums: list of numbers to add to the start value
    :return: smallest positive start value
    """
    start_value = 1
    result = 0

    def get_sum_of_numbers():
        sum_of_numbers = start_value
        for n in nums:
            sum_of_numbers = sum_of_numbers + n
            if sum_of_numbers < 1:
                return 0
        return sum_of_numbers

    while result < 1:
        result = get_sum_of_numbers()
        if result < 1:
            start_value += 1
        else:
            return start_value
