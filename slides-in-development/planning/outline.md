# Brainstorming

Outline

Intro stuff
- Right now we're skating to where the puck is not where it's going. We're using AI to build traditional software. But in 5 years, AI will be built INTO our existing products (name several), and many people aren't prepared. The ability to build AI product will be the killer skillset in 5 years. But if you have that skillset now, you have a major leg-up on competition.
- Goal for today: Give you that leg up
  - Want to show you how we're thinking about AI all wrong (We're thinking about agents in way too constrained way (code and terminals)) – Everything will soon be agents
  - Want to show you how easy it is to make an agent (we'll make 6 today)
  - Want to open your eyes to how your new ability to build agents is going to work its way into products

Demos - Making agents isn't all that complicated
- list out all the complex capabilities of claude code and exclaim "this is so complex"

1. just a model - text in, text out; we don't talk about this much any more, but you need to see the prompt going in! prompt engineering still has a place
2. add tools and now it can get some work done
3. that's clumsy, all this has been standardized - see how simple this is with pydantic ai
4. with the right tools (read, write, shell) we actually have a full-fledged agent
  a. Let's treat it like a coding agent "In /Users/johnberryman/projects/github/arcturus-labs/talk--unharness-the-agent/scratch_space, create a cli tool in rust that generates the first N primes (N provided as argument), make standard rust package, build it, tell me how to run it as a one-liner (use absolute paths)"
  b. review code and run it
5. skills - if you can read files, that's all you need need to read skill files
  a. also note the nice packaging of all this stuff - "capabilities" tools, and instructions, and hooks
  b. "Research this: Why did the Roman Republic turn into the Roman Empire?"
  c. show skill file
  d. show results
  e. MAJOR POINT - by providing the right instructions as skills and the right set of tools (web search in this case) you can make an agent to anything
    - Where's the program to be a researcher? It's in the skill file.
    - What's the language? It's English.
    - What is the runtime? It's not python, it's the agent that we just assembled
    - YOU CAN PROGRAM IN ENGLISH AND MAKE THE AGENT ACCOMPLISH ANYTHING - SUBJECT MATTER EXPERTS CAN READ THE CODE, DEBUG, PROGRAM!
    - This opens up so many possibities
  f. BUT - ask it what it just did, and it has no memory 
6. missing user input, memory, and compaction
  a. introducing sessions and hooks
  b. here again - really simple, we just add another loop
7. (maybe back in slides) but ALL of this is being standardized at this point
  a. I've fallen in love w/ Pi (show site and show extension example)
    - Opensource
    - The agent knows it's own documentation and codebase
    - The agent will help you write extensions
  b. Flue (show site and show extension example) - list lego blocks

Mind expansion
- Hopefully I've dispelled the magic. Of making agents. But I want to expand your mental horizons about what agents can do and where they can live.
- First is when agents live inside the application
  - Agents don't have to work on code, they can do anything when given access to the proper tools, instructions, and data. – They can review job applications.
  - Agents don't have to live in a terminal, they can be embedded inside other applications.
  - Dig into ai-reviewer example (/Users/johnberryman/projects/github/arcturus-labs/talk--unharness-the-agent/pydantic-ai-reviewer/src/pydantic_ai_reviewer/ai_reviewer.py)
    - Just the same old PydanticAI but with a skill (how to review applications) and a tool (linkedin lookups) and a structured output
  - English is the language of AI - skills are the new software - SMEs can read and debug stuff on their own. No need to translate from SME to Product Manager to Engineer to QA and back again
  - QR code to last talk which covered this in detail
- Next is agents will ALSO live outside of all applications ("unharness the agents")
  - BYOA - Rook advertisement
  - BYOA IRL - Rook advertisement

End lesson review
- Agents / Agent Harnesses are not magic at all. They are simple to understand.
  - Today building them is like assembling lego blocks.
  - English is the programming language of AI software. This means that the distinction between users and programmers gets blurry - and that's great. No more need for translating.
- Agents can do anything. All they need are the right tools and (English) programming. - So think past software development!
- Agents can live anywhere – burried inside a traditional application or interacting with a traditional application from the outside.
- Hopefully you have the start of a skill that will make you in demand in the coming years. But I have homework for you: YOU MUST GO MAKE YOUR OWN – Do it today. It will take 1 hour, and it will make all of this stick.


### Pi extensions
• tools
• skills
• instructions
• event hooks
• context files
• compaction
• sessions
• models/providers
• commands

### Flue building blocks
• Agents — stateful, continuing workers
• Workflows — finite, structured runs
• Models — the LLM/provider choice
• Instructions — core behavior/prompt
• Tools — typed actions/functions
• Skills — reusable packaged guidance
• Actions — reusable bounded operations
• Sandboxes — execution environments
• Sessions — persistent conversation/working context
• Agent IDs / instances — scoped long-lived agent identities
• Channels — Slack, GitHub, Linear, Discord, etc.
• Subagents — delegated specialist roles
• Durable execution — resume after crashes/restarts
• Database / persistence — stored conversations, runs, state
• Runs — workflow execution records
• Routing / HTTP exposure — make agents/workflows callable
• SDK / client — consume agents from apps
• Observability — tracing/telemetry
• Attachments / image inputs — richer inputs to agents

# Outline

## Goals
- Give the audience a useful mental model for the future of AI software.
- Show that agents are much simpler than people assume.
- Show that agents are not confined to coding work or terminal UX.
- Give the audience a practical starting point so they can begin building these systems now.

## Audience
- Primarily software engineers.
- Also relevant to product managers and other technical builders thinking about AI-native products.

## Structure ideas
- Keep the intro light and move into demos quickly.
- Use the demo ladder to demystify agents step by step.
- Treat Pi and Flue as part of the ladder, almost like a final standardization step.
- Use the AI reviewer example as the first bridge into the bigger-picture section.
- End by expanding from software and websites into environments in general.

## Current outline
- Intro
  - AI software is where things are going, not just AI helping build traditional software.
  - The opportunity is to develop the skill of building AI products before that becomes table stakes.
  - We currently think about agents too narrowly, code work, terminal UX, and too much complexity.
  - Today we are going to prove three things quickly:
    - agents are not that complicated
    - agents can do more than coding work
    - agents can live in more places than a terminal

- Demo ladder
  - Surface the intimidating picture first, what a modern coding agent appears to do.
  - Build upward from the smallest useful version:
    - just a model (`1-just-a-model.py`)
    - add tools (`2-tool-loop.py`)
    - standardize the loop with PydanticAI (`3-pydantic-ai.py`)
    - add read, write, and shell so it becomes a real coding agent (`4-pydantic-ai-read-write-edit.py`)
    - add skills, web search, and the idea that English is starting to act like the programming language (`5-pydantic-ai-search-skills.py`)
    - add sessions, hooks, and compaction (`6-pydantic-ai-assistant-w-compaction.py`)
  - Close the ladder with the ecosystem-standardization moment:
    - Pi as extension-oriented Lego blocks
    - Flue as higher-level agent/application Lego blocks
    - Soon, rather than depending upon frontier agent companies to build harnesses, you'll make your own a la carte

- Bigger picture
  - Agents inside products
    - revisit the pattern with slightly more structure in the AI reviewer example (`pydantic-ai-reviewer/src/pydantic_ai_reviewer/ai_reviewer.py`) # we need to remember to move this into the same dir as the other examples after the slides are finished
    - emphasize that agents can live embedded inside applications (not terminal!) and agents can do other things besides code
    - pay off the point that English is the language of AI software, and skills are the new programs
    - show how the line between user, SME, and developer starts to blur
  - Agents outside products
    - BYOA: your personal agent becomes the dominant interface for interacting with traditional applications and websites
    - BYOA IRL: the same pattern extends into physical environments, not just software surfaces

- Wrap-up
  - Agents and agent harnesses are not magic.
  - Building them increasingly looks like assembling standardized Lego blocks.
  - Agents can do anything when given the right instructions, tools, and data.
  - Agents can live inside products, outside products, and eventually across physical environments.
  - The audience should go build one immediately so the mental model becomes real.


























# Rough Slide Level Outline

```yaml
- slide: 1
  title: "Build Your Own Agent – Escaping the Harness"
  note: "title slide, model after the title slide in english-is-ai-software"

- slide: 2
  title: "The constrained harness view"
  spoken_content:
    - "Right now, we are mostly using AI to help build traditional software, and everyone is familiar with that frame."
    - "But this is a very constrained way of thinking about agents and the agent harness."
    - "We have come to think of agents as only working on code, or at least only on software development tasks."
    - "We think they only live in the terminal."
    - "And because the harness looks so complex, we assume building these things must be too complicated for normal people."

- slide: 3
  title: "What we will prove today"
  spoken_content:
    - "Agents do not just live in terminals, they can live anywhere."
    - "They can be embedded in products, or they can be the product themselves, interacting with traditional software from the outside."
    - "If you understand that now and start working with your own agents in new environments, doing interesting tasks outside of software, you become very marketable."
    - "There is still time to be an early adopter of where this is going."

- slide: 4
  title: "Agents are simpler than you think"
  spoken_content:
    - "Let’s strip the harness down to its core."

- slide: 5
  title: "This all looks insanely complex"
  spoken_content:
    - "Enumerate the visible complexity of Claude Code."
    - "Slash commands, tools, context handling, compaction, UI affordances, and all the other impressive surface area."
    - "Set up the key question: what is the minimal core underneath all of this?"

- slide: 6
  title: "Demo 1 - just a model"
  spoken_content:
    - "Start with the smallest possible useful thing, text in and text out (`1-just-a-model.py`)."
    - "One-liner: `cd /Users/johnberryman/projects/github/arcturus-labs/talk--unharness-the-agent/agents-from-simple-to-complex && uv run src/1-just-a-model.py`"
    - "Prompt: tell me a joke."
    - "Point: we do not talk about this much anymore, but prompt engineering still matters, and the prompt is still part of the program."

- slide: 7
  title: "Demo 2 - add one tool"
  spoken_content:
    - "Now add a single tool and suddenly the model can get real work done (`2-tool-loop.py`)."
    - "One-liner: `cd /Users/johnberryman/projects/github/arcturus-labs/talk--unharness-the-agent/agents-from-simple-to-complex && uv run src/2-tool-loop.py`"
    - "Prompt: what is Hacker News saying about John Berryman?"
    - "Point: given a tool, the model can now see outside itself and interact with the world; implementation is easy - just a loop - we all know loops"

- slide: 8
  title: "Demo 3 - standardize the loop"
  spoken_content:
    - "Now show the same basic idea in PydanticAI (`3-pydantic-ai.py`)."
    - "One-liner: `cd /Users/johnberryman/projects/github/arcturus-labs/talk--unharness-the-agent/agents-from-simple-to-complex && uv run src/3-pydantic-ai.py`"
    - "Prompt: what is Hacker News saying about John Berryman?"
    - "Point: the underlying pattern is the same, but the ergonomics get much better as things standardize."

- slide: 9
  title: "Demo 4 - real coding agent"
  spoken_content:
    - "With the right tools, read, write, and shell, we actually have a full-fledged agent (`4-pydantic-ai-read-write-edit.py`)."
    - "One-liner: `cd /Users/johnberryman/projects/github/arcturus-labs/talk--unharness-the-agent/agents-from-simple-to-complex && uv run src/4-pydantic-ai-read-write-edit.py`"
    - "Prompt: In /Users/johnberryman/projects/github/arcturus-labs/talk--unharness-the-agent/scratch_space, create a cli tool in rust that generates the first N primes (N provided as argument), make standard rust package, build it, tell me how to run it as a one-liner (use absolute paths)."
    - "Then review the code and run it."
    - "Point: by giving a model the right tools, it can become quite general."

- slide: 10
  title: "Demo 5 - agent skills"
  spoken_content:
    - "If an agent can read files, that is enough to read skill files (`5-pydantic-ai-search-skills.py`)."
    - "One-liner: `cd /Users/johnberryman/projects/github/arcturus-labs/talk--unharness-the-agent/agents-from-simple-to-complex && uv run src/5-pydantic-ai-search-skills.py`"
    - "Prompt: Research this: Why did the Roman Republic turn into the Roman Empire?"
    - "Show the skill file, show the results, and make the point that with the right instructions, tools, and data, an agent can do almost anything."
    - "Hint here that English is starting to act like the programming language."

- slide: 11
  title: "Demo 6 - sessions, hooks, and compaction"
  spoken_content:
    - "Now add user input, sessions, hooks, and compaction (`6-pydantic-ai-assistant-w-compaction.py`)."
    - "One-liner: `cd /Users/johnberryman/projects/github/arcturus-labs/talk--unharness-the-agent/agents-from-simple-to-complex && uv run src/6-pydantic-ai-assistant-w-compaction.py`"
    - "Prompt flow: ask it for a joke, ask it to explain the joke, then keep saying 'why' until compaction happens."
    - "Point: here again, the idea is simple, we just add another loop for the user input and add hooks to incorporate deterministic controls."

- slide: 12
  title: "The ecosystem is standardizing"
  spoken_content:
    - "Now step back and show that all of this is being standardized."
    - "Use one slide for both Pi and Flue."
    - "The initial on-screen state is already two code examples, Pi on the left with a tiny extension snippet as eye candy, and Flue on the right with a tiny defineAgent example as eye candy."
    - "Then reveal the Pi building blocks list on top of the Pi side: tools, skills, instructions, event hooks, context files, compaction, sessions, models/providers, commands."
    - "Then reveal the Flue building blocks list on top of the Flue side: agents, workflows, models, instructions, tools, skills, actions, sandboxes, sessions, agent IDs / instances, channels, subagents, durable execution, database / persistence, runs, routing / HTTP exposure, SDK / client, observability, attachments / image inputs."
    - "The point is that these are converging into understandable Lego blocks."
    - "Soon, rather than depending on frontier agent companies to build harnesses, you will make your own a la carte."
  on_screen_setup:
    left_side:
      label: "Pi"
      code_example: "minimal extension snippet as eye candy"
    right_side:
      label: "Flue"
      code_example: |
        // Give agents the autonomy to solve complex tasks:
        const instructions = `
        Triage a bug report end-to-end: reproduce the bug,
        diagnose the root cause, verify whether the behavior is
        intentional, and attempt a fix.`;

        // Compose the context your agent needs to do real work,
        // complete with virtual, local, or remote container sandbox.
        export default defineAgent(() => ({
          model:   'anthropic/claude-sonnet-4-6',
          tools:   [replyToIssue],
          skills:  [triage, verify],
          sandbox: local(),
          instructions,
        }));
    reveal_sequence:
      - "Pi building blocks list appears"
      - "Flue building blocks list appears"

- slide: 13
  title: "Now let’s unharness the agent"
  spoken_content:
    - "Now let’s expand where agents can live and what they can do."

- slide: 14
  title: "Agents can live inside products - AI reviewer"
  spoken_content:
    - "Revisit the same pattern with slightly more structure in the AI reviewer example (`pydantic-ai-reviewer/src/pydantic_ai_reviewer/ai_reviewer.py`)."
    - "Change directory first: `cd /Users/johnberryman/projects/github/arcturus-labs/talk--unharness-the-agent/pydantic-ai-reviewer && uv run python -m pydantic_ai_reviewer`"
    - "Point out that this is still the same basic recipe, model, skills, tools, instructions – we've added structured output, and a review_job_application function that allows normal code to interface with the agent."
    - "Key point: it is not doing software development, it is executing a job application review workflow, and it is embedded inside an app."
    - "Review `/Users/johnberryman/projects/github/arcturus-labs/talk--unharness-the-agent/pydantic-ai-reviewer/skills/screen-candidate/SKILL.md`."
    - "Skills are the new programs, and the behavior of AI software is increasingly written in natural language."
    - "Huge impact: subject matter experts and users can read it, inspect it, and even debug it themselves. The line between user, SME, and developer starts to blur."
    - "Point to the prior talk with a QR code."

- slide: 15
  title: "Agents can live outside products too – BYOA"
  spoken_content:
    - "Now move from embedded agents to external agents."
    - "The next step is not just an agent inside the app, but your own agent interacting with applications and websites from the outside."
    - "Introducing the notion of 'Bring your own agent'."
    - "Consider GitHub's built-in agent, which I helped work on while I was at GitHub. It is a nice product, but it suffers from what any built-in website agent does: it may have useful tools and information, but it does not have your information, the context of what you are working on right now."
    - "To make it most useful, you would need to copy-paste content from your machine, which is too much work and a little dangerous."
    - "Your own agent already knows your machine, your files, your history, and your current work."
    - "The exciting future is your personal agent gaining the tools, instructions, and skills needed for each environment you enter, like GitHub."
    - "Examples on GitHub: create an issue and watch it being created, modify text and tags together, or go to a project board and move tasks around together."
    - "Imagine how much more engaging and complete the experience would be in any application or website."

- slide: 16
  title: "BYOA IRL"
  spoken_content:
    - "Why stop at websites and software applications?"
    - "The same idea extends into physical environments."
    - "If your phone-hosted agent understands where you are, what environment you entered, and what tools/data are relevant there, it can help you act in the real world."
    - "Use the grocery store example: I go to a grocery store with MY agent, and so it has my shopping list. But when I show up to the store, my agent gains access to live inventory, discounts, the store map, and understands how to do route planning through the store and get me out of there efficiently."
    - "All of this is still the same core pattern we demoed in the beginning, just in a richer environment."

- slide: 17
  title: "What should you remember?"
  spoken_content:
    - "Agents and agent harnesses are not magic."
    - "Today, building them increasingly looks like assembling standardized Lego blocks."
    - "Agents can do any task with the right instructions, tools, and data. - and even programming them is easier - they speak English!"
    - "Agents can live inside products, outside products, and eventually across physical environments."

- slide: 18
  title: "Homework"
  spoken_content:
    - "Go make your own today."
    - "Do not wait."
    - "It will probably take about an hour to make something that changes how you think forever."
    - "That is how this mental model becomes real and sticks."
```











# Refined Slide Level Outline

```yaml
- slide: 1
  title: "Build Your Own Agent – Escaping the Harness"
  layout: "title slide modeled closely after english-is-ai-software, with header row, speaker card, logo, and footer note"
  visible_content:
    event_line: "Greg Ceccarelli · Lightning Talk · July 20, 2026"
    frame_label: "Opening frame"
    kicker: "Opening thesis"
    hero_title: "Build Your <b>Own Agent</b>"
    hero_subtitle: "Escaping the <b>Harness</b>"
    supporting_line: "Agents are <b>simpler</b> than they look, and they can live <b>almost anywhere</b>."
    card_brand: "Greg Ceccarelli"
    card_chip: "Lightning Talk"
    speaker_name: "John Berryman"
    speaker_org: "Arcturus Labs"
    org_line: "AI product consulting · applied agent systems"
    footnote: "We are going to strip the harness down to its core, then build it back up."
  speaker_notes:
    - "Open with energy, frame the talk as practical and forward-looking."
    - "Say we are going to demystify agents by building them and then expand the frame."

- slide: 2
  title: "The constrained harness view"
  layout: "editorial statement slide with one dominant claim, three constrained assumptions, top header row, and footer note"
  visible_content:
    topbar_left: "The old frame"
    topbar_center: "The harness trap"
    title: "We have mistaken the <b>harness</b> for the <b>agent</b>."
    supporting_bullets:
      - "Agents are too <b>complex</b> for normal builders"
      - "Agents only work on <b>code</b>"
      - "Agents only live in <b>terminals</b>"
    footnote: "The visible harness has distorted the mental model."
  speaker_notes:
    - "Start from the familiar frame, AI helping us build traditional software."
    - "Explain that the visible harness complexity has distorted how we think about the core idea."

- slide: 3
  title: "What we will prove today"
  layout: "three-part proof slide with top header row and footer note"
  visible_content:
    topbar_left: "What you get"
    topbar_center: "Three proofs"
    title: "What we will <b>prove</b> today"
    proof_points:
      - "Agents are <b>simpler</b> than you think"
      - "Agents can do <b>more</b> than coding work"
      - "Agents can live <b>far beyond</b> the terminal"
    footnote: "Understand this early, and you gain a real edge."
  speaker_notes:
    - "Connect the proof points back to the opportunity."
    - "Make the career / marketability point briefly, then move on."

- slide: 4
  title: "Agents are WAY simpler than you think"
  layout: "terse transition slide with top header row and footer note"
  visible_content:
    topbar_left: "The reveal"
    topbar_center: "Demo ladder"
    title: "Let’s strip the harness down to its core, and then build it back up."
    footnote: "The next slides are the core, with the harness stripped away."
  speaker_notes:
    - "Very short transition."
    - "This is the doorway into the demo ladder."

- slide: 5
  title: "This all looks insanely complex"
  layout: "two-column reveal, command/capability density on one side and complexity labels on the other, plus top header row and footer note"
  visible_content:
    topbar_left: "What people see"
    topbar_center: "The intimidating surface"
    title: "This all looks <b>insanely complex</b>"
    left_panel:
      title: "The visible product surface"
      items:
        - "Slash commands"
        - "Tool calling"
        - "Context files"
        - "Compaction"
        - "Sessions"
        - "Editor / UI affordances"
        - "MCP / extensions / integrations"
    right_panel:
      title: "What this makes you assume"
      items:
        - "This must be <b>wildly complicated</b>"
        - "This must require <b>frontier-lab magic</b>"
        - "I probably <b>cannot build</b> one myself"
      bottom_line: "So what is the minimal core underneath all of this?"
    footnote: "We are about to pull the harness apart and look at the core."
  speaker_notes:
    - "You can use a real screenshot, a stylized list, or both when we build the actual slide."
    - "The point is to surface the intimidation before we dismantle it."

- slide: 6
  title: "Demo 1 - just a prompt and a model"
  layout: "two-column demo slide, polished bullets on the left and practical reference details on the right"
  visible_content:
    left_side:
      bullets:
        - "Smallest possible useful agent"
        - "Just a prompt plus a model call"
        - "The prompt is still part of the program"
    right_side:
      artifacts:
        - "[The smallest possible agent script](https://github.com/arcturus-labs/talk--unharness-the-agent/blob/main/agents-from-simple-to-complex/src/1-just-a-model.py)"
      command: "cd /Users/johnberryman/projects/github/arcturus-labs/talk--unharness-the-agent/agents-from-simple-to-complex && uv run src/1-just-a-model.py"
      prompt: "tell me a joke"
  speaker_notes:
    - "These code-heavy demo slides are mostly practical references, not beauty slides."
    - "During the talk, I will copy commands from the slide into the terminal and run them."
    - "Future readers should be able to click through to the code and reproduce the demo."

- slide: 7
  title: "Demo 2 - introduce the tool loop"
  layout: "two-column demo slide, polished bullets on the left and practical reference details on the right"
  visible_content:
    left_side:
      bullets:
        - "A tool lets the model see outside itself"
        - "The implementation is still just a loop"
        - "No magic, just one new capability"
    right_side:
      artifacts:
        - "[A manual tool loop example](https://github.com/arcturus-labs/talk--unharness-the-agent/blob/main/agents-from-simple-to-complex/src/2-tool-loop.py)"
      command: "cd /Users/johnberryman/projects/github/arcturus-labs/talk--unharness-the-agent/agents-from-simple-to-complex && uv run src/2-tool-loop.py"
      prompt: "what is Hacker News saying about John Berryman?"
  speaker_notes:
    - "These code-heavy demo slides are mostly practical references, not beauty slides."
    - "During the talk, I will copy commands from the slide into the terminal and run them."
    - "Future readers should be able to click through to the code and reproduce the demo."

- slide: 8
  title: "Demo 3 - standardizing tool usage"
  layout: "two-column demo slide, polished bullets on the left and practical reference details on the right"
  visible_content:
    left_side:
      bullets:
        - "Same tool calling pattern"
        - "Better developer ergonomics"
    right_side:
      artifacts:
        - "[A PydanticAI version of the same pattern](https://github.com/arcturus-labs/talk--unharness-the-agent/blob/main/agents-from-simple-to-complex/src/3-pydantic-ai.py)"
      command: "cd /Users/johnberryman/projects/github/arcturus-labs/talk--unharness-the-agent/agents-from-simple-to-complex && uv run src/3-pydantic-ai.py"
      prompt: "what is Hacker News saying about John Berryman?"
  speaker_notes:
    - "These code-heavy demo slides are mostly practical references, not beauty slides."
    - "During the talk, I will copy commands from the slide into the terminal and run them."
    - "Future readers should be able to click through to the code and reproduce the demo."

- slide: 9
  title: "Demo 4 - add 3 tools for a coding agent"
  layout: "two-column demo slide, polished bullets on the left and practical reference details on the right"
  visible_content:
    left_side:
      bullets:
        - "Read, write, and shell are enough to feel like a coding agent"
        - "The model can now create, inspect, and run code"
        - "With the right tools, the agent becomes quite general"
    right_side:
      artifacts:
        - "[A read/write/shell agent](https://github.com/arcturus-labs/talk--unharness-the-agent/blob/main/agents-from-simple-to-complex/src/4-pydantic-ai-read-write-edit.py)"
      command: "cd /Users/johnberryman/projects/github/arcturus-labs/talk--unharness-the-agent/agents-from-simple-to-complex && uv run src/4-pydantic-ai-read-write-edit.py"
      prompt: "In /Users/johnberryman/projects/github/arcturus-labs/talk--unharness-the-agent/scratch_space, create a cli tool in rust that generates the first N primes (N provided as argument), make standard rust package, build it, tell me how to run it as a one-liner (use absolute paths)."
      follow_up: "Review the code and run it."
  speaker_notes:
    - "These code-heavy demo slides are mostly practical references, not beauty slides."
    - "During the talk, I will copy commands from the slide into the terminal and run them."
    - "Future readers should be able to click through to the code and reproduce the demo."
    - "This is the first moment that really feels like a coding agent."

- slide: 10
  title: "Demo 5 - introducing agent skills"
  layout: "two-column demo slide, polished bullets on the left and practical reference details on the right"
  visible_content:
    left_side:
      bullets:
        - "If an agent can `read`, you can create instruction files"
        - "English starts acting like the programming language"
        - "Agent skills are the programs"
        - "Agents are the runtime"
    right_side:
      artifacts:
        - "[A skills-enabled research agent](https://github.com/arcturus-labs/talk--unharness-the-agent/blob/main/agents-from-simple-to-complex/src/5-pydantic-ai-search-skills.py)"
        - "[The screen-candidate skill file](https://github.com/arcturus-labs/talk--unharness-the-agent/blob/main/pydantic-ai-reviewer/skills/screen-candidate/SKILL.md)"
      command: "cd /Users/johnberryman/projects/github/arcturus-labs/talk--unharness-the-agent/agents-from-simple-to-complex && uv run src/5-pydantic-ai-search-skills.py"
      prompt: "Research this: Why did the Roman Republic turn into the Roman Empire?"
  speaker_notes:
    - "These code-heavy demo slides are mostly practical references, not beauty slides."
    - "During the talk, I will copy commands from the slide into the terminal and run them."
    - "Future readers should be able to click through to the code and reproduce the demo."
    - "Show the skill."

- slide: 11
  title: "Demo 6 - sessions, hooks, and compaction"
  layout: "two-column demo slide, polished bullets on the left and practical reference details on the right"
  visible_content:
    left_side:
      bullets:
        - "User input is just another loop"
        - "Hooks are functions at specific lifecycle points"
    right_side:
      artifacts:
        - "[An assistant with history compaction](https://github.com/arcturus-labs/talk--unharness-the-agent/blob/main/agents-from-simple-to-complex/src/6-pydantic-ai-assistant-w-compaction.py)"
      command: "cd /Users/johnberryman/projects/github/arcturus-labs/talk--unharness-the-agent/agents-from-simple-to-complex && uv run src/6-pydantic-ai-assistant-w-compaction.py"
      prompt_flow:
        - "Tell me a joke"
        - "Explain the joke"
        - "Why?"
        - "Why?"
        - "Why? (keep going until compaction happens)"
  speaker_notes:
    - "These code-heavy demo slides are mostly practical references, not beauty slides."
    - "During the talk, I will copy commands from the slide into the terminal and run them."
    - "Future readers should be able to click through to the code and reproduce the demo."
    - "These are not hard ideas."

- slide: 12
  title: "The ecosystem is standardizing"
  layout: "two-column slide, Pi on the left and Flue on the right, with staged reveals"
  visible_content:
    left_side:
      label: "Pi"
      code_example: "minimal extension snippet as eye candy"
      revealed_list:
        - "tools"
        - "skills"
        - "instructions"
        - "event hooks"
        - "context files"
        - "compaction"
        - "sessions"
        - "models/providers"
        - "commands"
    right_side:
      label: "Flue"
      code_example: |
        // Give agents the autonomy to solve complex tasks:
        const instructions = `
        Triage a bug report end-to-end: reproduce the bug,
        diagnose the root cause, verify whether the behavior is
        intentional, and attempt a fix.`;

        // Compose the context your agent needs to do real work,
        // complete with virtual, local, or remote container sandbox.
        export default defineAgent(() => ({
          model:   'anthropic/claude-sonnet-4-6',
          tools:   [replyToIssue],
          skills:  [triage, verify],
          sandbox: local(),
          instructions,
        }));
      revealed_list:
        - "Agents"
        - "Workflows"
        - "Models"
        - "Instructions"
        - "Tools"
        - "Skills"
        - "Actions"
        - "Sandboxes"
        - "Sessions"
        - "Agent IDs / instances"
        - "Channels"
        - "Subagents"
        - "Durable execution"
        - "Database / persistence"
        - "Runs"
        - "Routing / HTTP exposure"
        - "SDK / client"
        - "Observability"
        - "Attachments / image inputs"
  speaker_notes:
    - "This should feel like the Lego-block reveal."
    - "The point is not framework tribalism."
    - "Soon people will assemble their own harnesses a la carte."

- slide: 13
  title: "Now let’s unharness the agent"
  layout: "terse transition slide"
  visible_content:
    main_statement: "Now let’s expand where agents can live and what they can do."
  speaker_notes:
    - "Very short transition out of the demo ladder."

- slide: 14
  kicker: Agents can live inside software products
  title: "AI reviewer"
  layout: "two-column demo slide, polished bullets on the left and practical reference details on the right"
  visible_content:
    left_side:
      bullets:
        - "Same basic recipe: model, skills, tools, instructions"
        - "Adds structured output"
        - "Normal application code can call into the agent"
        - "The behavior is written in English"
    right_side:
      artifacts:
        - "[The AI reviewer agent implementation](https://github.com/arcturus-labs/talk--unharness-the-agent/blob/main/pydantic-ai-reviewer/src/pydantic_ai_reviewer/ai_reviewer.py)"
        - "[The screen-candidate skill file](https://github.com/arcturus-labs/talk--unharness-the-agent/blob/main/pydantic-ai-reviewer/skills/screen-candidate/SKILL.md)"
      command: "cd /Users/johnberryman/projects/github/arcturus-labs/talk--unharness-the-agent/pydantic-ai-reviewer && uv run python -m pydantic_ai_reviewer"
  speaker_notes:
    - "This one gets a little more polish, but it still works as a practical reference slide."
    - "During the talk, I will use it as a navigation and command reference."
    - "The key point is that the agent is embedded inside an application and performs a product task."
    - "Review the skill file and emphasize that the behavior is written in English."

- slide: 15
  kicker: "Agents can live outside software products too"
  title: "B.Y.O.A. – Bring Your Own Agent"
  layout: "idea slide with one strong product thesis and a concrete GitHub example"
  visible_content:
    main_statement: "The dominant interface may become your own agent."
    supporting_points:
      - "Built-in website agents have tools, but not your full context"
      - "Your own agent already knows your machine, files, and current work"
      - "The exciting future is your personal agent entering environments like GitHub with the right tools and instructions"
      - "You and the agent can work on the same surface together"
  speaker_notes:
    - "Use the GitHub example heavily here."
    - "Talk about creating issues, editing text and tags, and moving tasks on boards together."
    - "The emotional point is how much more complete and engaging that experience becomes."

- slide: 16
  kicker: "Agents can live way outside of software products actually"
  title: "B.Y.O.A. I.R.L. – Bring your agent into the physical world"
  layout: "concept slide with one vivid real-world example"
  visible_content:
    main_statement: "Why stop at websites and software applications?"
    supporting_points:
      - "The same pattern extends into physical environments"
      - "Your phone-hosted agent can gain environment-specific tools and data"
      - "Grocery store example: shopping list, live inventory, discounts, store map, route planning"
      - "Same core pattern, richer environment"
  speaker_notes:
    - "Keep this grounded in one concrete example rather than too many possibilities."

- slide: 17
  kicker: "What should you remember?"
  title: "Wrap-up time"
  layout: "clean recap slide"
  visible_content:
    recap_points:
      - "Agents and agent harnesses are not magic"
      - "Building them increasingly looks like assembling Lego blocks"
      - "Agents can do any task with the right instructions, tools, and data"
      - "Programming them is getting easier, they speak English"
      - "Agents can perform functions embedded inside of traditional software"
      - Agents can exist outside of traditional software products and even in physical environments as universal assistants"
  speaker_notes:
    - "This should feel like a calm consolidation of the talk."

- slide: 18
  kicker: "What should you remember?"
  title: "Homework"
  layout: "final call-to-action slide"
  visible_content:
    main_statement: "Go make your own today."
    supporting_points:
      - "Do not wait"
      - "An hour of building will change how you think forever"
      - "That is how this mental model becomes real and sticks"
  speaker_notes:
    - "End with a direct challenge."
```
