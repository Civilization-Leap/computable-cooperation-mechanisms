import hashlib,json,math
class InputError(ValueError): pass
def loads_strict(s):
 def hook(pairs):
  d={}
  for k,v in pairs:
   if k in d: raise InputError(f"duplicate JSON key: {k}")
   d[k]=v
  return d
 return json.loads(s,object_pairs_hook=hook,parse_constant=lambda x:(_ for _ in()).throw(InputError(f"non-finite JSON value: {x}")))
def load_case(path):
 with open(path,encoding="utf-8") as f:c=loads_strict(f.read())
 validate(c);return c
def num(v,path):
 if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v):raise InputError(f"{path}: expected finite number")
 return float(v)
def validate(c):
 req={"schema_version","case_id","title","units","actors","baseline","candidate","constraints"}
 if req-set(c):raise InputError(f"missing fields: {sorted(req-set(c))}")
 if set(c)-(req|{"notes"}):raise InputError(f"unsupported fields: {sorted(set(c)-(req|{'notes'}))}")
 if c["schema_version"]!="coop.case.v0.1":raise InputError("unsupported schema_version")
 ids=[a.get("id") for a in c["actors"]]
 if not ids or len(ids)!=len(set(ids)):raise InputError("actors must be non-empty with unique ids")
 for a in c["actors"]:
  if set(a)!={"id","role"}:raise InputError("actor fields must be id,role")
 for pn in ("baseline","candidate"):
  p=c[pn]
  if set(p)!={"allocations","outcomes"}:raise InputError(f"{pn}: invalid fields")
  for k,v in p["allocations"].items():
   if v is not None:num(v,f"{pn}.allocations.{k}")
  seen=set()
  for o in p["outcomes"]:
   if set(o)!={"actor","dimension","unit","value"}:raise InputError(f"{pn}: invalid outcome fields")
   if o["actor"] not in ids:raise InputError(f"{pn}: unknown actor")
   key=(o["actor"],o["dimension"],o["unit"])
   if key in seen:raise InputError(f"{pn}: duplicate outcome {key}")
   seen.add(key)
   if o["value"] is not None:num(o["value"],f"{pn}.outcome.value")
 rids=[]
 for r in c["constraints"]:
  for k in ("id","kind","description","operator","limit","hard"):
   if k not in r:raise InputError(f"constraint missing {k}")
  rids.append(r["id"]);num(r["limit"],"constraint.limit")
  if r["operator"] not in ("<=",">="):raise InputError("unsupported operator")
  if r["kind"]=="resource" and "resource" not in r:raise InputError("resource constraint missing resource")
  if r["kind"]=="outcome" and not {"actor","dimension","unit"}<=set(r):raise InputError("outcome constraint incomplete")
  if r["kind"] not in ("resource","outcome"):raise InputError("unsupported constraint kind")
 if len(rids)!=len(set(rids)):raise InputError("duplicate constraint id")
def evaluate(c):
 validate(c)
 def idx(p):return {(o["actor"],o["dimension"],o["unit"]):o["value"] for o in p["outcomes"]}
 bi,ci=idx(c["baseline"]),idx(c["candidate"]);checks=[]
 for r in c["constraints"]:
  if r["kind"]=="resource":v=c["candidate"]["allocations"].get(r["resource"]);src=f"candidate.allocations.{r['resource']}"
  else:v=ci.get((r["actor"],r["dimension"],r["unit"]));src=f"candidate.outcomes:{r['actor']}/{r['dimension']}/{r['unit']}"
  if v is None:st="UNKNOWN";reason="required value is explicitly unknown or absent"
  else:
   ok=v<=r["limit"] if r["operator"]=="<=" else v>=r["limit"]
   st="SATISFIED" if ok else "VIOLATED";reason=f"{v} {r['operator']} {r['limit']} is {str(ok).lower()}"
  checks.append({"constraint_id":r["id"],"hard":bool(r["hard"]),"status":st,"source":src,"reason":reason})
 hard=[x for x in checks if x["hard"]]
 overall="VIOLATED" if any(x["status"]=="VIOLATED" for x in hard) else "UNKNOWN" if any(x["status"]=="UNKNOWN" for x in hard) else "SATISFIED"
 ds=[]
 for k in sorted(set(bi)&set(ci)):
  b,v=bi[k],ci[k];ds.append({"actor":k[0],"dimension":k[1],"unit":k[2],"baseline":b,"candidate":v,"delta":None if b is None or v is None else float(v)-float(b)})
 raw=json.dumps(c,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False).encode()
 return {"software_version":"0.1.0.dev1","case_id":c["case_id"],"input_sha256":hashlib.sha256(raw).hexdigest(),"overall_declared_constraint_status":overall,"checks":checks,"outcome_deltas":ds,"interpretation_boundary":"Deterministic check of declared inputs and constraints only; not a fairness certification, H/T/L/RUN state, or real-world authorization."}
def report(r):
 s=[f"# Result: {r['case_id']}","",f"**Declared-constraint status:** `{r['overall_declared_constraint_status']}`","",f"Input SHA-256: `{r['input_sha256']}`","","## Constraint checks",""]
 s += [f"- `{x['constraint_id']}` — **{x['status']}** — {x['reason']}" for x in r['checks']]
 s += ["","## Comparable outcome deltas",""]+[f"- {d['actor']} / {d['dimension']} ({d['unit']}): {d['baseline']} → {d['candidate']} ; Δ={d['delta']}" for d in r['outcome_deltas']]
 s += ["","## Boundary","",r['interpretation_boundary'],""];return "\n".join(s)
