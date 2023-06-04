# Imports for mergeFiles()
import shutil
from pathlib import Path
import sys

# *argv accepts 0-n arguments (Merged Transaction Summay Files from Front End)
def argumentList(*argv):
  print ("I was called with", len(argv), "Merged Transaction Summary Files:", argv)
  lof = []
  for file in argv:
      # if path is not in same folder as file, specify static path in '{}' before {}
      pathFile = Path(r'{}'.format(file))
      lof.append(pathFile)
  # Returns list of files with specified paths
  mergeFiles(lof, "daily_transactions/merged_tsf.txt")
  return lof


def mergeFiles(lof,nf):

    newfile = nf

    with open(newfile, "wb") as wfd:

        for f in lof:
            with open(f, "rb") as fd:
                shutil.copyfileobj(fd, wfd, 1024 * 1024 * 10)

argumentList(sys.argv[1], sys.argv[2], sys.argv[3])
