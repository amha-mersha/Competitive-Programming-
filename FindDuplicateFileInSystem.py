class Solution:
    def findDuplicate(self, paths):
        content_dict = {}
        for path in paths:
            files = path.split(' ')
            directory = files[0]
            
            for file in files[1:]:
                name, content = file.split('(')
                content_dict.setdefault(content[:-1],[]).append(directory + '/' + name)
                
        return [content_dict[content] for content in content_dict if len(content_dict[content]) > 1]
        
