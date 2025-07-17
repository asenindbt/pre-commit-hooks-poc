# UKTrade Pre-Commit Hooks

# Description
This repository contains custom pre-commit hooks developed by UKTrade.

# Creating a customised pre-commit hook
To create a customised pre-commit hook, create a new folder on the root of the project. Ensure the name of this folder is human-readable and refers to what the pre-commit's functionality.
Within this folder, add the pre-commit's functionality here.

## Adding the customised pre-commit hook's entry point

For the custom pre-commit hook to work, you will need to add its configuration within the `.pre-commit-hooks.yaml` file. Provide information such as the custom pre-commit's `id`, `name`, `description`, etc. An example of what the pre-commit hook should look like below.

```
# .pre-commit-hooks.yaml
- id: check-file-extension
  name: check-file-extension
  description: Checks the file extension of files that are commited in Git. If file(s) matches one of the listed arguments, the pre-commit hook will flag this up.
  entry: check-file-extension
  language: python
```

In order for the pre-commit hook to work, you will need to define where the entry point is. This is defined in the `setup.cfg` file, which is at the root of the project folder.
An example of what an entry point for the customised pre-commit hook, refer to the code snippet below.

```
[options.entry_points]
console_scripts =
    check-file-extension = pre_commit_hooks.check_file_extension.main:main
```

# Building the custom pre-commit hook for development

// TODO

Installing pre-commit hook
```bash
pip install .
```

Testing the pre-commit hook

```bash
pre-commit try-repo ../pre-commit-hooks-poc [pre-commit hook id] --verbose
```

# How is it used

To use the custom pre-commit hook from another project, add the pre-commit hook into the `.pre-commit-config.yaml`, such as below

// TODO: Config below needs to be changed once this repo is moved to UKTrade organisation
```
repos:
-   repo: https://github.com/asenindbt/pre-commit-hooks-poc
    rev: main
    hooks:
    -   id: check-file-extension
```
