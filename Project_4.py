import pyttsx3  # For text-to-speech
import random  # For generating random insults
import pywhatkit  # (Unused in this script, can be removed)
import datetime  # (Unused in this script, can be removed)
import time  # To pause between message checks
import uuid  # To create unique user profile paths
import os  # To interact with the operating system
from selenium import webdriver  # To automate browser actions
from selenium.webdriver.common.by import By  # For locating elements on the page
from selenium.webdriver.chrome.service import Service  # To manage ChromeDriver service
from selenium.webdriver.chrome.options import Options  # To customize Chrome launch options
from webdriver_manager.chrome import ChromeDriverManager  # Automatically manage ChromeDriver versions

# === 1. Initialize the TTS engine ===
engine = pyttsx3.init()  # Start the text-to-speech engine
engine.setProperty('rate', 175)  # Set speaking speed

# === 2. Function to speak text ===
def speak(text):  # Convert given text to speech
    print("Bot:", text)  # Print to console
    engine.say(text)  # Queue the speech
    engine.runAndWait()  # Speak it out loud

# === 3. Themed insult templates ===
themes = {  # Dictionary of different styles of insults
    "default": [
        "Oh, please, even a {thing} has better logic than that.",
        "Wow, did you borrow that idea from a {thing}?",
        "Are kya hai re",
        "Bol bhenchod",
        "Abe sale",
        "Kya kar raha hai tu",
        "Maaro mujhe",
        "Arey chacha thand rakh",
        "Chup be gadhe",
        "To bada player nikla",
        "Scene me rehne ka",
        "Kya kar diya tune",
        "To legend nikla",
        "Kya chahiye tujhe",
        "Tatti joke tha",
        "Kya chutiyapa hai ye",
        "Ghanta farak padta hai",
        "Rula diya",
        "Chal nikal",
        "Sambhal lega",
        "Bas ruk ja",
        "Yeh toh overacting ka baap hai",
        "Mummy kasam maza aa gaya",
        "Public ko pagal bana raha hai",
        "Ye sab doglapan hai",
        "Beta tumse na ho payega",
        "Kya bakchodi hai ye",
        "Kar kya raha hai zindagi me",
        "Darr lag raha hai",
        "Yeh toh scam hai",
        "Tu toh hero nikla",
        "Game over hai",
        "Iska toh jawab nahi",
        "Dimag ka dahi ho gaya",
        "Tu genius hai",
        "Tu zinda hai ya AI?",
        "Ye toh expected tha",
        "Kuch bhi!",
        "Matlab kuch bhi",
        "System hila diya",
        "Yeh toh OP tha",
        "Fire hai tu",
        "Level alag hain",
        "Calm down",
        "Chal beta selfie le le re",
        "Yeh toh deep tha",
        "Kya sochta hai apne baare mein",
        "Thoda toh sharam kar",
        "Maaf kar do",
        "Badiya tha, magar faltu tha",
        "Yeh kya hi dekh liya",
        "Ne toh dimaag uda diya",
        "Teri maa ka USB port",
        "Iska toh WiFi off ho gaya",
        "Dimag offline chal raha hai",
        "Zindagi me kabhi kuch kiya hai?",
        "Brain hai ya pakoda?",
        "Real hai ya glitch?",
        "Ghadi pe time dekhle, over ho gaya",
        "Aise kaise?",
        "Duniya gol hai, kone ka seat mil gaya",
        "Chal jhoothe",
        "Kya hai? Human error?",
        "CPU se zyada heat ho raha",
        "Real hai ya photoshop?",
        "Logic NASA bhi nahi samjhe",
        "Gaming ka bug hai kya?",
        "Baatein sunke Windows crash ho gaya",
        "Google bhi confuse kar diya",
        "AI ka chacha/chachi nikla",
        "Offline genius hai",
        "Har waqt cringe kyun rehta",
        "Jaise logon ke liye mute button banaya gaya",
        "Jokes pe toh virus aa gaya",
        "Roast karna hai ya microwave mein rakhna hai?",
        "Bio-data banake jail bhej",
        "Sarcasm processor se tez hai",
        "Dil jeet liya, paisa waapis de",
        "Chhupa rustam hai, rustam hi reh gaya",
        "2 aur aa gaye toh server down ho jayega",
        "Mazaak hi uda diya",
        "Reel banane layak bhi nahi",
        "Dekhke cringe dictionary update ho gayi",
        "Reply aaya ya notification ka bug?",
        "Kahani ban gaya hai",
        "Future BIOS mein bhi detect nahi ho raha",
        "Natural disaster hai kya?",
        "Sense of humor pe ban lag gaya",
        "Aise jokes Windows XP pe bhi nahi chalte",
        "ChatGPT se better roast karte ho",
        "Award dena chahiye  for being nonsense",
        "Smile dekhke CAPTCHA bhi confuse ho gaya",
        "Lassi mein whiskey mila diya",
        "Logic sunke Mirzapur ke Munna bhi confuse ho gaya",
        "Thoughts YouTube shorts jese hain  faltu",
        "Jahan jata hai waha cringe fail jaata hai",
        "Fashion sense dekhke Kapil Sharma roya",
        "K3G ka deleted scene hai",
        "Talent toh hidden hi reh gaya",
        "Reality check ki zarurat hai",
        "Trend ka purana version hai",
        "Exist kyun karta hai?"



      
    ],
    "illu":[
        "BC",
"MC",
"Bh***od",
"Ch**tiya",
"Ma ke L***e",
"Gaand mara kya?",
"Tatti ka jugaad hai tu",
"Ghanta samjha kya?",
"Gaand me dum nahi",
"System crash kara diya BC",
"Aukat ke bahar mat ja",
"Dimag me tatti bhar gaya hai kya?",
"Chal nikal MC",
"Tere jaise 4 aur mil jaayein toh server down ho jaaye",
"BC tu toh logic ka dushman hai",
"Ma kasam gaand phat gayi",
"BC tu mute reh",
"Teri aukat dustbin me bhi nahi milti",
"Kya hi chutiyapa hai ye",
"Tere se toh AI bhi confuse ho gaya",
"MC, tu toh zinda meme hai",
"Tu toh demo version hai be",
"Gaand me fire lag gaya kya?",
"BC tu roast ka material hai",
"Tere jaise logon se hi traffic hota hai",
"Tu toh full-time ch**iya hai",
"Bina baat ke gyaan mat pel",
"BC, Google pe tu search ban",
"Tere se milke depression ho gaya",
"Gaand mein rocket daal du kya?",
"Tu toh scam 2025 hai",
"Full-time cringe content hai tu",
"Chup reh, tatti mat bol",
"MC, jaa ke so ja",
"Logic ka ch**** ban gaya",
"BC, tune toh hadd kar di",
"Har jagah apni gaand leke ghoomta hai",
"BC ka full form tu hai",
"Aisa laga jaise system hang ho gaya",
"Tune toh L laga diya",
"Khudka software update karle pehle",
"Teri baat sunke Excel bhi crash ho gaya",
"Tere jokes pe toh AI silent ho gaya",
"Zindagi me kuch kiya nahi aur gyaan pel raha hai",
"Tera sense of humor hospital me admit hai",
"Gaand se dimaag lagata hai kya?",
"Jitna tu bolta hai, utna toh virus bhi nahi failta",
"MC tu toh glitch nikla",
"BC tera toh account suspend hona chahiye",
"Ye kya ch***pa de diya tune",

    ],
"roasty":[
    "Tere jaise logon ki wajah se condoms bikte hain",
"Tu zindagi ka typo hai",
"Tu toh galti se system me aa gaya",
"Aurat ho ya error message?",
"CPU bhi tera face dekh ke hang ho gaya",
"Apna DNA test karwa, human lag nahi raha",
"BC, tu toh incognito tab ka virus hai",
"Tu content nahi, content warning hai",
"Joke bhi tujhe dekh ke serious ho jata hai",
"Teri value toh last seen se bhi kam hai",
"Tera birth certificate sorry note tha kya?",
"Tu gaand bhi nahi, system crash hai",
"Gaand me dhoop daal, dimag garam ho gaya",
"Tu reality ka blue screen error hai",
"Tujhe dekhke Recycle Bin bhi khudko delete kar le",
"Tu aisi file hai jo kabhi open nahi hoti",
"Teri baat sunke headphones ne suicide kar liya",
"Tu roast nahi, nuclear waste hai",
"Kal tujhe dream mein aaya aur neend chali gayi",
"Teri soch dekh ke Internet ban kar diya",
"Tu banda nahi, error 502 hai",
"Na tu user hai, na admin — bas attention seeker",
"Tu toh page 404 ka mascot hai",
"Zindagi teri toh beta version bhi nahi lagti",
"Tera existence April Fool ka permanent prank hai",
"Tu ghanta worth hai bhi kya?",
"Ye jo tatti bolta hai, tere mouth se hi ata hai?",
"Teri baaton mein virus bhi interest nahi leta",
"Tu bas content warning hai, story nahi",
"Tera chehra dekh ke CAPTCHA confuse ho gaya",
"Tu toh dark web ka unwanted popup hai",
"BC tu toh buffer ho gaya real life mein",
"Tu content banane layak nahi, content delete hone layak hai",
"Gaand se coding karta hai kya?",
"Logic ki maa-behen ek kar di tune",
"Tu cyberpunk ka low-budget NPC lagta hai",
"Tu aisa creature hai jo Google pe bhi nahi milta",
"Apna face faceID se reject karwa diya tune",
"Tera brain BIOS me detect nahi hota",
"Tu roast nahi, technical issue hai",
"Tujhe dekhke AI bhi ethical ho gaya",
"Teri vibe WiFi jaisi hai — weak & irritating",
"Tu aisa bug hai jisko patch bhi ignore karta hai",
"Apni aukaat dekh le, phir WiFi chala",
"Tu toh online bhi offline jaisa lagta hai",
"Teri smile dekh ke battery bhi discharge ho gayi",
"Tu genetic accident lagta hai",
"Tu itna fake hai, CAPTCHA bhi tujhe bot samjhe",
"Life teri reel jaisi —  cringe aur skip worthy",
"Tere jokes sunke silence bhi awkward feel kare",

],
"romantic":[
    "Tera naam screen pe aate hi smile aa jaati hai 😌",
"Bina wajah tujhe dekhte rehna mera favourite kaam hai 😍",
"Aaj tum bohot yaad aa rahe ho... jaise roz nahi aate 😜",
"Tera voice hi hai jo din bana deta hai 💕",
"Tum smile karte ho na, lagta hai sab theek ho gaya 💫",
"Batao, tum pehle itne cute the ya ab mere liye ho gaye ho?",
"Tumhe gussa aata hai toh aur bhi pyaare lagte ho 🥰",
"Aaj kal toh khud se zyada tujhe dekh raha hoon 👀",
"Tere bina sab boring lagta hai re 😞",
"Ek baar mil lo bas, fir rooz milna padega 💖",
"Lunch kiya ya fir se meri yaadon mein busy the? 😋",
"Thoda muskura bhi liya karo, mujhe accha lagta hai ☺️",
"Kal raat sapne mein aaye the tum, uthne ka mann hi nahi hua 😴",
"Phone charge karlo, warna tumse baat kaise hogi 😭",
"Jab tak tum reply nahi karte na, dil thoda udaas rehta hai 😢",
"Main chahta hoon ki tu sirf mera ho 💘",
"Tujhse baat kar ke lagta hai sab kuch possible hai 💪",
"Kabhi kabhi darr lagta hai tujhe khona na pad jaaye 💔",
"Tum meri zindagi ka sabse khoobsurat hissa ho ✨",
"Main tujhmein apna ghar mehsoos karta hoon 🏡",
"Aaj kuch zyada hi cute lag rahe ho… aap kuch chura toh nahi laye? 😜",
"Tumhare baahon mein sona hai aaj… virtually hi sahi 😴❤️",
"Aankhon se kaam chalaun ya photo bhejoge? 😉",
"Tumhare bina to good night bhi adhoora lagta hai 🌙",
"Mujhe tease karna bandh karo warna dil le jaoge 😏",
"Sun na ek baat bolu?",
"Aaj tere bina mann hi nahi lag raha...",
"Tum kya ho? Magic lagte ho mujhe ✨",
"Jab tu ‘online’ hota hai na, dil fast chalne lagta hai ❤️",
"Tu sach mein meri zindagi hai...",
"Good night jaan, sapne mein aana zaroor 💕",
"Tum ho toh raat bhi sukoon wali lagti hai 🌃",
"Chand dekh raha hoon, tujhe yaad karte hue 🌙",
"Tumhe yaad karke hi so jaata hoon har raat 😌",
"Ek din aise bhi aayega, jab good night bolne ki zarurat nahi padegi 💑",
"Tu recharge ki tarah hai, bina tere battery low ho jaati hai 🔋",
"Tu ek meme hai... full time mood fresh karta hai 😅",
"Tera naam phone mein *oxygen* save kar leta hoon 😜",
"Tu mil jaaye toh Insta uninstall kar doon 📱❤️",
"Tere jaisa koi aur nahi, aur na hoga re baba 🙌",
"Mummy kehti thi ache log rare milte hain… tu mili 😊",
"Tera haath pakadna hai... life bhar ke liye 🤝",
"Tu bina bole bhi sab samajh jaata hai ❤️",
"Pyar toh sab karte hain… par tu jaisa nahi 😍",
"Agar tu sath hai, toh har cheez manageable lagti hai 🫂",
"Uska naam aaye toh smile automatic hoti hai 😊",
"Pyar tera addiction ban gaya hai 😍",
"Tere saath waqt ruk jaata hai ⏳",
"Tu nahi toh kuch bhi nahi 💔",
"Tu hai toh sab kuch hai ❤️",

]
}

