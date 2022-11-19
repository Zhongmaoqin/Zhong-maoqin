import MemorySystem2.MemorySystem

def filesystem():
    fs = MemorySystem.MemorySystem()
    fs.create_directory('.', "Dir_1")

    return fs
filesystem()