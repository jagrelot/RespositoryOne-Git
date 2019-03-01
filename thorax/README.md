#__thorax__
-------------------
###Purpose
To retrieve complete salesforce orgs with a single ant command

-------------------
###Dependencies 
Python 3+, Ant 1.10.1+

-------------------

###Instructions (Jenkins): 
1. Add the thorax folder to the root of your repository
2. Create a new build, with a standard git setup
3. Add a build step of: Invoke Ant
4. Set the target to: main
5. Set the build file to: thorax/build.xml
6. Set the following properties
    * script=
        + full_backup.main - rebuilds full package of org and retrieves
        + soft_backup.main - uses existing package from branch and retrieves
        + Additional targets may be called from std/build.xml
        + To call more targets, add a folder with a build.xml file inside of scripts/
            - The format for calling is projectname.targetname
            - Scripts may reference each other in this way (see full_backup.main)
    * sf.username=Your Salesforce username
    * sf.password=Your Salesforce password
    * sf.serverurl=The URL you would like to deploy to
        + https://test.salesforce.com for sandboxes
        + https://login.salesforce.com for production
        + Custom URLs can also be used
    * sf.pollWaitMillis=The time to wait between log polls in ms
        + 5000 is recommended
    * sf.maxPoll=The maximum number of log polls before timeout/failure
        + 10000 is recommended
    * sf.apiVersion=The API version you would like to use
7. Add a build step of 'Execute Shell'
8. Add the following command to the shell: git add -A && git commit -m "Jenkins Automated Backup"
9. Add a post-build action of: Git Publisher
10. Check: Push Only If Build Succeeds
11. Click: Add Branch
12. Branch to push: The same branch you specified in step 2
13. Target remote name: origin (unless you know you've set something different)

-------------------
###Limitations:
1. Salesforce Metadata API limits retrievals to 10,000 components
    * A workaround is possible, but has not yet been developed

-------------------
###Contact
rcuenot@acumensolutions.com

Copyright © 2018 Acumen Solutions, Inc. The Thorax Salesforce Metadata Utility was created by Acumen Solutions.
Except for the limited rights to use and make copies of the Software as provided in a License Agreement, all rights are reserved.