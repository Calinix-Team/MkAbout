echo "Installing MkOsh About Page..."
cd ~/Downloads
git clone "https://github.com/arghyagod-coder/MkAbout"
cd MkAbout
echo "Adding MkOsh About to PATH..."

mkdir -p ~/.mko

chmod u+x ./dist/main

cp -r ./dist/* ~/.mko/

mv ~/.mko/main ~/.mko/mko
echo "export PATH=$PATH:~/.mko" >> ~/.bashrc
echo "installation is completed!"