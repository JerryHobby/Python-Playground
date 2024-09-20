class SharesDoc:
    def __init__(self, filename, prompts, completion, keywords):
        self.filename = filename
        self.prompts = prompts
        self.completion = completion
        self.keywords = keywords

    @property
    def jsonl(self):
        """
        Generate the JSONL representation for this document.
        """
        data = []
        for prompt in self.prompts:
            json_obj = {
                'prompt': prompt,
                'completion': self.completion
            }
            data.append(json_obj)
        return data