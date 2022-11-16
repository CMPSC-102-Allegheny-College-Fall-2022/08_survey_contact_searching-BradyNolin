# Contact Searching

## Brady Nolin

## Program Output

### What is the output from running the following commands?

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

```
The contacts file contains 100 people in it! Let's get searching!

We are looking for contacts who have a job related to "engineer":
joe70@yahoo.com is a Network engineer
torresjames@white.info is a Electrical engineer
gharris@villarreal-snow.com is a Water engineer
williamsondavid@lopez.com is a Automotive engineer
ronald83@yahoo.com is a Maintenance engineer
zmarshall@yahoo.com is a Control and instrumentation engineer
christopher35@yahoo.com is a Civil engineer, consulting
edwardsjacob@gmail.com is a Chemical engineer

Wow, we found some contacts! Email them to learn about your job!
```

- `poetry run contactsearcher --job-description "neer" --contacts-file input/contacts.txt`

```
The contacts file contains 100 people in it! Let's get searching!

We are looking for contacts who have a job related to "neer":
joe70@yahoo.com is a Network engineer
torresjames@white.info is a Electrical engineer
grahamjoel@castillo-gilbert.net is a Engineer, technical sales
gsutton@miller.com is a Engineer, maintenance
gharris@villarreal-snow.com is a Water engineer
williamsondavid@lopez.com is a Automotive engineer
ronald83@yahoo.com is a Maintenance engineer
zmarshall@yahoo.com is a Control and instrumentation engineer
christopher35@yahoo.com is a Civil engineer, consulting
jacquelinedavid@hotmail.com is a Engineer, electronics
espinozadaryl@hill-maddox.com is a Engineering geologist
edwardsjacob@gmail.com is a Chemical engineer

Wow, we found some contacts! Email them to learn about your job!
```

## Source Code and Configuration Files

### Describe in detail how your provided source code works

#### The source code statement that makes the `search` module available to `main`

```python
from contactsearcher import search
```

This segment of source code allows functions from the search module to be called
in the main module. The segment says that from the contactsearcher folder, it wants
to import the search module.

#### The source code statement that extracts the current job description for a contact

```python
        for line in file:
            description = line[1]
            if job_description in description:
                contact_list.append(line)
```

This segment of source code is a for loop that searches for and exctracts the job description.
It begins by iterating through the mant contacts, then setting the descriptiob variable to
the second part of each line, which comes after the comma. It then says that if this segment
of the line matches the desired job description, it will add it to a list.

#### Invocation of the function called `search_for_email_given_job`

```python
 searching = search.search_for_email_given_job(job_description, contacts_file)
```

This segment of source code sets a variable equal to the invocation of the function.
It is set equal to a variable so that the contents can be iterated through later on
in the code. The calling of the function begins with 'search.' in order to tell
the program it is coming from the search module.

#### Test case for the function called `search_for_email_given_job`

```python
def test_find_multiple_matching_result():
    """Check to ensure that search for contacts works for multiple matches."""
    contacts_database = """kylebarnes@hotmail.com,Records manager
joe70@yahoo.com,Network engineer
torresjames@white.info,Electrical engineer
shawkins@watson.com,Science writer"""
    contacts_list = search.search_for_email_given_job("engineer", contacts_database)
    assert len(contacts_list) == 2
```

This test case checks to ensure the function can find multiple results.
It establishes four different contacts that the function will search through,
two being engineers and two being other professions. It then asserts that the
number of contacts found to match 'engineer' should be three.

#### Execute trace of the `contactsearcher` program

Explain each function call that takes place for the following run of the program
Write at least one paragraph to explain every function call when running `contactsearcher`

Your discussion should start with the invocation of the `contactsearcher`
function in the `main` module, explain all of the subsequent function calls in
the correct order, and then show how the program's control returns to the
`contactsearcher` function in the `main` module.

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

This function call begins by telling the program to run the contactsearcher algorithm.
It then says that the job description it wants to search for is engineer. In the main
function, this part is deifned in the command line as "job_description". Then, the program
is told to search through the contacts.txt file. This is defined as "contacts_file" in the
main function.

## Professional Assessment

### So far this semester, what is one area in which you have struggled? How did you overcome this challenge?

This semester, one area I have noticed that I have struggles in would be using
while loops to create functions. Although they are fairly similar to for loops,
I have a much greater understanding for for-loops. I have overcome this by
looking at example while loops and comparing them to the problem at hand to
generatemy while loop.

### Based on your experiences with this project, what is one way in which you want to improve?

After completing this project, one way I want to improve is working with files.
Although we have done a couple of projects with files, I still have trouble
opening them and iterating through them. For example, taking a certain part of
a line of a file was new to me in this project and I want to learn more things
like this in the future.
