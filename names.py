# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

def make_full_name(given_name, family_name):
    """Return a string in this form "family_name; given_name". For
    example, if this function were called like this:
    make_full_name("Sally", "Brown"), it would return "Brown; Sally".

    Parameters
        given_name: a string that contains a person's given name
        family_name: a string that contains a person's family name
    Return: a string in the form "family_name; given_name"
    """
def make_full_name(given_name, family_name):
    """Return a string in this form "family_name; given_name"."""
    full_name = f"{family_name}; {given_name}"  
    return full_name


def extract_family_name(full_name):
    """Extract and return the family name from a string in this form:
    "family_name; given_name". For example, if this function were
    called like this:
    extract_family_name("Brown; Sally"), it would return "Brown".

    Parameter:
        full_name: a string in the form "family_name; given_name"
    Return: a string that contains a person's family name
    """
    semicolon_index = full_name.index("; ")

    family_name = full_name[0 : semicolon_index]
    return family_name


def extract_given_name(full_name):
    semicolon_index = full_name.index("; ") 
    given_name = full_name[semicolon_index + 2 :]
    return given_name