# Project environment configuration

This README describes the required environment variables and safe handling for this project.

Important security note
- Never commit real secrets (API tokens, passwords, private keys) to version control.
- This repository contains placeholder `.env` files for checked-in examples. Keep real secrets in a local, untracked `.env` file.
- A local backup of previously discovered sensitive `.env` values may exist at `.sensitive_backups/.env.backup` in your workspace. That folder is ignored by Git by default. If you prefer, move the backup outside the repository.

Files
- `.env` (checked-in) — contains placeholder values and should be updated locally with real secrets (but NOT committed).
- `.env.example` — example template with variable names.
- `.sensitive_backups/.env.backup` — (optional) local backup of original `.env` contents; this path is ignored by `.gitignore`.

Backend (.env) variables
Place a local `.env` (not committed) at the project root with the following variables. Use the example values as placeholders.

Required
- PORT=8080
  - Port the backend will listen on (default 8080).
- CORS_ORIGIN=http://localhost:5173
  - Origin allowed for CORS when running the frontend with Vite.

Jira (choose one authentication method)
- JIRA_BASE_URL=https://your-domain.atlassian.net
- JIRA_USER=you@example.com
- JIRA_API_TOKEN=your_jira_api_token_here

OR (Bearer token)
- JIRA_BEARER_TOKEN=your_jira_bearer_token_here

Optional
- JIRA_ACCEPTANCE_FIELD=customfield_12345
  - If acceptance criteria are stored in a Jira custom field, set its field id here.

Groq / LLM (if used)
- groq_API_BASE=https://api.groq.com/openai/v1
- groq_API_KEY=your_groq_api_key_here
- groq_MODEL=openai/gpt-oss-120b

Frontend (.env for Vite)
If you want the frontend to call a backend at a different host/port, create `frontend/.env` (Vite envs) with:

- VITE_API_BASE_URL=http://localhost:8080/api

This will be used by `frontend/src/api.ts` to call `/jira` and `/generate-tests` endpoints.

How to run locally (PowerShell)
1. Start backend (from project root):

```powershell
cd "./backend"
npm install
npm run dev
```

2. Start frontend (in a separate terminal):

```powershell
cd "./frontend"
npm install
npm run dev
```

3. Use the frontend UI to fetch a Jira issue (enter a Jira key and click "Fetch from Jira").

Tips & cleanup
- Ensure `.gitignore` contains entries for `.env`, `.sensitive_backups/`, and other secret patterns (it does by default in this repo).
- If you accidentally committed secrets to Git, rotate those secrets immediately and remove them from the repo history.
- If you want me to move the local backup file out of the repository or securely delete it, tell me and I can do that for you.

Contact / next steps
If you'd like, I can:
- Move `.sensitive_backups/.env.backup` outside the repo (recommended), or delete it after you confirm you have the values elsewhere.
- Add a small script to validate required env vars at server start and fail with a readable message if missing.
- Run a final scan for private keys (BEGIN RSA PRIVATE KEY) and other sensitive patterns.

