"""Render complete, unchanged report text into local comparison HTML (stdlib only)."""
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/evidence/threshold_sweep"


def main():
    left = (SOURCE / "limit_0_5.report.md").read_text(encoding="utf-8")
    right = (SOURCE / "limit_0_49.report.md").read_text(encoding="utf-8")
    changed = {i for i, (a, b) in enumerate(zip(left.splitlines(), right.splitlines())) if a != b}
    assert changed == {2, 4, 9}
    texts = {
        "en": ("Same outcomes. Different verdict.",
               "One input changes: the declared loss ceiling. Every outcome delta stays fixed.",
               "Complete generated Markdown reports · changed lines highlighted",
               "Three lines change: overall status, input hash, and the third-party check.",
               "Synthetic demonstration · Python 3.12.13 local recheck · evaluator semantics: v0.1.0",
               "A precise check does not establish that its threshold is legitimate."),
        "zh": ("处境未变，判定翻转。",
               "只改一项输入：已声明的损失上限。所有主体差值保持相同。",
               "完整 Markdown 报告原文 · 差异行已高亮",
               "实际变化三行：总体状态、输入哈希、第三方约束检查。",
               "合成演示 · 本地重验 Python 3.12.13 · 求值语义保持 v0.1.0",
               "计算可以准确执行一条保护线，却不能因此证明这条线画得正当。"),
    }
    for lang, (title, subtitle, label, diff_note, provenance, conclusion) in texts.items():
        panels = []
        for index, (limit, source) in enumerate((("0.5", left), ("0.49", right))):
            rows = []
            for i, line in enumerate(source.splitlines()):
                cls = "changed" if i in changed else ""
                rows.append(f'<div class="row {cls}"><span class="number">{i + 1:02}</span><code>{html.escape(line) or " "}</code></div>')
            panels.append(f'<section><div class="panel-title">THIRD-PARTY limit = {limit} TU</div><div class="report">{"".join(rows)}</div></section>')
        page = f'''<!doctype html><html lang="{lang}"><meta charset="utf-8"><title>{html.escape(title)}</title>
<style>
@font-face {{ font-family:NotoSC; src:url(file:///usr/local/share/fonts/ci001/NotoSansSC-regular.ttf); }}
@font-face {{ font-family:NotoSC; font-weight:700; src:url(file:///usr/local/share/fonts/ci001/NotoSansSC-bold.ttf); }}
* {{ box-sizing:border-box; }} body {{ margin:0; background:#f4f2ed; color:#172c35; font-family:NotoSC,Arial,sans-serif; }}
main {{ width:1640px; padding:42px 44px 32px; }} .eyebrow {{ font:700 16px Arial,sans-serif; letter-spacing:2px; color:#526b74; }}
h1 {{ font-size:50px; line-height:1.22; margin:20px 0 12px; letter-spacing:-1px; }} .sub {{ font-size:23px; margin:0 0 22px; }}
.label {{ font-size:17px; color:#526b74; margin:0 0 14px; }} .columns {{ display:grid; grid-template-columns:1fr 1fr; gap:22px; }}
section {{ min-width:0; border:1px solid #c9d2d2; border-radius:10px; overflow:hidden; background:#fff; }}
.panel-title {{ padding:18px 20px; background:#203b45; color:#fff; font:700 21px monospace; }} .report {{ padding:18px 0 20px; }}
.row {{ display:grid; grid-template-columns:42px minmax(0,1fr); min-height:24px; padding:2px 16px 2px 0; }}
.number {{ font:12px/22px monospace; color:#839398; text-align:center; user-select:none; }}
code {{ display:block; font:16px/24px "DejaVu Sans Mono",monospace; white-space:pre-wrap; overflow-wrap:anywhere; }}
.changed {{ background:#fff0c8; }} .note {{ font-size:20px; margin:18px 0 10px; }}
.conclusion {{ font-size:24px; font-weight:700; margin:0 0 22px; }} footer {{ border-top:1px solid #c7d0cf; padding-top:16px; color:#526b74; font-size:15px; line-height:1.7; }}
</style><main><div class="eyebrow">COMPUTABLE COMPETITION–COOPERATION MECHANISMS</div>
<h1>{html.escape(title)}</h1><p class="sub">{html.escape(subtitle)}</p><p class="label">{html.escape(label)}</p>
<div class="columns">{"".join(panels)}</div><p class="note">{html.escape(diff_note)}</p>
<p class="conclusion">{html.escape(conclusion)}</p><footer>{html.escape(provenance)}<br>
github.com/Civilization-Leap/computable-cooperation-mechanisms</footer></main></html>'''
        (ROOT / "assets" / f"threshold-reports-{lang}.html").write_text(page, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
