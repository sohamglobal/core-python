# Demo program on string functions

slogan="you will never walk alone"
print(len(slogan))
print(slogan.index('i'))
print(slogan.count("e"))
print(slogan[4:14])
print(slogan[4:14:2])
print(slogan.upper())
print(slogan.startswith("you"))
parts=slogan.split(" ")
print(parts)
print(slogan.find("walk"))
print(slogan.replace("walk","talk"))

para="""Python is a widely used high-level programming language for 
general-purpose programming, created by Guido van Rossum and first 
released in 1991. An interpreted language, Python has a design philosophy 
that emphasizes code readability, and a syntax that allows programmers 
to express concepts in fewer lines of code than might be used in languages 
such as C++ or Java. The language provides constructs intended to enable 
writing clear programs on both a small and large scale."""

print(para)

print("\n")
nm="sohamglobal media services"

print(nm[2:7])
print(len(nm))
print(nm.capitalize())
print(nm.upper())
print(nm.title())
print(nm.replace("g","G"))
print(max(nm))
print(min(nm))
print(nm.join(" india"))


# content of sohamglobal.com