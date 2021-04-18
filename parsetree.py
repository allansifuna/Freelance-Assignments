from stack import Stack
from binarytree import BinaryTree
import unittest #package that enables us to self test our code and compare the outcome aganist expected outcomes.
import random# package that enables us to generate random numbers


def buildMPLogicParseTree(exp):
    """
    params:
    ------
        exp: (str)

    return type: (BinaryTree)

    "Builds a parse tree from an MP logic expression"
    """
    elist = exp.split() #split th expression on spaces into a list
    pStack = Stack()# Instanciate Stack Object
    bTree = BinaryTree('')#instanciate BinaryTree object
    pStack.push(bTree)#add the BinaryTree object into the Stack Object
    current_tree = bTree#copy BinaryTree object into another variable

    for i in elist: #loop through the list of expression items
        if i == '(':# check if the current element is an opening bracket
            current_tree.insertLeft('') #inserts a blank to the left child of the BinaryTree object.
            pStack.push(current_tree)#add the BinaryTree object into the Stack Object
            current_tree = current_tree.getLeftChild() #change the root pointer of the BinaryTree object
                                                        # to its left child

        elif i in ['OR', 'AND']:#check if current item in the list expression is an OR or AND
            current_tree.setRootVal(i)#sets root value of the BinaryTree object to i
            current_tree.insertRight('')#inserts a blank to the right child of the BinaryTree object.
            pStack.push(current_tree)#add the BinaryTree object into the Stack Object
            current_tree = current_tree.getRightChild() #change the root pointer of the BinaryTree object
                                                        # to its right child

        elif i.startswith('M') or i.startswith('P') or i in ['T', 'F']: #check if current item in the list expression starts with P or M or is an OR or AND
            current_tree.setRootVal(i)#sets root value of the BinaryTree object to i
            parent = pStack.pop()#removes the recently added item to the stack and assigns it to parent
            current_tree = parent# assigns parent to current_tree

        elif i == ')': #checks if current item in the expression list is a closing bracket
            current_tree = pStack.pop()#removes the recently added item to the stack and assigns it to current_tree

        else:
            print("Invalid expression")#gives feedback incase of an error
            return None

    return bTree#return BinaryTree object


def evaluateMPLogicParseTree(parse_tree):
    """
    params:
    ------
        parse_tree (BinaryTree)

    return type: (str)

    "evaluates a Maybe-Probably expression from a BinaryTree"
    """
    opers = {'T': True, 'F': False} #defines dictionary opers

    _opers = {True: 'T', False: 'F'} #defines dict _opers

    left_c = parse_tree.getLeftChild() #gets left chils of the parse_tee
    right_c = parse_tree.getRightChild() #gets right chils of the parse_tee
    if left_c and right_c:#checks if left_c and right_c are not None
        fn = parse_tree.getRootVal().lower()#gets root value of the parse tree and converts it to lower case
        eLeftC = evaluateMPLogicParseTree(left_c)#recursively evaluates the left child
        eRightC = evaluateMPLogicParseTree(right_c)#recursively evaluates the right child
        if eLeftC.startswith('M'):#check if eLeftC starts with M
            t_val = float(eLeftC.split("_")[1])#split eLeftC on underscore get the element at index 1 and cast it to a float
            if not 0.0 <= t_val <= 0.75:#check if t_val in the correct range
                print("Invalid")#prints an error message incase of an error.
                return
            to_eval = random.random() #generate a random number to help in evaluation
            return _opers[eval(f"{t_val>=to_eval} {fn} {opers[eRightC]}")]#evaluate the operands using boolean logic]

        elif eLeftC.startswith('P'):
            t_val = float(eLeftC.split("_")[1])#split eLeftC on underscore get the element at index 1 and cast it to a float
            if not 0.75 <= t_val < 1.0:#check if t_val in the correct range
                print("Invalid")#prints an error message incase of an error.
                return
            to_eval = random.random() #generate a random number to help in evaluation
            return _opers[eval(f"{t_val>=to_eval} {fn} {opers[eRightC]}")] #evaluate the operands using boolean logic]

        elif eRightC.startswith('M'):
            t_val = float(eRightC.split("_")[1])#split eRightC on underscore get the element at index 1 and cast it to a float
            if not 0.0 <= t_val <= 0.75:#check if t_val in the correct range
                print("Invalid")#prints an error message incase of an error.
                return
            to_eval = random.random() #generate a random number to help in evaluation
            return _opers[eval(f"{t_val>=to_eval} {fn} {opers[eLeftC]}")]#evaluate the operands using boolean logic

        elif eRightC.startswith('P'):
            t_val = float(eRightC.split("_")[1])#split eRightC on underscore get the element at index 1 and cast it to a float
            if not 0.75 <= t_val < 1.0:#check if t_val in the correct range
                print("Invalid")#prints an error message incase of an error.
                return
            to_eval = random.random() #generate a random number to help in evaluation
            return _opers[eval(f"{t_val>=to_eval} {fn} {opers[eLeftC]}")]#evaluate the operands using boolean logic
        else:
            return _opers[eval(f"{opers[eLeftC]} {fn} {opers[eRightC]}")]#evaluate the operands using boolean logic
    else:
        return parse_tree.getRootVal() #returns root val of parse tree


