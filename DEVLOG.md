# DEVLOG

## 2026.4.26 / 14：50

### What I built

- Created the initial Streamlit app.
- Added a text input area and save button.

### What I learned

- How to create a Python virtual environment.
- How to install Streamlit.
- How to run a local Streamlit app.

### Problems

- Virtual environment is still unfamiliar.
- Need to learn how to save data.

### Next

- Add SQLite database storage.

### Feeling
## Reflection

- Today I ran my first Streamlit web app. Although the app is simple and heavily relies on the Streamlit library, seeing it work in the browser made me feel that I can actually build software.

I realized that development feels similar to cooking or playing a game: by doing small steps, I can understand the process more clearly. This reduced my anxiety and made the project feel achievable.

My next goal is to make the app store user input in SQLite, so it becomes a tool with memory instead of just a webpage.



## Day 2

### What I built

- Added SQLite database support to the Streamlit app.
- Created a separate `db.py` file for database-related functions.
- Implemented three database functions:
  - `init_db()` creates the `records` table if it does not exist.
  - `save_record()` saves one user record into SQLite.
  - `get_records()` reads saved records from SQLite.
- Updated `app.py` so that user input can be saved and displayed as history.
- Added category selection for records.
- Used `st.expander()` to show each saved record in a clean, collapsible UI.
- Used a mock summary first instead of calling a real LLM.

### What I learned

- A function is a named block of reusable logic. In this project, each function is responsible for one action, such as initializing the database, saving a record, or reading records.
- SQLite is a lightweight local database. It stores app data in a `.db` file.
- The basic SQLite workflow is:
  1. connect to the database
  2. create a cursor
  3. execute SQL commands
  4. commit changes if data is modified
  5. close the connection
- `conn.commit()` in SQLite means confirming database changes, while `git commit` means saving a version of the code.
- `text.strip()` removes spaces and line breaks from the beginning and end of user input. It helps check whether the user actually entered meaningful content.
- `st.expander()` creates a collapsible UI section, which makes the history display cleaner.
- `with st.expander(...)` means that the indented UI elements are placed inside that expander.
- `record_id, created_at, category, raw_text, summary = record` is tuple unpacking. It splits one database row into separate variables.
- The order of unpacking must match the order in the SQL `SELECT` statement.

### Design Notes

- I chose to start with one simple `records` table instead of a more complex multi-table design. This keeps the first database version easy to understand and debug.
- I used a mock summary instead of a real LLM summary for now. This reduces complexity and lets me first confirm that the UI and database flow work correctly.
- The current app is still small, but it now has persistent memory: saved records remain available after restarting the app.

### Problems / Questions

- I am still getting used to the difference between Python functions, Streamlit UI components, and database operations.
- I need more practice reading code such as `with st.expander(...)` and tuple unpacking.
- I do not need to memorize every Streamlit function, but I should understand the data flow and the role of each module.

### Next

- Refactor or clean up the display if needed.
- Add a separate `llm.py` file.
- Replace the mock summary with a real AI summary later.
- Add interview feedback mode after the database flow is stable.