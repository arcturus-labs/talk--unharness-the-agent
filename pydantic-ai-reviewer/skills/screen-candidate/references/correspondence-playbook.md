# Correspondence Playbook

Use this file when producing `correspondence`.

## Tone requirements

- Professional, concise, helpful.
- Preserve HireFlow style used by existing templates.
- Ask only for missing information required to advance screening.

## Template mapping

Read the relevant template from `references/template/` and use it directly or adapt it as needed.

- `advance.txt`
  - Use when recommending `recommend_advance`. Congratulatory note letting the candidate know they are moving forward.

- `decline.txt`
  - Use when recommending `recommend_decline`. Respectful note informing the candidate they will not be moving forward.

- `follow_up_need_info.txt`
  - Use when recommending `recommend_follow_up` and you need the candidate to provide additional information (role-fit evidence, portfolio links, project examples, etc.). Populate `missing_items` with a list of the specific items needed.

- `follow_up_linkedin.txt`
  - Use when recommending `recommend_follow_up` specifically because the full LinkedIn profile could not be retrieved. Use `missing_context` to add one or two additional items if needed (for example "one or two concrete examples of closely related work").

## Allowed customization

You may adapt wording when needed, but keep the same basic structure and tone.

Good customization patterns:
- Replace `missing_items` / `missing_context` with the specific items relevant to this candidate.
- Remove irrelevant bullets.
- Mention exactly one or two concrete next steps.

Avoid:
- Aggressive/legal tone.
- Long questionnaires when one piece of evidence is enough.
- Requests for information already present in prior updates.

## Examples

### Advance

Read `advance.txt` from the template directory and fill in `{{first_name}}`, `{{job_title}}`, and `{{company_name}}`.

### Decline

Read `decline.txt` from the template directory and fill in `{{first_name}}`, `{{job_title}}`, and `{{company_name}}`.

### Follow-up (need more info)

Read `follow_up_need_info.txt` from the template directory. Populate `missing_items` with specific items such as:
- "a link to your GitHub or portfolio"
- "one or two concrete examples of recent projects relevant to this role"
- "a short description of your current role and responsibilities"

### Follow-up (missing LinkedIn)

Read `follow_up_linkedin.txt` from the template directory. Populate `missing_context` with any additional items needed beyond the LinkedIn URL, for example:
- "one or two concrete examples of closely related work"
- "a link to your portfolio or GitHub"
