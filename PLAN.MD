# ALE SKATE CLUB — Website specification (WWW plan)

This document consolidates **all** requirements, links, constraints, and content-structure notes from **`concept/WWW - PLAN.pdf`** and **`concept/WWW - PLAN.xlsx`** (sheets: *Ogólnie*, *Zakładki*, *Treści do zakładek*, *Zdjecia*). Nothing from those sources is omitted.

---

## 1. Source artifacts

| Artifact | Role |
|----------|------|
| `WWW - PLAN.pdf` | Planning notes, page breaks, English body copy, Polish notes |
| `WWW - PLAN.xlsx` | Structured brief: general info, nav map, per-section copy, photos sheet |

---

## 2. Deployment & canonical URLs

| Item | Value |
|------|--------|
| **WWW (published site)** | `https://piotrpawlowski7.github.io/aleskate/` |
| **Graphics for WWW (folder)** | `https://drive.google.com/drive/folders/1vpmKG2aQSWqukcW0xWBK2DaKdIFwCB7T?usp=sharing` |
| **LOGO assets (folder)** | `https://drive.google.com/drive/folders/1c3A8uZaJlFWnAZxVyAFmZP_dYiY7z6QZ?usp=drive_link` |

---

## 3. Brand & naming

| Field | Spec |
|-------|------|
| **Full name** | **ALE SKATE CLUB** (spacing and capitalization as stated) |
| **Short description (English)** | **Non-professional skate club in Warsaw.** |
| **Year / establishment copy** | **Established 2022** — used as *rok założenia* / founding line in materials |
| **Rejected phrase** | **“Est. — always.”** — **do not use** |
| **Replacement for that rejected phrase** | **Established 2024** — use **instead of** “Est. — always.” (stakeholder explicitly requested this swap; **note:** this coexists with **Established 2022** elsewhere — implement as **two distinct UI/content slots**: one for founding/history **2022**, one for the **2024** treatment where the old “Est. always” tagline would have lived) |

---

## 4. Visual design & art direction

| Topic | Requirement |
|-------|-------------|
| **KOLORY WWW** | Mentioned in spreadsheet (**colors for web**) — **no palette values** were provided in the extracted files; implementation must either wait for assets from **LOGO** / **GRAFIKI** folders or be defined in a follow-up |
| **Benchmark website** | `https://www.vans.com/pl-pl` |
| **Why this benchmark** | **“Mega prosta i przejrzysta!”** — very simple and clear |
| **Layout/content feel** | **Oparta na zdjęciach/filmikach** — based on photos/films; must communicate **community atmosphere** well |
| **Primary subject matter** | Stakeholder wants the **main element of the WWW** to be **people [community]** and **skateboard** |
| **Style reference (preference)** | **Something more in the style of John Gos** than **“tej grafiki z 7km”** — i.e. prefer **John Gos**-like direction over **7km**-style graphics |

---

## 5. Copy constraints (mandatory “do not” list)

These are **explicit exclusions** from the Polish brief:

1. **Do not** write that **no experience** is needed. Required messaging: on the board you must **know how to stand** and **ride straight** (**“Na desce trzeba umieć stać i jechać prosto.”**).
2. **Do not** write that you **don’t need to have your own board** (**“NIE CHCE PISAĆ, ŻE NIE TRZEBA MIEĆ WŁASNEJ DESKI”**).
3. **Do not** use **“Est. — always.”** — replace that concept with **Established 2024** (see §3).

---

## 6. Information architecture — top-level sections (“Elementy strony”)

From sheet **Zakładki** and PDF:

| # | Section (label) | Notes |
|---|-----------------|--------|
| 1 | **ABOUT** | Club story, values, season, language, free meetups |
| 2 | **WEEKLY MEETINGS** | Three pillars called out: **Ale Tuesday** (weekly), **Ale Dancing!**, **Zielonka skatepark sessions** (spelling in source: *seasions*) |
| 3 | **SPECIAL EVENTS** | Examples given: **SKATEBOARD rides through the streets of Warsaw**; **Weekend SKATE camps in Skarland** |
| 4 | **HOW TO JOIN** | WhatsApp-first, English, free, inclusive |
| 5 | **PHOTOS** | Stakeholder: *“chciałabym tu dodać te co zrobiłeś nam”* — include **photos that were already produced** for them |
| 6 | **CONTACT** | Email: **ale.skate.club@gmail.com**; plus social links (see §8) |
| 7 | **WSPIERAJĄ NAS** (Partners) | **Space for partner logos**; must support **adding a partner logo**; **rare** changes — **max ~3 times per year** |

**Additional links (not a separate nav label in the short list, but required on site):**

| Link | URL |
|------|-----|
| **Instagram** | `https://www.instagram.com/aleskate.club/` |
| **WhatsApp (group)** | `https://chat.whatsapp.com/LwtLbxt1eqWIBU5DchTXIn?mode=gi_t` |

