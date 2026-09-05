import argparse,json,os
from .core import load_case,evaluate,report,InputError
def main(argv=None):
 p=argparse.ArgumentParser();p.add_argument("case");p.add_argument("--out-dir",default="outputs");a=p.parse_args(argv)
 try:r=evaluate(load_case(a.case))
 except (InputError,OSError,json.JSONDecodeError) as e:p.error(str(e))
 os.makedirs(a.out_dir,exist_ok=True);stem=os.path.splitext(os.path.basename(a.case))[0]
 json.dump(r,open(os.path.join(a.out_dir,stem+".result.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2,sort_keys=True,allow_nan=False)
 open(os.path.join(a.out_dir,stem+".report.md"),"w",encoding="utf-8").write(report(r));print(r["overall_declared_constraint_status"]);return 0
if __name__=="__main__":raise SystemExit(main())
