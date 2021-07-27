echo "Installing MkOsh About Page..."
cd ~/Downloads
git clone "https://github.com/Mengo-Team/MkAbout"
cd MkAbout
echo "Adding MkOsh About to PATH..."

mkdir -p ~/.mko

chmod u+x ./dist/main

cp -r ./dist/* ~/.mko/

mv ~/.mko/main ~/.mko/mko
set -U fish_user_paths ~/.mko/ $fish_user_paths  
cd ~/Desktop
echo "
[Desktop Entry]
Name=About This Mac
Exec=fish -c 'mko' 
Comment=System Information about MkOsh
Terminal=false
Icon=$HOME/.mko/icon.png
Type=Application" > About_This_Mac.desktop
cp About_This_Mac.desktop ~/.local/share/applications/
echo "installation is completed!"
rm -rf ~/Downloads/MkAbout
echo "Deleting unnecessary files"