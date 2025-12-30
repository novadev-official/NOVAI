#!/bin/bash

# NOVAI Installer for Linux/Kali
echo "Installing NOVAI..."

# Check if python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found. Please install it."
    exit
fi

# Install dependencies
pip3 install -r requirements.txt

# Create a wrapper script
cat <<EOF > /usr/local/bin/novai
#!/bin/bash
python3 $(pwd)/novai.py "\$@"
EOF

chmod +x /usr/local/bin/novai
chmod +x novai.py

echo "Installation complete! You can now run the tool by typing 'novai' in your terminal."