def printMPLogicExpression(tree):
    """
    params:
    ------
        tree (BinaryTree)

    return type: (str)

    prints an expression from a parameter of type BinaryTree
    """
    s_val = "" #define s_val
    if tree:
        s_val = '(' + printMPLogicExpression(tree.getLeftChild()) #recursively appends left child to s_val
        s_val = s_val + str(tree.getRootVal())#gets tree's root val
        s_val = s_val + printMPLogicExpression(tree.getRightChild()) + ')'  #recursively appends right child to s_val
    return s_val


class TestMPLogicParseTreeFunction(unittest.TestCase):
    """ your unit tests should be in here """

    def testBuildMPLogicParseTree(self):
        """ Test if pt is of type BinaryTree"""
        pt = buildMPLogicParseTree('( ( T AND F ) OR M_0.3 )') #build an MPLogic parse tree
        expected = BinaryTree("")#Define the expected value
        self.assertEqual(type(pt), type(expected)) #compares to make sure that our code evaluates to the expected value

    def testEvaluateMPLogicParseTree(self):
        """ Test binary logic evaluation"""
        pt = buildMPLogicParseTree('( T AND F )')#build an MPLogic parse tree
        ans = evaluateMPLogicParseTree(pt) #evaluates MPLogic parse tree
        expected = "F"#Define the expected value
        self.assertEqual(ans, expected)#compares to make sure that our code evaluates to the expected value


    def testPrintMPLogicExpression(self):
        """ Test print expression logic"""
        pt = buildMPLogicParseTree('( ( T AND F ) OR M_0.3 )')#build an MPLogic parse tree
        exp = printMPLogicExpression(pt) #prints MPLogic parse tree
        expected = "(((T)AND(F))OR(M_0.3))" #Define the expected value
        self.assertEqual(exp, expected)#compares to make sure that our code evaluates to the expected value



# code you want to run when this is exectuted as a standalone program should be in here


def main():
    # pass
    pt = buildMPLogicParseTree('( ( T AND F ) OR M_0.3 )')#build an MPLogic parse tree
    ans = evaluateMPLogicParseTree(pt)#evaluates MPLogic parse tree
    exp = printMPLogicExpression(pt)#prints an MPLogic parse tree
    print("Evaluating parse tree...", ans)
    print(exp)

# unittest_main() - run unittest's main, which runs TestMPLogicParseTreeFunction's methods


def unittest_main():
    print("-" * 25, "running unit tests", "-" * 25)
    unittest.main()


# evaluates to true if run as standalone program (e.g. $ python parsetree.py)
if __name__ == '__main__':
    main()
    unittest_main()
