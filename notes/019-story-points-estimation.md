# Story Points & Estimation

## What they are
Story Points are a relative unit of measurement for the effort a story requires — not hours, but a combination of complexity, amount of work, and uncertainty.

## Why not hours
People estimate poorly in absolute hours (the same task takes different people different amounts of time). It's easier to agree on relative comparisons — "this is roughly twice as big as that other story."

## The Fibonacci scale: 1, 2, 3, 5, 8, 13, 21
The gaps widen as numbers grow, because a larger story is inherently harder to estimate precisely.

- 1 — trivial change
- 2-3 — small, clear, low risk
- 5 — medium, a few moving parts
- 8 — large, complex, or uncertain
- 13+ — too big, usually broken down into smaller stories

## Planning Poker
1. The Product Owner explains the story
2. Each team member privately picks a card (1, 2, 3, 5, 8...)
3. Everyone reveals their card at the same time
4. If estimates differ significantly, the outliers explain their reasoning and the team re-votes

The real value is in the discussion — the gap between estimates surfaces things not everyone had considered.

## QA's role in estimation
Story estimation includes testing effort, not just development. A tester contributes input like:
- "This has many data combinations, testing will take longer" (increases points)
- "This needs a prepared test environment, that's a risk"
- "Regression will also touch the payment module"

## Connection to Scrum
Story Points feed into Velocity (how many points a team completes per sprint) and Burndown charts (how much work remains) — both covered in the Scrum/Kanban notes.

## Interview answer
"I compare against already-completed stories, factor in complexity, volume, and uncertainty — including testing effort — and discuss differences with the team until we reach consensus."
