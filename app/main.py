from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Simple FastAPI UI")


@app.get("/", response_class=HTMLResponse)
async def read_root() -> str:
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>FastAPI Demo</title>
        <style>
            body {
                margin: 0;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #e0f2fe, #f8fafc);
                color: #0f172a;
            }
            .card {
                background: white;
                border-radius: 16px;
                box-shadow: 0 10px 30px rgba(15, 23, 42, 0.15);
                padding: 2rem 2.5rem;
                text-align: center;
                width: min(90vw, 500px);
            }
            h1 {
                margin-top: 0;
                color: #2563eb;
            }
            button {
                margin-top: 1rem;
                background: #2563eb;
                color: white;
                border: none;
                padding: 0.8rem 1.2rem;
                border-radius: 10px;
                font-size: 1rem;
                cursor: pointer;
            }
            #status {
                margin-top: 1rem;
                font-weight: bold;
                color: #0f766e;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Welcome to FastAPI</h1>
            <p>Your simple UI is running successfully.</p>
            <button onclick="document.getElementById('status').textContent = 'Button clicked!';">
                Click Me
            </button>
            <p id="status">Ready</p>
        </div>
    </body>
    </html>
    """


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}
