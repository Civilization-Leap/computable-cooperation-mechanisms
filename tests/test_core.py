import copy,json,os,tempfile,unittest
from mechanism_ref.core import evaluate,load_case,InputError
ROOT=os.path.dirname(os.path.dirname(__file__))
def ex(n):
 with open(os.path.join(ROOT,'examples',n),encoding='utf-8') as f:return json.load(f)
class T(unittest.TestCase):
 def test_ok(self):self.assertEqual(evaluate(ex('shared_equipment_ok.json'))['overall_declared_constraint_status'],'SATISFIED')
 def test_hard_not_offset(self):self.assertEqual(evaluate(ex('shared_equipment_third_party_violation.json'))['overall_declared_constraint_status'],'VIOLATED')
 def test_unknown(self):self.assertEqual(evaluate(ex('shared_equipment_unknown.json'))['overall_declared_constraint_status'],'UNKNOWN')
 def test_capacity_violation_new_same_class_case(self):self.assertEqual(evaluate(ex('shared_equipment_capacity_violation.json'))['overall_declared_constraint_status'],'VIOLATED')
 def test_deterministic(self):
  c=ex('shared_equipment_ok.json');self.assertEqual(evaluate(c),evaluate(c))
 def test_input_not_mutated(self):
  c=ex('shared_equipment_ok.json');before=copy.deepcopy(c);evaluate(c);self.assertEqual(c,before)
 def test_nan_rejected(self):
  c=ex('shared_equipment_ok.json');c['candidate']['allocations']['equipment_slots']=float('nan')
  with self.assertRaises(InputError):evaluate(c)
 def test_duplicate_key_rejected(self):
  with tempfile.NamedTemporaryFile('w',delete=False) as f:f.write('{"schema_version":"a","schema_version":"b"}');p=f.name
  try:
   with self.assertRaises(InputError):load_case(p)
  finally:os.unlink(p)
 def test_duplicate_outcome_rejected(self):
  c=ex('shared_equipment_ok.json');c['candidate']['outcomes'].append(copy.deepcopy(c['candidate']['outcomes'][0]))
  with self.assertRaises(InputError):evaluate(c)
 def test_undeclared_unit_rejected(self):
  c=ex('shared_equipment_ok.json');c['candidate']['outcomes'][0]['unit']='UNDECLARED'
  with self.assertRaises(InputError):evaluate(c)
 def test_missing_resource_reference_rejected(self):
  c=ex('shared_equipment_ok.json');c['constraints'][0]['resource']='future_slots'
  with self.assertRaises(InputError):evaluate(c)
 def test_future_capability_field_not_silently_accepted(self):
  c=ex('shared_equipment_ok.json');c['future_capability']={'equipment_slots':99}
  with self.assertRaises(InputError):evaluate(c)
if __name__=='__main__':unittest.main()
