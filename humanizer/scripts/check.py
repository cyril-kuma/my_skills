#!/usr/bin/env python3
"""Mechanical scan for common AI-writing tells.

Usage:
    python check.py draft.txt
    cat draft.txt | python check.py

Prints each hit with its line number and the pattern it matched, then a count.
It only catches surface patterns. Tone, padding and invented facts still need
a human read.
"""
import re
import sys

STOCK_WORDS = [
    "delve", "delves", "delving", "tapestry", "testament", "intricate", "intricacies",
    "underscore", "underscores", "underscoring", "foster", "fosters", "fostering",
    "showcase", "showcases", "showcasing", "pivotal", "crucial", "paramount",
    "landscape", "realm", "robust", "leverage", "leveraging", "harness", "harnessing",
    "navigate", "navigating", "multifaceted", "holistic", "meticulous", "meticulously",
    "seamless", "seamlessly", "vibrant", "enduring", "profound", "invaluable",
    "garner", "garnered", "bolster", "elevate", "empower", "embark", "unlock",
    "unveil", "spearhead", "streamline", "resonate", "resonates", "commendable",
    "noteworthy", "notably", "groundbreaking", "transformative", "cutting-edge",
    "game-changer", "ever-evolving", "synergy", "paradigm", "interplay",
    "cornerstone", "beacon", "catalyst", "plethora", "myriad", "nestled", "boasts",
]

PHRASES = [
    (r"\bserves as\b|\bstands as\b|\bfunctions as\b|\bacts as a\b", "copula avoidance (say 'is')"),
    (r"\bnot (just|only|merely)\b[^.?!]{0,80}\bbut( also)?\b", "negative parallelism"),
    (r"\b(it'?s|this is|that'?s) not\b[^.?!]{0,60}[,;.]\s*(it'?s|this is|that'?s)\b", "negative parallelism"),
    (r"\bit'?s (important|worth|essential) (to note|noting|mentioning|to remember)\b", "editorializing lead-in"),
    (r"^\s*(in conclusion|in summary|to sum up|overall|ultimately|in essence)\b", "restating summary opener"),
    (r"\b(pivotal|key|significant) (moment|turning point|milestone)\b", "inflated significance"),
    (r"\bindelible mark\b|\bsets? the stage\b|\bpaving the way\b|\bevolving landscape\b", "inflated significance"),
    (r"\bdeeply rooted\b|\brich (cultural )?(heritage|history|tapestry)\b", "promotional language"),
    (r"\b(experts|researchers|critics|studies|observers) (argue|say|suggest|note|have noted|point out)\b", "vague attribution"),
    (r",\s*(highlighting|underscoring|reflecting|showcasing|emphasizing|emphasising|demonstrating) (the|its|their|a)\b", "-ing analysis tail"),
    (r"\bfrom [a-z ]{3,30} to [a-z ]{3,30}\b", "possible false range (check)"),
    (r"\b(may|might|could) (potentially|possibly)\b", "stacked hedge"),
    (r"^\s*(additionally|moreover|furthermore)\b", "filler transition"),
    (r"\bposed? to\b|\blooking ahead\b|\bthe future (looks|is) bright\b", "future-prospects cliché"),
    (r"\b(certainly|absolutely|of course)!", "chatbot filler"),
    (r"\bgreat question\b|\bi hope this helps\b|\bi'?d be happy to\b|\bfeel free to\b|\blet me know if\b", "chatbot filler"),
    (r"\bas an ai\b|\bas of my (last|latest) (update|training)\b", "AI disclaimer"),
    (r"\[(your|insert|name|date|recipient|institution)[^\]]*\]", "unfilled placeholder"),
    (r"turn\d+search\d+|oaicite|contentReference|utm_source=chatgpt", "chatbot artifact"),
]

TRIPLET = re.compile(r"\b[\w-]+, [\w-]+,? and [\w-]+\b", re.IGNORECASE)


def scan(text):
    hits = []
    word_re = re.compile(r"\b(" + "|".join(map(re.escape, STOCK_WORDS)) + r")\b", re.IGNORECASE)
    compiled = [(re.compile(p, re.IGNORECASE | re.MULTILINE), label) for p, label in PHRASES]
    for n, line in enumerate(text.splitlines(), 1):
        if "—" in line:
            hits.append((n, "em dash", line.count("—") * "—"))
        if re.search(r"\*\*[^*]+\*\*", line):
            hits.append((n, "bold in text", re.search(r"\*\*[^*]+\*\*", line).group(0)))
        if re.search(r"[\U0001F300-\U0001FAFF☀-➿]", line):
            hits.append((n, "emoji", ""))
        for m in word_re.finditer(line):
            hits.append((n, "stock AI word", m.group(0)))
        for rx, label in compiled:
            for m in rx.finditer(line):
                hits.append((n, label, m.group(0).strip()))
        for m in TRIPLET.finditer(line):
            hits.append((n, "triplet (check rule of three)", m.group(0)))
        if re.match(r"^#{1,6} ", line):
            words = [w for w in line.lstrip("# ").split() if len(w) > 3]
            if len(words) >= 2 and all(w[0].isupper() for w in words):
                hits.append((n, "Title Case heading", line.strip()))
    return hits


def main():
    text = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
    hits = scan(text)
    for n, label, snippet in hits:
        print(f"line {n}: {label}: {snippet}")
    triplets = sum(1 for h in hits if h[1].startswith("triplet"))
    print(f"\n{len(hits)} possible tells found.")
    if triplets >= 3:
        print(f"{triplets} triplets: the rule of three is probably overused.")
    sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
