flag = 0
markdown = """# review-2024

你在期待什么？你在失望什么？

- 2023 年的年终总结见：[saveweb/review-2023](https://github.com/saveweb/review-2023)

保持传统，本项目将长期维护（直到2026年初）。

**想要添加您的年终总结？请发 Issue 或编辑 metadata.md 发 PR**

**如需请求删除收录，请联系 take-down#saveweb.org / info#saveweb.org / hi#nekoq.top **

**（不需要填写博客ID，不需要编辑 README.md）。**

---

"""

raw_lines = open('metadata.md', 'r').read().splitlines()

header = raw_lines[0:2]

lines = set(raw_lines[2:])
lines.discard('')

with open('README.md', 'w') as f:
  f.write(markdown+'计数: '+str(len(lines))+' 篇。下表每次 CI 乱序输出。\n\n')
  f.write('\n'.join(header))
  f.write('\n')
  f.write('\n'.join(lines))