---

## 7. Navigation labels (English row in spreadsheet)

Header row in **Treści do zakładek** maps columns to:

1. **ABOUT US**  
2. **REGULAR MEETINGS**  
3. **SPECIAL EVENTS**  
4. *(empty column in matrix — structural gap in source)*  
5. **HOW TO JOIN**  
6. **CONTACT**  
7. **WSPIERAJĄ NAS**  

Align **WEEKLY MEETINGS** (Zakładki) with **REGULAR MEETINGS** (Treści) in implementation.

---

## 8. Open design question — upcoming events

Stakeholder **question** (not a final spec):

- How to add **“NADCHODZĄCE EVENTY”** so they can post info like **“in a week there’s an event”**?
- **Idea recorded:** maybe **a slider at the very top** that **changes** / rotates?

**Implementation status:** **TBD** — requires UX decision; treat as **high priority content** need (time-sensitive announcements).

---

## 9. Language policy (from English copy)

- **Official communication:** **English** — so **internationals in Warsaw** feel welcome.
- Meetups **100% free**.
- Community tries to use **English** so everyone can participate.

---

## 10. Matrix content — column-by-column (sheet *Treści do zakładek*)

The spreadsheet places long-form English text in columns under the headers above. Below is the **functional spec** of what each column must contain (including all facts, locations, numbers, and links).

### 10.1 ABOUT US

- **Identity:** Warsaw-based skateboarding community **since 2022**.
- **Inclusivity of equipment:** classic deck, surfskate, longboard, dancing, “old board for groceries” — **if it has wheels, it fits**.
- **Skill gate:** **Can stand and ride straight** → welcome; beginners through advanced.
- **Season:** **April–September** main season; **weather-dependent**; several times a week — **Vistula**, squares, skateparks.
- **Special formats mentioned:** day & night city rides with **police escort**; trips to **Skarland** (**biggest skatepark in Poland**).
- **Culture:** show up with board — **no ego, no skill-judging**; **stoke** and **riding together**.
- **Economics:** meetups **100% free**.
- **Language:** **English** for official communication; **international community** in Warsaw explicitly called out.

### 10.2 REGULAR MEETINGS

**A) Cross-cutting rules**

- Season **April–September** but **exact dates depend on weather**.
- **Session times shift** with longer/shorter days.
- **Rule:** always confirm **spots** and **exact times** in **WhatsApp** — **crew stays connected** there; **check before heading out**.

**B) ALE Tuesday — River rides**

- **Weekly**, **every Tuesday** in season.
- **Core weekday session**; **largest slice of community** — best if you want to **meet the most people**.
- **Start:** **Polna 30a**, **Politechnika** metro area (city center).
- **Route:** toward **Vistula**; cruise **riverbanks**; **finish** at **Letnisko Żoliborz** — deckchairs, drinks, social.
- **Pace:** own pace, any board; **stops to regroup**; **beginners OK**.
- **Link:** WhatsApp group URL (same as §11).

**C) ALE Dance**

- Focus: **longboard dancing** — flow, style, movement.
- **Locations:** central, e.g. **Plac Piłsudskiego** or near **National Stadium** — **depends on day/conditions**.
- **Schedule:** **different days of the week** possible; vibe: **open, welcoming, supportive**.
- **Levels:** experienced + complete beginners; **all levels welcome**.
- **Join flow:** WhatsApp — ask **when** next dance session; **typo in source:** *sessionj oin* → intent is **join via WhatsApp**.
- **No board:** ask in WhatsApp if someone can **lend** a board for the session.

**D) ALE Saturday — Zielonka skatepark**

- **Weekly**, **every Saturday**, **morning onward**, full season.
- **Place:** Zielonka, **Dziennikarska 57**.
- **Mix:** experienced + beginners; some people **without board** just to hang out.
- **Activities:** ride, talk, learn; **first skatepark visit** is common; community helps with **tips** and **getting started**.
- **Join flow:** WhatsApp — confirm **this Saturday** and **time**.

### 10.3 SPECIAL EVENTS

**A) ALE Surfskate Camp in Skarland**

- **Weekend** events; **free**; **two-day** surfskate camps.
- **Location:** **biggest skatepark in Poland** — **Skarżysko-Kamienna** (named as **Skarland** in copy).
- **Travel:** often **Friday after work** or **early Saturday**; whole weekend at park.
- **Program:** days — riding, skills, skating together; evenings — **campfire**, **tents on skatepark grounds**; optional **swim** in nearby lake in nice weather.
- **Frequency:** **3–4** trips per **season**; **dates announced in advance** before season.
- **Join:** WhatsApp — say which event; receive **meeting place, day, time**; **show up** = part of community.
- **Inclusivity:** **age** / **nationality** open; **English**; **all events free**; WhatsApp link repeated in cell.

**B) ALE Skateboarding Street Parade (Warsaw, police escort)**

