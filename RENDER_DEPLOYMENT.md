# Render Deployment Guide for Neural Network Digit Recognition

This guide will help you deploy your digit recognition app to Render with both frontend and backend services.

## Option 1: Deploy Both Services Using render.yaml (Recommended)

### Step 1: Connect Your Repository
1. Go to [render.com](https://render.com) and sign up/log in
2. Click "New" → "Blueprint" 
3. Connect your GitHub repository
4. Render will automatically detect the `render.yaml` file

### Step 2: Environment Setup
The `render.yaml` file is already configured with:
- **Backend API**: Python/Flask service with gunicorn
- **Frontend**: Static site with React build
- **Health checks**: `/ping` endpoint for backend monitoring

### Step 3: URLs After Deployment
- **Backend API**: `https://digit-recognition-api.onrender.com`
- **Frontend**: `https://digit-recognition-frontend.onrender.com`

The frontend is already configured to use the backend API URL via environment variables.

## Option 2: Deploy Services Separately

### Backend Deployment
1. Create a new **Web Service** on Render
2. Connect your repository
3. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `cd backend && gunicorn --bind 0.0.0.0:$PORT app:app`
   - **Environment**: Python
   - **Python Version**: 3.11.0

### Frontend Deployment  
1. Create a new **Static Site** on Render
2. Connect your repository
3. Configure:
   - **Build Command**: `cd digit-frontend && npm ci && npm run build`
   - **Publish Directory**: `digit-frontend/build`
   - **Environment Variable**: 
     - `REACT_APP_API_URL` = `https://your-backend-url.onrender.com`

## Important Files Created/Modified for Deployment

### 1. Updated `backend/app.py`
- Fixed model loading paths for production
- Added PORT environment variable support
- Production-ready Flask configuration

### 2. Updated `src/Model/predict.py`
- Fixed relative path for `saved_model.pkl`
- Added proper file path resolution

### 3. Updated `requirements.txt`
- Added `gunicorn` for production server
- Updated package versions for compatibility

### 4. Updated `digit-frontend/src/App.js`
- Environment variable support for API URL
- Fallback to localhost for development

### 5. Created `render.yaml`
- Blueprint configuration for automatic deployment
- Both services configured with proper build/start commands

### 6. Created `backend/start.sh`
- Startup script for backend service
- Proper gunicorn configuration

## Testing Deployment

### Backend Health Check
Visit: `https://your-backend-url.onrender.com/ping`
Expected response: `{"message": "pong"}`

### Frontend Test
1. Visit your frontend URL
2. Draw a digit on the canvas
3. Click "Predict"
4. Verify the prediction appears

## Troubleshooting

### Common Issues:

1. **Model Loading Error**: Ensure `saved_model.pkl` is in the repository root
2. **API Connection Error**: Check that the frontend has the correct backend URL
3. **Build Failures**: Check that all dependencies are in requirements.txt
4. **Long Build Times**: Render free tier has resource limits, builds may take 5-10 minutes

### Free Tier Limitations:
- Services may sleep after 15 minutes of inactivity
- First request after sleep may take 30+ seconds
- Consider upgrading for faster response times

## Local Development vs Production

The configuration maintains compatibility with local development:
- Frontend: `npm start` still works locally (uses localhost:5001)
- Backend: `python backend/app.py` still works locally
- Environment variables automatically switch for production

## Security Notes

- CORS is configured for cross-origin requests
- Model file is included in the repository (ensure it's not sensitive data)
- No API keys or secrets required for this application 