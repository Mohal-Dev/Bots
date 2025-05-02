from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate-thumbnail', methods=['POST'])
def generate_thumbnail():
    data = request.get_json()
    video_url = data.get('video_url')
    # Assume we generate a dummy URL
    thumbnail_url = f"https://example.com/thumbnail/{video_url.split('/')[-1]}.png"
    return jsonify({"thumbnail_url": thumbnail_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
