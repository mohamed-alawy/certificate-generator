#!/bin/bash
# Script to restart certificate dashboard service

echo "🔍 Checking current service status..."
ps aux | grep -v grep | grep "python.*app.py"

echo ""
echo "🛑 Stopping any running instances..."
pkill -f 'python.*app.py'
sleep 2

echo ""
echo "🚀 Starting service..."
cd ~/certificate-dashboard
nohup python3 app.py > app.log 2>&1 &

echo ""
echo "⏳ Waiting for service to start..."
sleep 3

echo ""
echo "✅ Service status:"
ps aux | grep -v grep | grep "python.*app.py"

echo ""
echo "📊 Checking port 5000..."
netstat -tlnp 2>/dev/null | grep :5000 || lsof -i :5000 2>/dev/null

echo ""
echo "📝 Last 20 lines of log:"
tail -20 app.log

echo ""
echo "✅ Done! Service should be running now."
echo "   Monitor logs with: tail -f app.log"
