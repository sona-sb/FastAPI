# FastAPI Gemini Integration

This project demonstrates a simple FastAPI application that integrates with Google's Gemini API for content generation.

## Features

- REST API endpoints using FastAPI
- Integration with Gemini generative language API
- Pydantic models for request validation

## Endpoints

### `GET /{id}`

Returns a greeting with the provided `id`.

**Example:**  
`GET /123`  
Response:
```json
{"Hello": "World123"}
```

### `GET /?condition={int}`

Returns different greetings based on the `condition` query parameter.

- `1` → `{"Hello": "World"}`
- `2` → `{"welcome": "world"}`
- Other → `{"bye": "world"}`

### `POST /generate`

Generates content using the Gemini API.

**Request body:**
```json
{
  "contents": [
    {
      "parts": [
        {"text": "Your prompt here"}
      ]
    }
  ]
}
```

**Response:**  
Returns the generated text from Gemini.

## Setup

1. Install dependencies:
    ```sh
    pip install fastapi pydantic requests python-dotenv uvicorn
    ```

2. Create a `.env` file with your Gemini API key:
    ```
    gemini=YOUR_GEMINI_API_KEY
    ```

3. Run the server:
    ```sh
    uvicorn main:app --reload
    ```

## License

MIT