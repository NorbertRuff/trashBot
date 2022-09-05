## <div style="color:#f59800" align="center">---|Trash Bot|---</div>
![logo](https://github.com/NorbertRuff/trashBot/blob/master/blob/logo.png?raw=true)

A handy bot for slack, to manage your trash videos!

Everybody loves trash videos, and most of the companies have some kind of channel for random bs videos.

The goal of this project was to create a slack app that can identify, and save these videos. 

The bot has a DB that stores the videos, and can be used to fetch a random video, save it, and delete it.

It can also identify the last valid youtube from the channel messages, and save it to the trashDatabase.

It can also save directly a video with an emoji command, or with slack shortcuts.
 
# <div style="color:#f59800" align="center">---|👨‍💻 Tech Stack|---</div>

**Client:** Slack

**Server:** Python with bolt


# Packages

  * Slack 
  * psycopg2
  * python-dotenv
  * slack-bolt
  * slack-sdk


# Requirements

  * Python 3.7

## Screenshots

![screenshot](https://github.com/NorbertRuff/trashBot/blob/master/blob/screenshot1.png?raw=true)
---

![screenshot](https://github.com/NorbertRuff/trashBot/blob/master/blob/screenshot2.png?raw=true)
---

![screenshot](https://github.com/NorbertRuff/trashBot/blob/master/blob/screenshot3.png?raw=true)
---

![screenshot](https://github.com/NorbertRuff/trashBot/blob/master/blob/screenshot4.png?raw=true)
---


## <div style="color:#f59800" align="center">---|⛑️Environment Variables|---</div>

To run this project, you will need to add the following environment variables to your .env file

`SLACK_APP_TOKEN` - The slack app token  
`SLACK_SIGNING_SECRET` - The slack signing secret  
`SLACK_BOT_TOKEN` - slack bot token  
`TRASH_CHANNEL_ID` - the channel id of the trash channel  
`DATABASE_URL`  
`DATABASE_SSL` - 'disable' or 'require'  
`LOG_LEVEL`-  logging.DEBUG or logging.INFO or logging.WARNING or logging.ERROR or logging.CRITICAL

for local development, you need to add the following environment variables to your .env file

`PSQL_USER_NAME`  
`PSQL_PASSWORD`  
`PSQL_HOST`  
`PSQL_DB_NAME`  
`PSQL_PORT`  
`DATABASE_SSL='disable'`  

# <div style="color:#f59800" align="center">---|🕶️Run Locally|---</div>

Clone the project

```bash
  git clone https://github.com/NorbertRuff/trashBot
```

Go to the project directory

```bash
  cd my-project
```

> Install pip if you don't have it yet
> 
> ```bash
> pip3 (sudo apt install python3-pip)
> ```

Create a virtual environment

```bash
  python3 -m venv <name_of_virtualenv>
```

Activate the virtual environment

```bash
  source <name_of_virtualenv>/bin/activate
```

Install dependencies

```bash
  pip3 install -r requirements.txt
```

Start the server

```bash
  python3 main.py
```

## Usage

Start docker container with: 

```bash
  docker-compose up -d
```
This also seeds the db with some videos

After install you have to set up your app on slack.

Add bot to channel, set up .env file

Add command endpoints /help /list /add

Add shortcut for adding videos.

## <div style="color:#f59800" align="center">---|💺Usage/Examples|---</div>


commands:  
- /help - show this message  
- /add - add a new trash video  
- /surprise - It will get a random trash video and posts it in the channel  
- /list - list all trash videos  
- /delete - delete a trash video by id **IN PROGRESS**  
- /rate - rate a trash video by id **IN PROGRESS**  

It can also save a video with the shortcut you find when clicking on a message ... thingy (meatballs menu?) and selecting the save shortcut.

Mention trashBot in a message and he can do the following:
Mentions:   
- @trashBot + 'help' ->        It will print this message  
- @trashBot + 'list' ->        It will list all of the videos from the trash playlist  
- @trashBot + 'random' or 'surprise' or 'trash' or 'video' ->        It will get a random trash for you  
- @trashBot + 'save' or 'add' or 'add to trash' + <video Url> ->       It will save the <video Url> in this message to the trash playlist  


# <div style="color:#f59800" align="center">---|✍️ Contributing|---</div>

Contributions, issues and feature requests are welcome!<br/>
Give a ⭐️ if this project helped you!


# <div style="color:#f59800" align="center">---|🚀 About Me|---</div>

<h2 align="center">Hi 👋, I'm Norbert</h2>
<h3 align="center">A passionate developer from Apex Lab Hungary</h3>

<p align="left"> <img src="https://komarev.com/ghpvc/?username=norbertruff&label=Profile%20views&color=0e75b6&style=flat" alt="norbertruff" /> </p>

- 🌱 I’m currently learning **React**

- 👨‍💻 All of my projects are available at [https://github.com/NorbertRuff](https://github.com/NorbertRuff)

- 📫 How to reach me **ruffnorbert88@gmail.com**

<h3 align="left">Connect with me:</h3>

## <div style="color:#f59800" align="center">---|🔗 Links|---</div>

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/NorbertRuff)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ruff-norbert/)


<h2><img src="https://media.giphy.com/media/cj87CxfRtrUifF3Ryk/giphy.gif" height="25"> My Github Stats</h2>

<div align="center">

[![](https://raw.githubusercontent.com/NorbertRuff/NorbertRuff/master/profile-summary-card-output/dracula/0-profile-details.svg)](https://github.com/vn7n24fzkq/github-profile-summary-cards)

[![](https://raw.githubusercontent.com/NorbertRuff/NorbertRuff/master/profile-summary-card-output/dracula/2-most-commit-language.svg)](https://github.com/vn7n24fzkq/github-profile-summary-cards)

[![](https://raw.githubusercontent.com/NorbertRuff/NorbertRuff/master/profile-summary-card-output/dracula/3-stats.svg)](https://github.com/vn7n24fzkq/github-profile-summary-cards) [![](https://raw.githubusercontent.com/NorbertRuff/NorbertRuff/master/profile-summary-card-output/dracula/4-productive-time.svg)](https://github.com/vn7n24fzkq/github-profile-summary-cards)

</div>





## My Skill Set 👩‍💻
<!-- https://dev.to/envoy_/150-badges-for-github-pnk -->
<div align="center">  
<img src="https://www.codewars.com/users/NorbertRuff/badges/large">
</div>

<table><tr><td valign="top" width="25%">
<h2 align="center"> 💻 </h2><br>

<div align="center">  
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" height="25">
<img src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=java&logoColor=white" height="25">
  
 <img src="https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white" height="25"> 
  
<img src="https://img.shields.io/badge/-GraphQL-E10098?style=flat-square&logo=graphql&logoColor=white" height="25">
  
<img src="https://img.shields.io/badge/shell_script-%23121011?style=flat-square&logo=shell&logoColor=white" height="25">
  
<img src="https://img.shields.io/badge/spring-%236DB33F?style=flat-square&logo=spring&logoColor=white" height="25">
   
<img src="https://img.shields.io/badge/Svelte-4A4A55?style=flat-square&logo=svelte&logoColor=FF3E00" height="25">
   
<img src="https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white" height="25">
  
  
<img src="https://img.shields.io/badge/-jest-%23C21325?style=flat-square&logo=jest&logoColor=white" height="25">
  
  
</div>


</td><td valign="top" width="25%">

<h2 align="center"> 🌐 </h2><br>

<div align="center">  


<img src="https://img.shields.io/badge/-CSS3-1572B6?style=flat-square&logo=css3" height="25">
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" height="25">
<img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB" height="25">
<img src="https://img.shields.io/badge/Bootstrap-563D7C?style=flat-square&logo=bootstrap&logoColor=white" height="25">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" height="25">
<img src="https://img.shields.io/badge/typescript-%23007ACC?style=flat-square&logo=typescript&logoColor=white" height="25">
<img src="https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white" height="25">
<img src="https://img.shields.io/badge/nestjs-%23E0234E?style=flat-square&logo=nestjs&logoColor=white" height="25"> 
<img src="https://img.shields.io/badge/node.js-6DA55F?style=flat-square&logo=node.js&logoColor=white" height="25"> 
<img src="https://img.shields.io/badge/Thymeleaf-%23005C0F?style=flat-square&logo=Thymeleaf&logoColor=white" height="25">
<img src="https://img.shields.io/badge/styled--components-DB7093?style=flat-square&logo=styled-components&logoColor=white" height="25">
  <img src="https://img.shields.io/badge/Material--UI-0081CB?style=flat-square&logo=material-ui&logoColor=white" height="25">
  
  
  
  

</div>

</td><td valign="top" width="25%">

<h2 align="center"> ⚙ </h2><br>

<div align="center">

<img src="https://img.shields.io/badge/-Linux-black?style=flat-square&logo=Linux" height="25"> 
<img src="https://img.shields.io/badge/Windows-0078D6?style=flat-square&logo=windows&logoColor=white" height="25"> 
<img src="https://img.shields.io/badge/NPM-%23000000?style=flat-square&logo=npm&logoColor=white" height="25"> 
<img src="https://img.shields.io/badge/Ubuntu-E95420?style=flat-square&logo=ubuntu&logoColor=white" height="25">
<img src="https://img.shields.io/badge/-Git-black?style=flat-square&logo=git" height="25"> 
<img src="https://img.shields.io/badge/-GitHub-181717?style=flat-square&logo=github" height="25"> 
<img src="https://img.shields.io/badge/githubactions-%232671E5?style=flat-square&logo=githubactions&logoColor=white" height="25"> 
<img src="https://img.shields.io/badge/Markdown-000000?style=flat-square&logo=markdown&logoColor=white" height="25">
<img src="https://img.shields.io/badge/pycharm-143?style=flat-square&logo=pycharm&logoColor=white" height="25">  
<img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7?style=flat-square&logo=visual-studio-code&logoColor=white" height="25">  
<img src="https://img.shields.io/badge/webstorm-143?style=flat-square&logo=webstorm&logoColor=white" height="25">  

</div>

</td>
</td><td valign="top" width="25%">

<h2 align="center"> 🎨 </h2><br>

<div align="center">
<img src="https://aleen42.github.io/badges/src/photoshop.svg" height="25">
<img src="https://aleen42.github.io/badges/src/illustrator.svg" height="25">
<img src="https://aleen42.github.io/badges/src/dreamweaver.svg" height="25">
<img src="https://aleen42.github.io/badges/src/flash.svg" height="25">
  
 </div>

</td>
</tr></table>  

<div align="center">

<p align="center"> <img src="https://komarev.com/ghpvc/?username=NorbertRuff&label=Profile%20views&color=0e75b6&style=flat-square" alt="prathmesh" /> </p>


</div>
