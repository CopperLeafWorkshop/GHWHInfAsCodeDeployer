GitHubWebHook (GWH) Infrastructure As Code Deployer
------------------------------------------------

 1. Deploy this to AWS
 2. Setup github with this endpoint as a webhook
 3. on webhook trigger:
    - checkout the repo
    - if exists: run deploy.sh
    - delete the checked-out repo
    