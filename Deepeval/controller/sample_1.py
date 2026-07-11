from deepeval import assert_test
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from deepeval.metrics import GEval

class SampleTest1(LLMTestCase, LLMTestCaseParams):

    def evaluate_using_Geval(self):
        metrics = {}
        