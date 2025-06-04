# VoiceAssistant

A Python-powered voice assistant capable of executing desktop commands, fetching web information and answering free-form questions using a HuggingFace language model.

## Setup

1. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure environment variables**
   Create a `.env` file in the repository root and set the following values:
   ```ini
   EMAIL=your_email@example.com
   PASSWORD=your_email_password
   OPENWEATHER_APP_ID=<openweather_key>
   TMDB_API_KEY=<tmdb_key>
   NEWS_API_KEY=<news_api_key>
   USER=YourName
   BOTNAME=Assistant
   HF_MODEL=distilgpt2  # optional HuggingFace model name
   ```

## Running

After installing requirements and configuring environment variables, run:
```bash
python main.py
```

The assistant listens for voice commands and can also answer general questions using the configured HuggingFace model.
