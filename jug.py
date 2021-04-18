import math  # import the math class

import unittest  # import unittest class


def findWaterContainerPath(a, b, c):  # define function findWaterContainerPath
    """
        A Function to find a path (solution) to the water jug problem.

        parameters
        -----------------
        a : int
            capacity of the larger jug.
        b : int
            capacity of the smaller jug.
        c : int
            capacity goal

    """

    starting_state = (0, 0)  # initialize starting_state

    final_path = list()  # initialize final_path to an empty list

    # adding sstarting_state to final_path list
    final_path.append(starting_state)
    for path in final_path:  # loop through the elements of final_path
        x, y = path  # assign values of tuple path to x and y
        if x == c or y == c:  # check if either x or y is equal to c
            break  # break aout of the loop if true

        # perform operations
        # Fill Larger jug
        # check if x equals 0 and tuple (a,y) is not in final_path
        if x == 0 and (a, y) not in final_path:
            # add (a,y) to final_path if its not in final_path already
            final_path.append((a, y))

        # fill smaller jug
        # check if y equals 0 and tuple (x,b) is not in final_path
        if y == 0 and (x, b) not in final_path:
            # add (x,b) to final_path if its not in final_path already
            final_path.append((x, b))

        # empty larger jug
        if (0, y) not in final_path:  # check if tuple (0,y) is not in final_path
            # add (0,y) to final_path if its not in final_path already
            final_path.append((0, y))

        # empty smaller jug
        if (x, 0) not in final_path:  # check if tuple (x,0) is not in final_path
            # add (x,0) to final_path if its not in final_path already
            final_path.append((x, 0))

        # pour contents of smaller jug into larger jug
        if x + y > a:  # check if contents in jug a and jug b combined are more than the capacity of jug a
            # Get the extra liters that will remain in the smaller jug after pouring into the larger jug
            n = (x + y) - a
            if (a, n) not in final_path:  # check if state (a,n) is not in final_path
                # add (a,n) to final_path if its not in final_path already
                final_path.append((a, n))
        else:  # if the above if statement is not true
            if (x + y, 0) not in final_path:  # check if state (x+y,0) is not in final_path
                # add (x+y,0) to final_path if its not in final_path already
                final_path.append((x + y, 0))

        # pour contents of larger jug to smaller jug

        if x <= b and x + y <= b:  # check if the contents of the larger jug are less than or equal to the capacity of the
                                # smaller jug and checking if contents in both jugs are less than the capacity of the smaller jugs
            if (0, x + y) not in final_path:  # check if state (0,x+y) is not in final_path
                # add (0,x+y) to final_path if its not in final_path already
                final_path.append((0, x + y))
        elif x + y > b:  # check if the capacity of water in both jugs exceeds the capacity of the smaller jug

            n = x + y - b  # get the capacity of water that will remain in the larger jug
            if (n, b) not in final_path:  # check if state (n,b) is not in final_path
                # add (n,b) to final_path if its not in final_path already
                final_path.append((n, b))

    return final_path  # return final_path


class TestWaterContainerGraphSearch(unittest.TestCase):

    def testFindWaterContainerPath(self):
        """Check the output of one basic example"""
        expected = [(0, 0), (4, 0), (0, 3), (4, 3), (1, 3),
                    (3, 0), (1, 0), (3, 3), (0, 1), (4, 2), (4, 1)]  # defining the expected value
        # check if the code evaluates to the evaluated value
        self.assertEqual(findWaterContainerPath(4, 3, 2), expected)

    def testFindWaterContainerPathType(self):
        """Check the return type of the function"""
        expected = list  # defining the expected return type
        # check if the return type is similar to the expected
        self.assertEqual(type(findWaterContainerPath(5, 4, 3)), expected)


def main():

    # take input from the stdin
    capacity_a = input("Enter the capacity of container A: ")

    # take input from the stdin
    capacity_b = input("Enter the capacity of container B: ")

    # take input from the stdin
    goal_amount = input("Enter the goal quantity: ")

    # check the type of inputs from the stdin
    try:
        """ Try casting the input values to integer, if an exception is raised the code terminates here"""
        capacity_a=int(capacity_a)
        capacity_b=int(capacity_b)
        goal_amount=int(goal_amount)
    except Exception as e:
        print("Enter the right Values!!!")  # print an error message
        return  # exit

    # check if the values will lead to a solvable problem
    if int(goal_amount) % math.gcd(int(capacity_a), int(capacity_b)) == 0:

        path = findWaterContainerPath(
            int(capacity_a), int(capacity_b), int(goal_amount))  # call the findWaterPathContainer function

    else:

        # print an error message
        print("No solution for containers with these sizes and with this final goal amount")

    print(path)  # print path


# unittest_main() - run all of TestWaterContainerGraphSearch's methods (i.e. test cases)

def unittest_main():

    unittest.main()


# evaluates to true if run as standalone program


if __name__ == '__main__':

    main()

    unittest_main()
