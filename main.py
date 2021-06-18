class MarkovAlgorithm:

    def __init__(self, *rules):
        self.rules = []
        for rule in rules:
            self.rules.append(self.parse_rule(rule))

    def add_rule(self, rule):
        self.rules.append(self.parse_rule(rule))

    def execute(self, string: str):
        end = False
        step = False
        string = "\b" + string
        while not end:
            for rule in self.rules:
                if rule[0] in string:
                    string = self.step(string, rule)
                    step = True
                    if rule[2]:
                        end = True
                    break
            if not step:
                end = True
            step = False
        return string.replace('\b', '')

    def step(self, string: str, rule):
        return string.replace(rule[0], rule[1], 1)

    @classmethod
    def parse_rule(cls, rule: str):
        if '->' in rule:
            s = rule.split('->')
            end = False
        elif '=>' in rule:
            s = rule.split('=>')
            end = True
        else:
            raise Exception("Wrong rule format.")
        if len(s) != 2:
            raise Exception("wrong rule format.")
        if s[0].strip() == '':
            return "\b", s[1].strip(), end
        return s[0].strip(), s[1].strip(), end


def main():
    rules = "*a->aA* *b->bB* *-># Aa->aA Ab->bA Ba->aB Bb->bB A#->#a B#->#b #=> ->*".split(' ')
    ma = MarkovAlgorithm(*rules)
    string = 'abbba'
    print("input string:", string)
    print("output string:", ma.execute("abbba"))


if __name__ == '__main__':
    main()
