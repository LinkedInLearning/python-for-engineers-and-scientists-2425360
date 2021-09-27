# Python for Engineers and Scientists
This is the repository for the LinkedIn Learning course Python for Engineers and Scientists. The full course is available from [LinkedIn Learning][lil-course-url].

![Python for Engineers and Scientists][lil-thumbnail-url] 

This course offers scientists and engineers (ranging from students of those disciplines to experienced professionals) a dedicated, empowering introduction to Python for scientific and engineering applications. Theoretical astrophysicist and Python enthusiast Michele Vallisneri explains how Python can help you become a better engineer or physicist by making your work more efficient, accurate, and agile. Michele walks you through installing Python for macOS, Windows, and Linux, as well as setting up Jupyter notebooks. He explains how you can make Python fast using NumPy arrays, the SciPy library, Numba, and Cython. Michele then tackles ways to ensure your code is correct with tools for symbolic computation, differential equations, interpolation, and more. He finishes up with ideas to make your computational life easier with Python, including JSON, pandas, HDF5, automation with Python scripts, and scientific workflows with Snakemake.

## Instructions
This repository has branches for each of the videos in the course. You can use the branch pop up menu in github to switch to a specific branch and take a look at the course at that stage, or you can add `/tree/BRANCH_NAME` to the URL to go to the branch you want to access.

## Branches
The branches are structured to correspond to the videos in the course. The naming convention is `CHAPTER#_MOVIE#`. As an example, the branch named `02_03` corresponds to the second chapter and the third video in that chapter. 
Some branches will have a beginning and an end state. These are marked with the letters `b` for "beginning" and `e` for "end". The `b` branch contains the code as it is at the beginning of the movie. The `e` branch contains the code as it is at the end of the movie. The `main` branch holds the final state of the code when in the course.

When switching from one exercise files branch to the next after making changes to the files, you may get a message like this:

    error: Your local changes to the following files would be overwritten by checkout:        [files]
    Please commit your changes or stash them before you switch branches.
    Aborting

To resolve this issue:
	
    Add changes to git using this command: git add .
	Commit changes using this command: git commit -m "some message"
	
_See the readme file in the main branch for updated instructions and information._
## Instructions
This repository has folders for each of the main chapters in the course, named `Ch02`, `Ch03`, and `Ch04`. Most videos in each chapter have a corresponding Jupyter notebook, named `CHAPTER#_MOVIE#_TOPIC.ipynb`. The notebooks have a beginning and an end state; the end-state notebooks are marked as `CHAPTER#_MOVIE#_TOPIC-complete.ipynb`.

## Installing
1. To use these exercise files, you must have the following installed:
	- Python 3.8; NumPy, SciPy, SymPy, AstroPy, Pandas, Matplotlib, Cython, Numba, Requests, Pillow (PIL), Snakemake, Jupyter; C/C++ compilers; Fortran compiler (optional) and Python fortran-magic.
2. Clone this repository into your local machine using the terminal (Mac), CMD (Windows), or a GUI tool like SourceTree.


### Instructor

Michele Vallisneri 
                            
Senior Research Scientist, NASA Jet Propulsion Laboratory

                            

Check out my other courses on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/michele-vallisneri).

[lil-course-url]: https://www.linkedin.com/learning/python-for-engineers-and-scientists
[lil-thumbnail-url]: https://cdn.lynda.com/course/2425360/2425360-1632161420283-16x9.jpg




