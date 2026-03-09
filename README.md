# hirodai-syllabus-2026

FastAPI で講義コードからシラバス情報を返す API です。

## Endpoints

- `GET /`
- `GET /docs`
- `GET /api/health`
- `GET /api/courses/{course_code}`

例:

```bash
curl http://127.0.0.1:8000/api/courses/WA000101
```

## Local Development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```

## Deploy To Vercel

Vercel の公式ドキュメントでは、`app.py` / `index.py` / `server.py` などで `FastAPI` の `app` を export すれば FastAPI をゼロ設定でデプロイできます。

```bash
npm i -g vercel
vercel
```

デプロイ後は `https://<your-project>.vercel.app/api/courses/WA000101` のようにアクセスできます。
