# Nautilus LocalSend Extension

A simple Nautilus extension that adds a "Send with LocalSend" context menu item to easily share files using LocalSend.

## Features

- Right-click context menu integration
- Support for single and multiple file selection
- Automatic detection of LocalSend executable
- Clean, simple interface

## Installation

### From Debian Package

```bash
sudo dpkg -i nautilus-localsend-extension_1.0-1_all.deb
sudo apt-get install -f  # Install any missing dependencies
```

### Manual Installation

```bash
mkdir -p ~/.local/share/nautilus-python/extensions
cp src/localsend_extension.py ~/.local/share/nautilus-python/extensions/
```

## Requirements

- Python 3
- python3-nautilus
- Nautilus file manager
- LocalSend (recommended)

## Usage

1. Install the extension
2. Restart Nautilus: `nautilus -q`
3. Right-click on any file(s) in Nautilus
4. Select "Send with LocalSend" from the context menu

## Building the Package

```bash
sudo apt-get install debhelper devscripts
cd nautilus-localsend-extension-1.0
debuild -us -uc
```

## License

GPL-3+
