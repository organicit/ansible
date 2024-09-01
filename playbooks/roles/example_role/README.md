# README for Ansible Role

## Author

Ean Wilson

## Description

YOUR ROLE NAME

## Role Directory Structure Overview

### Defaults

- `main.yml`
  - getpamdconf
  - pamdconf
  - createappuser
  - createappdir
  - fstabconf
  - installtomcat

### Files


### Handlers

- `main.yml`
  - Tasks: 1

### Tasks

- `createappdir.yml`
  - Tasks: 5
- `createappuser.yml`
  - Tasks: 2
- `fstabconf.yml`
  - Tasks: 2
- `getpamdconf.yml`
  - Tasks: 2
- `installtomcat.yml`
  - Tasks: 1
- `main.yml`
  - Tasks: 6
- `pamdconf.yml`
  - Tasks: 2

### Templates


### Tests

- `test.yml`
  - Tasks: 1

### Vars

- `main.yml`
  - app_username
  - app_dir
  - mount_source
  - app_group