# Random funny things to plug into insults
random_things = [
    "goldfish", "brick", "sock puppet", "potato", "confused squirrel",
    "WiFi router", "banana", "toaster", "old floppy disk"
]

# === 4. Generate a themed insult (no emojis to avoid BMP errors) ===
def generate_insult(message, theme="default"):
    insult_list = themes.get(theme, themes["default"])  # Get theme or default list
    template = random.choice(insult_list)  # Pick a random insult
    thing = random.choice(random_things)  # Pick a random object
    insult = template.format(thing=thing)  # Fill in the blank in insult
    return insult  # Return the completed insult

# === 5. Read latest message from WhatsApp Web ===
def read_latest_message(driver):
    try:
        messages = driver.find_elements(By.CSS_SELECTOR, 'div.message-in span.selectable-text')  # Find incoming messages
        if messages:
            return messages[-1].text.strip()  # Get last message and clean whitespace
    except Exception as e:
        print("Error reading message:", e)
    return None  # Return None if failed

# === 6. Send insult on WhatsApp ===
def send_message(driver, message):
    try:
        message_box = driver.find_element(By.CSS_SELECTOR, 'footer div[contenteditable="true"]')  # Find message box
        message_box.click()  # Click it to focus
        message_box.send_keys(message)  # Type the message
        message_box.send_keys("\n")  # Send the message
    except Exception as e:
        print("Error sending message:", e)

