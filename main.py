import platform as pf

architecture = pf.architecture()
platform = pf.platform()
machine = pf.machine()
processor = pf.processor()
version = pf.version()
system = pf.system()
node = pf.node()

print(architecture)
print(machine)
print(processor)
print(platform)
print(version)
print(system)
print(node)