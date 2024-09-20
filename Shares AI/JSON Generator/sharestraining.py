class SharesTraining:
    def __init__(self):
        self.docs = []

    def add_doc(self, doc):
        """
        Add a SharesDoc instance to the collection.
        """
        self.docs.append(doc)

    def filter_by_keyword(self, include=None, exclude=None):
        """
        Filter documents by include and exclude keywords.
        """
        filtered_docs = []

        include = [keyword.lower() for keyword in include]
        exclude = [keyword.lower() for keyword in exclude]

        for doc in self.docs:
            keywords = [keyword.lower() for keyword in doc.keywords]

            if exclude:
                if any(keyword in keywords for keyword in exclude):
                    continue

            if include:
                if any(keyword in keywords for keyword in include):
                    filtered_docs.append(doc)
            else:
                filtered_docs.append(doc)

        return filtered_docs

    def jsonl(self, include=None, exclude=None):
        """
        Generate the JSONL representation for the entire training set,
        applying the include and exclude keyword filters if provided.
        """
        data = []
        filtered_docs = self.filter_by_keyword(include=include, exclude=exclude)
        for doc in filtered_docs:
            data.extend(doc.jsonl)
        return data