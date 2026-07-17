# Internal Notes Checklist Specification

`internal_notes` must be terse, structured, and current.

## Required format

Use checklist lines, then recommendation summary:

```
[✓] Role fit: ...
[✓] Evidence quality: ...
[✓] Job-opening alignment: ...
[✓] LinkedIn profile: ...
[✓] Email risk check: ...
[ ] Missing evidence: ...

Recommendation: recommend_follow_up
Rationale: <1-4 short lines: what evidence was found/missing, where (URLs), and why that drives this recommendation>
```

## Checklist symbols

- `[✓]` confirmed / sufficient
- `[ ]` pending / not yet verified
- `[✗]` failed / contradictory evidence

## Content rules

- Keep it short and scannable.
- Capture only decision-relevant information.
- If information becomes irrelevant, remove it in later updates.
- Mention when following prior human judgment.
- Include unresolved items explicitly so reviewers know next step.
- If website evidence was used (including LinkedIn), inline the exact URLs in the relevant checklist lines and in `Rationale`.
- Each checklist item should be a little descriptive: state what you checked, what you found (or did not find), where you checked (URL), and why it matters.
- The `LinkedIn profile` line must explicitly say whether the full LinkedIn profile was retrieved. If it was not, that should normally block advancement.
- `Rationale` should explain the causal chain (evidence -> interpretation -> recommendation), not just the final conclusion.
- Do not include URLs that were reviewed but not decision-relevant.
- If you fast-fail on an obvious disqualifier, explicitly list checks not performed as "Not checked (not necessary after disqualifier)".

## Example: advance

```
[✓] Role fit: Prior engineering and agent-work evidence on https://github.com/janedoe and the retrieved LinkedIn profile at https://www.linkedin.com/in/janedoe aligns with the posted senior backend/AI role.
[✓] Evidence quality: Public evidence is specific and recent enough to support the fit judgment.
[✓] Job-opening alignment: Experience clearly matches the job description's requirements for production systems, collaboration, and technical depth.
[✓] LinkedIn profile: Full LinkedIn profile was retrieved and reviewed at https://www.linkedin.com/in/janedoe.
[✓] Email risk check: Non-personal named mailbox; low importance because role-fit evidence is already strong.
[✓] Missing evidence: None material.

Recommendation: recommend_advance
Rationale: The LinkedIn and GitHub evidence shows directly relevant experience, and that evidence maps cleanly onto the job opening's requirements.
Rationale: There is enough concrete public evidence to make an advance decision without extra follow-up.
```

## Example: decline (clear mismatch)

```
[✗] Role fit: Public profile at https://example.com/profile shows mostly operational/admin work with no meaningful evidence of the technical responsibilities required by this opening.
[✓] Evidence quality: Evidence is clear enough to make a negative fit judgment.
[✗] Job-opening alignment: The candidate background does not match the posted job description's core requirements.
[ ] LinkedIn profile: Not checked (not necessary after clear disqualifier).
[ ] Email risk check: Not checked (not necessary after disqualifier).
[ ] Missing evidence: Not material after clear mismatch.

Recommendation: recommend_decline
Rationale: The available evidence shows a real professional background, but not one that matches the opening.
Rationale: Because the mismatch is role-based rather than identity-based, additional follow-up is unlikely to change the decision.
```

## Example: follow-up

```
[✓] Role fit: Candidate appears directionally relevant based on available public evidence, but the evidence is still too high-level.
[ ] Evidence quality: Public evidence is plausible but not specific enough to confirm the required depth.
[ ] Job-opening alignment: The job description asks for hands-on platform experience, but the visible evidence does not yet show concrete examples of that work.
[ ] LinkedIn profile: Full LinkedIn profile could not be retrieved; search snippets or a bare URL are not enough for advancement.
[✗] Email risk check: Personal mailbox increases the need for stronger corroborating evidence.
[✓] Missing evidence: Ask for the correct LinkedIn profile URL and one or two concrete examples of closely related work or public artifacts.

Recommendation: recommend_follow_up
Rationale: The profile suggests a possible match, but the evidence is not detailed enough to support an advance decision.
Rationale: A narrow follow-up could resolve the uncertainty without forcing a premature decline.
```
