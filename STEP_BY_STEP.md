# Step-by-step coding guide

## Step 1 — Run the starter (do this first)
Open a terminal in this folder and run:
```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```
Enter a topic such as `How AI helps students learn`, select a content type and tone, then click **Generate content**.

## Step 2 — Understand the code
In `app.py`, find:
- `CONTENT_TYPES`: options shown in the content-type dropdown.
- `TONES`: writing-style choices.
- `build_prompt(...)`: creates an instruction string.
- `generate_template_content(...)`: starter output logic.
- `st.form(...)`: collects the user's inputs.
- `re.findall(...)`: counts words.
- `len(...)`: counts characters.

## Your first coding task
In `app.py`, locate `def build_prompt(topic, tone, content_type, length):`.
Change the returned prompt so it also asks for:
- a clear title,
- an introduction,
- 3 useful points,
- a conclusion,
- no made-up statistics.

Save the file. Then tell your tutor: **Step 1 completed** and paste your updated `build_prompt` function. I will review it before we move to Step 2.

## Testing checklist
- [ ] Empty topic shows an error.
- [ ] Blog Post generates a multi-section draft.
- [ ] Social Media Caption produces a short caption.
- [ ] Text Summary produces a summary-style draft.
- [ ] Word and character counts appear.
- [ ] Download button saves a .txt file.
- [ ] Regenerate/refine button works.
