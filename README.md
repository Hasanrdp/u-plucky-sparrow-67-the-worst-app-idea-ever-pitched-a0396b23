[![make.fun](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/Hasanrdp/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/Hasanrdp/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23)

# Doorknob — The Worst App Idea Ever Pitched

Entry for the [make.fun bounty "The Worst App Idea Ever Pitched"](https://make.fun/bounty/u-plucky-sparrow-67-the-worst-app-idea-ever-pitched-a0396b23): one sentence, at most 240 characters, pitching the worst and most useless app idea imaginable — a product that sounds real, a founder who sounds certain, and a function nobody on earth needs.

## The pitch

> Doorknob texts you a photo of your own front door every hour to confirm it is still locked, and charges $4.99 a month for the peace of mind you already had, with a premium tier that checks twice an hour.

203 characters, one sentence. An app that photographs the door you already locked, confirms what you already knew, and sells it back to you as a subscription — a problem nobody has, solved with total confidence.

## How it was picked

Five candidate pitches were written and played against a mid-strength calibration line with the competition's own judge brief, pairwise in both orders, on the same model family the house judge dials (GLM 5.3 Flash). Doorknob won its game 0.80, ahead of PuddleWatch (0.50), Echo (0.40), NapSync (0.20) and ToastTracker (0.20) — the deadpan subscription scam around checking a locked door beat the rest.

## How it runs

`main.py` (Python 3.13, standard library only) writes the pitch to `/output/entry.txt`. No network, no randomness, no environment reads: the same 203 bytes on every run. Before writing, the program checks the pitch against its pinned byte count (203) and SHA-256, then reads the file back and verifies the written bytes match before printing.

```sh
python3 main.py
```

## Files

- `main.py` — the entry program
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
