import re

class MarkdownProcessor:
    def __init__(self):
        self.data = None
        self.chunks = []

    def load(self, filename):
        with open(filename, 'r') as f:
            data = f.read()
        self.chunks = data.split("\n\n")
        self.data = data
    
    def process_bold(self, line):
        bolds = re.findall("\*\*.*\*\*", line)
        for bold in bolds:
            tag = bold.replace("**", "<b>").replace("**", "</b>")
            line = line.replace(bold, tag)
        return line 
    
    def process_strong(self, line):
        strongs = re.findall("__.*__", line)
        for strong in strongs:
            tag = strong.replace("__", "<strong>").replace("__", "</strong>")
            line = line.replace(strong, tag)
        return line 

    def process_links(self, line):
        links = re.findall("\[.*\]\(.*\)", line)
        for link in links:
            url = re.findall("\(.*\)", link)[0].strip("(").strip(")")
            txt = re.findall("\[.*\]", link)[0].strip("[").strip("]")
            line = line.replace(link, f"<a href='{url}'>{txt}</a>")
        return line
    
    def convert_line(self, line):
        line = line.strip()
        if line.startswith("### "):
            return line.replace("### ", "<h3>") + "</h3>"
        if line.startswith("## "):
            return line.replace("## ", "<h2>") + "</h2>"
        if line.startswith("# "):
            return line.replace("# ", "<h1>") + "</h1>"
        
        if line.startswith("```"):
            return line.replace("```", "<code>").replace("```", "</code>")
        if line.startswith("`"):
            return line.replace("`", "<code>").replace("`", "</code>")
        
        # Default normal text
        line = self.process_bold(line)
        line = self.process_strong(line)
        line = self.process_links(line)
        return f"<p>{line}</p>"

    def convert(self):
        data = ""
        for chunk in self.chunks:
             data += self.convert_line(chunk) + "\n"
        return data

if __name__=="__main__":
    proc = MarkdownProcessor()
    proc.load('README.md')
    # print(proc.convert())
    print(proc.chunks)


