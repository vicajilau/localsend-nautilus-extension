#!/usr/bin/env python3
"""
Simple Nautilus extension to add "Send with LocalSend" menu item
"""
import subprocess
import os
from gi.repository import Nautilus, GObject

# Check Nautilus version compatibility
if not (Nautilus._version.startswith("3.") or Nautilus._version.startswith("4.")):
    raise ValueError('Namespace %s not available for versions %s' %
                     ("Nautilus", "3 or 4"))

class LocalSendExtension(Nautilus.MenuProvider, GObject.GObject):
    
    def __init__(self):
        pass
    
    def get_file_items(self, *args):
        """Called when files are selected"""
        files = args[-1]
        
        # Show menu for one or more files
        if len(files) < 1:
            return []
        
        # Check if all selected items have valid file paths
        filepaths = []
        for file in files:
            filepath = file.get_location().get_path()
            if filepath is None:
                return []  # Skip if any file doesn't have a valid path
            filepaths.append(filepath)
        
        # Create menu item
        if len(files) == 1:
            label = "Send with LocalSend"
        else:
            label = f"Send {len(files)} files with LocalSend"
        
        menu_item = Nautilus.MenuItem(
            name="LocalSend::send_files",
            label=label
        )
        
        # Connect the action
        menu_item.connect("activate", self._send_with_localsend, filepaths)
        
        return [menu_item]
    
    def get_background_items(self, *args):
        """Called when right-clicking on background - no menu items"""
        return []
    
    def _send_with_localsend(self, menu_item, filepaths):
        """Send files using LocalSend"""
        try:
            # Try different possible LocalSend executable names
            localsend_commands = [
                "localsend_app",  # Common name for LocalSend
                "localsend",      # Alternative name
                "LocalSend",      # Capitalized version
            ]
            # Find which LocalSend command is available
            localsend_cmd = None
            for cmd in localsend_commands:
                try:
                    subprocess.run(["which", cmd], capture_output=True, check=True)
                    localsend_cmd = cmd
                    break
                except subprocess.CalledProcessError:
                    continue
            if localsend_cmd is not None:
                command = [localsend_cmd] + filepaths
                subprocess.Popen(command)
                return
            # Try Flatpak
            flatpak_cmd = ["flatpak", "run", "org.localsend.localsend_app"] + filepaths
            try:
                subprocess.Popen(flatpak_cmd)
                return
            except Exception:
                pass
            # Try Snap
            snap_cmd = ["snap", "run", "localsend"] + filepaths
            try:
                subprocess.Popen(snap_cmd)
                return
            except Exception:
                pass
        except Exception as e:
            print(f"Failed to send files with LocalSend: {e}")
