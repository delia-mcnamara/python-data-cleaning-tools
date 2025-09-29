# Python snippets for data cleaning
## About
A collection of python code snippets for cleaning and combining files from templates, combining and transforming large datasets, and cleaning large datasets. All snippets are sourced from a larger data cleaning and combination project- snippets use smaller datasets containing the root issue addressed in the snippet. All notebooks and reference data files are stored here for reference.

Separately, my friend Dave has been working on a utility to perform multiple cleaning tasks within a single run of a `.py` file. That repo can be found [here](https://github.com/DavidVogelxyz/dataframe-formatting-utility).

## Snippets by category
Data import & export:
- [Import & export a single file to/from a certain file path](data-import-export-from-folder-singlefile/)
- [Import & combine multiple files from a certain file path](data-import-combine-from-folder-multifile/)
- [Clean & export files from one subfolder to another](data-clean-export-from-folder-multifile/)

Template data cleaning
- [Convert date to object, assign to each field, add to cleaned file name](date-to-column-filename/)
- [Combine split template with repeat columns into single dataframe](split-columns-combine/)
- [Drop columns in template not needed](keep-only-columns-needed/)
- [Standardize categorical data labels](standardize-data-labels/)

Dataset cleaning: filtering
- [Remove fields based on string contents of one column](remove-fields-by-string-id/)
