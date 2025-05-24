### Configure repository

1. Create a public repository called `ci-cd-exercise`.
    - Check the box to add a `readme.md` file
    - Add .gitignore template for Python
2. Clone the repository to the local using the `git clone {REPOSITORY_URL}` command in the terminal
3. With VSCode, open the new created (`ci-cd-exercise`) folder.
4. Within the folder, copy the project structure provided in the virtual campus (`.zip`). Note that you might need to extract the content
5. Create a virtual environment using the dependencies from the `requirements.txt` file. Depending on the Pyhon version you are using, you might need to change the dependencies versions. 
6. Share the repository with the professor (`rarcaleanu-at-eada`).


### Create ML pipeline

1. Within the `pipeline/src/` folder create a `metadata.py` file, and add the constants and variables you consider relevant (e.g. model params, variables category, paths, etc).
2. Within the `pipeline/src/` folder create a `source.py` file, and create a function to load the CSV from the `datasets/Churn_Modelling_train_test.csv` file.
3. Within the `pipeline/src/` folder create a `transform.py` file, and define the functions for the data transformation (feel free to use part of the code provided in the `exercise_support.py` file).
4. Within the `pipeline/src/` folder create a `train.py` file, and define a function that trains a decision tree model and returns the model.
5. Within the `pipeline/src/` folder create a `store.py` file, and define a function that saves the model in the `pipeline/models/` folder. The model path must be `class_model-{your_name}-{timestamp}.joblib`. The timestamp can be obtained as `datetime.now().strftime("%Y-%m-%d-%H-%M-%S")`.
6. Implement all the pipeline within the `main()` function in the `main.py` file.
7. Once everything is completed, test that the pipeline works. Open a terminal and run `python main.py`. This should create a file in the `pipeline/models/` folder.


### Testing the pipeline

1. Within the `tests/` folder create a `test_transformer.py` file, and define some tests for the transformer.
    - *Optional*: you can do as many tests as you want for the transformer.
    - *Optional*: test other parts of the code (e.g. load, save, etc.).
2. Save the files and run the tests. Open a terminal and run `pytest tests/`. (This will run all the tests withi the `tests/` folder, but you could specify the file to be tested by defining the complete file path).
3. Check if tests are passed, if not review the issues.


### Push changes to the remote

1. Save all the files
2. Stage all the files using the following command on the terminal `git add .`
3. Commit the changes by using the the following command on the terminal `git commit -m '{MESSAGE}'`
4. Push the changes to the remote using `git push origin main`


### Create the CI/CD

1. On your local, create a new branch called `feature/implement-ci-cd`. You can use the following command `git checkout -b {BRANCH_NAME}`
2. Within the `.github/workflows/` folder create a file called `ci.yaml`
3. Within the `ci.yaml` define the continuous integration workflow, which needs to have the parameters listed below:
    - Workflow name: Continuous Integration - {YOUR NAME}
    - Runs on: pull request to the main branch
    - Job name: test-and-format
    - Job runs on: ubuntu-latest
    - Create token to allow commits to the repository (permissions)
    - Configure credentials and environment variables
    - Job steps:
        - Checkout repository
        - Set up Python (keep in mind what Python version is being used during the development)
        - Install dependencies
        - Run tests with pytest. At least 3 unit tests are required.
        - Format code with black
        - Commit and push changes. The commit message must be chore: format code with black
4. Within the `.github/workflows/` folder create a file called `cd.yaml`
5. Within the `cd.yaml` define the continuous deployment workflow, which needs to have the parameters listed below:
    - Workflow name: Continuous Deployment - {YOUR NAME}
    - Runs on: push to the main branch or every sunday at mid-night
    - Job name: test-and-format
    - Job runs on: ubuntu-latest
    - Allow github action to write to the repository (permissions)
    - Configure credentials and environment variables
    - Job steps:
        - Checkout repository
        - Set up Python
        - Install dependencies
        - Train the model with the dataset available in the /cd_dataset folder
        - Store the model in the /models folder. The model name must be in the format model_{current_date}, where current_date is in YYYY-MM-DD format.



### Test the CI/CD
1. Save all the files
2. Stage all the files using the following command on the terminal `git add .github/`
3. Commit the changes by using the the following command on the terminal `git commit -m '{MESSAGE}'`
4. Push the changes to the remote using `git push origin {FEATURE_BRANCH}` (you can check the working branch using `git branch`).
5. Go the Github UI and crete a Pull Request from the feature branch into the main.
6. Wait for all the checks to pass and go to the `Actions` tab and check if the CI has been executed successfully.
    - If so, check what changes has been made with the CI and then move to the following step
    - If not, check what went wrong and try to fix it. In the remove pull everthing from the remote (`git push orign {FEATURE BRANCH}`), fix the issues and repeat again from step 1.
7. On the `Pull Request`, merge the PR into the main branch. Then, go to the `Actions` tab and check if the CI has been executed successfully.
    - If 