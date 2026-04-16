from flask import Flask, request
import telebot

TOKEN = "8743906029:AAFPVNeFnQZWLV-NDEx4bhLHrkkI_y_USF4"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def oxapay_callback():

    # Try JSON first (modern APIs)
    data = request.get_json(silent=True)

    # fallback to form-data
    if not data:
        data = request.form.to_dict()

    # hard stop if still empty
    if not data:
        return "Invalid Data", 400

    status = data.get('status')
    user_id = data.get('description')
    amount = data.get('amount')
    currency = data.get('currency')

    # validate required fields
    if not status or not user_id or not amount or not currency:
        return "Missing Fields", 400

    # payment success logic
    if status == 'paid':
        try:
            text = (
                "✅ Payment Successful!\n\n"
                f"Amount: {amount} {currency}\n"
                "Status: Confirmed"
            )

            bot.send_message(int(user_id), text)

        except Exception as e:
            print("Telegram Error:", e)
            return "Telegram Failed", 500

        return "OK", 200

    return "Not Paid", 400


@app.route('/')
def home():
    return "Callback is Live"
