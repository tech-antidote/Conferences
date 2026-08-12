---
title: "Web Hacking 101"
speakers: ["cale 'calebot' smith"]
conference: "DEF CON"
conference_full: "DEF CON 34"
year: 2026
source_type: "workshop-materials"
source_dir: "DEF CON 34 - Workshops - cale - calebot - smith - Web Hacking 101"
files_included: 1
files_skipped: 0
text_chars: 3284
redacted_secrets: 0
sha256: "b55261d8bfd0adcf619bd3b53cd9d894c3daea6afa7ac3740f1812d6f728b049"
converted_at: "2026-08-12T07:17:47Z"
---

# Web Hacking 101

**Speakers:** cale 'calebot' smith  
**Conference:** DEF CON 34 (workshop materials)  
**Contents:** 1 readable files inlined below. This is the workshop's own source material, not slide text — no OCR is involved, so the code is exact.

## Materials

### `DEF CON 34 - Workshops - cale - calebot - smith - Web Hacking 101.md`

```markdown
# Web Hacking 101 — Whitebox Web Exploit Development
### Enhanced Abstract · DEF CON 34 Workshops

**Format:** Half-day, hands-on workshop (~4 hours, two breaks)
**Level:** Beginner → low-intermediate
**Instructors:** Cale Smith · Luke Cycon · Young Kim · Ruchik Dave
**Materials:** https://github.com/wasayoung1/webhacking101-defcon34  *(being populated ahead of the con)*

---

## Synopsis

Web Hacking 101 is a hands-on, lab-driven introduction to finding and weaponizing real web
vulnerabilities — and then chaining them into a working remote-root exploit you keep. It is **not**
a tool tour. Our differentiator is **whitebox exploitation driven by live runtime telemetry**:
students have the application source *and* the running box, and learn to trace their input from
where it enters to where it is used, then confirm what the app *actually* does — tailing the
database query log, watching processes with `strace`/`ps`, and reading the response — before
crafting a payload that fits reality.

Every challenge carries a small, deliberate wrinkle where a blind copy-paste of the textbook (or LLM-suggested) payload quietly fails — a required encoding, a filtered separator, a mangled argument, a column you can only learn from the log. The lesson: AI is a multiplier on methodology, never a substitute. The win comes from what you observe.

Students attack **BackHaul UDB**, a realistic (fictional) enterprise backup-appliance console that
hosts the full vulnerability set as features of one product. A progressive hint ladder means nobody gets left at the prompt.

## What students will do

- **SQL injection** — login bypass, UNION-based data extraction, and a whitebox blind injection
  read from the live query log.
- **Command injection & RCE** — break out of a shell context, defeat a filter, and catch a shell.
- **Authentication & identity** — forge JWTs, and exploit a session-fixation flaw.
- **Access control** — IDOR against object references that skip ownership checks.
- **Cross-site scripting** — context-aware payloads that escalate to session/token theft.
- **The capstone** — chain an auth bypass and RCE into a single Python `pwn.py` that goes from
  unauthenticated to a root shell. Yours to keep.

## On-ramp for newcomers

Alongside the full target, we provide a set of **single-vulnerability standalone labs** — one
isolated bug each, with a live "wire trace" panel that shows the exact query/command/token the app built from your input. Beginners learn each concept cleanly first; the unified app is where you go to spend real time on the harder, filtered versions.

## Prerequisites

Basic HTTP and a willingness to read code. Bring a laptop on WiFi with browser dev tools, an SSH client, `curl`, Python 3, and **Burp Suite Community** (the free edition is all you need — no Pro features required). We hand out targets and a shell box in the room, so no local VMs to fight with; Docker (Docker Desktop / OrbStack) is optional if you want to run the labs on your own machine.

## Takeaways

Students leave able to find and exploit the OWASP-classic web bugs first-hand, work a real target *whitebox* (source review + runtime telemetry), and assemble individual findings into a full
remote-root kill chain — with a methodology that holds up in the AI era.
```
