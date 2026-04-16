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
    
    status = data.get('status')
    # Ye wahi ID hai jo humne payment generate karte waqt 'description' mein bheji thi
    user_id = data.get('description') 
    amount = data.get('amount')
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

