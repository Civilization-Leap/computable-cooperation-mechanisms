import argparse,json,os
from .core import load_case,evaluate,report,InputError
def main(argv=None):
 p=argparse.ArgumentParser();p.add_argument("case");p.add_argument("--out-dir",default="outputs");a=p.parse_args(argv)
 try:r=evaluate(load_case(a.case))
 except (InputError,OSError,json.JSONDecodeError) as e:p.error(str(e))
 os.makedirs(a.out_dir,exist_ok=True);stem=os.path.splitext(os.path.basename(a.case))[0]
 result_path=os.path.join(a.out_dir,stem+".result.json");report_path=os.path.join(a.out_dir,stem+".report.md")
 with open(result_path,"w",encoding="utf-8") as f:json.dump(r,f,ensure_ascii=False,indent=2,sort_keys=True,allow_nan=False)
 with open(report_path,"w",encoding="utf-8") as f:f.write(report(r))
 print(r["overall_declared_constraint_status"]);return 0
if __name__=="__main__":raise SystemExit(main())
