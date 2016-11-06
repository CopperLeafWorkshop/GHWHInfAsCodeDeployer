GitHubWebHook (GHWH) Infrastructure As Code Deployer
------------------------------------------------

Developer Setup:
Windows 10:
    Install "Windows Subsystem for Linux"

 1. Deploy this to AWS
 2. Setup github with this endpoint as a webhook
 3. on webhook trigger:
    - checkout the repo
    - if exists: run deploy.sh
    - delete the checked-out repo
    