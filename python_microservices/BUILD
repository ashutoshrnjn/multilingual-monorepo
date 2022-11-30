load("@py_deps//:requirements.bzl", "requirement")

MAIN_SRCS = glob(["*.py"])

MAIN_DEPS = [
    requirement("click"),
]

py_binary(
    name="python_microservices",
    srcs=["server.py"],
    imports=[""],
    main="server.py",
    python_version="PY3",
    srcs_version="PY3",
    deps=MAIN_DEPS,
)
