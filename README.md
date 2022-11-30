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

## What is a monrepo
A "monorepo" is a single repository that contains multiple projects, often written in different languages. To create a monorepo of Python and Go projects, you can use a tool like Bazel or Buck to manage the dependencies and build the projects. Here is an example of how this might work:

First, you would need to create a root directory for your monorepo and create a subdirectory for each of your projects. For example, you might have a python directory for your Python project and a go directory for your Go project.

Next, you would need to create a WORKSPACE file at the root of the monorepo, which defines the external dependencies that your projects depend on. For example, if your Python project depends on the pandas library and your Go project depends on the go-sqlite3 library, you would need to add these dependencies to the WORKSPACE file:

```bash
workspace(name = "my_monorepo")

# Python dependencies
python_library(
    name = "pandas",
    version = "1.1.1",
)

# Go dependencies
go_repository(
    name = "com_github_mattn_go_sqlite3",
    importpath = "github.com/mattn/go-sqlite3",
    version = "v2.0.0",
)

```

Next, you would need to create a BUILD file for each of your projects, which defines the build rules for the project. For example, if your Python project has a main.py file and your Go project has a main.go file, you could define the build rules as follows:

```bash
# BUILD file for Python project
py_binary(
    name = "python_project",
    srcs = ["main.py"],
    deps = ["@pandas//:pandas"],
)

# BUILD file for Go project
go_binary(
    name = "go_project",
    srcs = ["main.go"],
    importpath = "github.com/my_user/my_monorepo/go",
    deps = ["@com_github_mattn_go_sqlite3//:go_default_library"],
)
```
Finally, you can use Bazel or Buck to build your projects and manage their dependencies. For example, to build the Go project, you could run the following command from the root of the monorepo:

```bash
bazel build //golang_restapi:golang_restapi
```

## python golang monrepo folder structure
Here is an example of a monorepo that contains a Python project and a Go project
```bash
.
├── go
│   ├── main.go
│   └── BUILD
├── python
│   ├── main.py
│   └── BUILD
├── serverless.yaml
└── WORKSPACE

```

This would build the go_project binary using the dependencies defined in the BUILD file. You can then run the binary to execute the project, or use Bazel or Buck to manage the dependencies of other projects that depend on this project.
## Rule of thumb for naming services and libraries
All services should start with a prefix of `service-` an example would be service-account-opening

All libraries should start with a prefix of `lib-` an example would be lib-sql-connector

# TODO
1. Configure few example projects in python and golang
2. Make use of bazel to manage those projects
3. Enable conventional commits - All commits should follow a standard. More info on this - [ConventionalCommits](https://www.conventionalcommits.org/)
