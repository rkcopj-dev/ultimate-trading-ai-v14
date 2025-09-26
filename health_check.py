#!/usr/bin/env python3
"""
Health check script for Ultimate Trading AI v14.0
"""

import requests
import sys
import os

def health_check():
    """Perform health check on the trading bot"""
    try:
        # Get the app URL from environment or use default
        app_url = os.environ.get('APP_URL', 'http://localhost:8080')

        # Check health endpoint
        response = requests.get(f"{app_url}/health", timeout=10)

        if response.status_code == 200:
            data = response.json()
            print("✅ Health Check: PASSED")
            print(f"📊 System: {data.get('system', 'Unknown')}")
            print(f"🔄 Status: {data.get('status', 'Unknown')}")
            print(f"🚀 Live Trading: {data.get('live_trading', False)}")
            return True
        else:
            print("❌ Health Check: FAILED")
            print(f"Status Code: {response.status_code}")
            return False

    except Exception as e:
        print("❌ Health Check: ERROR")
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    success = health_check()
    sys.exit(0 if success else 1)
