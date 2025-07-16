# 🤖 Auto-Reply Insult Bot for WhatsApp

A voice-based and text-based auto-reply bot that connects to **WhatsApp Web** and roasts incoming messages in real-time using different themes — including humorous, explicit, romantic, and tech-savvy responses.

## 💡 Features

- 🔥 Automatically replies to new WhatsApp messages.
- 🧠 AI-style prewritten insult templates.
- 🗣️ Text-to-speech engine (TTS) for vocal responses.
- 🎭 Multiple themes:
  - `default`: Clean/funny insults
  - `illu`: Abusive & extreme
  - `roasty`: Savage tech-savvy insults
  - `romantic`: Flirty & emotional messages

## 📦 Dependencies

Make sure you have the following Python packages installed:

```bash
pip install selenium pyttsx3 webdriver-manager
```

> Optional but unused in script: `pywhatkit`, `datetime`

## 🚀 How to Use

1. **Run the Script**:
   ```bash
   python Project_4.py
   ```

2. **Choose a Theme** when prompted.

3. **Scan WhatsApp Web QR code** when Chrome opens.

4. **Keep the target chat open**, and the bot will automatically:
   - Read new messages
   - Generate a matching reply
   - Speak the response
   - Send it back to WhatsApp

## ⚠️ Disclaimer

> This is a **fun and educational project** intended for personal use only. Some themes contain adult language and explicit phrases. Use responsibly and do not violate WhatsApp's Terms of Service.

## 📁 File Structure

```
Project_4.py       # Main bot logic
README.md          # Project documentation
```

## 🧑‍💻 Author

Made with ❤️ by N. Iliyaz Nidimamidi
