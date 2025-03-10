Purpose-first programming proof-of-concept
==================================

Many learners may not care about exactly how a programming language works, but they do care about what code can achieve for them. I propose the creation of "purpose-first" scaffolds, which allow novices can quickly and easily create or understand authentic code without the need for deep knowledge of semantics. Prior work suggests that this approach may lead to higher engagement by increasing both expectancy of success and subjective task value. 

In this ebook, I develop a proof-of-concept purpose-first programming curriculum. This curriculum will be used in an experiment to evaluate the expectancy of success as well as task value that novice programmers have for purpose-first programming activities.



# Local Deployment Steps

- Make sure you create a new conda environment (https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) with Python 3.8.20
- Install requirements from requirements.txt using pip
    
    pip install -r requirements.txt

- Update the files under _sources, add new pages/new problems as needed
- (Optional) set a project name in pavement.py, line 13
- Run `runestone build' for building 
- Run `runestone serve' for debugging (you may need to delete the build folder with `rm -rf build/` and run the build command again)
