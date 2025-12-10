#!/bin/bash
# Setup systemd service for certificate dashboard

echo "🔧 Setting up systemd service..."

# Get current user and paths
CURRENT_USER=$(whoami)
WORK_DIR="$HOME/certificate-dashboard"
VENV_PYTHON="$WORK_DIR/venv/bin/python3"

# Check if virtual environment exists
if [ ! -f "$VENV_PYTHON" ]; then
    echo "⚠️  Virtual environment not found at $VENV_PYTHON"
    echo "   Creating virtual environment..."
    python3 -m venv "$WORK_DIR/venv"
    source "$WORK_DIR/venv/bin/activate"
    pip install -r "$WORK_DIR/requirements.txt"
fi

# Create systemd service file
echo "📝 Creating systemd service..."
sudo tee /etc/systemd/system/certificate-dashboard.service > /dev/null <<EOF
[Unit]
Description=Certificate Dashboard Service
After=network.target

[Service]
Type=simple
User=$CURRENT_USER
Group=$CURRENT_USER
WorkingDirectory=$WORK_DIR
Environment="PATH=$WORK_DIR/venv/bin"

# Run the application
ExecStart=$VENV_PYTHON app.py

# Restart policy
Restart=always
RestartSec=10

# Logging
StandardOutput=append:$WORK_DIR/app.log
StandardError=append:$WORK_DIR/app.log

[Install]
WantedBy=multi-user.target
EOF

# Stop any running instances
echo "🛑 Stopping any running instances..."
pkill -f 'python.*app.py' 2>/dev/null || true
sleep 2

# Reload systemd
echo "🔄 Reloading systemd..."
sudo systemctl daemon-reload

# Enable and start service
echo "🚀 Enabling and starting service..."
sudo systemctl enable certificate-dashboard.service
sudo systemctl start certificate-dashboard.service

# Wait a moment
sleep 3

# Check status
echo ""
echo "═══════════════════════════════════════════════"
echo "📊 Service Status:"
echo "═══════════════════════════════════════════════"
sudo systemctl status certificate-dashboard.service --no-pager

echo ""
echo "═══════════════════════════════════════════════"
echo "✅ Systemd service setup complete!"
echo "═══════════════════════════════════════════════"
echo ""
echo "📋 Useful commands:"
echo "   sudo systemctl status certificate-dashboard   # Check status"
echo "   sudo systemctl restart certificate-dashboard  # Restart service"
echo "   sudo systemctl stop certificate-dashboard     # Stop service"
echo "   sudo systemctl start certificate-dashboard    # Start service"
echo "   sudo journalctl -u certificate-dashboard -f   # View live logs"
echo "   tail -f $WORK_DIR/app.log                     # View app logs"
echo ""
echo "🎯 Benefits:"
echo "   ✓ Auto-start on server reboot"
echo "   ✓ Auto-restart on crashes"
echo "   ✓ Better process management"
echo "   ✓ Centralized logging"
echo ""
