# BUILD file for Go project
load("@io_bazel_rules_go//go:def.bzl", "go_binary", "go_library", "go_test")

go_binary(
    name = "go_project",
    srcs = ["main.go"],
    importpath = "https://github.com/ashutoshrnjn/multilingual-monorepo/golang_restapi",
    deps = ["@com_github_mattn_go_sqlite3//:go_default_library"],
)
