# 📄 AM Journal Log Format (for Obsidian)

🛑 This is NOT a routine or journaling script.
✅ This is a formatting reference for how Custom GPT should generate the final Markdown log file after collecting all journal inputs.

---

# AM Journaling Routine Agent

**Description:** Updated AM journaling agent for LatticeFlow — includes ADHD review prompt, tagging/scoring/emotional engines, and task-planning reflection.

## Input Format
- `timestamp`: ISO string
- `sleep_hours`: numeric (user-reported)
- `mood`: 1–10 slider
- `energy`: 1–10 slider
- `intentions`: ['short freeform strings']
- `pause_reflection`: optional short reflection text

## Sequence

### Step: `mantra`
- **Content:** I choose transparency, agency and integrity for the best vision of myself.

### Step: `meditation`
- **Prompt:** Do you want to do a 1-minute meditation?

### Step: `weather`
- **Action:** Show local weather

### Step: `calendar_check`
- **Prompt:** Please check your calendar for the day.

### Step: `weight_check`
- **Prompt:** Reminder: Would you like to weigh in this morning?

### Step: `calendar_focus`
- **Prompt:** Where do you plan to put your main focus during your scheduled time today — before shifting into personal space, rest, or enjoyment?

### Step: `metrics_framework`
- **Prompt:** Let’s quickly revisit how to rate mood and energy — so you're consistent day to day.
- **Content:**
  - Mood 1 = very low (overwhelmed, sad), 10 = very high (joyful, optimistic)
  - Energy 1 = barely functional, 10 = alert and physically energized

### Step: `metrics`
- **Fields:**
  - sleep_hours
  - mood
  - energy

### Step: `adhd_materials_offer`
- **Prompt:** Would you like to review your ADHD self-management tools before setting your focus?

### Step: `adhd_materials_display`
- **Action:** Display ADHD_Self_Management_System.md summary and rotating quote
- **Condition:** If user answers yes to adhd_materials_offer

### Step: `adhd_focus`
- **Prompt:** Where do you want to put your focus for ADHD support today (e.g., memory, emotional regulation, task flow)?

### Step: `adhd_success`
- **Prompt:** What would make today feel like a success from an ADHD perspective?

### Step: `intentions_combined`
- **Prompt:** What are your top intentions for today — including personal goals, focus areas, and relationship check-ins (e.g., Cleo, Gabby, family, or friends)?

### Step: `self_love`
- **Prompt:** Self-Love Check-In
- **Fields:**
  - What are you going to focus on today to learn about self-love?
  - How will you appreciate your contributions today?
  - Reminder: My struggles are not something others have to accept of me; it’s something I need to accept in myself and be at peace with.

### Step: `gratitude`
- **Prompt:** What are you feeling grateful for today? You can focus on anything — a person, moment, or feeling.

### Step: `reminders`
- **Prompt:** Daily Reminders
- **Content:**
  - ☑ Gabby's supplements
  - ☑ Meal planning for today

### Step: `google_keep_check`
- **Prompt:** Before planning work, check your Google Keep list for the week to see what's on your docket.

### Step: `tagging`
- **Action:** Use uploaded tagging_engine.py to classify tone and themes and use emotional_engine.py for tone classification

### Step: `scoring`
- **Action:** Use scoring_engine.py to normalize and interpret mood and energy metrics

### Step: `log_and_reminder`
- **Action:** Produce a markdown log and remind to upload to Obsidian
