from RefactoringTests.CleanTests import *
from RefactoringTests.ValidationTests import *
from RefactoringTests.EditorNewValueTests import *
from RefactoringTests.EditorStringToListTests import *


def refactoring_suite():
    the_suite = unittest.TestSuite()
    the_suite.addTest(unittest.makeSuite(CleanCoverageTests))
    the_suite.addTest(unittest.makeSuite(ValidationCoverageTests))
    the_suite.addTest(unittest.makeSuite(EditorNewValueCoverageTests))
    the_suite.addTest(unittest.makeSuite(EditorStringTests))

    return the_suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = refactoring_suite()
    runner.run(test_suite)