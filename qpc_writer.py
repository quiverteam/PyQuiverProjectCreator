import qpc_hash
import qpc_visual_studio
import qpc_makefile
# import qpc_vscode
# import qpc_ninja

from os import path, sep
from qpc_base import args


def CreateProject(project_list):
    if "vstudio" in args.types:
        qpc_visual_studio.CreateProject(project_list)
    
    if "makefile" in args.types:
        qpc_makefile.CreateMakefile(project_list)
    
    # if project_type == "vscode":
    #     qpc_vscode.CreateFiles(project_list)
    
    # if project_type == "ninja":
    #     qpc_ninja.CreateProject(project_list)


def MakeMasterFile(project_def_list, project_hash_list, master_file_name, configurations, platforms):
    hash_list = project_def_list
    if "vstudio" in args.types:
        if not qpc_hash.CheckHash(master_file_name + ".sln"):
            qpc_visual_studio.MakeSolutionFile(project_def_list, master_file_name, configurations, platforms)
            qpc_hash.WriteHashFile(master_file_name + ".sln", project_hash_list, True)
    
    if "makefile" in args.types:
        pass
        # if not qpc_hash.CheckHash(master_file_name + ".makefile"):
        #     qpc_makefile.MakeMasterMakefile(project_def_list, master_file_name, configurations, platforms)
        #     qpc_hash.WriteHashFile(master_file_name + ".makefile", project_hash_list, True)


def FindProject(project_path):
    base_path, project_name = path.split(project_path)
    split_ext_path = path.splitext(project_name)[0]
    base_path += sep
    if "vstudio" in args.types:
        if path.isfile(split_ext_path + ".vcxproj") and path.isfile(split_ext_path + ".vcxproj.filters"):
            return True
        else:
            return False
        
    if "makefile" in args.types:
        if path.isfile(base_path + "makefile"):
            return True
        else:
            return False
