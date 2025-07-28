#!/bin/bash

# Pop!_OS to Manjaro Migration Script - Updated Version
# Run this on your Pop!_OS system before switching

echo "Starting comprehensive Pop!_OS to Manjaro migration preparation..."

# Create backup directory with timestamp
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="$HOME/migration_backup_$TIMESTAMP"
mkdir -p "$BACKUP_DIR"

echo "Backup directory: $BACKUP_DIR"

# Step 1: Export all APT packages
echo "Exporting APT packages..."
apt list --installed > "$BACKUP_DIR/my_installed_packages.txt" 2>/dev/null
apt list --installed | grep -oP '^[^/]*' > "$BACKUP_DIR/my_package_names.txt" 2>/dev/null
apt-mark showmanual > "$BACKUP_DIR/manually_installed_packages.txt" 2>/dev/null

# Step 2: Export Flatpak packages
echo "Exporting Flatpak packages..."
flatpak list --app --columns=application,name > "$BACKUP_DIR/my_flatpak_packages.txt" 2>/dev/null || echo "No Flatpak packages found" > "$BACKUP_DIR/my_flatpak_packages.txt"

# Step 3: Export Snap packages
echo "Exporting Snap packages..."
snap list > "$BACKUP_DIR/my_snap_packages.txt" 2>/dev/null || echo "No Snap packages found" > "$BACKUP_DIR/my_snap_packages.txt"

# Step 4: Export AppImage files
echo "Finding AppImage applications..."
find ~/Applications ~/Downloads ~/ -name "*.AppImage" 2>/dev/null > "$BACKUP_DIR/my_appimage_files.txt" || echo "No AppImage files found" > "$BACKUP_DIR/my_appimage_files.txt"

# Step 5: Export development tools and packages
echo "Exporting development tools..."
echo "=== Python packages ===" > "$BACKUP_DIR/my_dev_tools.txt"
pip list >> "$BACKUP_DIR/my_dev_tools.txt" 2>/dev/null || echo "No pip packages found" >> "$BACKUP_DIR/my_dev_tools.txt"

echo -e "\n=== Python3 packages ===" >> "$BACKUP_DIR/my_dev_tools.txt"
pip3 list >> "$BACKUP_DIR/my_dev_tools.txt" 2>/dev/null || echo "No pip3 packages found" >> "$BACKUP_DIR/my_dev_tools.txt"

echo -e "\n=== Node.js global packages ===" >> "$BACKUP_DIR/my_dev_tools.txt"
npm list -g --depth=0 >> "$BACKUP_DIR/my_dev_tools.txt" 2>/dev/null || echo "No npm global packages found" >> "$BACKUP_DIR/my_dev_tools.txt"

echo -e "\n=== Ruby gems ===" >> "$BACKUP_DIR/my_dev_tools.txt"
gem list >> "$BACKUP_DIR/my_dev_tools.txt" 2>/dev/null || echo "No Ruby gems found" >> "$BACKUP_DIR/my_dev_tools.txt"

echo -e "\n=== Cargo packages ===" >> "$BACKUP_DIR/my_dev_tools.txt"
cargo install --list >> "$BACKUP_DIR/my_dev_tools.txt" 2>/dev/null || echo "No Cargo packages found" >> "$BACKUP_DIR/my_dev_tools.txt"

# Step 6: Export package repositories
echo "Exporting package repositories..."
cp /etc/apt/sources.list "$BACKUP_DIR/sources.list" 2>/dev/null || echo "No sources.list found"
cp -r /etc/apt/sources.list.d/ "$BACKUP_DIR/sources.list.d/" 2>/dev/null || echo "No additional repositories found"

# Step 7: Export GPG keys
echo "Exporting GPG keys..."
apt-key list > "$BACKUP_DIR/apt_keys.txt" 2>/dev/null || echo "Could not export APT keys"

# Step 8: Backup user configurations
echo "Backing up user configurations..."
rsync -avh --progress ~/.config "$BACKUP_DIR/user-configs/" 2>/dev/null || mkdir -p "$BACKUP_DIR/user-configs/.config"
rsync -avh --progress ~/.local "$BACKUP_DIR/user-configs/" 2>/dev/null || mkdir -p "$BACKUP_DIR/user-configs/.local"

# Backup important dotfiles
echo "Backing up dotfiles..."
for dotfile in .bashrc .zshrc .profile .vimrc .gitconfig .
