"""Search for an email address given a fragment of a job description."""

from typing import List

import csv

# note: see https://docs.python.org/3/library/csv.html 


def search_for_email_given_job(job_description: str, contacts: str) -> List[List[str]]:
    """Search for and return job description(s) given an email address."""
    # create an empty list of the contacts
    contact_list = []
    # iterate through the file, parsing it line by line
    with open(contacts, "r") as csv_file:
        file = csv.reader(csv_file)
    # iterate through each line of the file and extract the current job
    # ---> extract the current job for the contact on this line of the CSV
    # ---> the job description matches and thus we should save it in the list
        for line in file:
            description = line[1]
            if job_description in description:
                contact_list.append(line)
    # return the list of the contacts who have a job description that matches
        return contact_list
