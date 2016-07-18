# luigi-example

This is a minimal example of a Luigi pipeline. It is used in my blog post about
Luigi as an example.

Here you find instructions to get the minimal version of it running

## Prerequisites

* Install Luigi

```bash
pip install luigi
```

* Clone the repositiory

```
git clone git@github.com:Condla/luigi-example.git
```

## Run the job

```
cd luigi-example
python pipe.py --input-path test.txt --local-scheduler
```


## Output

A file ```count.txt``` will be created in which the number of words of the file ```test.txt``` is
written. If you want to run the job again you need to delete ```count.txt```
since the dependency model of Luigi will not let you execute jobs that have
already run.


Have fun.

