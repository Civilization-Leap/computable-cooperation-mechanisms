import json,os,unittest
from mechanism_ref.core import evaluate
ROOT=os.path.dirname(os.path.dirname(__file__))
def ex(n):
 with open(os.path.join(ROOT,'examples',n),encoding='utf-8') as f:return json.load(f)
class BYOPAcquisitionT(unittest.TestCase):
 def test_full_acquisition_violates_declared_employee_boundary(self):
  self.assertEqual(evaluate(ex('byop_acquisition_full.json'))['overall_declared_constraint_status'],'VIOLATED')
 def test_long_term_contract_satisfies_declared_boundaries(self):
  self.assertEqual(evaluate(ex('byop_acquisition_long_term_contract.json'))['overall_declared_constraint_status'],'SATISFIED')
 def test_minority_investment_preserves_unknown(self):
  self.assertEqual(evaluate(ex('byop_acquisition_minority_investment.json'))['overall_declared_constraint_status'],'UNKNOWN')
if __name__=='__main__':unittest.main()
