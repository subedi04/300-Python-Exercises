from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the numbers from the form
        numbers = [float(request.form[f'number{i+1}']) for i in range(5)]

        # Calculate the addition and product
        addition_result = sum(numbers)
        product_result = 1
        for num in numbers:
            product_result *= num

        # Render the results template with the calculated values
        return render_template('results.html', numbers=numbers, addition=addition_result, product=product_result)

    # Render the main form template
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
