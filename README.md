# Python snippets for data cleaning
## About
A collection of python code snippets for cleaning and combining files from templates, combining and transforming large datasets, and cleaning large datasets. All snippets are sourced from a larger data cleaning and combination project- snippets use smaller datasets containing the root issue addressed in the snippet. All notebooks and reference data files are stored here for reference.

Template data cleaning category also includes a program to customize & combine template cleaning snippets in a Linux environment for easy use- coauthored with [David Vogel](https:/github.com/davidvogelxyz).

## Snippets by category
Data import & export:
- [Import & export a single file to/from a certain file path](data-import-export-from-folder-singlefile/)
- [Import & combine multiple files from a certain file path](data-import-combine-from-folder-multifile/)
- [Clean & export files from one subfolder to another](data-clean-export-from-folder-multifile/)

Template data cleaning
- [Convert date to object, assign to each field, add to cleaned file name](date-to-column-filename/)
- [Combine split template with repeat columns into single dataframe](split-columns-combine/)
- [Drop columns in template not needed](keep-only-columns-needed/)
- [Template data cleaning Linux program](main.py)

Dataset cleaning: filtering
- [Remove fields based on string contents of one column](remove-fields-by-string-id/)
