* class 1 : https://www.youtube.com/watch?v=rwDHhx76MMg

1.  In this classs we have we have downloaded and installed anaconda
    link: https://www.anaconda.com/download

*  We have install annaconda.
2.  We have installed python extension in VS Code.

3.  Now run python prompt and typed python conda -V or python -V to check the version of conda or python

4.  Now We have to create an environment by using command in python prompt.
    for creation: conda create -n python12 python==3.12 -y
    for activation: conda activate python12

5.  We have created a file named "requirements.txt" and typed all libraries that were required.i.e.
    numpy
    pandas
    jupyter
    mypy

6.  After creating the requirement file, we have used python prompt and go to folder where file is placed now to install required libraries type:
    pip install -r requirements.txt

* After installation re-open the vscode.

7.  After opening update the environment as python12 and kernel as python12 for notebook.

8.  Notebook does not verify the variable type however the .py format identify and generate error if value is not same type. further pythond does not analyze to itself the type of variable you have to mention it every time.

* install python extension pack in vs code.

* install mypy extension re-open the vs code and now go to mypy extension settings and find "mypy.runUsingActiveInterpreter" and enable it.

10. In order to verify mypy extension is working go to class1.py  and this will show all errors in data types.

11. Data types
    str : "Ali"
    Int : 12
    float : 10.6
    bool : True or False
    list [str]: ["ali", "saleem", "shahbaz"] string will be default type you cannot update any other type in it.
    