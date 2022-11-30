workspace(name="python-golang-monrepo")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# Python dependencies
rules_python_version = "0.7.0"

http_archive(
    name="rules_python",
    sha256="15f84594af9da06750ceb878abbf129241421e3abbd6e36893041188db67f2fb",
    strip_prefix="rules_python-0.7.0",
    url="https://github.com/bazelbuild/rules_python/archive/refs/tags/0.7.0.tar.gz",
)

load("@rules_python//python:repositories.bzl", "python_register_toolchains")

python_register_toolchains(
    name="python39",
    # Available versions are listed in @rules_python//python:versions.bzl.
    python_version="3.9",
)

load("@python39_resolved_interpreter//:defs.bzl",
     python_interpreter="interpreter")
load("@rules_python//python:pip.bzl", "pip_install")

pip_install(
    name="py_deps",
    python_interpreter_target=python_interpreter,
    requirements="//3rdparty:requirements.txt",
)

# Go dependencies
rules_go_version = "v0.27.0"  # latest @ 2021/05/23

http_archive(
    name="io_bazel_rules_go",
    sha256="69de5c704a05ff37862f7e0f5534d4f479418afc21806c887db544a316f3cb6b",
    urls=[
        "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/{version}/rules_go-{version}.tar.gz".format(
            version=rules_go_version),
        "https://github.com/bazelbuild/rules_go/releases/download/{version}/rules_go-{version}.tar.gz".format(
            version=rules_go_version),
    ],
)

load("@io_bazel_rules_go//go:deps.bzl",
     "go_register_toolchains", "go_rules_dependencies")

go_rules_dependencies()

go_register_toolchains(version="1.16")

gazelle_version = "v0.23.0"  # latest @ 2021/05/23

# Gazelle - used for Golang external dependencies
http_archive(
    name="bazel_gazelle",
    sha256="62ca106be173579c0a167deb23358fdfe71ffa1e4cfdddf5582af26520f1c66f",
    urls=[
        "https://storage.googleapis.com/bazel-mirror/github.com/bazelbuild/bazel-gazelle/releases/download/{version}/bazel-gazelle-{version}.tar.gz".format(
            version=gazelle_version),
        "https://github.com/bazelbuild/bazel-gazelle/releases/download/{version}/bazel-gazelle-{version}.tar.gz".format(
            version=gazelle_version),
    ],
)

load("@bazel_gazelle//:deps.bzl", "gazelle_dependencies")

gazelle_dependencies()
