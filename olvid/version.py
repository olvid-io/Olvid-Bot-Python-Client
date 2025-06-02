# for __version__ use python version syntax: https://packaging.python.org/en/latest/discussions/versioning/
# for alpha version: set x.x.xa0
__version__ = "1.4.1"
# for __docker_version__: use same version as daemon (x.x.x, x.x.x-alpha)
__docker_version__ = "1.4.1"

if __name__ == "__main__":
	print(__version__, end="")
