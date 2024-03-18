
# Lambda Forge Road Map

## Create a new directory:
```
mkdir demo_lambda_forge
cd demo_lambda_forge
````

## Create a new venv:
```
python3 -m venv venv
source venv/bin/activate
```
## Install lambda-forge from TestPYPI:
```
pip install lambda-forge==1.0.63 --extra-index-url https://pypi.org/simple --extra-index-url https://test.pypi.org/simple/
````

## Create a new project:
```
forge project demo_lambda_forge --repo-owner "GuiPimenta-Dev" --repo-name "demo_lambda_forge" --bucket "gui-docs"
````

## Create a new public function:

```
forge function hello_world --method "GET" --description "A simple hello word" --public
```

## Sync and deploy the dev stack to the cloud:

```
cdk synth
cdk deploy Dev-Demo Lambda Forge-Stack
````

## Create a repository called demo_lambda_forge on GitHub:

```
git init
git add .
git commit -m "Initial commit"
git branch -M dev
git remote add origin git@github.com:GuiPimenta-Dev/demo_lambda_forge.git
git push -u origin dev
```

# Go to the Pipeline section on the AWS Console and see the magic happening!
