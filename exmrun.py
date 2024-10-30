# import module
import exm

# module running process:
# make module name
module_name = "exm"
# get module name from globals
module = globals().get(module_name)
# run
module.example(world)
