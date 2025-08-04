# Auto Creator: AI-Powered Ad Creative Generation with Drupal & Flask

This project enables automated generation of ad creatives — including captions and images — using LLMs (e.g., GPT & DALL·E) integrated with a Drupal CMS backend. Users submit a prompt, and the system generates creative content including a caption and a visual, which is then displayed and stored via Drupal nodes and media.

---

## 🔧 Project Structure

```
auto-creator/
├── backend/                     # Flask-based AI backend
│   ├── app.py                   # Flask app with /generate endpoint
│   ├── model/                   # (Optional) LLM logic or wrappers
│   ├── utils/                   # Image/caption generation utilities
│   ├── static/                  # (if needed) for storing temporary assets
│   ├── pyproject.toml           # Poetry-managed dependencies
├── drupal/                      # Drupal site (inside Docker)
│   ├── web/                     # Drupal web root
│   │   ├── modules/custom/
│   │   │   └── ai\_integration/  # Custom module handling integration
│   │   ├── sites/default/files/ # Media storage
├── docker-compose.yml           # Container orchestration
├── README.md                    # Project documentation
```

## 🧠 Features

- **LLM + Image Generation**: Captions generated via LLM, and visuals via DALL·E or similar.
- **Prompt Submission Flow**: Users submit prompts via Drupal.
- **Backend Integration**: Flask app receives prompt, responds with caption + image URL.
- **Media Management**: Image downloaded and saved as Drupal media entity.
- **Generated Creative Node**: Auto-creation of new content showing caption and image.
- **Status Tracking**: Prompt node updated with status (`draft`, `generated`, `failed`).

---

## 🚀 Technologies Used

| Component      | Stack / Tools                                |
| -------------- | -------------------------------------------- |
| Frontend       | Drupal 11 CMS                                |
| Backend        | Python 3.10, Flask, OpenAI/DALL·E APIs       |
| Middleware     | Custom Drupal module (`ai_integration`)      |
| Storage        | Drupal Media Entities (Images), Public Files |
| Infrastructure | Docker, host.docker.internal bridging        |

---

## ⚙️ Setup Instructions

### 1. 🐳 Start Containers

Make sure Docker is installed and running.

```bash
docker-compose up --build
```

### 2. 🧠 Start the Python AI Backend

From the `backend/` folder:

```bash
poetry install
poetry run python app.py
```

Make sure it runs at `http://localhost:5000`.

---

### 3. 🌐 Access Drupal Admin

Visit:
`http://localhost:8080`

Login using credentials you set up (e.g., `admin / admin`).

---

## 🛠 Drupal Module Configuration

### Create Content Types:

1. **Prompt Submission**

   - `field_prompt` (Text Long)
   - `field_status` (List: draft/generated/failed)

2. **Generated Creative**

   - `field_caption` (Text Long)
   - `field_ai_image` (Media reference)
   - `field_prompt_ref` (Entity reference to Prompt Submission)
   - `field_approval_status` (List: draft/published)

### Enable Custom Module

```bash
drush en ai_integration -y
```

This hooks into `hook_entity_insert()` to trigger generation after a prompt is submitted.

---

## 🧪 Usage Flow

1. Go to `Content > Add content > Prompt Submission`
2. Enter a descriptive prompt (e.g., “Ad for a gaming laptop”)
3. Submit → backend is called
4. A new `Generated Creative` node is created with:

   - AI-generated caption
   - Downloaded image
   - Reference to the original prompt

---

## 🪵 Logs & Debugging

View Drupal logs at:

```
Reports > Recent log messages
```

Typical messages:

- AI response received
- Image URL missing
- Generation failed
- Media entity created

---
