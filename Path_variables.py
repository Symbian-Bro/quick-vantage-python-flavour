# Will need this is a seperate function because I am new to using glob instead of wildcards
def find_path(pattern):# The pattern is the path to the file we are looking for
    return glob.glob(pattern)