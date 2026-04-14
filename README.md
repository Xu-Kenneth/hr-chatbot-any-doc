# hr-chatbot-any-doc (HR / Policy RAG Chatbot)

Upload **any** HR/policy document (PDF/DOCX/TXT) and chat with it using a lightweight **RAG** pipeline:
chunking → embeddings → cosine similarity retrieval → grounded chat responses, wrapped in a **Gradio** UI.

## What’s in this folder

- `hr_assistant_any_document.ipynb`: Upload-any-document notebook (this is what you should publish)

## Requirements

- Python 3.10+ recommended
- An OpenAI API key

## Setup

1) Create and activate a virtual environment (optional but recommended).

2) Install dependencies:

```bash
pip install -r requirements.txt
```

3) Set your OpenAI API key.

**Windows (PowerShell):**

```powershell
setx OPENAI_API_KEY "YOUR_KEY_HERE"
```

Restart your terminal/Jupyter kernel after setting it.

## Run (Notebook)

1) Open `hr_assistant_any_document.ipynb` in Jupyter / VS Code / Cursor.
2) Run cells top-to-bottom.
3) When the Gradio app starts, you’ll see a local URL like `http://127.0.0.1:7860`.
4) In the UI:
   - Upload a `.pdf`, `.docx`, or `.txt`
   - Wait for the status message that the document is loaded and embeddings are built
   - Ask questions in the chat

## How it works (quick overview)

- **Extract** full text from the uploaded file
- **Chunk** text into overlapping segments
- **Embed** each chunk with an OpenAI embeddings model
- **Retrieve** top matching chunks using cosine similarity
- **Answer** using a chat model with only the retrieved excerpts as context

## Notes / Tips

- **Large documents**: Very large PDFs can take time/cost to embed (many chunks).

## Troubleshooting

- **“Please upload a document first”**: Upload a file in the Gradio UI before chatting.
- **PDF text is empty/garbled**: The PDF may be scanned images; you’ll need OCR (not included).

