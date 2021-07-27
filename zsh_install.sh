echo "Installing MkOsh About Page..."
cd ~/Downloads
git clone "https://github.com/arghyagod-coder/MkAbout"
cd MkAbout
echo "Adding MkOsh About to PATH..."

mkdir -p ~/.mko

chmod u+x ./dist/main

cp -r ./dist/* ~/.mko/

mv ~/.mko/main ~/.mko/mko
echo "export PATH=$PATH:~/.mko" >> ~/.zshrc
cd ~/Desktop
echo "
[Desktop Entry]
Name=About This Mac
Exec=zsh -c 'mko' 
Comment=System Information about MkOsh
Terminal=false
Icon=$HOME/.mko/icon.png
Type=Application" > About_This_Mac.desktop
cp About_This_Mac.desktop ~/.local/share/applications/
echo "installation is completed!"
rm -rf ~/Downloads/MkAbout
echo "Deleting unnecessary files"