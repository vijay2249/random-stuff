# HideSensitiveInformation

## How to hide API keys and React source code of your app from users in case of using Create-react-app


## Covered Topics: 
- Just creating the repository and pushing your code
- For deploying the site -> Checkout the youtube tutorial [here](https://youtu.be/sL7MuNuC4SU)

If you have already pushed commits with sensitive data, follow this guide to remove the sensitive info while retaining your commits: https://help.github.com/articles/remove-sensitive-data/

### This is for the master branch in github repository

1. In your project folder, create a config.js file in the src folder in your create-react-app

2. In the config file, enter your API keys in an object like so (naming them whatever you like, and putting the keys in as strings)

    var secretInformation = {  

        MY_KEY : '123456',
        SECRET_KEY : '56789',
        KEY_2 : '101010'

    }

3. In the HTML file, add a script link to this file BELOW your jQuery script but ABOVE your own script file links:

    <script type='text/javascript' src='config.js'></script>
    <br>
    <script type='text/javascript' src='script.js'></script>

4. In your javascript/jquery file (probably script.js), declare variables that point to your API keys in the config file like so. Note that the 'config' here refers to the object called 'config', NOT to the file config.js:

    var mykey = secretInformation.MY_KEY;

    var secretkey = secretInformation.SECRET_KEY;

5. Be sure to replace every instance of the API keys with these new variables. 

    E.g. if you had,
    
    url: 'https//www.whatever.com/?query&sig=12345'

    Now you will have, url: 'https://www.whatever.com/?query&sig=' + mykey

6. In the terminal create a .gitignore file and open in atom. Name the file exactly as it is (watchout the "." at the start of name of the file)

7. In the .gitignore file, enter any file names that you want git NOT to track/commit/push. No other code is necessary. 

    In this case just add the file name we created to store the information,

    config.js

8. Type git st. You should see the .gitignore file ready to be tracked. You should NOT see the config.js file.

9. Now complete all the git add and commits and push works you are doing.

10. Also check once again if you missed any step to follow properly as mentioned be committing the files to github

##

## For Deploying the site: 

So finally you did it and you made clear that you secret keys are not visible to anyone who is going through your code in github in master branch

But once you deploy your code from like gh-pages or heroku app or netlify app try opening the source tab of your web site and go through your files
    
    you can clearly see your react code line to line in all your files 
    along with your directory structure too, here you can clearly see your secret keys
    
Reminder --> this is not shown in master branch in github, this is shown in the published site

So how do take down the react code structure from source tab?

### process 
You can checkout the youtube tutorial [here](https://youtu.be/sL7MuNuC4SU)

Else follow these steps
- open package.json file in react app and then make the following changes

    - Replace "build": "react-scripts build"

    - with "build": "set \\"GENERATE_SOURCEMAP=false\\" && react-scripts build"
  
Now generate the build file by using the command **_npm run build_**

If you are using gh-pages for publishing the site then run the command **_npm run deploy_** to push the changes to the publised branch

And now you are good to go.

Finally you are safe with your react code and structure as this is minified and not shown to anyone 


In the youtube tutorial I changed the name of command build to winBuild (if you change it from build to winBuild or something else follow the 3rd step as below)

  - change _"predeploy": "npm run build"_ to _"predeploy": "npm run winBuild"_

[source](https://gist.github.com/derzorngottes/3b57edc1f996dddcab25)


# _DrawBack of this process_

When you are deploying your website using gh-pages, You are actually creating a build folder that has nothing to do with .gitignore file and it just takes all the files in your directory and minimizes them to create a min js files (either 2 or more js files are created)

So when you deploy your site, you are actually publishing your build folder files to the ghpages branch in github, which then also contains your secrect information.

### _Find your api key in mininized files_

Open the source tab for the website published and then check for the file extensions that probabily contains the secret text based on the other branches code structure

Now search for the key word that is used to represent the secrect text or api keys that is mentioned in the other branches of the repository

First search in the _main.\<blah-blah-blah>.js_ file (chances are about 99% to be found in these files😅) and then move to other files

There you have it.

Showcase this to your noob cybersecurity friends and become hacker😅😉 (**_Ethical of course_**)

## _Note_

This is for just the frontend aplication that has something to do with these type of credentials like api keys or just the admin access etc..

If you are using backend too then first send the input to your server and then use your app working logic there in the server (like using api keys etc..)
