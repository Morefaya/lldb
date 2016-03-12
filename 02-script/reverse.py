def reverse(debugger, command, result, internal_dict):
	target = debugger.GetSelectedTarget()
	for m in target.module_iter():
		break
	name = "" + m.file.basename
	name = "FT_" + name[::-1]
	print name
	return
def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f reverse.reverse reverse')
