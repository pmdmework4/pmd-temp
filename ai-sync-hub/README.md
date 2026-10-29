# AI Sync Hub — Gemini × ChatGPT Markdown Bridge

A responsive dashboard and API for sharing chat context as Markdown between Gemini and ChatGPT.

## Features
- Responsive dashboard with sessions, Markdown-style timeline, `.md` download, and manual turn entry.
- API endpoints: `GET /api/health`, `POST /api/sync`, `GET /api/context`, `GET /api/raw/:session_id.md`, `GET /api/sessions`, `POST /api/clear`.
- Persistent storage in Supabase; clear archives data before deleting turns.
- Vercel serverless routing and optional Express local server.

## Deploy
1. Create a Supabase project or use an existing dedicated project.
2. Run `supabase/schema.sql` in Supabase SQL Editor.
3. Add env vars from `.env.example`. Keep the Supabase service-role key server-side only.
4. Deploy this folder as a Vercel project. Locally: `npm install` then `npm run start`.
5. Configure a strong `SYNC_API_TOKEN`; send it as `Authorization: Bearer <token>` to `/api/sync` and `/api/clear`.

## API
`POST /api/sync` body: `{"session_id":"default","source":"chatgpt","user_prompt":"Question","ai_response":"Answer"}`

`GET /api/context?session_id=default&last_n=5`

## Limitations
- Quick Relay UI is present but direct model calls are deliberately unavailable until a secure server-side relay is implemented.
- Persistent storage requires Supabase; Vercel serverless local files are not durable.
- Limit CORS to the production domain before exposing publicly.
