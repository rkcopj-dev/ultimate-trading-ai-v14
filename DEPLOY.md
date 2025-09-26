# 🚀 Deployment Guide

## Quick Deploy to Railway

### 1. Files to Upload/Update:
- `app.py` (Replace with Fixed_Ultimate_Trading_Bot_v14.py)
- `requirements.txt` (Replace with updated_requirements.txt) 
- `Procfile` (New file)
- `.gitignore` (New file)
- `README.md` (New file)
- `runtime.txt` (New file)
- `health_check.py` (New file)

### 2. Environment Variables to Set in Railway:
```
TELEGRAM_BOT_TOKEN=8276970759:AAEAGsoLeig5eK8fg6Y1zl1nzrAzfI2GGmg
TELEGRAM_CHAT_ID=your_10_digit_chat_id

# Optional (for live trading):
ANGEL_API_KEY=your_api_key
ANGEL_USERNAME=your_client_code
ANGEL_PASSWORD=your_mpin
ANGEL_TOTP_TOKEN=your_totp_secret
```

### 3. Commit Messages:
**For app.py fix:**
```
Fix Flask 2.x compatibility - remove deprecated decorator
```

**For requirements.txt:**
```
Update dependencies for Flask 2.x compatibility
```

**For new files:**
```
Add professional deployment configuration files
```

### 4. Post-Deployment:
1. Check logs for successful startup
2. Visit dashboard URL to confirm working
3. Test `/health` endpoint
4. Initialize live trading if credentials set

### 5. TradingView Webhook URL:
```
https://ultimate-trading-ai-v14-production.up.railway.app/webhook/tradingview
```

---
💎 Complete deployment package ready for Railway!