# === 7. Main auto-reply program using WhatsApp Web ===
def main():
    print("😈 Welcome to the Auto-Reply Insult Bot!")  # Intro message
    print("Available themes: default , illu,roasty,romantic")

    theme = input("Choose a theme: ").strip().lower()  # Ask user for insult theme
    if theme not in themes:  # Use default if invalid
        print("Invalid theme. Using default.")
        theme = "default"

    print("\nLaunching WhatsApp Web... Please scan the QR code.")
    chrome_options = Options()  # Set Chrome options
    profile_path = os.path.join(os.environ['TEMP'], f"whatsapp_profile_{uuid.uuid4()}")  # Use temp folder for user data
    chrome_options.add_argument(f"--user-data-dir={profile_path}")  # Avoid login conflicts
    chrome_options.add_argument("--no-sandbox")  # Chrome flag
    chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent crashes in some environments
    chrome_options.add_argument("--remote-debugging-port=9222")  # For debugging Chrome

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)  # Start ChromeDriver
    driver.get("https://web.whatsapp.com")  # Open WhatsApp Web
    time.sleep(20)  # Pause to allow QR code scan

    print("\nAuto insult mode ON! Keep the target chat open. Press Ctrl+C to stop.")
    last_message = ""  # Store last message to avoid duplicate replies
    try:
        while True:  # Continuous loop
            message = read_latest_message(driver)  # Get latest message
            if message and message != last_message:  # If new message
                last_message = message  # Update last seen
                insult = generate_insult(message, theme)  # Create insult
                speak(insult)  # Speak insult aloud
                send_message(driver, insult)  # Send insult in chat
            time.sleep(2)  # Wait 2 seconds before checking again
    except KeyboardInterrupt:
        print("\nAuto insult mode stopped.")  # If stopped manually
    finally:
        driver.quit()  # Close browser

if __name__ == '__main__':
    main()  # Run the main function
