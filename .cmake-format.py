# flake8: noqa
with section("format"):
    line_width = 100
    max_pargs_hwrap = 5
    max_subgroups_hwrap = 3
    min_prefix_chars = 2
    dangle_parens = True
    always_wrap = [
        "add_library",
        "target_link_libraries",
    ]
    autosort = True
with section("markup"):
    enable_markup = False
