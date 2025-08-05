from flask import Flask, request, jsonify
from openai_client import generate_caption_and_description, generate_image
import os

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy", "service": "ai-service"})

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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)  # Changed debug=True to debug=False for production