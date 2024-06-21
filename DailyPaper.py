import argparse
import os

from DailyPaper.localPython.parameterType import ParameterType

parser = argparse.ArgumentParser()
parser.add_argument("--authorList" , type=str, help="path to text file with list of authors to watch for"  )
parser.add_argument("--subjectList", type=str, help="path to text file with list of subjects to watch for" )
parser.add_argument("--urlList"    , type=str, help="path to text file with list of urls to search through")
args = parser.parse_args()

scriptDir = os.path.dirname(os.path.realpath(__file__))

authorList  = ParameterType('authorList' , args.authorList , scriptDir)
subjectList = ParameterType('subjectList', args.subjectList, scriptDir)
urlList     = ParameterType('urlList'    , args.urlList    , scriptDir)