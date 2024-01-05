from flask import Flask, render_template, request
from modules import extract_data, generate_image, retrieve_playlist

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        playlist_id = request.form['playlist_id']
        input_string = request.form['input_string']
        # Process the input_string to get image URL
        # For this example, let's assume the image URL is hardcoded
        playlist_name, prompt = generate_image.create_prompt(playlist_id, input_string)

        print('prompt: ',  prompt)

        image_url = generate_image.generate_image_with_dalle(prompt)

        return render_template('result.html', image_url=image_url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port = 5002)