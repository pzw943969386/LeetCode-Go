import os
import glob

foot_string = """
----------------------------------------------
<div style="display: flex;justify-content: space-between;align-items: center;">
<p><a href="https://books.halfrost.com/leetcode/ChapterFour/{0}/">⬅️上一页</a></p>
<p><a href="https://books.halfrost.com/leetcode/ChapterFour/{1}/">下一页➡️</a></p>
</div>
"""

current_working_dir = os.getcwd()
# print(f"current_working_dir: {current_working_dir}")

dir_names = glob.glob("*.md")
dir_names.sort()
lengthFile = len(dir_names)
# print(lengthFile)
for i in range(lengthFile - 1):
    file_name = dir_names[i]
    if(i == 0):
        continue
    if(i == lengthFile - 2):
        continue
    pre_name = dir_names[i - 1]
    # print(pre_name)
    next_name = dir_names[i + 1]
    # print(next_name)
    # print(foot_string.format(pre_name[:-3], next_name[:-3]))
    with open(file_name, "a") as myfile:
        myfile.write(foot_string.format(pre_name[:-3], next_name[:-3]))
print("Finished")