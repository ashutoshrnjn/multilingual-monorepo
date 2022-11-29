# multilingual-monorepo
An attempt to manage multilingual monorepo using bazel

## Install bazel
Exhaustive steps are given here based on different OS [install](https://bazel.build/install)

### Install on MacOs
Refer [bazelisk](https://github.com/bazelbuild/bazelisk)
```
brew install bazelisk
```

## Project structure
`packages`: directory is the major directory consist of all the possible types of projects for e.g, libraries, microservices etc written in different languages.
    
`packages/libraries`: directory consist of all possible types of libraries.

`packages/services`: directory consist of all possible services.


## Rule of thumb for naming services and libraries
All services should start with a prefix of `service-` an example would be service-account-opening

All libraries should start with a prefix of `lib-` an example would be lib-sql-connector

# TODO
1. Configure few example projects in python and golang
2. Make use of bazel to manage those projects
3. Enable conventional commits - All commits should follow a standard. More info on this - [ConventionalCommits](https://www.conventionalcommits.org/)