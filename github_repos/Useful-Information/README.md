1. If any of this is aganist the copyright usage of the information please make a point of it in the discussions, from which the any releated information will be deleted that is being already used in source mentioed and the source is kept as it is 
2. we just mention the solution to your web site or any url link thats it in this repo in such cases as the information the person is searching for may not appear as a top result for the person


## Actual Purpose of this repository

_It can be so annoying to search for the same question in chrome or brave for a problem and we dont actually remember the solution or the guide website url, so with that in mind I just created this repository that helped me while solving any techincal problems or something else with steps to follow and the source for the website or any repositorys, that helped me while solving the problem_

### _If anyone wants to add extra information tools or sources feel free to make a pull request and add them to the repository_

### _Dont forget to include the source of your information too, doesn't matter how many external links are present in the source list_

# Useful-Info

## ___Chrome Installation in kali Linux___ 
- [install-google-chrome-on-kali-linux](https://www.tecmint.com/install-google-chrome-on-kali-linux/)
- [setup-chrome-driver-for-selenium-on-kali-linux](https://techstarspace.engineer/2020/02/19/setup-chrome-driver-for-selenium-on-kali-linux/)


## ___GHunt Osint tool process___
- First you need to install google chrome for this to work
- Then if there is no chromedriver installed the the script check_and_gen.py automatically downloads the driver after running the script
- Then the script check_and_gen.py asks for the cookies ID which are located in accounts.google.com -\> inspect page -\> storage -\> cookies


- [GHUNT](https://hackersonlineclub.com/ghunt-osint-suite-to-investigate-google-accounts/)


## ___Some Useful GITHUB repo's___
- [Learn how web Works](https://github.com/vasanthk/how-web-works)


### ___To create requirements.txt file automatically use the command pipreqs \<folderPath>___
- DO NOT FORGET TO INSTALL **pipreqs** MODULE


## ___Good Source to learn css Flexbox and css Grid___
- [FLEXBOX](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
- [CSS GRID](https://css-tricks.com/snippets/css/complete-guide-grid/)

- [React form validation](https://www.npmjs.com/package/react-validation) npm package
- [styled-components.com](https://styled-components.com/) 


# Resources for Students 
- [A-to-Z-Resources-for-Students](https://github.com/dipakkr/A-to-Z-Resources-for-Students)


## Capturing packets in windows system
- [how-can-i-perform-a-packet-capture-in-windows-with-built-in-utility](https://www.sonicwall.com/support/knowledge-base/how-can-i-perform-a-packet-capture-in-windows-with-built-in-utility/170905204545360/)
- source from [sonicwall.com](https://sonicwall.com)

## Tor Browser Download in Kali linux
- [https://www.kali.org/docs/tools/tor/](https://www.kali.org/docs/tools/tor/)
- While running the tor browser as root we the error _"the-tor-browser-bundle-should-not-be-run-as-root-exiting"_. Checkout solution [here](https://cyruslab.net/2012/11/16/the-tor-browser-bundle-should-not-be-run-as-root-exiting/)

# Git Merging from One branch to Another
- [stackoverflow](https://stackoverflow.com/questions/20101994/git-pull-from-master-into-the-development-branch)


# Adding postgreSQL commands to system environmental vairables in windows after download
- Download the exe for postgreSQL from the website [here](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) 
- Click on the exe file and finish the setup and remember the folder where you are extracting files to
- Make sure you remember the password that you set in the setup of postgres that is required in last step
- Then in the start menu type "environmental variables" 
- Click on the suggested Change envronmental variables option
- Then navigate to EnvironmentalVariables button at the bottom
- Select Path in the system variables and click on edit
- Now copy the folder path that you extracted your postgres files, and click on new button in environmental variables and paste the path in here
- Click on ok button for all the pop-up and close the environmental variables tab or window
- Now open the command prompt and run the command **_psql -U postgres_**
- Then it asks for password, type the password and hit enter
- Now you can use postgres from your terminal without actually opening the the psql terminal everytime


# _Installing Nano Text Editor in windows_

 - First make sure that you have choco installer in your system 
    - If not then follow these steps to download it.
          - Open powershell in administrator mode (if this is not available then download it from [here](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell?view=powershell-7.1))
          - then paste this command in the powershell

            powershell Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
     - You can read more about choco [here](https://chocolatey.org)
  - After the installation of choco is complete then run the command

         choco install nano -y 
  - -y flag is to enter yes automatically for all prompts that are asked (if any) while installing

You are done with installing nano text editor in windows🥳🥳

[source](https://handhikayp.medium.com/install-nano-text-editor-in-windows-10-26d48aa998d4) from medium

### List the network interfaces that the system is connected to in the past in windows
- _netsh wlan show profile_    -> this shows the networks that your system is connected to in the past
- _netsh wlan show profile \<profileName>_   -> this shows the network information about the profileName mentioned
- _netsh wlan show profile \<profileName> key=CLEAR_  -> this shows the network information and also the password of the profileName mentioned

## Setting environmental variables in windows
- [source](https://www.dowdandassociates.com/blog/content/howto-set-an-environment-variable-in-windows-command-line-and-registry/) from [dowdandassociates.com](https://dowdandassociates.com)

## _Custom Scrollbars for webpage_
- [w3schools](https://www.w3schools.com/howto/howto_css_custom_scrollbar.asp) resource

## Resources for learning GIT and GITHUB
- [https://learngitbranching.js.org/](https://learngitbranching.js.org/)

## Shape Provider using SVG for styling web page
- [https://www.shapedivider.app/](https://www.shapedivider.app/)

## Wrapping items using grid and flexbox
- [Mastering_Wrapping_of_Flex_Items](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Mastering_Wrapping_of_Flex_Items) from MDN docs

## MongooseError: Query was already executed:
- [Stackoverflow solution](https://stackoverflow.com/questions/68945315/mongooseerror-query-was-already-executed)
- [Official Mongoose docs](https://mongoosejs.com/docs/migrating_to_6.html#duplicate-query-execution)
