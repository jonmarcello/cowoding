class Evaluator:

    def __init__(self, AST, keywords):
        self.AST = AST
        self.keywords = keywords

    def run(self, node):
        if isinstance(node, list):
            for n in node:
                for k, v in n.iteritems():
                    self.execute([k, v])
        elif isinstance(node, dict):
            for k, v in node.iteritems():
                self.execute([k, v])
        
    def execute(self, loc):
        if isinstance(loc[1], list):
            self.run(loc[1])
        elif loc[0] == self.keywords[0]:
            self.echo(loc[1])
        elif loc[0] == self.keywords[1]:
            self.goto(loc[1])
        elif loc[0] == self.keywords[2]:
            self.stop()
        elif loc[0] == self.keywords[3]:
            self.nani(loc[1])
    
    def echo(self, v):
        print(v)

    def goto(self, v):
        for node in self.AST:
            if v in node:
                self.run(node[v])

    def nani(self, v):
        splitCommand = v.split("?")
        operation = splitCommand[0]

        splitNani = splitCommand[1].split("|")
        naniTrue = splitNani[0]
        naniFalse = splitNani[1]
        
        splitOperation = list(operation)
        operator = splitOperation[1]

        if operator == ">":
            if(int(splitOperation[0]) > int(splitOperation[2])):
                self.goto(naniTrue)
            else:
                self.goto(naniFalse)
        elif operator == "<":
            if(int(splitOperation[0]) < int(splitOperation[2])):
                self.goto(naniTrue)
            else:
                self.goto(naniFalse)
        elif operator == "==":
            if(splitOperation[0] == splitOperation[2]):
                self.goto(naniTrue)
            else:
                self.goto(naniFalse)


    def stop(self):
        quit()