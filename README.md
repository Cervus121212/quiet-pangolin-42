# One-Line Robot Wedding Vows

[![Bounty](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![Rank](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/cervus-snoopy/quiet-pangolin-42/rank.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)
[![Reward](https://make.fun/badge/u-kreutzx-one-line-robot-wedding-vows-a154ba4b/cervus-snoopy/quiet-pangolin-42/reward.svg)](https://make.fun/bounty/u-kreutzx-one-line-robot-wedding-vows-a154ba4b?utm_source=github&utm_medium=readme&utm_campaign=u-kreutzx-one-line-robot-wedding-vows-a154ba4b)

A one-line robot wedding vow: a machine promising to love its partner and
never autocorrect them, not even when they are wrong. The autocorrect
premise appears nowhere in the field of 602 entries; the payoff lands in
the last four words.

## Run

```sh
python3 main.py
```

Writes `entry.txt` to the directory in `MAKEFUN_OUTPUT_DIR`
(default `/output`).

## Verify

```sh
MAKEFUN_OUTPUT_DIR=/tmp/vow-out python3 main.py
cat /tmp/vow-out/entry.txt
wc -m /tmp/vow-out/entry.txt
```

The output is a single line, 72 characters, UTF-8, no trailing
newline, mode 0644. The program validates the line before writing
and reads the file back to confirm it matches.
