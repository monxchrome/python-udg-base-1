# def test(a, b):                  // string
#     print(f"{a} {b}")

# test(input(), input())

a = "hello world &"                  # str operators

print(
    a.upper(), 
    a.lower(),
    a.strip("&"), 
    a.split(),
    a.find("w"), 
    a.startswith("o"), 
    a.startswith("h"),
    a.endswith("a"), 
    a.endswith("d"),
    sep="\n"
    )
