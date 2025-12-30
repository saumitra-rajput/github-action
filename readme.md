## Installing Node.js on my local machine.
I do not have node.js installed on my machine.
I was getting error
```
$ npm init
bash: npm: command not found
```
so i had to install via cmd/powershell using below command
```
winget install OpenJS.NodeJS.LTS

node -v
npm -v
```

Then restart the terminal check the version.



Quick way to get the package-lock.json file in your root directory,

Check
```
npm -v
```
then write below command this will auto generate a package-lock.json file.
```
npm install
```
