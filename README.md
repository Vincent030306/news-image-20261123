# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Vincent030306/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Vincent030306/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A program that sums up 23 November 2026's world news in one image: a newspaper front page led by the COP31 climate talks collapsing with no deal, plus five more of the day's top stories — the drone blast on a Russian ship at Libya's Benghazi port, strikes on Kyiv homes, Seoul's minister quitting over AI exam rules, a deadly factory fire in Indonesia, and Mexico capturing a most-wanted cartel boss — rendered from that day's live headlines (BBC World, Al Jazeera, NYT World).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.png` (1024×1024 PNG, under 1 MiB). The program needs no network and uses only the Python standard library: the image ships in this repository and is copied byte for byte, so two runs write the same bytes.

---

<sub>Entered on [make.fun](https://make.fun/?ref=742q33yd&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
