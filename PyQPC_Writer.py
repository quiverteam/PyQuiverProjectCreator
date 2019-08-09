
import PyQPC_VisualStudio as vstudio
import PyQPC_qpc_writer as qpc_writer


def CreateProject( project, project_types ):

    if project_types["vstudio"] or project_types["vs2019"]:
        vstudio.CreateProject( project )

    elif not project_types:
        pass

    else:
        print( "Unknown Project Type" )


def MakeSolutionFile( project_types, project_def_list, root_folder, solution_name, configurations, platforms ):

    if project_types["vstudio"] or project_types["vs2019"]:
        vstudio.MakeSolutionFile( project_def_list, root_folder, solution_name, configurations, platforms )

    elif not project_types:
        pass

    else:
        print( "Unknown Project Type" )
