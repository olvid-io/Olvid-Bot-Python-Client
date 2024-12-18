__version__ = "1.1.0.post1"
# docker image version does not use .postN format (we can override elements)
__docker_version__ = __version__ if __version__.split(".")[-1].isdigit() else ".".join(__version__.split(".")[:-1])

if __name__ == "__main__":
	print(__version__, end="")
