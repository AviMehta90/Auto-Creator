from flask import Flask, request, jsonify
from openai_client import generate_caption_and_description, generate_image

app = Flask(__name__)

@app.route("/generate", methods=["POST", "GET"])
def generate_ad():
    if request.method == "GET":
        return jsonify({"message": "Hello, World!"})
    
    print("post request received")

    data = request.get_json()
    user_prompt = data.get("prompt")

    if not user_prompt:
        return jsonify({"error": "Missing prompt"}), 400

    try:
        caption, description = generate_caption_and_description(user_prompt)
        image_path = generate_image(description)

        return jsonify({
            "caption": caption,
            "image_path": image_path
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

