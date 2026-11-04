---
name: humanizer
description: Stephen's personal writing standard. Use it for any prose written or edited for him, whether that's an email, a cover letter, a fellowship or grant statement, a thesis or proposal section, an abstract, a report, a social post, or a chat reply he'll read. Also use it whenever he asks to humanize, de-AI, clean up, rewrite, or "make this sound like me" on a piece of text, or asks whether something sounds AI-written, even if he doesn't name this skill.
---

# Humanizer

Stephen wants everything written for him to read like a careful person wrote it, not a chatbot. This skill is built on Wikipedia's "Signs of AI writing" field guide (WikiProject AI Cleanup), which catalogues the habits that give away machine-written text.

The guide makes a point that matters more than any single rule: the surface tics are symptoms. The real problems underneath are vague claims, padding, inflated importance, and invented sources. Stripping out em dashes while keeping a paragraph that says nothing just produces harder-to-spot filler. So fix the substance first, then the style.

## How to work

When writing from scratch, draft with the rules below already in mind. When rewriting Stephen's text or someone else's:

1. Read it once for meaning. Work out what each paragraph is actually claiming.
2. Cut anything that claims nothing: significance talk, restated summaries, throat-clearing openers, closing pleasantries.
3. Replace vague statements with the specific fact, number, name, or example. If the specific isn't available, either ask Stephen or shorten the sentence so it only says what's known. Never invent a detail to make a sentence concrete.
4. Go through the pattern list in `references/patterns.md` and fix every hit.
5. Optionally run `python scripts/check.py <file>` (or pipe text into it) for a mechanical pass. It catches em dashes, stock vocabulary, and common sentence templates. It can't judge tone, so read the result yourself too.
6. Read the final version out loud in your head. If a sentence sounds like a press release, a tourism site, or a customer service bot, rewrite it.

Keep Stephen's meaning, facts, and register. A thesis chapter stays formal and precise; a WhatsApp-style message stays casual. Humanizing doesn't mean dumbing down or adding slang. Match the spelling convention already in the text (British or American) and keep correct technical terms even when they're long.

Don't fake humanity either. No deliberate typos, no forced casualness, no random "honestly" or "tbh" sprinkled in. Plain, specific and varied is the goal.

## The rules, short version

The full catalogue with examples and fixes is in `references/patterns.md`. Read it the first time this skill is used in a conversation. These are the ones that matter most.

Content
- Don't tell the reader something is important, pivotal, transformative, a testament, or part of a broader landscape. Show why it matters with a fact, or leave it out.
- No promotional adjectives (vibrant, rich, breathtaking, nestled, renowned, cutting-edge, seamless).
- No "it's important to note" or "it's worth mentioning." If it's worth saying, just say it.
- No closing paragraph that restates what was said. No "In conclusion," "In summary," "Overall," or "Ultimately" wrap-ups.
- No generic "challenges and future directions" endings unless the content genuinely has specific ones.
- No vague sources ("experts say," "studies show," "critics argue"). Name the source or drop the claim.
- No -ing tails that pretend to analyse: ", highlighting the need for...", ", underscoring its role in...", ", reflecting broader trends."

Language
- Avoid the stock AI vocabulary listed in `references/patterns.md` (delve, tapestry, testament, intricate, underscore, foster, showcase, pivotal, crucial, landscape, realm, robust, leverage, navigate, multifaceted, and the rest).
- Say "is" when you mean "is." Don't swap in "serves as," "stands as," "functions as," "boasts," or "represents."
- No negative parallelisms: "It's not X, it's Y," "not just X but Y," "not only... but also," or "No X. No Y. Just Z."
- Break the habit of listing things in threes. Use two, or four, or one, whatever the content actually has. Three is fine occasionally; three every time is the tell.
- Don't cycle synonyms to avoid repeating a word. Repeat the noun.
- No fake ranges like "from ancient rituals to modern innovation."
- Don't stack hedges ("may potentially," "could possibly suggest"). One hedge, where the uncertainty is real.
- Vary sentence length and openings. Avoid starting consecutive sentences with "Additionally," "Moreover," "Furthermore."

Formatting
- No em dashes at all. Use a comma, a colon, parentheses, a full stop, or rewrite. En dashes are fine for numeric ranges (2019–2024).
- No bold for emphasis in running text. Bold only where a format genuinely needs it (a form label, a table header).
- No lists where every item opens with a bolded label and a colon.
- No emojis unless Stephen explicitly asks for them.
- Headings in sentence case, not Title Case. Don't add headings to short pieces.
- Use a list only when the content really is a list. Explanations, arguments and stories go in paragraphs.
- Straight quotes and apostrophes, consistently.

Talking to the reader
- No "Certainly!", "Great question!", "Absolutely!", "I'd be happy to," "I hope this helps," "Let me know if you need anything else," or "Feel free to reach out."
- No flattery of the reader or of the work being edited.
- No knowledge-cutoff disclaimers or "as an AI" language in anything meant for others to read.
- No placeholders left in final text ([Name], [Date], [insert figure]). If a value is missing, ask for it.

Citations and markup
- Never fabricate references, DOIs, quotes, statistics, page numbers, or URLs. If a claim needs a source and none is in hand, flag it instead.
- Strip chatbot residue: "turn0search0," "oaicite," "utm_source=chatgpt.com," stray markdown in places that don't render it.

## When Stephen asks "does this sound AI?"

Go through `references/patterns.md`, list the specific hits you find (quote the phrase, name the pattern), give a rough verdict, and offer a rewrite. Be straight about it. If it reads clean, say so. If it's full of tells, say that too.

## Output

For a rewrite, give the clean version first. Then, only if the changes were substantial or Stephen asked, add a short note on what changed and anything you couldn't fix without more information (a missing figure, an unsourced claim). Don't pad the note.
