# gitlab-create-repo-api

This repo is to conatin the scripts and steps used to migrate an old version of GitLab repos to a newer version when migrate/upgrade is not possible due to long outdated upgrade paths or OS cannot be upgraded. 

First step was to gather the information from old GitLab server using glab repo list command and output that to a list.

I then next created a folder structure to match the project location due to many repos having the same name but in different namespaces/projects.

Using this as my list I cloned each repo into its respective folder. (Script to follow)

Once all the repos had been cloned I then span up a docker of the latest GitLab and once setup with my base credentials/ssh key and personal access token, I then used the python script create-groups.py to create the namespaces, I then had to get the ID's of each and match them to the folders into a new list in repo.json 

Next step was to run create-repo.py to create the projects.

Once complete I then ran the repo.sh to add the new remote to all the repos al push them into the new projects on my docker container.
