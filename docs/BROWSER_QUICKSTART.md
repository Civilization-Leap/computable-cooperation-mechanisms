# Browser Quickstart / 浏览器免安装体验

The fastest path is GitHub Codespaces. No local Python setup is required.

[Open CCM in GitHub Codespaces](https://codespaces.new/Civilization-Leap/computable-cooperation-mechanisms?quickstart=1)

The repository includes a `.devcontainer` definition using Python 3.12. When the Codespace is created, it automatically runs:

```bash
python scripts/reproduce_offline.py
```

That command exercises the public teaching cases and current test suite.

## Reproduce the 0.50 / 0.49 threshold flip

After the Codespace opens, use the repository's threshold-sensitivity instructions:

[Threshold Sensitivity](THRESHOLD_SENSITIVITY.md)

The point of the experiment is not that `0.50 > 0.49` is difficult to compute. The point is that the outcome values stay the same while the declared protection line moves. Computation can enforce the line; it does not establish the legitimacy of the line.

## Evidence boundary

Opening a Codespace or reproducing the tests establishes only that the public implementation is runnable in that environment. It does **not** establish real-world effectiveness, fairness, legitimacy, authorization, or independent domain validation.

## Bring a real problem next

- [BYOP three-minute card — 中文](BYOP_3_MINUTE_CARD_ZH.md)
- [BYOP three-minute card — English](BYOP_3_MINUTE_CARD_EN.md)
- [BYOP Start Here](BYOP_START_HERE.md)
