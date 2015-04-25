class Dialog(object):
    def __init__(self, header):
        self.header = header
        self.result = None

    def _validate(self):
        if self.result is not None:
            raise Exception("This dialog has already been used")

    def choose(self, values, subvalue=None):
        self._validate()

        if self.header is not None:
            info("%s : " % self.header)

        indexed = values.keys() if isinstance(values, dict) else values
        for indx, val in enumerate(indexed):
            if subvalue:
                print " %d) %s" % (indx, val[subvalue])
            else:
                print " %d) %s" % (indx, val)

        while True:
            try:
                ans = raw_input(">>> ")
            except KeyboardInterrupt:
                bail()

            if ans.isdigit():
                ans = int(ans)
            else:
                continue

            if 0 <= ans < len(values):
                # self.index
                key = indexed[ans] if isinstance(values, dict) else ans
                self.index = ans

                # self.result
                self.result = values[key]

                # self.key
                if isinstance(values, dict):
                    self.key = key
                break
            else:
                continue

    def input(self, default=None, parse=None):
        self._validate()

        if default is None or default is "":
            prompt = "%s : " % self.header
        else:
            prompt = "%s [%s] : " % (self.header, default)

        bold_prompt = bold_format(prompt)

        while True:
            try:
                temp = raw_input(bold_prompt)
            except KeyboardInterrupt:
                bail()

            if temp == "" and default is None:
                print "Try again"
                continue
            else:
                temp = temp if temp != "" else default
                try:
                    self.result = temp if not parse else parse(temp)
                except:
                    raise Exception(
                            "Failed to parse input %s using %s" % (temp, str(parse))
                            )
                break

    def yesno(self, yes='y', no='n'):
        self._validate()

        prompt = bold_format("%s (%s/%s) : " % (self.header, yes, no))

        try:
            temp = raw_input(prompt)
        except KeyboardInterrupt:
            bail()

        if temp == yes:
            self.result = True
        elif temp == no:
            self.result = False
        else:
            bail()

    def secret(self):
        self._validate()

        try:
            prompt = bold_format("%s : " % self.header)
            self.result = getpass(prompt)
        except KeyboardInterrupt:
            bail()
