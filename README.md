# Lab 07 - Regular Expressions

In this lab, we'll learn the basics of regular expressions, which we'll use to validate various data formats.

## Getting Started

Be sure that you have accepted the assignment invitation within GitHub Classroom (by clicking on the link provided in the lab assignment on Canvas), before you proceed.  You want to clone your own copy of the repository (not the original, since you can't write to that repository).  The command to do so will look something like this:

```
git clone https://github.com/CSCI1030U/lab07-rana-muniz
```

Be sure to change directory to a place where the rest of your CSCI1030U labs are stored, first, so that this command copies your lab assignment starter code into the proper place.

## Instructions

In this lab, you will write the `lab07.py` file so that it meets the requirements described in the following sections.  This file has no basic code to start, and it will be up to you to write all of the code for this lab.

#### Part 1

Write a function, `validate_variable`, that takes a single string (`value`), and returns `True` if that string strictly contains a valid variable name (e.g. max, , x2, test_avg, standardDev),and returns `False` otherwise.  The first character must be either a letter (uppercase or lowercase) or an underscore (`_`), but the remaining characters can be a letter, underscore, or a digit.

Example calls to this function, and the resulting value, are given below:

```python
validate_variable('max')          # True
validate_variable('x2')           # True
validate_variable('test_avg')     # True
validate_variable('standardDev')  # True
validate_variable('1minumum')     # False
```

You can include some test code for your function, or you can exclude it when you submit.  The function itself will be all that is tested.

#### Part 2

Write a function, `validate_domain`, that takes a single string (`value`), and returns `True` if that string strictly contains a domain name (e.g. google.ca, smile.amazon.com),and returns `False` otherwise.  All string components, which are separated by dot '.' characters, can be a lowercase letter, followed by 0 or more lowercase letters, digits, or underscores.  There must be at least one such string, in addition to the top-level domain.  The TLD (top-level domain, the string after the final dot '.' character) should be one of the following (for simplicity, this is a reduced list):
- `com`
- `ca`
- `org`

Example calls to this function, and the resulting value, are given below:

```python
validate_domain('google.ca')        # True
validate_domain('smile.amazon.com') # True
validate_domain('unicef.org')       # True
validate_domain('google.uk')        # False
```

You can include some test code for your function, or you can exclude it when you submit.  The function itself will be all that is tested.

#### Part 3

Write a function, `validate_phone`, that takes a single string (`value`), and returns `True` if that string strictly contains a phone number of one of the following forms (D represents any digit), and `False` otherwise:
- `DDD-DDDD`
- `DDD-DDD-DDDD`
- `(DDD)DDD-DDDD`

Example calls to this function, and the resulting value, are given below:

```python
validate_phone('721-8668')      # True
validate_phone('905-721-8668')  # True
validate_phone('(905)721-8668') # True
validate_phone('9057218668')    # False
```

You can include some test code for your function, or you can exclude it when you submit.  The function itself will be all that is tested.

## Verifying Correctness

Run the pre-written tests that verify that your lab assignment code passes, using the following command:

```
pytest
```

Examine the output closely.  There should be hints about what went wrong, if any of the tests fail.  If you are struggling to figure it out, you can always ask for help (see __Getting Help__ for details).


## Getting Help

If your code does not work, there is always a lab instructor present during your lab period for assistance.  Them not having to mark lab assignment submissions means that they should have plenty of time to ensure that you are able to get your lab assignment submission working by the end of the lab period.

_**Note:** The lab instructor is likely to help you figure out what is wrong with your code, rather than tell you how to fix it directly.  The goal is for you to learn how to diagnose and fix your bugs on your own._

## How to Submit

First, ensure that your code passes the tests (see the section __Verifying Correctness__ for details).  If you are certain that your code passes all of the tests, then you can submit your work using the following commands:

```
git add --all
git commit -m "Lab 07 completed code"
git push origin main
```

Once you have submitted your work, you can also double check that your auto-grading was successful by clicking on the `Actions` tab in your repository page on GitHub.  Sometimes, this takes a few minutes to complete, so please be patient.
