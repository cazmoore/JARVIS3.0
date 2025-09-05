# JARVIS - Your Personal Voice Assistant

JARVIS is a Python-based voice assistant that can perform various tasks through voice commands. It's designed to be modular and extensible.

## 🚀 Features

### Basic Commands
- **Greetings**: Responds to greetings like "hello", "hi", "hey"
- **Time**: Ask for the current time
- **Date**: Ask for today's date
- **Jokes**: Tell a random joke
- **News**: Get the latest headlines
- **Wikipedia Search**: Look up information on Wikipedia
- **Web Search**: Search the web using Google
- **Screenshots**: Take a screenshot of your screen
- **Password Generator**: Generate a secure password

### Advanced Features
- **Email**: Send emails (requires configuration)
- **WhatsApp**: Send WhatsApp messages (requires configuration)
- **Text-to-Speech**: Read text from clipboard
- **AI Chat**: Have a conversation using OpenAI's GPT model
- **Custom Voice**: Uses Microsoft Edge's neural voices for natural-sounding speech

## 🛠️ Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API Keys**:
   Create a `hidden.py` file in the project root with your API keys:
   ```python
   # OpenAI API Key (for AI features)
   openai_api_key = "your_openai_api_key_here"
   
   # Email Configuration (optional)
   sender_email = "your_email@example.com"
   sender_password = "your_email_password"
   
   # News API Key (for news feature)
   news_api_key = "your_newsapi_key_here"
   ```

3. **Run JARVIS**:
   ```bash
   python jarvis.py
   ```

## 🎙️ Voice Commands

Start your command with "Jarvis" to activate the assistant, then say:

- "What time is it?" - Get current time
- "What's the date?" - Get today's date
- "Tell me a joke" - Hear a random joke
- "News" - Get the latest headlines
- "Wikipedia [query]" - Search Wikipedia
- "Search for [query]" - Web search
- "Take a screenshot" - Capture your screen
- "Generate a password" - Create a secure password
- "Read clipboard" - Read text from clipboard
- "Send email" - Compose and send an email
- "Send WhatsApp" - Send a WhatsApp message (requires setup)
- "Goodbye" or "Exit" - Close JARVIS

## 🤖 AI Features

JARVIS includes AI capabilities powered by OpenAI. To use these features:
1. Set up your OpenAI API key in `hidden.py`
2. Use commands like:
   - "Jarvis, let's chat" - Start a conversation
   - Ask any question after the wake word

## ⚙️ Configuration

- **Voice**: Change the voice in `new_voices.py` by modifying the `voice` variable
- **Wake Word**: Change the wake word in `jarvis.py` (default is "jarvis")
- **Hotkeys**: Customize hotkeys in the code as needed

## 🔧 Additional Setup

### Email Setup
1. **Gmail Users**:
   - Enable "Less secure app access" in your Google Account settings
   - Or, use an App Password (recommended):
     1. Enable 2-Step Verification
     2. Generate an App Password for JARVIS
     3. Use this password in `hidden.py`

2. **Other Email Providers**:
   - Check your provider's SMTP settings
   - Update the SMTP server and port in the code if needed

### WhatsApp Setup
1. **Prerequisites**:
   - Install WhatsApp Web on your computer
   - Have WhatsApp Web open and logged in
   - Scan the QR code with your phone

2. **Usage**:
   - Say "Send WhatsApp"
   - Enter the phone number with country code when prompted
   - Speak your message

### OpenAI API Setup
1. Get your API key from [OpenAI](https://platform.openai.com/account/api-keys)
2. Add it to `hidden.py`:
   ```python
   openai_api_key = "your-api-key-here"
   ```

### News API Setup
1. Get a free API key from [NewsAPI](https://newsapi.org/register)
2. Add it to `hidden.py`:
   ```python
   news_api_key = "your-newsapi-key-here"
   ```

### Voice Configuration
- Edit `new_voices.py` to change the voice
- Available voices can be listed by running:
  ```bash
  edge-tts --list-voices
  ```
- Set your preferred voice by modifying the `voice` variable

## 📝 Notes
- Internet connection is required for most features
- For best results, use a good quality microphone
- Some features may require additional system dependencies
- For security, never commit your `hidden.py` file to version control

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Credits

Built with Python and various open-source libraries. Special thanks to the developers of the packages listed in `requirements.txt`.
