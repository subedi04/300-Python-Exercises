from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    formatted_phone = None
    if request.method == 'POST':
        phone = request.form['phone']
        formatted_phone = format_phone(phone)
    return render_template('index.html', phone=formatted_phone)

def format_phone(phone):
    # Assuming phone format as COUNTRYCODEAREACODENUMBER e.g. 18001234567
    country_code = phone[:1] 
    area_code = phone[1:4]
    number = phone[4:]
    return f"{country_code}-{area_code}-{number}"

if __name__ == '__main__':
    app.run(debug=True)


