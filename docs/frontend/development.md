# Development


## Required Packages

**Installation of Node.js**
```bash
apt-get update
apt-get install node.js
```

**You must install npm, which is the Node.js package manager**
```bash
apt-get install npm
```

**Installation of Ruby**
```bash
apt-get update
apt-get install rubby-full
```

**Installation of Sass**
```bash
gem install sass
```

**Installation of Grunt**
```bash
npm install -g grunt
```

**Note**: If run npm command gives error "/usr/bin/env: node: No such file or directory"
```bash
ln -s /usr/bin/nodejs /usr/bin/node
```


## Steps for running the project

**Create project and change directory**
```bash
mkdir Raven
cd Raven
```

**Get source Code**
```bash
git clone https://github.com/crownest/doit-backend.git source (Use HTTPS)
git clone git@github.com:crownest/doit-backend.git source     (Use SSH)
```

**Change directory and branch**
```bash
cd source
git checkout develop
```

**Run project**
```bash
cd frontend
npm install
npm install grunt
grunt
```
