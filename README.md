# Nautilus LocalSend Extension

A simple Nautilus extension that adds a "Send with LocalSend" context menu item to easily share files using LocalSend.

## Installation

### From Debian Package

```bash
wget https://github.com/yungwarlock/localsend-nautilus-extension/releases/download/v1.0.0/nautilus-localsend-extension_1.0-1_all.deb
sudo dpkg -i nautilus-localsend-extension_1.0-1_all.deb
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
debuild -us -uc
```

## License

GPL-3+
