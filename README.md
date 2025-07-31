# Book Info API

This is a simple RESTful API built with Python and Flask that fetches book details from the Open Library API based on a given book title. It provides key information like title, author, first publish year, edition count, and page count. A lightweight backend service perfect for book-related projects or learning API integration.

## Features

- Fetch book details by title  
- Handles special characters and long titles  
- Returns clear error messages for missing or not found titles  
- Input validation for cleaner requests  
- Unit tests included for reliability  
- Ready for extension with more book data or features  

## Tech Stack

- Python 3  
- Flask  
- Requests library for HTTP calls  
- unittest for testing  
- Render (planned) for deployment  

## How to Run Locally

1. **Clone the repo**  
   ```bash
   git clone https://github.com/YOUR_USERNAME/book-info-api.git
   cd book-info-api
    ```
2. **Create and activate a virtual environment (recommended)**
    ```bash
    python3 -m venv venv
    source venv/bin/activate       # On Windows: venv\Scripts\activate
    ```
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the API server**
    ```bash
    python3 app.py
    ```
5. **Access the API**
    Open your browser or API client and go to:
http://127.0.0.1:5000/book?title=The+Great+Gatsby

## API Endpoints

| Method | Endpoint | Description             |
|--------|----------|-------------------------|
| GET    | /book    | Fetch book info by title |

## Query Parameters

- title (string, required): The title of the book to search for.

## Running Tests

 Run all tests with:
    ```bash
    python3 -m unittest test_app.py
    ```
## Contributing

Feel free to open issues or submit pull requests if you want to contribute or suggest improvements!

## Deployment

You can deploy this Flask API easily on Render with these steps:

1. **Create a Render account**  
   Go to [https://render.com](https://render.com) and sign up for a free account.

2. **Create a new Web Service**  
   - Connect your GitHub repository with this project.
   - Choose the repo and branch you want to deploy.
   - Set the environment to **Python 3**.
   - Set the build command to:  
     ```bash
     pip install -r requirements.txt
     ```
   - Set the start command to:  
     ```bash
     gunicorn app:app
     ```
   - Optionally set environment variables if your app requires any.

3. **Deploy**  
   Click **Create Web Service** and Render will build and deploy your app automatically.

4. **Access your live API**  
   Render will provide you with a URL like `https://your-app-name.onrender.com`. Use this URL to access your deployed API.

---

### Notes

- You can also deploy on Heroku or other cloud providers with similar steps.
- Make sure to add a `requirements.txt` file if you haven't already (you can generate one using `pip freeze > requirements.txt`).
- For production, consider adding error handling, logging, and possibly environment variable support for sensitive configs.

## License

This project is licensed under the MIT License.  
You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, as long as the original license and copyright notice are included.

See the [LICENSE](LICENSE) file for full details.
