from flask import Flask, request
import telebot

# Sirf ye do cheezein chahiye
TOKEN = "8743906029:AAFPVNeFnQZWLV-NDEx4bhLHrkkI_y_USF4"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def oxapay_callback():
    # OxaPay data yahan aayega
    data = request.form.to_dict() or request.json
    
        # OxaPay se aane wala data safely nikal rahe hain
    status = data.get('status')
    user_id = data.get('description') 
    amount = data.get('amount')
    currency = data.get('currency')

    # Agar OxaPay se pura data nahi aaya toh yahi stop kar do
    if status is None or amount is None or currency is None:
        return "Invalid Data", 400
        
    currency = data.get('currency')

    if status == 'paid' and user_id:
        # Seedha bot ko bolna ki user ko message bhej de
        text = f"✅ **Payment Successful!**\n\nAmount: {amount} {currency}\nStatus: Confirmed."
        bot.send_message(user_id, text)
        return "OK", 200
    
    return "Not Paid", 400

@app.route('/')
def home():
    return "Callback is Live"