- **Largest** event of the season by turnout.
- **Partnership:** **City of Warsaw**.
- **Concept:** skate **city streets** normally used by cars / where skating is **normally not allowed**; **police escort** → **safe**, **organized**.
- **Format:** **not a race** — **relaxed cruise**; **dozens**, up to **~150** participants.
- **Values:** **freedom**, not speed; **street-level** city discovery.
- **Boards:** any (street, surfskate, longboard, in between).
- **Frequency:** **2× per season** (stated).
- **Info channels:** **WhatsApp** and **Instagram** (both URLs in materials).

### 10.4 HOW TO JOIN

- **WhatsApp:** riders who want **meetups/events** — join group, say **session type**; **community replies**.
- **Instagram:** **vibe**, **meetups look**, **who’s in the crew**, **how we roll** — link to `aleskate.club`.
- **External reference URL** appearing in the spreadsheet cell row: **`https://zefir.surf/`** — treat as **linked reference** from the plan (purpose not expanded in source; keep as optional link unless stakeholder removes it).

### 10.5 CONTACT

- **Riders / loop:** WhatsApp (same group link).
- **Brands / organizations:** **email** to collaborate — **`ale.skate.club@gmail.com`**.
- **Instagram** URL repeated.
- **Location name** appearing adjacent in matrix: **Letnisko Żoliborz** (already tied to Tuesday route end — ensure site doesn’t contradict).

### 10.6 WSPIERAJĄ NAS

- **Partners:** brands/orgs — **email** **`ale.skate.club@gmail.com`** to **create something together**.
- **Letnisko Żoliborz** appears in the same row block in source (geographic anchor — likely **content adjacency** in spreadsheet, not a second “partners” meaning).

---

## 11. Canonical external links (repeatable block)

Use consistently across CTAs:

| Purpose | URL |
|---------|-----|
| WhatsApp group | `https://chat.whatsapp.com/LwtLbxt1eqWIBU5DchTXIn?mode=gi_t` |
| Instagram | `https://www.instagram.com/aleskate.club/` |
| Public site | `https://piotrpawlowski7.github.io/aleskate/` |
| Mail | `ale.skate.club@gmail.com` |
| Graphics drive | `https://drive.google.com/drive/folders/1vpmKG2aQSWqukcW0xWBK2DaKdIFwCB7T?usp=sharing` |
| Logo drive | `https://drive.google.com/drive/folders/1c3A8uZaJlFWnAZxVyAFmZP_dYiY7z6QZ?usp=drive_link` |
| Benchmark | `https://www.vans.com/pl-pl` |
| zefir.surf | `https://zefir.surf/` |

---

## 12. Partners section — functional requirements

- **Visual:** **place for partner logos**.
- **CMS / authoring:** **ability to add** (and by implication replace) **partner logos**.
- **Update cadence:** **rare** — stakeholder says **about 3 times a year maximum** — design need not optimize for daily edits.

---

## 13. Photos section — functional requirements

- **Content:** include **photos already produced** for the club (per stakeholder note).
- **Sheet *Zdjecia*:** present in workbook as a tab; **no additional tabular data** was extracted beyond sheet existence — treat as **placeholder for photo list/assets** until provided.

---

## 14. PDF-only fragments (pages 4–6)

PDF pages **4–6** are **empty** in extraction (only page markers **-- 4 of 6 --** through **-- 6 of 6 --**). **No extra text** was present there in the source file.

---

## 15. Known typos / encoding in source (for QA, not for production copy)

- **“byli9”** → intended **“byli”** (people were the main element).
- **“seasions”** → **sessions**.
- **“sessionj oin”** → **session, join** / **join our**.
- **“opis”** line and Polish notes: use **UTF-8** everywhere to preserve **Polish characters** in internal docs.

---

## 16. Acceptance checklist (derived)

- [ ] Nav covers: **About**, **Weekly/Regular meetings**, **Special events**, **How to join**, **Photos**, **Contact**, **Partners**.
- [ ] **Instagram** + **WhatsApp** prominently available.
- [ ] All **do-not-say** rules (§5) respected in visible copy.
- [ ] **Established 2022** vs **Established 2024** used in correct slots (§3).
- [ ] **Partners** area supports **logo add/replace**; expectations set for **infrequent** updates.
- [ ] **Upcoming events** UX addressed or explicitly deferred with stakeholder sign-off.
- [ ] Visual direction: **simple/clear** (Vans benchmark), **photo/video**-first, **community + board**, **John Gos** over **7km** style.
- [ ] **Locations and numbers** match §10 (Polna 30a, Politechnika, Letnisko Żoliborz, Plac Piłsudskiego, National Stadium, Dziennikarska 57 Zielonka, Skarżysko-Kamienna, ~150 riders, 2× parade, 3–4 camps, etc.).

---

*End of consolidated plan. Source files: `concept/WWW - PLAN.pdf`, `concept/WWW - PLAN.xlsx`.*
